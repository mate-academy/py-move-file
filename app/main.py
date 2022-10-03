import os


def move_file(command: str) -> None:
    command_list = command.split()
    cmd = command_list[0]
    old_path = command_list[1]
    new_path = "/".join(command_list[2].split("/")[:-1])
    new_file_name = command_list[2].split("/")[-1]

    if cmd != "mv" or old_path == new_path:
        return print("Wrong data")
    else:
        with open(old_path, "r") as file:
            data = file.read()
            os.makedirs(new_path)
            with open(new_path + "/" + new_file_name, "w") as new_file:
                new_file.write(data)
        os.remove(old_path)
