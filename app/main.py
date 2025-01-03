import os
import platform


def get_sys_delimiter() -> str:
    sys_name = platform.system()
    if sys_name == "Windows":
        return "\\"
    return "/"


# def change_sys_delimiter(path: str) -> str:
#     cur_os_delimiter = get_sys_delimiter()
#     other_delimiter = "/" if cur_os_delimiter == "\\" else "/"
#     return path.replace(other_delimiter, cur_os_delimiter)


def check_intput(command: str, src: str, dest: str) -> tuple:
    if not command == "mv":
        raise ValueError("Command should be mv...")
    if len(src) == 0:
        raise ValueError("Src is too short")
    if len(dest) == 0:
        raise ValueError("Destination is too short")
    cur_os_delimiter = get_sys_delimiter()
    other_delimiter = "/" if cur_os_delimiter == "\\" else "/"
    if not dest.count(other_delimiter) == 0:
        dest = dest.replace(other_delimiter, cur_os_delimiter)
    return command, src, dest


def move_file(command_line: str) -> None:
    command, src, dest = command_line.split(" ")
    command, src, dest = check_intput(command, src, dest)
    sys_delimiter = get_sys_delimiter()

    # mv in current dir
    if dest.count(sys_delimiter) == 0:
        os.rename(src, dest)
        return

    *dirs, file_name = dest.split(sys_delimiter)
    # create dirs
    path = ""
    for folder in dirs:
        path += f"{folder}{sys_delimiter}"
        if os.path.exists(path):
            continue
        os.mkdir(path)
    # create file and write
    with open(src, "r") as src_file, \
            open(f"{path}{file_name}", "w") as file_dest:
        content = src_file.read()
        file_dest.write(content)
    # remove file
    os.remove(src)
