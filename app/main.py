import os


def move_file(command: str) -> None:
    commands = command.split(" ")
    destination = commands[2].split("/")
    new_file = destination.pop()
    target_directory = ""
    if len(commands) == 3:
        if commands[0] == "mv":
            for folder in destination:
                target_directory += folder + "/"
                if os.path.isdir(target_directory):
                    continue
                os.mkdir(target_directory)
    with (open(commands[1], "r") as file,
          open(target_directory + new_file, "w") as moved):
        moved.write(file.read())
    os.remove(commands[1])
