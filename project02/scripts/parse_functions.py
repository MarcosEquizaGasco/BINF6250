def text_to_list(new_text, separator="\n\n", START="*S*", END="*E*", NL="*NL*"):
    """
    Converts text into a token sequence with START/END/NL markers.
    Args:
        new_text: New text.
        separator: String that splits the text into chunks. END, START are inserted between chunks.
            If None, the entire file is treated as a single chunk.
        START: Token to mark the start of a chunk.
        END: Token to mark the end of a chunk.
        NL: Placeholder for newlines.
    Returns:
        List of lowercase tokens including START, END and NL indicators.
    """
    
    if separator is None:
        chunks = [new_text]
    else:
        chunks = new_text.split(separator)

    text_list = [START]

    for i, chunk in enumerate(chunks):
        chunk = chunk.strip()
        if chunk:
            # explicitly preserve within-chunk newlines
            chunk = chunk.replace("\n", f" {NL} ")

            # split on any whitespace
            text_list.extend(chunk.split())

        if i != len(chunks) - 1:
            # if there are still more chunks, do END START
            text_list.append(END)
            text_list.append(START)

    text_list.append(END)
    return text_list

def list_to_text(text_list, separator="\n\n", avoid_double_newlines=True, START="*S*", END="*E*", NL="*NL*"):
    """
    Reconstructs plain text from a token list that includes START/END/NL markers.
    ("reverts" text_to_list)
    Args:
        text_list: List of tokens produced by `text_to_list` or the generator.
        separator: Separator to use between logical chunks when END markers are hit.
        avoid_double_newlines: If True, collapse consecutive newline markers to a single newline.
        START: Token to mark the start of a chunk.
        END: Token to mark the end of a chunk.
        NL: Placeholder for newlines.
    Returns:
        A cleaned text string without START/END indicators and NL converted into newlines.
    """

    out = []
    at_line_start = True

    for word in text_list:
        if word == START:
            continue
        if word == END:
            if not at_line_start and avoid_double_newlines:
                out.append("\n")
            at_line_start = True
        elif word == NL:
            if not at_line_start and avoid_double_newlines:
                out.append("\n")
            at_line_start = True
        else:
            if not at_line_start:
                out.append(" ")
            out.append(word)
            at_line_start = False

    return "".join(out).strip()

def read_text_file(path):
    """
    Reads text file
    """
    with open(path, "r", encoding="utf-8") as f:
        new_text = f.read().lower()
        return new_text