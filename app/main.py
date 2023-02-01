from pathlib import Path
import os


def move_file(command: str) -> None:
    command, old_file, new_file = command.split()

    if command == "mv":
        created_dir = ""
        new_file_path = list(Path(new_file).parts)
        new_file_name = old_file

        if "." in new_file_path[-1].strip():
            new_file_name = new_file_path[-1]
            new_file_path.pop()

        if len(new_file_path) > 1:
            for index in range(len(new_file_path)):
                created_dir = os.path.join(created_dir, new_file_path[index])
                if not os.path.isdir(created_dir):
                    os.mkdir(created_dir)

        with open(old_file, "r") as file_old, open(
                os.path.join(created_dir, new_file_name),
                "w"
        ) as file_copy:
            file_copy.write(file_old.read())

        os.remove(old_file)

    return
