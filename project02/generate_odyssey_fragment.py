from scripts import build_markov_model, normalize_model, generate_random_text
import random 

if __name__ == "__main__":

    path = "data/odyssey.txt"

    START = "*S*"
    END = "*E*"
    NL = "*NL*"
    seed = random.random()
    order = 2
    limit_by = "line"
    limit = 10
    separator = None

    markov_model = {}
    build_markov_model(markov_model, path, order=order, separator=separator)

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
