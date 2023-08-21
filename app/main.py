import os


def move_file(command: str) -> None | str:
    # Split the command by 3 aspects
    command, source_file, target = command.split()
    # Check that command is "mv"
    if command != "mv":
        return f"'{command}' is incorrect"
    # Check if target has path or it's just file
    if "/" in target:

        path, moved_file = os.path.split(target)
        os.makedirs(path, exist_ok=True)

        with (open(source_file, "r") as sf, open(target, "w") as nf):
            nf.write(sf.read())

        os.remove(source_file)
    # if it's file, rename it
    else:
        os.rename(source_file, target)
