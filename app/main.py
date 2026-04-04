import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    command_mv, file, file_mv_to = parts

    if command_mv != "mv" or file == file_mv_to:
        return

    head, tile = os.path.split(file_mv_to)

    if not head:
        os.rename(file, file_mv_to)
        return

    os.makedirs(head, exist_ok=True)
    os.rename(file, file_mv_to)
