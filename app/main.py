import os


def move_file(command: str) -> None:
    try:
        mv_command, source_file, dstn_path = command.split()
    except ValueError:
        raise ValueError(
            "Command must have format: mv source_file destination/file_name"
        )

    if mv_command != "mv":
        raise ValueError("Command must begging with 'mv' without flags")

    if os.path.isdir(dstn_path):
        if not os.path.exists(dstn_path):
            os.makedirs(dstn_path)
        if "/" in source_file:
            source_file_name = os.path.split(source_file)[1]
            os.rename(source_file, f"{dstn_path}{source_file_name}")
        else:
            os.rename(source_file, f"{dstn_path}{source_file}")
        return

    if "/" in dstn_path:
        path = os.path.split(dstn_path)[0]
        if not os.path.exists(path):
            os.makedirs(path)

    if os.path.isfile(dstn_path):
        user_input = input(
            f"Do you want rewrite {dstn_path} with {source_file}: yes/no?"
        )
        if user_input.lower() == "no":
            raise ValueError("Please, rename destination file")

    with (
        open(source_file, "r") as source,
        open(dstn_path, "w") as output_file
    ):
        output_file.write(source.read())

    if dstn_path != source_file:
        os.remove(source_file)
