import os


def move_file(command: str) -> None:
    command = command.split()
    route = command[2].split("/")
    if command[0] != "mv":
        return
    if len(route) > 1:
        route.pop()
    else:
        new_file_name = route[0]
        with (
            open(command[1], "r") as file_in,
            open(new_file_name, "x") as file_out,
        ):
            file_out.write(file_in.read())
        os.remove(command[1])
        return
    for directory in route:
        if not os.path.exists(directory):
            os.mkdir(directory)
        os.chdir(directory)
    for _ in range(len(route)):
        os.chdir("..")
    os.rename(command[1], command[2])
