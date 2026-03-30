
path = "data/sonnets.txt"

START = "*S*"
END = "*E*"
NL = "*NL*"
# ignoring tabs for now  

def text_to_list(path, separator="\n\n"):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read().lower()

    chunks = raw.split(separator)

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


def list_to_text(text_list, separator="\n\n", avoid_double_newlines=True):
    out = []
    at_line_start = True

    for word in text_list:
        if word == START:
            continue
        if word == END:
            if not at_line_start and avoid_double_newlines:
                out.append("\n") # avoid double newlines
            at_line_start = True
        elif word == NL:
            if not at_line_start and avoid_double_newlines:
                out.append("\n") # avoid double newlines
            at_line_start = True
        else:
            if not at_line_start:
                out.append(" ")
            out.append(word)
            at_line_start = False

    return "".join(out).strip()

text_list = text_to_list(path) 
retextified_list = list_to_text(text_list)
#print(retextified_list)