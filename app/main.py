import os


def move_file(command: str) -> None:
    split_command = command.split()
    old_filename = split_command[1]
    directories = split_command[2].split("/")
    new_filename = directories[-1]
    with open(old_filename) as old_file:
        reader = old_file.read()
    os.remove(old_filename)
    for direct_name in directories:
        if direct_name.endswith("_dir"):
            os.mkdir(direct_name)
            os.chdir(f"{os.getcwd()}/{direct_name}")
            continue
    with open(new_filename, "w") as new_file:
        new_file.write(reader)
