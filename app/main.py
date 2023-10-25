import os


def move_file(command: str) -> None:
    tokens = command.split()

    if tokens[0] == "mv":
        source_file = tokens[1]
        target_path = tokens[2]

        #  simply renames the file
        if "/" not in target_path:
            if os.path.exists(source_file):
                os.rename(source_file, target_path)

        # create directories and file
        elif target_path.find("/"):

            last_slash_index = target_path.rfind("/")
            created_dir_name = target_path[:last_slash_index]

            if not os.path.exists(created_dir_name):
                os.makedirs(created_dir_name)

            with (
                open(source_file, "r") as file_out,
                open(target_path, "w") as file_in
            ):
                file_in.write(file_out.read())
            os.remove(source_file)
