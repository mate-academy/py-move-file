import os


def move_file(command: str) -> None:
    files = command[3:].split(" ")
    source_name = files[0]
    dest_path = files[1]
    if "/" in dest_path:
        dest_file = dest_path.rstrip("/").split("/")[-1]
        dest_dir = "/".join(dest_path.rstrip("/").split("/")[0:-1])
        if not os.path.exists(os.path.dirname(dest_path)):
            os.makedirs(dest_dir)
        with (
            open(source_name, "rb") as src_file,
            open(f"{dest_dir}/{dest_file}", "wb") as dest_file
        ):
            dest_file.write(src_file.read())
        os.remove(source_name)
    else:
        os.rename(source_name, dest_path)


# move_file("mv file.txt first/file.txt")
