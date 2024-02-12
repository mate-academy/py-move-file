import os


def move_file(parameter: str) -> None:
    filtered_param = parameter.replace("\\", "/")
    command, source_filename, destiny_file = filtered_param.split()
    if command == "mv":
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
