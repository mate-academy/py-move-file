import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError(
            "three variables are needed to transfer a file"
        )

    command, source, target = parts
    if any((command != "mv", source == target)):
        raise ValueError(
            "to move the file you need to use the 'mv' command "
            "and write the target."
        )
    target_dir, target_file = os.path.split(target)
    if target_dir != "":
        os.makedirs(target_dir, exist_ok=True)

    with open(source, "r") as file1, open(target, "w") as file2:
        file2.write(file1.read())
    os.remove(source)
