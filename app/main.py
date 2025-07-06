import os


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) < 3:
        return None
    move_command, input_file_name, output_file_path_with_name = commands
    if move_command != "mv":
        return None

    file_path_list = output_file_path_with_name.split("/")
    output_file_name = file_path_list[-1]

    if len(file_path_list) > 1:
        output_file_path = output_file_path_with_name.rstrip(output_file_name)
        os.makedirs(output_file_path, exist_ok=True)

    try:
        with open(input_file_name, "r") as file_in, open(
            output_file_path_with_name, "w"
        ) as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        print("Input file not found!")
    else:
        os.remove(input_file_name)
