import os


class CommandError(Exception):
    def __str__(self) -> str:
        return "Your command is not complete or invalid."


def move_file(command: str) -> None:
    try:
        copy_command, old_place, new_place = command.split(" ")
    except ValueError:
        raise CommandError

    if not os.path.isfile(old_place):
        raise FileNotFoundError(f"The source file"
                                f" '{old_place}' does not exist.")

    destination_path = ""

    if copy_command == "mv" and old_place != new_place:
        if new_place.endswith("/"):
            os.makedirs(new_place, exist_ok=True)
            destination_path += os.path.join(new_place,
                                             os.path.basename(old_place))
        else:
            dir_path = os.path.dirname(new_place)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
            destination_path += new_place

        try:
            with open(old_place, "rb") as src_file:
                with open(destination_path, "wb") as dest_file:
                    dest_file.write(src_file.read())
            os.remove(old_place)
            print(f"File '{old_place}' successfully"
                  f" moved to '{destination_path}'")
        except Exception as e:
            raise Exception(f"An error occurred"
                            f" while moving the file: {e}")
