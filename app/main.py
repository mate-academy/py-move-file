import os


def move_file(command: str):
    command = command.split()
    file = command[1]
    direct = command[2]
    with open(f"..\\{file}", "r") as f:
        file_info = f.read()
    direct_ls = direct.split("/")
    direct = direct.replace("/", "//")
    new_direct = ""
    for i in direct_ls:
        new_direct += f"{i}"
        try:
            with open(direct, "w") as f:
                f.write(file_info)
        except FileNotFoundError:
            os.mkdir(new_direct)
            new_direct += "\\"


