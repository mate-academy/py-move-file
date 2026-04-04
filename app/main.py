import os


def move_file(command: str) -> None:
    input_tokens = command.split()
    command_name, source, destination = input_tokens
    if len(input_tokens) != 3:
        return

    if command_name != "mv":
        return

    if not os.path.isfile(source):
        return

    content = None

    with open(source, "rb") as file:
        content = file.read()

    path = os.path.dirname(destination)
    filename = os.path.basename(destination)

    if filename == "":
        filename = source

    if path != "" and not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

    if path == "" or path == "/":
        out = filename
    else:
        out = os.path.join(path, filename)

    with open(out, "wb") as file:
        file.write(content)

    os.remove(source)
