import os


def move_file(command: str) -> None:
    split_command = command.split()
    move_path = split_command[-1].split("/")
    move = ""
    for di in move_path[:-1]:
        move += di + "/"
        os.makedirs(move, exist_ok=True)

    with (open(split_command[1], "r") as file_out,
          open(move + move_path[-1], "w") as file_in):

        file_in.write(file_out.read())

    os.remove(split_command[1])
