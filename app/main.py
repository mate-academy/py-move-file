import os


def move_file(command: str) -> None:
    try:
        mv_command, source_file, destination = command.split()
    except ValueError:
        raise ValueError(
            "Command must have format: mv source_file destination/file_name"
        )

    if mv_command != "mv":
        raise ValueError("Command must begging with 'mv' without flags")

    if os.path.isdir(destination):
        if not os.path.exists(destination):
            os.makedirs(destination)
        if "/" in source_file:
            source_file_name = os.path.split(source_file)[1]
            os.rename(source_file, f"{destination}{source_file_name}")
        else:
            os.rename(source_file, f"{destination}{source_file}")
        return

    if "/" in destination:
        path = os.path.split(destination)[0]
        if not os.path.exists(path):
            os.makedirs(path)

    if os.path.isfile(destination):
        user_input = input(
            f"Do you want rewrite {destination} with {source_file}: yes/no?"
        )
        if user_input.lower() == "no":
            raise ValueError("Please, rename destination file")

    with (
        open(source_file, "r") as source,
        open(destination, "w") as output_file
    ):
        output_file.write(source.read())

    if destination != source_file:
        os.remove(source_file)
