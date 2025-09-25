import os


def move_file(command: str) -> None:
    first_split = command.split()
    if len(first_split) == 3:
        command, original_file, dir_and_new_file = first_split
    else:
        return

    if (
            command == "mv"
            and os.path.exists(original_file)
    ):
        second_split = dir_and_new_file.split(os.path.sep)
        new_file = second_split[-1]
        second_split.remove(new_file)

        if original_file == new_file:
            os.rename(original_file, new_file)
            os.remove(original_file)
            return

        current_path = ""

        for item in second_split:
            current_path = os.path.join(current_path, item) if current_path else item

            if not os.path.exists(current_path):
                os.mkdir(current_path)

        new_file = os.path.join(current_path, new_file)

        with (
            open(original_file, "rb") as original,
            open(new_file, "wb") as new
        ):
            new.write(original.read())

        os.remove(original_file)
