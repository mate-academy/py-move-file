import os


def move_file(command: str) -> None:
    command_name, file, direct, *_ = command.split()

    if "/" in direct:
        directory = direct.split("/")
        os.makedirs("/".join(directory[:-1]), exist_ok=True)

    with (open(file, "r") as file_in,
          open(direct, "w") as file_out):
        file_out.write(file_in.read())
    os.remove(file)
