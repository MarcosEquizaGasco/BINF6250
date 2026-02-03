from .parse_functions import text_to_list

def build_markov_model(markov_model, path, order=1, separator="\n\n", START="*S*", END="*E*", NL="*NL*"):
    """
    Update a count dictionary that defines a markov model using new text from a source file.

    Args:
        markov_model: Dict mapping state tuples to next-token count dicts.
        path: Path to the training text file.
        order: Markov order (token length of the count dictionary's key).
        separator: Chunk separator passed to `text_to_list`.
        START: Token to mark the start of a chunk.
        END: Token to mark the end of a chunk.
        NL: Placeholder for newlines.

    Returns:
        The same markov_model dict updated with transition counts learned from input text.
    """

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
    """
    Convert a count-based Markov model into per-state probability distributions.
    Args:
        markov_model_counts: Dict of {state: {next_token: count}}, produced by `build_markov_model`.
    Returns:
        Dict of {state: {next_token: probability}} where probabilities in each state have a sum = 1.
    """

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