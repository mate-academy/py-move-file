import os


def move_file(command: str) -> None:
    _, file_name, destination = command.split()
    destination_file = os.path.basename(destination)
    path_for_func = destination.split("/")
    path_for_func.pop(-1)
    temp = ""
    for directory in path_for_func:
        temp = os.path.join(temp, directory)
        if not os.path.exists(temp):
            os.mkdir(temp)

    with open(file_name, "r") as file:
        data = file.read()

    with open(os.path.join(temp, destination_file), "w") as file:
        file.write(data)

    os.remove(file_name)
