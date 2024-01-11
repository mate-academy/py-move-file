import os


def move_file(command: str) -> None:
    parts = command.split()
    if (len(parts) == 3
            and parts[0] == "mv"
            and parts[1] != parts[2]):
        way, name_file = os.path.split(parts[2])
        if way:
            os.makedirs(way, exist_ok=True)
        with (open(parts[1], "r") as source,
              open(parts[2], "w") as new_file):
            new_file.write(source.read())
        os.remove(parts[1])
