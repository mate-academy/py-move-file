import os


def move_file(command: str) -> None:  # mv file.txt some_dir/new_file.txt
    comman_parts = command.strip().split()

    if len(comman_parts) != 3 or comman_parts[0] != "mv":
        return

    source = comman_parts[1]
    destination = comman_parts[2]

    if destination.endswith("/"):
        destination_directory = destination.rstrip("/")
        destination_filename = ""
    else:
        parts = destination.rsplit("/", 1)
        if len(parts) == 2:
            destination_directory, destination_filename = parts
        else:
            destination_directory = ""
            destination_filename = parts[0]

    if destination_directory == "":
        try:
            os.rename(source, destination_filename)
            return
        except FileNotFoundError:
            return

    try:
        with open(source, "r") as f:
            content = f.read()
    except FileNotFoundError:
        return

    else:
        if destination_filename == "":
            destination_filename = source
        os.makedirs(destination_directory, exist_ok=True)
        with open(
            os.path.join(destination_directory, destination_filename), "w"
        ) as f:
            f.write(content)

    if os.path.exists(source):
        os.remove(source)
    else:
        print("File does not exist.")
