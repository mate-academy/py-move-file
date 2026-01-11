import os


def move_file(command: str) -> None | str:

    if len(command.split()) == 3:
        action, file_name, path = command.split()
        if file_name == path:
            return ("Are you kidding? "
                    "Are you really gonna move file to itself? :)")
        if action == "mv":
            head = os.path.split(path)[0]
            if head:
                os.makedirs(os.path.join(os.getcwd(), head), exist_ok=True)

            with (open(path, "w") as file_to_write,
                  open(file_name) as file_to_read):
                file_to_write.write(file_to_read.read())

            os.remove(file_name)
