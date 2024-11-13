import os


def move_file(command: str) -> None:
    command_listed = command.split(" ")
    source_file = command_listed[1]

    if command_listed[0] != "mv" or len(command_listed) != 3:
        return

    file_path, file_name = os.path.split(command_listed[2])

    if file_path:
        os.makedirs(file_path, exist_ok=True)

    if source_file != command_listed[2]:

        with open(f"{source_file}", "r") as f:
            info = f.read()

        with open(os.path.join(file_path, file_name), "w") as nf:
            nf.write(info)

        os.remove(source_file)

    else:
        os.rename(source_file, file_name)
