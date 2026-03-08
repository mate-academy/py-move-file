import os


def move_file(command: str) -> None:
    files = command.split(" ")

    if len(files) != 3 or files[0] != "mv":
        return

    _, first_file, second_file = files
    target_dir = ""

    try:
        if second_file[-1] == "/":
            target_dir = second_file

        elif "/" in second_file and second_file[-1] != "/":
            target_dir = os.path.dirname(second_file)

        else:
            target_dir = None

        if target_dir:
            os.makedirs(target_dir, exist_ok=True)

        with (open(first_file, "r") as file_in,
              open(second_file, "w") as file_out):

            file_out.write(file_in.read())

        os.remove(first_file)

    except FileNotFoundError:
        return
