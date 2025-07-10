import os


def move_file(command: str) -> None:
    words = command.split()

    if len(words) != 3 or words[0] != "mv":
        return

    file_from, file_to = words[1:]

    if not os.path.isfile(file_from):
        return

    destination = os.path.dirname(file_to)

    if destination:
        os.makedirs(destination, exist_ok=True)

    if file_from == file_to:
        return

    try:
        with open(file_from, "r") as f_from, open(file_to, "w") as f_to:
            from_content = f_from.read()
            f_to.write(from_content)
    except FileNotFoundError:
        return
    finally:
        os.remove(file_from)
