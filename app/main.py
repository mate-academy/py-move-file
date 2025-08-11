import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        return
    _, source_path, destination_path = command_list
    destination_dir = os.path.dirname(destination_path)
    if not destination_dir:
        try:
            with (open(source_path, "r") as f1,
                  open(destination_path, "w") as f2):
                f2.write(f1.read())
            os.remove(source_path)
        except FileNotFoundError as e:
            print(e)
    elif destination_dir:
        try:
            os.makedirs(destination_dir, exist_ok=True)
            with (open(source_path, "r") as f1,
                  open(destination_path, "w") as f2):
                f2.write(f1.read())
            os.remove(source_path)
        except FileNotFoundError as e:
            print(e)
        except FileExistsError as e:
            print(e)
        except PermissionError as e:
            print(e)
