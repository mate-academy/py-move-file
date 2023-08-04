from pathlib import Path


def move_file(command: str) -> None:
    cmd, source_file, result_file = command.split()
    flag = cmd == "mv" and Path(source_file).exists()
    base_direction = Path(".").cwd()

    if "/" in result_file:
        root_add = [comp for comp in result_file.split("/") if comp]

        if result_file.endswith("/"):
            for root in root_add:
                base_direction = base_direction.joinpath(root)
            path_to_result = base_direction.joinpath(source_file)
        else:
            for root in root_add[:-1]:
                base_direction = base_direction.joinpath(root)
            path_to_result = base_direction.joinpath(root_add[-1])

        path_to_result.parent.mkdir(parents=True, exist_ok=True)
    else:
        path_to_result = Path(result_file).resolve()

    if flag:
        with open(source_file, "r") as source, open(
            path_to_result, "w"
        ) as res:
            source_file_data = source.read()
            res.write(source_file_data)
        Path(source_file).unlink()
