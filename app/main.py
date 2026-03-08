import os


def move_file(command: str) -> None:
    files = command.split(" ")

    if len(files) != 3 or files[0] != "mv":
        return

    first_file = files[1]
    second_file = files[2]

    try:
        if second_file[-1] == "/":
            directories = second_file.split("/")
            directories = [directory for directory in directories if directory]
            current_path = ""

            for directory in directories:
                current_path = os.path.join(current_path, directory)
                if not os.path.exists(current_path):
                    os.mkdir(current_path)

            second_file = os.path.join(current_path, first_file)

        elif "/" in second_file and second_file[-1] != "/":
            directories = second_file.split("/")
            directories = directories[:-1]
            current_path = ""

            for directory in directories:
                current_path = os.path.join(current_path, directory)
                if not os.path.exists(current_path):
                    os.mkdir(current_path)

        with (open(first_file, "r") as file_in,
              open(second_file, "w") as file_out):

            file_out.write(file_in.read())

        os.remove(first_file)

    except FileNotFoundError:
        return
