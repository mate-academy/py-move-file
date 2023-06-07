import os


def move_file(command: str) -> None:
    current_command, source_file, destination_file = command.split()
    if current_command == "mv":
        try:
            root = destination_file.split("/")
        except ValueError:
            pass
        else:
            current_dir = ""
            for dirrectory in root:
                if dirrectory != root[-1]:
                    current_dir += dirrectory
                    try:
                        os.mkdir(current_dir)
                    except FileExistsError:
                        pass
                    current_dir += "/"
        finally:
            with open(source_file) as first_file, \
                    open(destination_file, "w") as result_file:
                data = first_file.read()
                result_file.write(data)
            os.remove(source_file)
