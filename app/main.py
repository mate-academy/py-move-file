import os


def move_file(command: str) -> None:
    if not command.startswith("mv"):
        return

    command_split = command.split()
    if len(command_split) != 3:
        return

    _, filename_in, filename_out = command_split

    if filename_out.find("/") != -1:
        if filename_out.endswith("/"):
            filename_out = os.path.join(filename_in)

        os.makedirs(os.path.dirname(filename_out), exist_ok=True)

    with (open(filename_in, "r") as file_in,
          open(filename_out, "w") as file_out):
        file_out.writelines(file_in.read())
        os.remove(filename_in)
