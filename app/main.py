import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        cheat, source_f, copy_path = command_list
        path = ""
        for value in copy_path.split("/"):
            if value.endswith("txt"):
                with open(copy_path, "w")as copy, open(source_f, "r")as source:
                    copy.write(source.read())
                    continue
            path += f"{value}/"
            if not os.path.exists(path):
                os.mkdir(path)
        os.remove(source_f)
