import os


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) < 3:
        return None
    move_command, input_file_name, output_file_name_with_path = commands
    if move_command != "mv":
        return None

    file_path_list = output_file_name_with_path.split("/")
    output_file_name = file_path_list[-1]
    universal_output_file_path = output_file_name

    if len(file_path_list) > 1:
        universal_output_file_path = file_path_list[0]
        for i in range(1, len(file_path_list) - 1):
            directory = file_path_list[i]
            universal_output_file_path = os.path.join(
                universal_output_file_path, directory
            )

        os.makedirs(universal_output_file_path, exist_ok=True)
        universal_output_file_path = os.path.join(
            universal_output_file_path, output_file_name
        )

    try:
        with open(input_file_name, "r") as file_in, open(
            universal_output_file_path, "w"
        ) as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        print("Enter file not found!")
    else:
        os.remove(input_file_name)
