import os


def move_file(command: str) -> None:
    parts_of_command = command.split()

    if len(parts_of_command) == 3 and parts_of_command[0] == "mv":
        _, existing_file_name, new_file_path = parts_of_command

        if os.path.exists(existing_file_name):
            if new_file_path[-1] == "/":
                new_file_path = os.path.join(new_file_path, existing_file_name)

            if "/" in new_file_path:
                parts_of_directory = new_file_path.split("/")[:-1]

                for i in range(len(parts_of_directory)):
                    dir_path = os.path.join(*parts_of_directory[:i + 1])
                    if not os.path.exists(dir_path):
                        os.mkdir(dir_path)

            with (open(new_file_path, "w") as file_copy,
                  open(existing_file_name, "r") as existing_file):
                file_copy.write(existing_file.read())

            os.remove(existing_file_name)
