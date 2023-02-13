import os


def move_file(command_line: str) -> None:
    command, first_file, second_file = command_line.split()
    last_slash_index = second_file.rfind("/")
    second_file_path = second_file[:last_slash_index]
    content = ""

    if not os.path.exists(second_file_path):
        os.makedirs(second_file_path)

    with open(first_file, "r") as file_content:
        content += file_content.read()

    with open(second_file, "w") as file_out:
        file_out.write(content)
        os.remove(first_file)
