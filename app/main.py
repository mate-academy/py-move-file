import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command_name, source_file_name, destination_file_name = parts
    if command_name != "mv":
        return
    if source_file_name == destination_file_name:
        return
    if not os.path.exists(source_file_name):
        return
    if destination_file_name.endswith("/"):
        final_destination = os.path.join(destination_file_name,
                                         os.path.basename(source_file_name))
    else:
        final_destination = destination_file_name
    dir_name = os.path.dirname(final_destination)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    with (open(source_file_name, "r", encoding="utf-8") as file_in,
         open(final_destination, "w", encoding="utf-8") as file_out):
        file_out.write(file_in.read())
    os.remove(source_file_name)
