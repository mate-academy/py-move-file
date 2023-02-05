import os


def move_file(command: str) -> None:
    if not command.startswith("mv"):
        print("Error: invalid command")
        return

    src, dst = command.split()[1:]
    dst_folder, dst_filename = os.path.split(dst)

    try:
        os.makedirs(dst_folder, exist_ok=True)
    except FileExistsError:
        pass

    with (
        open(src, "r") as file_input,
        open(dst, "w") as file_output
    ):
        text = file_input.read()
        file_output.write(text)

    try:
        os.remove(src)
    except FileNotFoundError:
        print(f"Error: source file '{src}' does not exist")
