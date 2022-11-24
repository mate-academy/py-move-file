import os


def move_file(command: str) -> None:
    if command.split()[0] != "mv":
        return

    if "/" not in command:
        os.rename(command.split()[1], command.split()[2])

    command_parsed = command.split()
    new_directories_and_file_parsed = command_parsed[-1].split("/")
    path_to_new_final_directory = \
        "/".join(new_directories_and_file_parsed[:-1])
    new_file_name = new_directories_and_file_parsed[-1]

    if not os.path.exists(path_to_new_final_directory):
        os.makedirs(path_to_new_final_directory)

    path_to_new_file = \
        os.path.join(path_to_new_final_directory, f"{new_file_name}")
    with open(command_parsed[1], "r") as original_file, \
            open(path_to_new_file, "w") as moved_file:
        for line in original_file:
            moved_file.write(line)

    os.remove(command_parsed[1])
