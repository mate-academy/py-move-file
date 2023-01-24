import os


def move_file(command: str) -> None:
    cmd, current_file_name, new_path = command.split()
    new_file_name = new_path.split("/")[-1]
    new_dirs = new_path.split("/")[:-1]
    if len(new_dirs) > 1:
        os.makedirs(os.path.join(*new_dirs), exist_ok=True)

    with open(current_file_name, "r") as source,\
            open(os.path.join(*new_dirs, new_file_name), "w+") as new_path:
        read_current_file = source.read()
        print(read_current_file)
        new_path.write(read_current_file)
        if len(new_dirs) == 1:
            os.rename(current_file_name, new_file_name)
        new_path.seek(0)
        print(new_path.read())
        os.remove(current_file_name)
