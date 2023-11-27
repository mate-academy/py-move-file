import os


def move_file(command: str) -> None:
    user_input = command.split()
    if len(user_input) == 3:
        filename, directories = user_input[1], user_input[2]

        if "/" in directories:
            new_filename = directories[directories.rfind("/"):]
            without_name_directories = directories.replace(new_filename, "")

            if not os.path.exists(without_name_directories):
                os.makedirs(without_name_directories)

            with open(filename, "r") as source_file:
                user_input = source_file.read()

            with open(directories, "w") as dest_file:
                dest_file.write(user_input)

        else:
            new_filename = directories
            with open(filename, "r") as source_file:
                user_input = source_file.read()

            with open(new_filename, "w") as dest_file:
                dest_file.write(user_input)

        os.remove(filename)
