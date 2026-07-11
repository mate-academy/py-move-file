import os


def move_file(command: str) -> None:
    command_components = command.split()
    if command.startswith("mv ") and len(command_components) == 3:
        mv, source, destination = command_components
        if "/" in destination:
            destination_path_components = destination.split("/")
            current_path = ""
            for folder in destination_path_components[:-1]:
                current_path = os.path.join(current_path, folder)
                if not os.path.exists(current_path):
                    os.mkdir(current_path)
            if destination.endswith("/"):
                destination += source

            with open(source, "r") as file_in, open(
                destination, "w"
            ) as file_out:
                file_out.write(file_in.read())

            os.remove(source)
        else:
            os.rename(source, destination)
