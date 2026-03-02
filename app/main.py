import os


def move_file(command: str) -> None:
    command_log = command.split(" ")

    if len(command_log) == 3 and command.startswith("mv"):
        command_name, origin_file, created_path = command_log

        if os.path.isdir(created_path):
            final_path = os.path.join(created_path,
                                      os.path.basename(origin_file))
        else:
            final_path = created_path

        dir_part = os.path.dirname(final_path)
        if dir_part:
            os.makedirs(name=dir_part, exist_ok=True)

        with (open(origin_file, "r") as or_file,
              open(final_path, "w") as mov_file):
            mov_file.write(or_file.read())

        os.remove(origin_file)
