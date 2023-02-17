import os


def move_file(command: str) -> None:
    command, first_file, second_file = command.split()
    second_file_part = os.path.split(second_file)
    directories_list = second_file_part[0].split("/")
    directories_path = os.path.join(*directories_list)
    path_with_file = os.path.join(directories_path, second_file_part[1])

    if command == "mv":
        if not os.path.exists(directories_path):
            os.makedirs(directories_path)

        with (open(first_file, "r") as file_content,
              open(path_with_file, "w") as file_out):
            file_out.write(file_content.read())

        os.remove(first_file)
