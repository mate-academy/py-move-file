import os


def move_file(command: str) -> None:
    command = command.split()
    if command[0] == "mv":
        whole_data = ""
        with open(command[1]) as file:
            whole_data = file.read()

        os.remove(command[1])
        path_to_new_file = command[2].split("/")
        if len(path_to_new_file) == 1:
            with open(path_to_new_file[0], "w") as file:
                file.write(whole_data)
        else:
            previous_path = ""
            for directory in path_to_new_file[:-1]:
                if not os.path.isdir(previous_path + directory):
                    os.mkdir(previous_path + directory)
                previous_path = previous_path + directory + "/"

            combined_path = ""
            for path in path_to_new_file:
                combined_path = os.path.join(combined_path, path)

            with open(combined_path, "w") as file:
                file.write(whole_data)
