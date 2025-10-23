import os


def move_file(command: str) -> None:
    divided_command = command.split()
    if not divided_command and len(divided_command) != 3:
        return
    user_command, source_filename, target_file_location = divided_command

    if user_command == "mv":
        with open(source_filename) as source_file:
            path = os.path.dirname(target_file_location)
            if not path:
                with open(target_file_location, "w") as file_out:
                    file_out.write(source_file.read())
                    os.remove(source_filename)
                    return

            os.makedirs(path, exist_ok=True)

            if target_file_location.endswith("/"):
                os.path.join(target_file_location, source_filename)

            with open(target_file_location, "w") as file_out:
                file_out.write(source_file.read())

            os.remove(source_filename)
