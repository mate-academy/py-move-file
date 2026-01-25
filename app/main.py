import os
from pathlib import Path


def move_file(comand: str) -> None:
    try:
        parameters = comand.split()
        if parameters[0] != "mv" or len(parameters) != 3:
            raise ValueError("Command error")
        src = Path(parameters[1])
        dest = parameters[2]

        if dest.endswith("/"):
            dst = Path(dest) / src.name
        else:
            dst = Path(dest)

        dst.parent.mkdir(parents=True, exist_ok=True)

        with src.open("rb") as file_in, dst.open("wb") as file_out:
            file_out.write(file_in.read())
        os.remove(src)
    except Exception as e:
        print(e)
