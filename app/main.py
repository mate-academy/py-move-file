import os


def move_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "mv":
        mv, file1_name, destination = command.split()
        dirs = destination.split("/")[:-1]
        file2_name = destination.split("/")[-1]

        dir_path = ""
        for folder in dirs:
            dir_path = os.path.join(dir_path, folder)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

        dir_path = os.path.join(dir_path, file2_name)
        with open(file1_name, "r") as source, open(dir_path, "w") as clone:
            clone.write(source.read())
        os.remove(file1_name)
