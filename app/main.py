import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Bad command!")
    source = parts[1]
    destination = parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"{source} not found.")

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    destination_directory = os.path.dirname(destination)

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory, exist_ok=True)

    elif (os.path.exists(destination_directory)
          and not os.path.isdir(destination_directory)):
        raise FileExistsError(f"{destination_directory}"
                              f" exist, but is not directory.")

    if os.path.exists(destination):
        raise FileExistsError(f"{destination} already exist.")

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(destination, "w") as destination_file:
        destination_file.write(content)

    os.remove(source)
