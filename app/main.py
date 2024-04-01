from os import mkdir, remove, path


def move_file(command: str) -> None:

    command_parts = command.split()
    if not len(command_parts) == 3 and command_parts[0] == "mv":
        raise Exception(f"Entered incorrect command {command}")
    with open(command_parts[1], "r") as main_file:
        content_of_file = main_file.read()

    dirs = command_parts[2]
    final_path = ""
    for file_dir in dirs.split("/")[:-1]:
        final_path += f"{file_dir}/"
        if not path.exists(final_path) is True:
            mkdir(final_path)
    with open(final_path + dirs.split("/")[-1], "w") as copied_file:
        copied_file.write(content_of_file)
        remove(command_parts[1])
