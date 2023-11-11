import os


def move_file(command: str) -> None:
    # Get correct slash based on OS, fix command if needed
    correct_slash, wrong_slash = get_slash()
    if wrong_slash in command:
        command = command.replace(wrong_slash, correct_slash)

    # Check if input command format is correct
    if not is_input_data_correct(command, correct_slash):
        return

    # Get correct paths for source and destination files
    origin_file_path, dest_file_path = command.split()[1:]
    if dest_file_path.endswith(correct_slash):
        origin_file_name = origin_file_path.split(correct_slash)[-1]
        dest_file_path += origin_file_name


def is_input_data_correct(command_text: str, correct_slash: str) -> bool:
    try:
        command_name, origin_path, destination_path = command_text.split()
    except ValueError:
        print(r"Correct input format: <command> <origin file path/name> "
              r"<destination file path/name>")
        return False

    if command_name != "mv":
        print("Incorrect command name. Type 'mv' for move.")
        return False

    if origin_path == destination_path:
        print("Nothing to move.")
        return False

    return True


def get_slash() -> str:
    for slash in ["/", "\\"]:
        if slash in os.getcwd():
            correct = slash
        else:
            wrong = slash
    return correct, wrong
