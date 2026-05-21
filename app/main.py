import os


def move_file(command: str) -> None:
    pars_command = command.split(" ")

    if pars_command[0] != "mv":
        return "It`s not a command"

    if len(pars_command) != 3:
        return "Incorect command"

    if "/" not in pars_command[2]:
        os.rename(pars_command[1], pars_command[2])
        return

    source_file = pars_command[1]
    path = pars_command[2].split("/")
    new_file = path.pop()
    full_path = os.path.join(*path)

    content = ""
    with open(source_file, "r") as file:
        content = file.read()

    os.makedirs(full_path, exist_ok=True)

    new_file_path = os.path.join(full_path, new_file)

    with open(new_file_path, "w") as file:
        file.write(content)

    os.remove(source_file)
