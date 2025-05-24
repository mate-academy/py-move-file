import os


def move_file(command: str) -> None:
    if command:
        command_ = command.split()

        if len(command_) == 3 and command_[0] == "mv":
            source_file = command_[1]
            target_file = command_[2]

            if "/" in target_file and not target_file.endswith("/"):
                target_dirs = target_file.split("/")
                target_file_name = target_dirs.pop()
                target_path = ""

                for dir_ in target_dirs:
                    target_path = os.path.join(target_path, dir_)
                    try:
                        os.mkdir(target_path)
                    except FileExistsError:
                        print("Directory exists:", target_path)

                target_file = os.path.join(target_path, target_file_name)

            if source_file != target_file:
                with (open(source_file, "r") as file_in,
                      open(target_file, "w") as file_out):
                    for line in file_in:
                        file_out.write(line)

                os.remove(source_file)
