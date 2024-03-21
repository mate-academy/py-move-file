import os


def move_file(command: str) -> None:
    commands = command.split()
    input_file = commands[1]
    output_file = commands[2]
    with open(input_file, "r") as input_data:
        input_content = input_data.read()
    if "/" in output_file:
        output_directory = os.path.dirname(output_file)
        os.makedirs(output_directory, exist_ok=True)
        with open(output_file, "w") as output_data:
            output_data.write(input_content)
        os.remove(input_file)
    else:
        os.rename(input_file, output_file)
