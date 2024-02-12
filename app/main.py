import os


def move_file(command: str) -> None:
    filtered_command = command.replace("\\", "/")
    param, source_filename, destiny_file = filtered_command.split()
    if param == "mv":
        destiny_folder = f"{os.sep}".join(destiny_file.split("/")[:-1:])
        output_filename = destiny_file.split("/")[-1]
        if destiny_folder:
            os.makedirs(os.path.join(destiny_folder), exist_ok=True)

        with open(source_filename, "r") as source_file:
            data = source_file.read()

        with open(
                file=os.path.join(destiny_folder, output_filename),
                mode="w"
        ) as output_file:
            output_file.write(data)
        os.remove(source_filename)
