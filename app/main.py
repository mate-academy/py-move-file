import os


def move_file(command: str) -> None:
    my_com, file_name, destination = command.split()

    if my_com == "mv":
        list_path = destination.split("/")
        new_name = list_path.pop()
        make_dir = ""
        while list_path:
            make_dir += f'{list_path.pop(0)}/'
            os.mkdir(make_dir)
        with open(file_name, "r") as old_file,\
                open(make_dir + new_name, "w") as new_file:
            new_file.write(old_file.read())
        os.remove(file_name)
