import os
import shutil


def move_file(command: str) -> None | ValueError | FileExistsError:
    """
    Moves a file from a source to a destination,
    similar to the Linux `mv` command.

    The function takes a command in the format: 'mv <source> <destination>'.
    If the destination ends with '/', it will be treated as a directory,
    and the file will be moved or renamed inside that directory.
    If the destination does not exist, the function
    will create any necessary directories along the path.

    Args:
        command (str):
            The command string in the format 'mv <source> <destination>'.

    Raises:
        ValueError: If the command format is invalid.
        FileNotFoundError: If the source file does not exist.
    """

    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid format. Use: mv <source> <destination>")

    src_path, dest_path = parts[1:]

    if not os.path.isfile(src_path):
        raise FileNotFoundError(f"The file '{src_path}' does not exist.")

    dest_dir, dest_file = get_dir_and_file(dest_path)
    dest_file = dest_file if dest_file else os.path.basename(src_path)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    dest_path = os.path.join(dest_dir, dest_file)

    shutil.move(src_path, dest_path)


def get_dir_and_file(path: str) -> tuple[str, str]:
    """
    Splits a given path into directory and file components.

    Args:
        path (str): The full path to be split.

    Returns:
        tuple[str, str]:
            A tuple where the first element is the directory part
            and the second element is the file name.
            If no file is provided, the second element will be an empty string.
    """
    dirs = os.path.dirname(path)
    file_name = os.path.basename(path)
    return dirs, file_name
