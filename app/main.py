import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise Exception("Invalid command")
    command, current_file_name, new_file_path = command.split()
    if command != "mv":
        raise Exception("Command not found")
    destination_dir, new_file_name = os.path.split(new_file_path)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)
    os.replace(current_file_name, os.path.join(destination_dir, new_file_name))


if __name__ == "__main__":
    move_file("mv file.txt f/p/file1.txt")
