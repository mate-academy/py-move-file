import os


def move_file(command: str) -> None:
    try:
        _, source, destination = command.split()
    except ValueError as e:
        print("Incorrect command specified: ", e)
    else:
        if _ == "mv" and source != destination:
            directory_path = os.path.dirname(destination)

            if directory_path != "" and not os.path.exists(directory_path):
                os.makedirs(directory_path)

                with (open(source, "r") as file,
                      open(destination, "w") as moved_file
                      ):
                    moved_file.write(file.read())
                os.remove(source)

            else:
                os.rename(source, destination)
