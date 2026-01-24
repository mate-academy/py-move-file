import os


def move_file(command: str) -> None:
    command = command.split(" ")
    file_to_move = command[1]
    destination = command[2].split("/")
    if file_to_move != "".join(destination):
        if not os.path.exists(file_to_move):
            raise FileNotFoundError
        path = ""
        path = os.path.join(path, *destination[:-1])
        if path:
            os.makedirs(path, exist_ok=True)
        path = os.path.join(path, destination[-1])
        with (open(file_to_move, "r") as file,
              open(path, "w") as destination_file):
            destination_file.write(file.read())
        os.remove(file_to_move)
