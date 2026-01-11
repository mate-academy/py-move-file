import os


def move_file(command: str) -> None:
    mv, file_to_move, new_file = command.split(" ")
    if mv != "mv" or file_to_move == new_file:
        print("Not mv command or the same file")
        return

    dir_list = new_file.split("/")
    current_path = ""
    for i in range(len(dir_list) - 1):
        current_path += dir_list[i] + "/"
        if os.path.isdir(current_path):
            continue
        os.mkdir(current_path)
    current_path += dir_list[len(dir_list) - 1]

    with open(file_to_move, "r") as f_from, open(current_path, "w") as f_to:
        content = f_from.read()
        f_to.write(content)

    os.remove(file_to_move)
