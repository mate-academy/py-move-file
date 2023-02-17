import os


class DirectoryExistError(Exception):

    def __init__(self, path: str) -> None:
        self.path = path

    def __str__(self) -> str:
        return f"Directory with path {self.path} is already exist!"


def move_file(command: str) -> None:
    input_command, path_file_in, path_file_out = command.split(" ")

    if input_command != "mv":
        return

    if ("/" or "\\") not in path_file_out:
        os.rename(path_file_in, path_file_out)
        return

    absolute_file_in = os.path.join(os.getcwd(), path_file_in)
    output_directory_path = os.path.join(
        os.getcwd(), "\\".join(path_file_out.split("/")[:-1])
    )
    output_directory_file_path = os.path.join(os.getcwd(), path_file_out)

    try:
        if os.path.exists(output_directory_path):
            raise DirectoryExistError(output_directory_path)
    except DirectoryExistError as e:
        print(e)
    else:
        os.makedirs(output_directory_path)

    with (
        open(absolute_file_in, "r") as file_in,
        open(output_directory_file_path, "w") as file_out,
    ):
        read_content = file_in.read()
        file_out.write(read_content)

    os.remove(absolute_file_in)
