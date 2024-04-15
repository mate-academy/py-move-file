import os


def move_file(command: str) -> None:
    command, source_file, moved_file = command.split()
    if command != "mv":
        print("Wrong command")
    if "/" not in moved_file:
        if not os.path.exists(moved_file):
            os.rename(source_file, moved_file)
            return None
        else:
            print("File already exists.")
            return None
    else:
        os.makedirs(os.path.dirname(moved_file), exist_ok=True)
        with (open(source_file, "r") as old_file,
              open(moved_file, "w") as new_file):
            new_file.write(old_file.read())
        os.remove(source_file)
