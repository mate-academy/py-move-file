import os


def move_file(parameters: str) -> None:
    if not parameters:
        return None

    command = parameters.split()

    if command[0] != "mv" or len(command) < 3:
        return None

    origin_file_name = command[1]
    new_file = command[2]

    try:
        directory = os.path.dirname(new_file)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(origin_file_name, "r") as origin, open(new_file, "w") as new:
            for line in origin:
                new.write(line)
        os.remove(origin_file_name)

    except FileNotFoundError:
        print(f"No such file or directory: {origin_file_name}")
