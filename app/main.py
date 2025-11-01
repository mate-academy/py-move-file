import os


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3:
        return

    cmd, source_file_name, destination_path = parts
    if cmd != "mv":
        return

    if destination_path.endswith(("/", "\\")):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_file_name)
        )

    if os.path.abspath(source_file_name) == os.path.abspath(destination_path):
        return

    destination_dir = os.path.dirname(destination_path)
    if destination_dir:

        norm_dir = os.path.normpath(destination_dir)
        drive, tail = os.path.splitdrive(norm_dir)
        root_prefix = os.path.sep if tail.startswith(os.path.sep) else ""
        tail = tail.lstrip(os.path.sep)

        current_path = drive + root_prefix
        for part in tail.split(os.path.sep):
            if not part:
                continue
            current_path = (os
                            .path
                            .join(current_path, part)
                            ) if current_path else part
            if not os.path.isdir(current_path):
                try:
                    os.mkdir(current_path)
                except FileExistsError:
                    pass

    with (open(source_file_name, "rb") as src_f,
          open(destination_path, "wb") as dst_f):
        while True:
            chunk = src_f.read(1024 * 1024)
            if not chunk:
                break
            dst_f.write(chunk)

    os.remove(source_file_name)
