import os


def move_file(command: str):
    arr = command.split(" ")
    if arr[0] != "mv":
        print("enter correct command!")
    else:
        with open(arr[1], "r") as old_file:
            data = old_file.read()

        if "/" in arr[2]:
            for_path = arr[2].split("/")
            new_file_name = for_path.pop()
            path = "/".join(for_path)
            os.makedirs(path)
            os.chdir(path)
            arr[2] = new_file_name

        with open(arr[2], "w") as new_file:
            new_file.write(data)

        os.remove(arr[1])
    pass
