import os


def move_file(command: str) -> None:
    splitted_command = command.split(" ")

    if len(splitted_command) == 3:
        _, initial_file, destination_file = splitted_command

        if (
                splitted_command[0] == "mv"
                and os.path.exists(initial_file)
                and initial_file != destination_file
        ):
            destination_path = destination_file.split("/")
            current_path = "."
            for i in range(0, len(destination_path) - 1):
                current_path = os.path.join(current_path, destination_path[i])
                if not os.path.exists(current_path):
                    os.mkdir(current_path)

            final_file_name = os.path.basename(initial_file) \
                if destination_file[-1] == "/" else destination_path[-1]

            with (open(initial_file, "r") as old_file,
                  open(os.path.join(current_path, final_file_name), "w")
                  as new_file):
                new_file.write(old_file.read())

            os.remove(initial_file)
