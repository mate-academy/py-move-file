import os.path
import shutil


def move_file(command: str) -> None:
    parsed_command = command.split()
    cmd_name = parsed_command[0]
    src_file = parsed_command[1]
    dst_file = parsed_command[2]

    src_file_path = os.path.abspath(src_file)
    dst_file_path = os.path.abspath(dst_file)

    if cmd_name == "mv":
        if os.path.exists(src_file_path) and not os.path.exists(dst_file_path):
            dir_path = os.path.dirname(dst_file_path)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
            shutil.move(src_file_path, dst_file_path)
        else:
            print("""Check:
            - is source file exist
            - destination file not exist in destination directory
            - destination directory is exist""")
