import os


def move_file(command: str) -> None:
    splitted_command = command.split()
    if len(splitted_command) == 3:
        if splitted_command[0] == "mv":
            mv, src, dest = splitted_command

            if dest.endswith("/"):
                dest = os.path.join(dest, os.path.basename(src))

            directory = os.path.dirname(dest)

            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            with open(src, "rb") as first_src:
                with open(dest, "wb") as first_dst:
                    first_dst.write(first_src.read())

            os.remove(src)
