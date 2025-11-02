from os import remove, mkdir, path, sep


def move_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) == 3 and command_parts[0] == "mv":
        file_in, file_out = command_parts[1:]
        if file_in != file_out:
            dir_path, file_name = path.split(file_out)
            if not file_name:
                file_out = path.join(file_out, file_in)
            if dir_path:
                path_parts = dir_path.split(sep)
                make_dir = ""
                for catalogue in path_parts:
                    make_dir = path.join(make_dir, catalogue)
                    if not path.exists(make_dir):
                        mkdir(make_dir)
            try:
                with (
                    open(file_in) as source_file,
                    open(file_out, "w") as target_file
                ):
                    target_file.write(source_file.read())
                    remove(file_in)
            except FileNotFoundError:
                pass


move_file("mv new/dir/test.txt /")