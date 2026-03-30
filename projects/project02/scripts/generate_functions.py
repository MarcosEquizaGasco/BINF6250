from .parse_functions import list_to_text
import random 

def get_next_word(current_state, markov_model_normalized, rng_object, END="*E*"):
    """
    Sample the next token for a state using weighted random choice.
    Args:
        current_state: Tuple of tokens ("words") representing the current Markov state.
        markov_model_normalized: {state: {next_token: probability}} dict from `normalize_model`.
        rng_object: random.Random instance used for reproducible random sampling.
        END: Token to mark the end of a chunk.
    Returns:
        The sampled next token, or END if the state is unrecognized.
    """
    dist_dict = markov_model_normalized.get(current_state)
    if not dist_dict:
        # end it if cant be found
        return END

    words = list(dist_dict.keys())
    probs = list(dist_dict.values())

    return rng_object.choices(words, weights=probs, k=1)[0]

# another method for get_next_word
def get_next_word_alternative(current_state, markov_model_normalized, rng_object, END="*E*"):
    """
    Alternate sampler that draws the next token via cumulative probability.
    Args:
        current_state: Tuple of tokens ("words") representing the current Markov state.
        markov_model_normalized: {state: {next_token: probability}} dict from `normalize_model`.
        rng_object: random.Random instance used for reproducible random sampling.
        END: Token to mark the end of a chunk.
    Returns:
        The sampled next token, or END if the state is unrecognized.
    """

    dist_dict = markov_model_normalized.get(current_state)
    if not dist_dict:
        # end it if cant be found
        return END

    r = rng_object.random()
    cumulative = 0.0

    for next_word in dist_dict .keys():
      cumulative += dist_dict [next_word]
      if r <= cumulative:
        return next_word

    return next_word

def generate_random_text(markov_model_normalized, seed, order=1,
    limit_by="word", limit=200, separator="\n\n",
    hard_limit=2000, 
    START="*S*", END="*E*", NL="*NL*"):
    """
    Generate text from a normalized Markov model with configurable stopping rules.
    Args:
        markov_model_normalized: {state: {next_token: probability}} dict used for sampling.
        seed: Seed for the internal RNG to make output deterministic.
        order: Markov order (length of state). Default 1.
        limit_by: Stop criterion: one of {"word", "line", "probabilistic"}. Default "word".
            "word": generation continues until (limit) number of tokens ("words") have been added
            "line": geneeration continues until (limit) number of newlines have been added
        limit: Maximum words/lines, used by limit_by. Default 200.
        separator: Chunk separator passed through to `list_to_text`. Default "\n\n"
        hard_limit: Absolute cap on generated tokens to prevent runaway loops. Default 2000.
        START: Token to mark the start of a chunk.
        END: Token to mark the end of a chunk.
        NL: Placeholder for newlines.
    Returns:
        A string of generated text.
    """

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

    return list_to_text(generated_list, separator=separator)