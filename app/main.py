import os


def move_file(command: str) -> None:
    if len(command.split()) != 3 or command.split()[0] != "mv":
        print("invalid command")
        return
    cmd, source_file, destination = command.split()
    if len(os.path.split(destination)[0]) == 0:
        print("simple source")
        os.rename(source_file, destination)
        return
    path_to_create = os.path.split(destination)[0]
    os.makedirs(path_to_create, exist_ok=True)
    os.rename(source_file, destination)
    return
