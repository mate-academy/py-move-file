import os.path
import shutil


def move_file(command: str) -> None:
    parsed_command = command.split()
    cmd_name = parsed_command[0]
    src_file = parsed_command[1]
    dst_file = parsed_command[2]

    if cmd_name == "mv":
        src_file_path = os.path.abspath(src_file)
        dst_file_path = os.path.abspath(dst_file)

        if src_file_path != dst_file_path:
            dst_dir = os.path.dirname(dst_file_path)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)

            shutil.move(src_file_path, dst_file_path)
    else:
        "Command name is not correct!"
