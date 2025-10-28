import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3 and command_split[0] == "mv":
        mv, source_file, destination_file = command_split
    else:
        raise ValueError("Invalid command")
    if destination_file.endswith("/"):
        destination_file = (os.path.join
                            (destination_file,
                             os.path.basename(source_file))
                            )
    dir_name = os.path.dirname(destination_file)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(source_file, "r") as file1, open(destination_file, "w") as file2:
        file_content = file1.read()
        file2.write(file_content)
    os.remove(source_file)
