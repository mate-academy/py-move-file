import os


def command_validation(command: str) -> list[str]:
    args = command.split()
    if len(args) != 3:
        raise ValueError("Wrong number of arguments (3 needed)")

    cmd, origin, dest = args
    if cmd != "mv":
        raise ValueError("Invalid command (only mv supported)")
    if origin == dest:
        raise ValueError("Origin and destination must differ")

    return args


def create_directories(path: str) -> None:
    dir_path = os.path.dirname(path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)


def move_file(command: str) -> None:
    cmd, origin, dest = command_validation(command)

    try:
        create_directories(dest)
        with open(origin, "r") as origin_file, open(dest, "w") as dest_file:
            for line in origin_file:
                dest_file.write(line)

        os.remove(origin)

    except FileNotFoundError:
        print(f"File {origin} not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(f"Unexpected error: {e}")
