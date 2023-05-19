import os


def move_file(command: str) -> None:
    if len(command.split(" ")) != 3 or command.split(" ")[0] != "mv":
        return
    file_orig, file_goal = command.split(" ")[1:]
    if "/" not in file_goal:
        os.rename(file_orig, file_goal)
        return
    if not file_goal.endswith("/"):
        *path, file_name = file_goal.split("/")
    else:
        path = file_goal[:-1].split("/")
    every_path_name = []
    for i in range(len(path)):
        every_path_name.append("/".join(path[:i + 1]))
    for directory in every_path_name:
        if not os.path.exists(directory):
            os.mkdir(directory)
    if not file_goal.endswith("/"):
        file_name = every_path_name[-1] + "/" + file_name
    else:
        file_name = every_path_name[-1] + "/" + file_orig
    with open(file_orig) as origin_file, open(file_name, "w") as new_file:
        new_file.write(origin_file.read())
    os.remove(file_orig)
