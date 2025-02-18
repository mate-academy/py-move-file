import os


def move_file(command: str) -> None:
    print(f"command: {command}")
    arr = command.split(" ")
    command = arr[0]
    source = arr[1]
    destination = arr[2]
    if command != "mv":
        raise NotImplementedError("Not implemented other command than mv")
    if "/" not in source and "/" not in destination:
        os.rename(source, destination)
    else:
        folders = destination.split("/")
        folders.remove(folders[-1])
        print(folders)
        joined_folders = os.path.join(*folders, "")
        print("joined:")
        print(f"joined: {joined_folders}")
        if not os.path.exists(joined_folders):
            os.makedirs(joined_folders)
        if not os.path.isfile(destination):
            os.replace(source, destination)
