import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3:
        mv_cmd, moving_file, move_file_to = split_command
        if mv_cmd == "mv":
            if "/" not in move_file_to:
                os.rename(moving_file, move_file_to)
            else:
                *directories, _ = move_file_to.split("/")
                os.makedirs("/".join(directories), exist_ok=True)

                with (open(moving_file, "r") as source_file,
                      open(move_file_to, "w") as end_file):
                    end_file.write(source_file.read())
                os.remove(moving_file)
