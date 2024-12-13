import os


def move_file(command: str):
    command = command.split()
    file = command[1]
    direct = "../" + command[2]
    with open(f"../{file}", "r") as f:
        file_info = f.read()
    direct_ls = direct.split("/")[1:]
    new_direct = "../"
    for path_part in direct_ls:
        new_direct += f"{path_part}"
        try:
            with open(direct, "w") as file:
                file.write(file_info)
        except FileNotFoundError:
            os.mkdir(new_direct)
            new_direct += "/"
