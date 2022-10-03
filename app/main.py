import os


def move_file(command: str):
    parts_of_command = command.split(" ")
    command = parts_of_command[0]
    if command == "mv":
        file = parts_of_command[1]
        new_path = parts_of_command[2]
        new_file = new_path.split("/")[-1]
        new_path = new_path.replace(new_file, "")
        path = os.path.join(new_path)
        os.makedirs(path)
        with open(file, "r") as current_file:
            file_copy = current_file.read()
        os.remove(file)
        os.chdir(path)
        with open(new_file, "w") as new_file:
            new_file.write(file_copy)
