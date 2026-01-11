import os


def move_file(command: str) -> None:

    if len(command.split()) != 3:
        return
    cmd, source_name, destination_name = command.split()

    if cmd == "mv":
        list_dir, file_destination_name = os.path.split(destination_name)
        print(list_dir, file_destination_name)
        if list_dir:
            os.makedirs(list_dir, exist_ok=True)

        with (open(source_name) as f_source,
              open(destination_name, "w") as f_destination):
            buff = f_source.read()
            f_destination.write(buff)

        os.remove(source_name)
