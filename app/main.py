# write your code here
import os


def move_file(command: str) -> None:
    input_tokens = command.split()

    if len(input_tokens) != 3:
        return

    command_name, source, destination = input_tokens

    if command_name != "mv":
        return

    input_file_name = os.path.basename(source)

    if not os.path.exists(source) and not os.path.isfile(source):
        return

    content = None

    with open(source, "rb") as file:
        content = file.read()

    out_file_path = os.path.dirname(destination)
    out_file_name = os.path.basename(destination)

    if not out_file_name:
        out_file_name = input_file_name

    if out_file_path and not os.path.exists(out_file_path):
        os.makedirs(out_file_path, exist_ok=True)

    if out_file_path == "/":
        out_file_path = ""

    out = os.path.join(out_file_path, out_file_name)
    with open(out, "wb") as file:
        file.write(content)

    os.remove(source)
