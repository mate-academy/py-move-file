import os


def move_file(command: str) -> None:
    destination = command.split()[2]
    if "/" in destination:
        directories = destination.split("/")[:-1]
        concurrent_dir = directories[0]
        for directory in directories[1:]:
            concurrent_dir = os.path.join(concurrent_dir, directory)
        try:
            os.makedirs(concurrent_dir)
        except FileExistsError:
            pass
    with (open(command.split()[1], "r") as old,
          open(destination, "w") as new):
        copied = old.read()
        new.write(copied)
    os.remove(command.split()[1])
