from __future__ import annotations

from app.copy_content import manager_call


def move_file(command: str) -> None:
    split_cmd = command.split()
    if len(split_cmd) != 3 or "mv" not in split_cmd:
        raise ValueError("Wrong 'move' command input")

    cmd, source_file, moved_file = split_cmd
    path = ""
    if "/" not in moved_file:
        manager_call(source_file, moved_file, path)
        return

    if ".txt" in moved_file:
        for i in range(len(moved_file) - 1, 0, -1):
            if moved_file[i] == "/":
                path = moved_file[:i + 1]
                print(path)
                break
    else:
        path = moved_file
        moved_file += "/file2.txt"

    manager_call(source_file, moved_file, path)
