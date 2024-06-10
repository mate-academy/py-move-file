import os


def move_file(command: str) -> None:
    command_name, file_to_move, new_file = command.split()
    if command_name == "mv":
        whole_data = ""
        with open(file_to_move) as file:
            whole_data = file.read()

        os.remove(file_to_move)
        path_to_new_file = new_file.split("/")

        combined_path = ""
        for path in path_to_new_file[:-1]:
            combined_path = os.path.join(combined_path, path)

        if (combined_path
                and len(path_to_new_file) > 1
                and not os.path.exists(path_to_new_file[-2])):
            os.makedirs(combined_path)

        with open(new_file, "w") as file:
            file.write(whole_data)
