import os


def move_file(command: str):
    command_params = command.split(" ")
    command = command_params[0]
    if command == "mv":
        filename = command_params[1]
        new_dir = command_params[2]
        new_filename = new_dir.split("/")[-1]
        new_dir = new_dir.replace(new_filename, "")
        path = os.path.join(new_dir)
        os.makedirs(path)
        with open(filename, "r") as current_file:
            file_copy = current_file.read()
        os.remove(filename)
        os.chdir(path)
        with open(new_filename, "w") as new_file:
            new_file.write(file_copy)
