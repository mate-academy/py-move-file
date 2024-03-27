import os


def move_file(command: str) -> None:
    command = command.split()
    initial_file, destination = command[1], command[2]
    if "/" not in command[2]:
        os.rename(initial_file, destination)
        return
    with open(initial_file, "r") as file_in:
        content = file_in.read()
    os.remove(initial_file)
    path = destination.split("/")[:-1]
    step = ""
    for i in path:
        step += i + "/"
        if os.path.exists(step) is False:
            os.mkdir(step)
    with open(command[2], "w") as file_out:
        file_out.write(content)
