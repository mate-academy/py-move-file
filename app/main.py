import os


def move_file(command: str) -> None:

    command = command.split()
    print(command)

    if len(command) < 3 or command[0] != "mv":
        raise ValueError

    source_path = command[1]
    destination_path = command[2]

    separator = os.path.sep

    dir_path, destination_file_name = os.path.split(destination_path)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if separator not in destination_path:
        with (open(source_path, "r") as source_file,
              open(destination_path, "w") as destination_file):
            destination_file.write(source_file.read())

        os.remove(f"{source_file.name}")
        return

    with (open(f"{source_path}", "r") as source_file,
          open(destination_file_name, "w") as destination_file):

        destination_file.write(source_file.read())
        os.remove(f"{source_file.name}")
