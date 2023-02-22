import os


def move_file(command: str) -> None:
    if command.count(" ") == 2:
        command1, source_file_path, destination_file_path = command.split()
        if '/' not in command:
            os.rename(source_file_path, destination_file_path)
        else:
    #       separated = destination_file_path.split("/")
            os.makedirs(destination_file_path, exist_ok=True)
            with open(f"{source_file_path}", "r") as file_1, open(f"{destination_file_path}", "w") as file_2:
                file_2.write(file_1.read())
        os.remove(source_file_path)

