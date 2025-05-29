import os


def move_file(command: str) -> None:
    src_file = command.split()[1]
    destination = command.split()[2]
    command = command.split()[0]
    directory_path = ""

    directories = destination.split("/")
    # des_file = directories[-1]

    directories.pop()

    if (command == "mv" and os.path.exists(src_file)):
        if "/" not in destination:
            os.rename(src_file, destination)
        else:
            for directory in directories:
                directory_path += f"{directory}/"
                if not os.path.exists(directory_path):
                    os.mkdir(directory_path)

            if not os.path.exists(destination):
                with (open(src_file, "r") as src_f,
                      open(destination, "w")as des_f):
                    des_f.write(src_f.read())
                os.remove(src_file)
