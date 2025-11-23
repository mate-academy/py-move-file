import os


def move_file(input_command: str) -> None:
    try:
        command, old_file_path, new_file_path = input_command.split(" ")
        if command != "mv":
            raise ValueError
    except ValueError:
        return

    directories, new_file_name = os.path.split(new_file_path)
    directives_list = directories.strip().split("/")

    new_path = ""
    for directory in directives_list:
        if directory != "":
            new_path = os.path.join(new_path, directory)
            if not os.path.exists(new_path):
                os.mkdir(new_path)

    if not new_file_name:
        new_file_path += old_file_path

    with (open(old_file_path, "r") as old_file,
          open(new_file_path, "w") as new_file):
        new_file.write(old_file.read())

    os.remove(old_file_path)
