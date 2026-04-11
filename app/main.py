import os


def move_file(command_line: str) -> None:
    commands = command_line.split(" ")
    if commands[0] == "mv" and len(commands) == 3:
        _, src_path, dest_path = commands

        if dest_path.endswith(("/", os.sep)):
            file_name = os.path.basename(src_path)
            dest_path = os.path.join(dest_path, file_name)

        dir_path = os.path.dirname(dest_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
            try:
                with (
                    open(dest_path, "wb") as f_dest,
                    open(src_path, "rb") as f_src,
                ) :
                    f_dest.write(f_src.read())
            except FileNotFoundError:
                print(f"File {src_path} not found")
            except Exception as e:
                print(f"Error: {e}")
            else:
                os.remove(src_path)
        else:
            os.rename(src_path, dest_path)
    else:
        print("Invalid command")
