import os


def move_file(command: str):
    cmd = command.split()
    if cmd[0] != "mv":
        return
    old_file_name = cmd[1]
    file_path = cmd[2].split("/")[:-1]
    new_file_name = "".join(cmd[2].split("/")[-1:])
    if len(file_path) == 0:
        os.renames(old_file_name, new_file_name)
        return
    elif len(file_path) == 1:
        os.mkdir(file_path[0])
    else:
        os.makedirs("/".join(file_path))
        with open(old_file_name, "r") as old_file:
            with open(f"{''.join(file_path)}"
                      f"/{new_file_name}", "w") as new_file:
                new_file.writelines(old_file.readlines())
    os.remove(old_file_name)


print(move_file("mv file.txt first_dir/second_dir/new_file.txt"))
