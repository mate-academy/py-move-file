import os

from app.cleaner import CleanUpFile


def move_file(command: str) -> None:
    command_split = command.split(" ")

    if len(command_split) != 3:
        return

    mv, original_file_name, new_destination = command_split

    if mv != "mv" or original_file_name == new_destination:
        return
    try:
        with open(original_file_name, "r"):
            pass
    except FileNotFoundError:
        print(f"{original_file_name} does not exist")
        return
    print("new dest ", new_destination)
    new_destination_split = new_destination.split("/")
    new_path = ""
    new_name = original_file_name

    if ".txt" in new_destination_split[-1]:
        new_name = new_destination_split[-1]
        new_destination_split = new_destination_split[0:-1]
    print("newname ", new_name)
    print("newdestsplit ", new_destination_split)
    for path_part in new_destination_split:
        new_path = os.path.join(new_path, path_part)
        print("new_path in loop ", new_path)
        if not os.path.isdir(new_path):
            os.mkdir(new_path)

    new_full_path = os.path.join(new_path, new_name)

    with CleanUpFile(original_file_name):
        with (
            open(original_file_name, "r") as old_file,
            open(new_full_path, "w") as new_file
        ):
            for line in old_file:
                new_file.write(line)
