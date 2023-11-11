import os


def move_file(command: str) -> None:
    # Get correct slash based on OS, fix command if needed
    correct_slash, wrong_slash = get_slash()
    if wrong_slash in command:
        command = command.replace(wrong_slash, correct_slash)


def get_slash() -> str:
    for slash in ["/", "\\"]:
        if slash in os.getcwd():
            correct = slash
        else:
            wrong = slash
    return correct, wrong
