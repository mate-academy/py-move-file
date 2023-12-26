from os import rename, mkdir, remove, path, getcwd


def move_file(command: str) -> None:
    if command[-1] != "/" and len(command.split()) == 3:
        command_part, source_file, destination_path = command.split()
        if command_part == "mv":
            if "/" not in destination_path:
                rename(source_file, destination_path)
                return
            destination_parts = destination_path.split("/")
            destination_file = destination_parts.pop(-1)
            check_path = getcwd()
            for part in destination_parts:
                check_path = path.join(check_path, part)
                if not path.exists(check_path):
                    mkdir(check_path)
                print(check_path)
            with (
                open(source_file, "r") as old_file,
                open(f"{check_path}/{destination_file}", "w") as new_file
            ):
                new_file.write(old_file.read())
            remove(source_file)
