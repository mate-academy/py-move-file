import os


def move_file(command: str) -> None | str:
    command, source_file, target = command.split()
    if command != "mv":
        return f"'{command}' is incorrect"
    if "/" in target:

        path, moved_file = os.path.split(target)
        os.makedirs(path, exist_ok=True)

        with (open(source_file, "r") as sf, open(target, "w") as nf):
            nf.write(sf.read())

        os.remove(source_file)
    else:
        os.rename(source_file, target)
