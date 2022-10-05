import os


def move_file(command):
    string = command.split(" ")
    if string[0] == "mv":
        file1 = string[1]
        list_dir = string[2].split("/")
        path = ""
        for i in range(len(list_dir) - 1):
            path = os.path.join(path, list_dir[i])
        if path:
            os.makedirs(path)
        with open(f"{file1}", "r") as file, \
                open(f"{string[2]}", "w") as file_copy:
            content = file.read()
            file_copy.write(content)
        os.remove(f"{file1}")
