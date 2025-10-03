import os


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) == 3 and commands[0] == "mv":
        directories = commands[2].split("/")
        if len(directories) > 1:
            path_to_dir = ""
            for i in range(len(directories) - 1):
                if i == 0:
                    os.mkdir(directories[i])
                else:
                    path_to_dir = os.path.join(path_to_dir, directories[i])
                    os.mkdir(path_to_dir)

        with open(commands[1]) as file_to_read:


