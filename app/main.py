import os


def copy_file_and_remove_original(file_in: str, file_out: str) -> None:
    with open(file_in, "r") as f1, open(file_out, "w") as f2:
        f2.write(f1.read())


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command, file, new_file = command.split()
        if command == "mv":
            if "/" in new_file:
                dirs = new_file.split("/")[:-1]
                os.makedirs("/".join(dirs), exist_ok=True)
            copy_file_and_remove_original(file, new_file)
            os.remove(os.path.abspath(file))