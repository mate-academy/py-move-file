import os


def move_file(command: str) -> None:
    part = command.split()
    first_file = part[1]
    second_file = part[2]
    if first_file != second_file and part[0] == "mv":
        if os.path.exists(first_file):
            if "/" in second_file:
                directories = second_file.split("/")
                directories = directories[0:len(directories) - 1]
                current = ""
                for directory in directories:
                    current += directory
                    if not os.path.exists(current):
                        os.mkdir(current)
                    current += "/"

            with (open(part[1], "r") as old,
                  open(part[2], "w") as new):
                new.write(old.read())

            os.remove(first_file)
