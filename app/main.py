import os


def move_file(command: str) -> None:
    part_of_command = command.split()

    if len(part_of_command) != 3 or part_of_command[0] != "mv":
        print("Incorrect file format")
        return

    _, source_file, destination = part_of_command

    if "/" not in destination:
        os.rename(source_file, destination)
        print(f"File renamed to {destination}")
        return

    if "/" in destination:
        path_parts = destination.split("/")
        folder_path = "/".join(path_parts[:-1])

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        os.rename(source_file, destination)
        print(f"File moved to {destination}")

        if not os.path.exists(source_file):
            print(f"{source_file} successfully removed after moving.")

        with open(destination, "r") as destination_object:
            print(destination_object.read())
