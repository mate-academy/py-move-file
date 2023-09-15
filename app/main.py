import os


def move_file(command: str) -> None | str:
    if not command.startswith("mv "):
        print("write correct command: it should start with 'mv '")
        exit()
    if not len(command.split(" ")) == 3:
        print("write correct command: mv source_file destination_file")
        exit()
    source_name, dest_path = command[3:].split(" ")
    if os.path.sep in dest_path:
        dest_file = dest_path.rstrip("/").split("/")[-1]
        dest_dir = "/".join(dest_path.rstrip("/").split("/")[0:-1])
        if not os.path.exists(os.path.dirname(dest_path)):
            os.makedirs(dest_dir)
        with (
            open(source_name, "rb") as src_file,
            open(os.path.join(dest_dir, dest_file), "wb") as dest_file
        ):
            dest_file.write(src_file.read())
        os.remove(source_name)
    else:
        os.rename(source_name, dest_path)
