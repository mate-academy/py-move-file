import os


def move_file(command: str) -> None:

    parts = command.split()

    if len(parts) == 3 and parts[0] == "mv":
        mv, file_name, new_file_name = parts

        if "/" in new_file_name:
            way, name_file = os.path.split(new_file_name)
            os.makedirs(way, exist_ok=True)

            with (open(file_name, "r") as file1,
                  open(new_file_name, "w") as file2):
                file2.write(file1.read())
            os.remove(file_name)
        else:
            os.rename(file_name, new_file_name)
