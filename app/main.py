import os


def create_dirs(path_to_create: str) -> None:
    try:
        os.makedirs(os.path.dirname(path_to_create), exist_ok=True)
    except OSError as e:
        print(f"Error creating directories: {e}")


def copy_and_delete_file(file_from: str, file_to: str) -> None:
    try:
        with (open(file_from, "r") as read_file,
              open(file_to, "x") as write_file):
            write_file.writelines(read_file.readlines())
        os.remove(file_from)

    except OSError as e:
        print(f"Error copying or deleting file: {e}")


def move_file(command: str) -> None:
    key_word, move_from, move_to = command.split()
    if key_word == "mv" and os.path.exists(move_from):
        create_dirs(move_to)
        copy_and_delete_file(move_from, move_to)
    else:
        print("Invalid command or source file does not exist.")
