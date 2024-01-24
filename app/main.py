import os


def move_file(command: str) -> None:
    split_command = command.split()
    source_path = split_command[1]
    destination_path = split_command[2]
    if (len(split_command) == 3
            and source_path != destination_path
            and split_command[0] == "mv"):

        destination_directory, file_name = os.path.split(destination_path)

        if destination_directory:
            os.makedirs(destination_directory, exist_ok=True)

        with (open(source_path, "r") as source_file,
              open(destination_path, "w") as destination_file):
            destination_file.write(source_file.read())

        os.remove(source_path)
