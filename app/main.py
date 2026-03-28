import os


def move_file(command: str) -> None:
    parts = command.split()

    if (len(parts) == 3
            and parts[0] == "mv"
            and parts[1] != parts[2]):

        with open(parts[1], "r") as file_in:
            head_tail = os.path.split(parts[2])
            if head_tail[0] != "":
                os.makedirs(head_tail[0], exist_ok=True)

            with open(parts[2], "w") as new_file:
                new_file.write(file_in.read())

        os.remove(parts[1])
