import os


def move_file(command: str) -> None:
    print(f"command: {command}")
    arr = command.split(" ")
    command = arr[0]
    source = arr[1]
    destination = arr[2]

    file1 = os.path.abspath(source).split("\\")
    file1.pop()
    file2 = os.path.abspath(destination).split("\\")
    file2.pop()
    if file1 == file2:
        os.rename(source, destination)
    else:
        folders = destination.split("/")
        folders.pop(-1)
        print(folders)
        joined_folders = os.path.join(*folders, "")
        if not os.path.exists(joined_folders):
            os.makedirs(joined_folders)
        os.replace(source, destination)
