import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3:
        cmd, original, file_path = command_parts
        if cmd == "mv":
            if "/" in file_path:
                head, tail = os.path.split(file_path)
                os.makedirs(head, exist_ok=True)
                with open(original, "r") as file1,\
                        open(file_path, "w") as file2:
                    file2.write(file1.read())
                os.remove(original)
            else:
                os.rename(original, file_path)
