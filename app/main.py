import os


def move_file(command: str) -> None:
    input_tokens = command.split()
    if len(input_tokens) != 3:
        return

    if input_tokens[0] != "mv":
        return

    input_file_name = input_tokens[1]

    if not os.path.isfile(input_file_name):
        return

    content = None

    with open(input_file_name, "rb") as file:
        content = file.read()

    path = os.path.dirname(input_tokens[2])
    filename = os.path.basename(input_tokens[2])

    if filename == "":
        filename = input_file_name

    if path != "" and not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

    if path == "" or path == "/":
        out = filename
    else:
        out = os.path.join(path, filename)

    with open(out, "wb") as file:
        file.write(content)

    os.remove(input_file_name)
