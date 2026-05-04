import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        return
    _, file_in, file_out = command_list

    if file_out.endswith("/"):
        file_out = os.path.join(file_out, os.path.basename(file_in))

    if file_in == file_out:
        return

    directory = os.path.dirname(file_out)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(file_in, "r") as f:
        content_file = f.read()
    with open(file_out, "w") as new_f:
        new_f.write(content_file)
    os.remove(file_in)
