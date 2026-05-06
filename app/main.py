import os


def move_file(command: str) -> None:
    command_split = command.split()
    if "/" in command_split[2]:
        prev_dir = ""
        for directory in command_split[2].split("/")[:-1]:
            if prev_dir:
                # os.mkdir(prev_dir + "/" + directory)
                os.makedirs(prev_dir + "/" + directory, exist_ok=True)
                prev_dir += "/" + directory
            else:
                # os.mkdir(directory)
                os.makedirs(directory, exist_ok=True)
                prev_dir = directory
    with (open(command_split[1], "r") as file_read,
          open(command_split[2], "w") as file_write):
        file_write.write(file_read.read())
    os.remove(command_split[1])
