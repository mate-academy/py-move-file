import os


def move_file(command_and_destination_file_path: str) -> None:
    cmd_dest_f_path = command_and_destination_file_path.split()
    source = cmd_dest_f_path[1]
    destination = cmd_dest_f_path[2]
    if "mv" in cmd_dest_f_path and len(cmd_dest_f_path) == 3:
        if "/" not in destination:
            os.rename(source, destination)
        elif "/" in destination:
            dir_names = []
            for name in destination.split("/")[:-1]:
                dir_names.append(name)
                if not os.path.exists("/".join(dir_names)):
                    os.mkdir("/".join(dir_names))
            os.rename(source, destination)
