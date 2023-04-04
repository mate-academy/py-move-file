import os


def move_file(command: str) -> None:
    splitted_command = command.split()
    if "/" not in splitted_command[-1]:
        comm, old_name, new_name = splitted_command
        os.rename(old_name, new_name)
    else:
        name_dir, new_file_name = splitted_command[-1].rsplit("/", maxsplit=1)
        old_file_name = splitted_command[1]
        os.makedirs(name_dir, exist_ok=True)

        new_dir = name_dir + "/" + new_file_name
        with (open(old_file_name, "r") as old_file,
              open(new_dir, "w") as new_file):
            new_file.write(old_file.read())
        os.remove(old_file_name)
