import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Input should consist of 3 parts: "
                         "command, source file, target file")
    else:
        command, source_file, target_file = command.split()

    if source_file == target_file:
        raise ValueError("Source file and target file must be difference")

    if command != "mv":
        raise ValueError("Command must be 'mv'")

    folders, file = os.path.split(target_file)
    if len(folders) != 0:
        os.makedirs(folders, exist_ok=True)

    with (
        open(source_file, "r") as file_in,
        open(target_file, "w") as file_out
    ):
        file_out.write(file_in.read())
    os.remove(source_file)
