import os


def move_file(command: str) -> None:
    if command.count(" ") == 2:
        command1, source_path, destination_path = command.split()
        if "/" not in command:
            os.rename(source_path, destination_path)
        else:
            head_path, tail = os.path.split(destination_path)
            os.makedirs(head_path, exist_ok=True)
            with (
                open(f"{source_path}", "r") as file_1,
                open(f"{destination_path}", "w") as file_2
            ):
                file_2.write(file_1.read())
            os.remove(source_path)
