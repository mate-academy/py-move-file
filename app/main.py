import os


def move_file(command: str) -> None:
    command_split = command.split()

    if len(command_split) == 3:
        action, file_in, file_out = command_split

        if action == "mv":
            file_out_path = file_out.split("/")[:-1]
            file_in_content = open(file_in, "r").read()
            os.remove(file_in)

            if len(file_out_path) > 0:

                for i in range(1, len(file_out_path) + 1):
                    try:
                        os.mkdir(os.path.join(file_out_path[:i]))
                    except FileExistsError:
                        continue

            with open(file_out, "w") as file_out:
                file_out.write(file_in_content)
