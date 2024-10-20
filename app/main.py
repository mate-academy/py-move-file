import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    file1 = command_list[1]
    file2_path = command_list[-1]
    if "/" in command:
        directories = command_list[-1].split("/")[:-1]
        file_path = ""
        for directory in directories:
            file_path += f"{directory}/"
            if not os.path.isdir(file_path):
                os.mkdir(file_path)
        with open(file1, "r") as f:
            text = f.read()
        with open(f"{file2_path}", "w") as w:
            w.write(text)
    else:
        new_file = command_list[-1]
        with open(file1, "r") as f:
            text = f.read()
        with open(new_file, "w") as w:
            w.write(text)
    os.remove(file1)
