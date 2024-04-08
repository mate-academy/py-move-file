import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "mv":
        _, file_source, path_another_file, *_ = parts
        folders, new_name = os.path.split(path_another_file)

        if folders:
            if file_source == new_name:
                return

            os.makedirs(folders, exist_ok=True)

            with (
                open(file_source, "r") as source,
                open(os.path.join(folders, new_name), "w") as moved
            ):
                moved.write(source.read())
            os.remove(file_source)
            return
        os.rename(file_source, new_name)
