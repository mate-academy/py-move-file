import os


def move_file(command: str) -> None:
    try:
        _, file_in, file_out = command.split()

        if os.path.exists(file_in) is False:
            raise FileNotFoundError
        if "/" in file_out:
            os.makedirs(os.path.dirname(file_out), exist_ok=True)

        with (open(file_in, "r") as f_inp,
              open(file_out, "w") as f_out):

            file1 = f_inp.read()
            f_out.write(file1)

        os.remove(file_in)

    except ValueError:
        print("Incorrect command format. Expected: move <source> <destination>")
    except FileNotFoundError as error:
        print(error, "File not found")
    except OSError as error:
        print(error)

