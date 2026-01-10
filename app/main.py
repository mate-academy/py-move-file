import os.path
import shutil


def move_file(command: str) -> None:
    parsed_command = command.split()
    command_name = parsed_command[0]
    source_file = parsed_command[1]
    destination_file = parsed_command[2]

    src_file_path = os.path.abspath(source_file)
    dst_file_path = os.path.abspath(destination_file)

    if command_name == "mv":
        if os.path.exists(src_file_path) and not os.path.exists(dst_file_path):
            dir_path = os.path.dirname(dst_file_path)
            os.makedirs(dir_path, exist_ok=True)
            shutil.move(src_file_path, dst_file_path)
        else:
            raise Exception("""Check:
            - is source file exist
            - destination file not exist in destination directory
            - destination directory is exist""")
