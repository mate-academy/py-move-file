import os


def move_file(command: str) -> None:

    mv, old_file_name, new_path_file_name = command.split(" ")

    if new_path_file_name[-1] == "/":
        directories = new_path_file_name
        new_file_name = old_file_name
    else:
        new_file_name = new_path_file_name.split("/")[-1]
        directories = new_path_file_name.replace(new_file_name, "")

    try:
        if directories != "":
            os.makedirs(directories)
    except FileExistsError:
        pass

    with (open(old_file_name, "r") as old_file,
          open(directories + new_file_name, "w") as new_file):
        new_file.write(old_file.read())

    os.remove(old_file_name)
