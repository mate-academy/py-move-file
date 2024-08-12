import os


def move_file(command: str) -> None:
    command_content = command.split()
    if (
        len(command_content) == 3
        and command_content[0] == "mv"
        and command_content[1] != command_content[2]
    ):
        path_components = command_content[2].split("/")

        if len(path_components) > 1:
            path_components = path_components[:-1]
            new_directory_path = os.path.join(*path_components)

            if not os.path.exists(new_directory_path):
                os.makedirs(new_directory_path)

            with (open(command_content[1], "r") as file,
                  open(command_content[2], "w") as moved_file
                  ):
                moved_file.write(file.read())
            os.remove(command_content[1])

        else:
            os.rename(command_content[1], command_content[2])
