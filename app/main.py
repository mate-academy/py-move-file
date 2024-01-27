import os


def move_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) == 3 and split_command[0] == "mv":
        source_path, destination_path = split_command[1], split_command[2]

        if source_path != destination_path:
            destination_directory, _ = os.path.split(destination_path)

            if destination_directory:
                os.makedirs(destination_directory, exist_ok=True)

            with (open(source_path, "r") as source_file,
                  open(destination_path, "w") as destination_file):
                destination_file.write(source_file.read())

            os.remove(source_path)
        else:
            print("Source and destination paths are the same.")
    else:
        print("Invalid command format. "
              "Usage: move_file mv <source_path> <destination_path>")
