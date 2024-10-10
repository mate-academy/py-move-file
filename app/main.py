import os


def move_file(command: str) -> None:
    command = command.split(" ")
    mv = command[0]
    file_to_move = command[1]
    destination = command[2].split("/")
    if mv != "mv":
        raise SyntaxError(f"Command {mv} not found")
    if file_to_move != "".join(destination):
        try:
            with open(file_to_move, "r") as source_file:
                data = source_file.read()
            os.remove(file_to_move)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_to_move} not found")
        path = ""
        if len(destination) == 1:
            path = os.path.join(path, destination[0])
        else:
            for i in range(len(destination) - 1):
                path = os.path.join(path, destination[i])
                if not os.path.exists(path):
                    os.mkdir(path)
            path = os.path.join(path, destination[-1])
        with open(path, "w") as destination_file:
            destination_file.write(data)
