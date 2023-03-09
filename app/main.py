import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_split = command.split()
        if command_split[0] == "mv" and "/" in command_split[2]:
            os.makedirs(os.path.dirname(command_split[2]), exist_ok=True)
        with (open(command_split[1], "r") as file_one,
              open(command_split[2], "w") as file_two):
            file_two.write(file_one.read())
        os.remove(command_split[1])
