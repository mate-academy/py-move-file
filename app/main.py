import os


def move_file(command: str) -> None:
    command_list = command.split()
    first_file = command_list[1]
    if "/" in command:
        file_path = "/".join(command_list[-1].split("/")[:-1])
        os.makedirs(file_path, exist_ok=True)
        with (open(f"{file_path}/{command_list[-1].split('/')[-1]}", "w") as f,
              open(first_file, "r") as src_file):
            f.write(src_file.read())
        os.remove(first_file)
    else:
        second_file = command_list[2]
        os.rename(first_file, second_file)
