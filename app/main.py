import os


def move_file(command: str) -> None:

    if len(command.split()) == 3:
        action, file_name, path = command.split()
        if action == "mv":
            head, tail = os.path.split(path)
            with open(file_name) as file_to_read:
                current_path = os.getcwd()
                if head:
                    try:
                        current_path = os.path.join(current_path, head)
                        os.makedirs(current_path)
                    except OSError:
                        pass

                with (open(os.path.join(current_path, tail), "w")
                      as file_to_write):
                    file_to_write.write(file_to_read.read())

            os.remove(file_name)
