import os


def move_file(command: str) -> None:
    command_split = command.split()
    if command_split[0] == "mv" and "/" in command_split[2]:
        directory = command_split[2].split("/")
        current_directory = ""
        for subdirectory in directory:
            current_directory = os.path.join(subdirectory, current_directory)
            os.mkdir(current_directory)
        with open(command_split[1], "r") as source_file, \
                open(current_directory, "w") as new_file:
            new_file.write(source_file.read())
        os.remove(command_split[1])
    elif command_split[0] == "mv" and len(command_split) == 3:
        os.rename(command_split[1], command_split[2])
