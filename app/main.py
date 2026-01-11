from os import mkdir, path, remove


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError(
            "Command must be in the format: mv source_path dest_path"
        )

    mv, source_path, dest_path = parts

    if mv != "mv":
        raise ValueError("Invalid command. Only 'mv' command is supported.")

    current_path = ""

    for directory in dest_path.split("/")[:-1]:
        current_path = path.join(current_path, directory)
        print(current_path)
        if not path.exists(current_path):
            mkdir(current_path)

    with open(source_path, "r") as file1, open(dest_path, "w") as file2:

        content = file1.read()
        file2.write(f"{content}")

    remove(source_path)
