import os


def move_file(command: str) -> None:
    command = command.split(" ")
    mv = command[0]
    file_to_move = command[1]
    destination = command[2].split("/")
    if mv == "mv" and file_to_move != "".join(destination):
        try:
            with open(file_to_move, "r") as f:
                data = f.read()
            os.remove(file_to_move)
        except FileNotFoundError:
            print("File not found")
        path = ""
        if len(destination) == 1:
            path = destination[0]
        else:
            for i in range(len(destination) - 1):
                path += destination[i] + "/"
                if not os.path.exists(path):
                    os.mkdir(path)
            path += destination[-1]
        with open(path, "w") as f:
            f.write(data)
