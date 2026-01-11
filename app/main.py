import os


def move_file(command: str) -> None:
    user_input = command.split()
    if len(user_input) == 3 and user_input[0] == "mv":
        filename, directories = user_input[1], user_input[2]

        if os.path.sep in directories:
            new_filename = directories[directories.rfind(os.path.sep):]

            without_name_directories = directories.replace(new_filename, "")

            if not os.path.exists(without_name_directories):
                os.makedirs(without_name_directories)

            os.replace(filename, directories)
        else:
            new_filename = directories
            os.replace(filename, new_filename)
