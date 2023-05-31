import os


def move_file(commnad: str) -> None:
    try:
        command, current_file_name, new_file_path = commnad.split()
    except ValueError:
        print("Command must have 3 arguments")
        return
    if current_file_name == new_file_path or command != "mv":
        return
    destination_path = os.path.dirname(new_file_path)
    if destination_path:
        os.makedirs(destination_path, exist_ok=True)
    os.replace(current_file_name, new_file_path)


if __name__ == "__main__":
    move_file("mv file.txt f/p/file1.txt")
