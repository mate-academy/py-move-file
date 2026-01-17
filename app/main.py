import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) < 3:
        print("Not enough arguments")
        return
    cd, source_name, target_name, *_ = command_parts
    if cd != "mv":
        return

    if "/" in target_name:
        target_dir, file_name = os.path.split(target_name)
        os.makedirs(target_dir, exist_ok=True)

        target_name = os.path.join(target_dir, file_name)
    try:
        with open(source_name, "rb") as source_file:
            with open(target_name, "wb") as target_file:
                target_file.write(source_file.read())

        os.remove(source_name)

    except FileNotFoundError:
        print(f"File not found: {source_name}")
