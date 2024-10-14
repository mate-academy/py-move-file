import os.path
import shutil


def move_file(command: str) -> None:
    parsed_command = command.split()
    src_file = parsed_command[1]
    dst_file = parsed_command[2]

    src_file_path = os.path.abspath(src_file)
    dst_file_path = os.path.abspath(dst_file)

    if src_file_path != dst_file_path:
        dst_dir = os.path.dirname(dst_file_path)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        shutil.move(src_file_path, dst_file_path)
