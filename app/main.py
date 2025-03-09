import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if command_list[0] == "mv" and len(command_list) == 3:
        path_to_new_file = command_list[-1].split("/")
        current_dir = ""
        file_name =""
        if len(path_to_new_file) == 1:
            current_dir = path_to_new_file[0]
        else:
            for directory in path_to_new_file:
                if "." in directory:
                    file_name = directory
                    break
                current_dir = os.path.join(current_dir, directory)
                if not os.path.exists(current_dir):
                    os.mkdir(current_dir)
        with (open(command_list[1], "r") as source_file,
              open(current_dir + file_name, "w") as new_file):
            new_file.write(source_file.read())
        os.remove(command_list[1])
