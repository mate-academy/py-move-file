import os

from app.cleaner import CleanUpFile


def move_file(command: str) -> None:
    command_split = command.split(" ")

    if len(command_split) != 3:
        return

    mv, original_file_name, new_destination = command_split

    if (mv != "mv" or os.path.abspath(original_file_name)
            == os.path.abspath(new_destination)
    ):
        return
    if not os.path.isfile(original_file_name):
       print(f"{original_file_name} does not exist")
       return

    new_destination_split = new_destination.split("/")
    new_path = ""
    new_name = original_file_name

    if ".txt" in new_destination_split[-1]:
        new_name = new_destination_split[-1]
        new_destination_split = new_destination_split[0:-1]

    for path_part in new_destination_split:
        new_path = os.path.join(new_path, path_part)
        os.makedirs(new_path, exist_ok=True)

    new_full_path = os.path.join(new_path, new_name)

    with CleanUpFile(original_file_name):
        with (
            open(original_file_name, "r") as old_file,
            open(new_full_path, "w") as new_file
        ):
            for line in old_file:
                new_file.write(line)
