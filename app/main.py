import os


def move_file(command: str) -> None:
    com_ls = command.split()
    path = com_ls[2]
    sour_file = com_ls[1]
    path_ls = path.split("/")
    current_path = ""

    for i in path_ls[:-1]:
        current_path = os.path.join(current_path, i)
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    new_file_path = os.path.join(current_path, path_ls[-1])

    if path.endswith("/"):
        new_file_path = os.path.join(new_file_path, sour_file)

    with open(sour_file, "r") as file_in, open(new_file_path, "w") as new_file:
        new_file.write(file_in.read())

    os.remove(sour_file)
