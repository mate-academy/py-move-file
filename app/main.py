import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) == 3 and command[0] == "mv":
        with open(command[1], "r") as file_to_delete:
            context = file_to_delete.read()

            os.remove(command[1])

            if "/" in command[2]:

                dirs_to_create = "/".join(command[2].split("/")[:-1])
                file_to_create = command[2].split("/")[-1]

                os.makedirs(dirs_to_create, exist_ok=True)

                with open(
                        dirs_to_create + "/" + file_to_create, "w"
                ) as file:
                    file.write(context)

            else:
                with open(command[2], "w") as file:
                    file.write(context)
