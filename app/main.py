import os


def move_file(command: str) -> None:
    command_mv, file, file_mv_to = command.split()

    if command_mv != "mv":
        return

    head, tile = os.path.split(file_mv_to)

    if not head:
        os.rename(file, file_mv_to)
        return

    os.makedirs(head, exist_ok=True)
    os.rename(file, file_mv_to)
