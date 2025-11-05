import os


def move_file(command: str) -> None:
    if (
            len(cmd_chain := command.split(" ")) == 3
            and cmd_chain[0] == "mv"
            and os.path.exists(cmd_chain[1])
            and not cmd_chain[2].startswith("-")
    ):
        source, destination = cmd_chain[1], cmd_chain[2]
        parent = os.path.dirname(destination)
        basename = os.path.basename(source)

        if parent:
            os.makedirs(parent, exist_ok=True)

        if not basename or os.path.isdir(destination):
            destination = os.path.join(destination, os.path.basename(source))

        with (
            open(source, "rb") as file_in,
            open(destination, "wb") as file_out
        ):
            file_out.write(file_in.read())

        os.remove(source)
