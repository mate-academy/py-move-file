import os


def move_file(command: str) -> None:
    if command.split()[0] == "mv" and len(command.split()) == 3:
        cmd, file_original, new_file_directory = command.split()
        directories, file_name = os.path.split(new_file_directory)

        if directories:
            os.makedirs(directories, exist_ok=True)

        new_file_name = os.path.join(directories, file_name)

        with open(file_original, "r") as file_origin, open(
            new_file_name, "w"
        ) as file_new:
            for line in file_origin:
                file_new.write(line)
        os.remove(file_original)
