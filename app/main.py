import os


def move_file(command: str) -> None:
    components = command.split()

    if len(components) == 3 and components[0] == "mv":

        source_file = components[1]
        destination_path = components[2]

        file_name, directory = os.path.split(destination_path)

        if not os.path.exists(source_file):
            return
        if directory:
            os.makedirs(directory, exist_ok=True)

        with (
            open(source_file, "r") as source,
            open(destination_path, "w") as destination
        ):
            destination.write(source.read())
            os.remove(source_file)


if __name__ == "__main__":
    move_file("mv source.txt destination_file/")
