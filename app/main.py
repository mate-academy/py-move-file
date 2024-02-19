import os


def move_file(command: str) -> None:
    commands = command.split(" ")
    if len(commands) == 3 and commands[0] == "mv" and os.path.exists(commands[1]):
        destination = commands[2]
        new_file = destination.split("/")[len(destination.split("/")) - 1]
        target_directory = os.path.join(
            destination.replace(f"{new_file}", ""))
        if len(target_directory) != 0:
            os.makedirs(target_directory, exist_ok=True)
        with (open(commands[1], "r") as file,
              open(destination, "w") as moved):
            moved.write(file.read())
        os.remove(commands[1])
