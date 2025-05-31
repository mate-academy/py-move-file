import os


def move_file(command: str) -> None:
    if len(command.strip()) == 0:
        raise ValueError("Enter file name!")

    command_list = command.split()
    source = command_list[1]  # изначальный файл
    target = command_list[2]  # файл который создаем

    if len(command_list) != 3:
        raise ValueError("Command must be in format: mv source target!")
    if command_list[0] != "mv":
        raise ValueError("Command must been have: mv!")

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist!")

    if command_list[0] == "mv" and len(command_list) == 3:
        if "/" not in target:
            try:
                with open(
                        source, "r"
                ) as file_in, open(
                    target, "w"
                ) as file_out:
                    file_out.write(file_in.read())
                os.remove(source)
                return
            except Exception as e:
                raise e
        if target.endswith("/"):
            new_name = os.path.basename(source)
            target_path = os.path.join(target, new_name)
        else:
            target_path = target

        dir_path = os.path.dirname(target_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)

        try:
            with open(
                    source, "r"
            ) as file_in, open(
                target_path, "w"
            ) as file_out:
                file_out.write(file_in.read())
            os.remove(source)
        except Exception as e:
            raise e
