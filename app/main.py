import os


def move_file(command: str) -> None:
    try:
        _command, file_in, file_out = command.split()

        if "/" in file_out:
            os.makedirs(os.path.dirname(file_out), exist_ok=True)

        with (open(file_in, "r") as f_in,
              open(file_out, "w") as f_out):

            file_content = f_in.read()
            f_out.write(file_content)

        os.remove(file_in)

    except ValueError as error:
        print(error)
    except OSError as error:
        print(error)
