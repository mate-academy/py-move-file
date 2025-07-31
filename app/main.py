import os


def move_file(command: str) -> None:
    input_filename = command.split(" ")[1]
    output_filename = command.split(" ")[2]

    if "/" in output_filename:
        os.makedirs("/".join(output_filename.split("/")[:-1]), exist_ok=True)

    with (
        open(input_filename, "r") as input_file,
        open(output_filename, "w") as output_file
    ):
        output_file.write(input_file.read())

    os.remove(input_filename)
