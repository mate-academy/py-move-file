from os import mkdir, path, remove


def move_file(command: str) -> None:
    action, file_out, file_in = command.split()

    if action != "mv":
        raise ValueError("Wrong command")

    *folders, new_file_name = file_in.split("/")
    new_file_path = ""
    for folder in folders:
        new_file_path = path.join(new_file_path, folder)
        mkdir(new_file_path)

    with open(file_out, "r") as original_file, open(file_in, "a") as new_file:
        for line in original_file:
            new_file.write(line)
        remove(file_out)
