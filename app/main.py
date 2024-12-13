import os


def move_file(command: str) -> None:

    parts = command.split()

    if len(parts) == 3 and parts[0] == "mv":
        _, file_source, file_destination = parts

        if "/" in file_destination or "\\" in file_destination:
            way, name_file = os.path.split(file_destination)
            os.makedirs(way, exist_ok=True)

            with (
                open(file_source, "r") as file_in,
                open(file_destination, "w") as file_out
            ):
                file_out.write(file_in.read())
            os.remove(file_source)
        else:
            os.rename(file_source, file_destination)
