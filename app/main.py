import os


def move_file(command: str) -> None:
    if len(command) == 3:
        keyword, moving_file, path_to_file = command.split()
        if keyword == "mv" and path_to_file != moving_file:

            directories = os.path.split(path_to_file)[0]

            if directories:
                os.makedirs(directories, exist_ok=True)

            with (
                open(moving_file, "r") as file_in,
                open(path_to_file, "w") as file_out
            ):
                file_out.write(file_in.read())
            if os.path.exists(moving_file):
                os.remove(moving_file)
    else:
        raise ValueError("expected three commands")
