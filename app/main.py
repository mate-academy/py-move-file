import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()

    if (len(parts) != 3 or parts[0] != "mv"):
        raise ValueError(
            "Invalid command format. Expected: 'mv <source> <destination>'")

    source_file = parts[1]
    dest_file = parts[2]

    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"Source file '{source_file}' does not exist.")

    # determine destination directory and target file path
    if dest_file .endswith("/"):
        target_dir = dest_file .rstrip("/")
        target_file = os.path.join(target_dir, os.path.basename(source_file))
    else:
        target_dir = os.path.dirname(dest_file)
        target_file = dest_file

    # create directories recursively using os.mkdir segment by segment
    if target_dir:
        segments = target_dir.replace("\\", "/").split("/")
        current_path = ""
        for segment in segments:
            if not segment:
                continue
            current_path = os.path.join(current_path, segment) \
                if current_path \
                else segment
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    shutil.copyfile(source_file , target_file)
    os.remove(source_file)
