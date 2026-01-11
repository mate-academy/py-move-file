from os import mkdir, remove, rename, path


def move_file(command: str) -> None:
    cmd_list = command.split()
    source = cmd_list[1]
    destination = cmd_list[2]
    if (len(cmd_list) != 3
            or not cmd_list[0].startswith("mv")
            or source == destination
            or not path.isfile(source)):
        return

    if "/" not in command and not path.isfile(destination):
        rename(source, destination)
        return

    dir_path = ""
    if destination.endswith("/"):
        for dir_item in destination.split("/"):
            dir_path = path.join(dir_path, dir_item)
            if not path.isdir(dir_path):
                mkdir(dir_path)
        dest_file = path.join(dir_path, path.basename(source))
    else:
        for dir_item in path.dirname(destination).split("/"):
            dir_path = path.join(dir_path, dir_item)
            if not path.isdir(dir_path):
                mkdir(dir_path)
        dest_file = destination

    with (open(source, "r") as file_in, open(dest_file, "w") as file_out):
        file_out.writelines(file_in)
    remove(source)
