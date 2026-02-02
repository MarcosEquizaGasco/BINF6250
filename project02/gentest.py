from parsetest import text_to_list, list_to_text, path, START, END, NL
import random

#print(list_to_text(text_to_list(path)))

#markov_model = {}

def build_markov_model(markov_model, path, order=1, separator="\n\n"):
    text_list = text_to_list(path, separator=separator)

    expanded = []
    for word in text_list:
        if word == START:
            expanded.extend([START] * order)
        else:
            expanded.append(word)

    for i in range(len(expanded) - order):
        state = tuple(expanded[i : i + order])
        nxt = expanded[i + order]

        if state not in markov_model:
            markov_model[state] = {}
        if nxt not in markov_model[state]:
            markov_model[state][nxt] = 0

        markov_model[state][nxt] += 1

    return markov_model


def normalize_model(markov_model_counts):
    # converts counts into probs
    normalized = {}

    for k, v in markov_model_counts.items():
        # k is a tuple, v is a dict, vv is an int

        total = sum(v.values())
        if total == 0:
            continue

        normalized[k] = {}
        for v, vv in v.items():
            normalized[k][v] = vv / total

    return normalized


#counts = build_markov_model(markov_model,path)
#normalized = normalize_model(counts)
#print(counts.get(("the",)))
#print(normalized.get(("the",)))

def get_next_word(current_state, markov_model_normalized, rng_object):
    
    dist_dict = markov_model_normalized.get(current_state)
    if not dist_dict:
        # end it if cant be found
        return END

    words = list(dist_dict.keys())
    probs = list(dist_dict.values())

    # from my understanding, rng.choices uses weights so we could even pass pure counts
    return rng_object.choices(words, weights=probs, k=1)[0]

# the seed will be set by generate_random_text 
# calling rng_object will advance the random state reproducibly
# if you just pass the seed then the same thing will be chosen every time for following "the"


# alternative is to use cumulative prob:
# def get_next_word(current_state, markov_model_normalized, rng):
#    dist_dict = markov_model_normalized.get(current_state)
#    r = rng.random()
#    cumulative = 0.0
#    for next_word in dist_dict .keys():
#       cumulative += dist_dict [next_word]
#        if r <= cumulative:
#            return next_word
#    return next_word

def generate_random_text(markov_model_normalized, seed=12321, order=1,
    limit_by="word", limit=200, separator="\n\n",
    hard_limit=2000):

    if order < 1:
        raise ValueError("order must be >= 1")
    if limit_by not in ("word", "line", "probabilistic"):
        raise ValueError('limit_by must be "word", "line",or "probabilistic"')
    if limit < 1:
        raise ValueError("limit must be >= 1")
    if hard_limit < 1:
        raise ValueError("hard_limit must be >= 1")

    rng_object = random.Random(seed)

    generated_list = [START] * order
    word_count = 0
    line_count = 0

    while True:
        if len(generated_list) >= hard_limit:
            break
        if limit_by == "word" and word_count >= limit:
            break
        if limit_by == "line" and line_count >= limit:
            break

        state = tuple(generated_list[-order:])
        nxt = get_next_word(state, markov_model_normalized, rng_object)
        
        if limit_by == "probabilistic" and nxt == END:
            break

        generated_list.append(nxt)

        if nxt == NL:
            line_count += 1
        elif nxt not in (START, END):
            word_count += 1
    #print(generated_list)
    return list_to_text(generated_list, separator=separator)
    

if __name__ == "__main__":
    path = "data/sonnets.txt"
    order = 1
    separator = "\n\n"

    markov_model = {}
    build_markov_model(markov_model, path, order=order, separator=separator)
    markov_model_normalized = normalize_model(markov_model)

    output = generate_random_text(
        markov_model_normalized,
        seed=12345,
        order=order,
        limit_by="line",
        limit=14,
        separator=separator
    )

    print(output)