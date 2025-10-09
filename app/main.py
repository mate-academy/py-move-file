import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")
    if (len(command_parts) != 3
            or command_parts[0] != "mv"
            or not os.path.exists(command_parts[1])
            or not command_parts[1].endswith(".txt")
            or not command_parts[2].endswith(".txt")):
        return
    file_r = open(command_parts[1], "r")
    data = file_r.read()
    file_r.close()
    os.remove(command_parts[1])
    new_file_path = command_parts[2].split("/")
    if len(new_file_path) == 1:
        file_w = open(new_file_path[0], "w")
        file_w.write(data)
        file_w.close()
        return
    dir_path = ""
    for idx in range(len(new_file_path) - 1):
        dir_path += new_file_path[idx] + "/"
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    file_w = open("/".join(new_file_path), "w")
    file_w.write(data)
    file_w.close()
