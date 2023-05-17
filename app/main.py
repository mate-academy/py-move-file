import os


def move_file(command: str) -> None:
    if isinstance(command, str) and len(command.split()) == 3:
        cmd, source_path, destination_path = command.split()

        if cmd == "mv":

            if os.path.split(command)[0] == "":
                try:
                    os.rename(source_path, destination_path)
                except FileNotFoundError:
                    print(f"{source_path} not found")

            else:
                os.makedirs(os.path.split(destination_path)[0], exist_ok=True)
                with (
                    open(f"{source_path}", "r") as source_file,
                    open(f"{destination_path}", "w") as new_file
                ):
                    new_file.write(source_file.read())
                os.remove(source_path)
