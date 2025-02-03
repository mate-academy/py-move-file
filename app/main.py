from pathlib import Path


def move_file(command_file1_file2: str) -> None:
    data = command_file1_file2.split()
    if len(data) != 3:
        print("Invalid command format. Use: mv source destination")
        return

    cmd, src, dest = data
    src_file = Path(src)
    dest_file = Path(dest)
    dest_file.parent.mkdir(parents=True, exist_ok=True)

    try:
        if cmd != "mv":
            raise ValueError(f"command: -->> {cmd} <<-- Allowed only: mv")

        src_file.rename(dest_file)

    except FileNotFoundError:
        print("There not exist file to move")
    except ValueError as e_info:
        print(e_info)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
