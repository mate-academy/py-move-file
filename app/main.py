import os


def move_file(command: str) -> None:
    try:
        if not isinstance(command, str):
            raise ValueError(
                "Input must be a string formatted as: 'mv <source> <target>'"
            )

        parts = command.strip().split()
        if len(parts) != 3 or parts[0] != "mv":
            raise ValueError(
                f"Invalid command: '{command}'. Expected: "
                "'mv <source> <target>'"
            )

        _, source, target = parts

        source_abs = os.path.abspath(source)

        if target.endswith(os.path.sep) or (
            os.path.exists(target) and os.path.isdir(target)
        ):
            final_dest = os.path.join(target, os.path.basename(source))
        else:
            final_dest = target

        dest_abs = os.path.abspath(final_dest)

        if source_abs == dest_abs:
            return

        if not os.path.exists(source_abs):
            raise OSError("Source file does not exist")

        dest_dir = os.path.dirname(dest_abs)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        with open(source, "r") as file_in, open(target, "w") as file_out:
            file_out.write(file_in.read())

        os.remove(source)

    except ValueError as e:
        print(
            "Invalid input. Expected format: 'mv <source> <target>'. "
            f"Got: '{command}'.",
            e,
        )
    except OSError as e:
        print(f"Error processing file moving: {e}. Command: '{command}'")
