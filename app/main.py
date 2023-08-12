import os


def move_file(command: str) -> None:
    command, file_in, file_out = command.split()

    if command == "mv" and file_in != file_out:
        path = file_out.split("/")[:-1]

        for num in range(1, len(path) + 1):
            """I think, it was easier to make it with
            os.makedirs(exist_ok=True), but
            as task asks to use os.mkdir, I did it with os.mkdir :("""
            dir_path = os.path.join(*path[:num])
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

        with (open(file_in) as old_file,
              open(file_out, "w") as new_file):
            new_file.write(old_file.read())

        os.remove(file_in)
