import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        return
    mv, source, target = command

    if mv != "mv":
        return

    source_filename = os.path.basename(source)
    target_folder = os.path.dirname(target)
    target_filename = os.path.basename(target)

    if not target_filename:
        target_filename = source_filename

    if target_folder and not os.path.exists(target_folder):
        print(f"Creating {target_folder}")
        os.makedirs(target_folder, exist_ok=True)

    with (open(source, "r") as s,
          open(os.path.join(target_folder, target_filename), "w") as t):
        for line in s:
            t.write(line)

    if os.path.exists(source):
        os.remove(source)
