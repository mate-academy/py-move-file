import os


def move_file(command: str) -> None:
    command_split = command.split()

    if len(command_split) == 3:
        action, file_in, file_out = command_split

        if action == "mv":
            file_out_path = file_out.split("/")

            if file_out_path[-1] != "":
                os.rename(file_in, file_out_path[-1])

            if len(file_out_path) > 1:
                file_directory = file_out_path[:-1]
                new_directory = "/".join(file_directory)

                for i in range(len(file_directory)):
                    try:
                        os.mkdir("/".join(file_directory[:i]))
                    except FileExistsError:
                        pass

                os.rename(file_out_path[-1], os.path.join(new_directory, file_out_path[-1]))
