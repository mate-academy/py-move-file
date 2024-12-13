import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3 and split_command[0] == "mv":
        move_path = split_command[-1].split("/")
        move = ""
        for path_stage in move_path[:-1]:
            move += path_stage + "/"
            os.makedirs(move, exist_ok=True)

        with (open(split_command[1], "r") as file_out,
              open(move + move_path[-1], "w") as file_in):

            file_in.write(file_out.read())

        os.remove(split_command[1])
