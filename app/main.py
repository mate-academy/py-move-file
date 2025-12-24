import os


def move_file(command):
    if not command.split(" ")[0] == "mv":
        return
    old_file = command.split(" ")[1]
    new_file = command.split(" ")[2]
    if "/" in new_file:
        path_parts = new_file.split("/")
        created_path = ""
        for i in range(len(path_parts) - 1):
            created_path += path_parts[i] + "/"
            os.mkdir(created_path)
    try:
        with open(old_file, "r") as old, open(new_file, "w") as new:
            new.write(old.read())
    except FileNotFoundError:
        print("File does not exist.")
    else:
        os.remove(old_file)
