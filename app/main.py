import os


def move_file(command: str) -> None:
    command, existing_file, new_file = command.split()
    if len(new_file.split("/")) > 1:
        directories = new_file.split("/")
        path = ""
        for directory in directories[:-1]:
            path += f"{directory}/"
            os.mkdir(path)
        with open(existing_file, "r") as f:
            content = f.read()
            with open(f"{path}/{directories[-1]}", "w") as f:
                f.write(content)
        os.remove(existing_file)
    else:
        os.rename(existing_file, new_file)
