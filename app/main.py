import os


def move_file(command: str) -> None:
    try:
        mv, source, destination = command.split()
    except ValueError:
        print("Wrong argument")
    else:
        if mv != "mv" or not os.path.exists(source):
            return

        dirs_and_file_name = destination.split(os.path.sep)
        dirs, file_name = dirs_and_file_name[:-1], dirs_and_file_name[-1]

        if dirs:
            to_join = os.path.sep.join(dirs)
            os.makedirs(to_join, exist_ok=True)
            file_name = os.path.join(to_join, file_name)

        with (open(source, "r") as file_in,
              open(file_name, "w") as file_out):
            text_to_copy = file_in.read()
            file_out.write(text_to_copy)
        os.remove(source)
