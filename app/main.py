import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, file_to_move, new_file = command.split()
        if command_name == "mv":
            path_to_new_file = os.path.split(new_file)
            combined_path = ""
            for path in path_to_new_file[:-1]:
                combined_path = os.path.join(combined_path, path)

            if (combined_path
                    and len(path_to_new_file) > 1
                    and not os.path.exists(path_to_new_file[-2])):
                os.makedirs(combined_path)

            with (open(file_to_move, "r") as file_in,
                  open(new_file, "w") as file_out):
                whole_data = file_in.read()
                file_out.write(whole_data)
            os.remove(file_to_move)
