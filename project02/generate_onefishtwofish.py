from scripts import build_markov_model, normalize_model, generate_random_text, read_text_file
import random 

if __name__ == "__main__":

    path = "data/one_fish_two_fish.txt"

    START = "*S*"
    END = "*E*"
    NL = "*NL*"
    seed = random.random()
    order = 1
    limit_by = "line"
    limit = 10
    separator = None

    new_text = read_text_file(path)

    markov_model = {}
    build_markov_model(markov_model, new_text, order=order, separator=separator)

    markov_model_normalized = normalize_model(markov_model)

    output = generate_random_text(
        markov_model_normalized,
        seed = seed,
        order = order,
        limit_by = limit_by,
        limit = limit,
        separator = separator
        )

    print(output)
