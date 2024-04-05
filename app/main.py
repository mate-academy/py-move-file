import os


def move_file(command: str) -> str | None:
    if not command.startswith("mv "):
        return "Wrong command"

    _, source_file, new_file = command.split()
    new_file = new_file.rstrip("/")

    if not os.path.exists(source_file):
        return

    new_dir, new_name = os.path.split(new_file)

    if not new_name:
        new_name = os.path.basename(source_file)

    if new_dir:
        os.makedirs(new_dir, exist_ok=True)
    new_file_path = os.path.join(new_dir, new_name)

    with (open(source_file, "r") as old_file,
          open(new_file_path, "w") as new_file):

        new_file.write(old_file.read())
    os.remove(source_file)
