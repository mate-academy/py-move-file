import os


def move_file(cmd: str) -> None:
    cmd_split = cmd.split(" ")
    if len(cmd_split) != 3:
        return
    command, source, destination = cmd_split
    if command != "mv":
        return
    if destination.endswith("/"):
        destination = os.path.join(
            *destination.split("/"),
            os.path.basename(source)
        )
    path = ""
    if len(destination.split("/")) > 1:
        path = os.path.join(*destination.split("/")[:-1])
    if path and not os.path.exists(path):
        os.makedirs(path)
    with open(source, "r") as inf:
        with open(f"{destination}", "w") as of:
            of.write(inf.read())
    os.remove(source)
