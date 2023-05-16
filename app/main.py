import os


def move_file(command: str) -> None:
    cmd, source_path, destination_path = command.split(" ")

    if len(command.split()) == 3 and "mv" in cmd:

        if "/" not in destination_path:  # because name cannot contain "/"
            os.rename(source_path, destination_path)

        os.makedirs(os.path.split(destination_path)[0])
        with (
            open(f"{source_path}", "r") as source_file,
            open(f"{destination_path}", "w") as new_file
        ):
            new_file.write(source_file.read())
        os.remove(source_path)
