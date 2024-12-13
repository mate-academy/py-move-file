import os


def move_file(command: str) -> None:
    cmd, src_path, dst_path = command.split()
    if cmd == "mv":
        if "/" not in dst_path:
            os.rename(src_path, dst_path)

        dir_path, file_name = os.path.split(dst_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        new_file = os.path.join(dir_path, file_name)
        with (
            open(src_path, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
        os.remove(src_path)
