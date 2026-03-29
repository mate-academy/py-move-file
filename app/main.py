import os


def move_file(command: str) -> str:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Error: Invalid command format. "
              "Expected: mv <source_file> <destination_path>")
        return

    source_file = parts[1]
    destination_path = parts[2]

    source_abs_path = os.path.abspath(source_file)
    destination_abs_path = os.path.abspath(destination_path)

    if source_abs_path == destination_abs_path:
        return

    if destination_path.endswith("/"):
        target_path = os.path.join(destination_path,
                                   os.path.basename(source_file))
    else:
        target_path = destination_path

    target_dir = os.path.dirname(target_path)
    if target_dir and not os.path.exists(target_dir):
        try:
            os.makedirs(target_dir, exist_ok=False)
        except FileExistsError:
            print(f"Error: Directory {target_dir} already exists.")
            return
        except OSError as e:
            print(f"Error: Could not create directory {target_dir}: {e}")
            return

    try:
        os.rename(source_file, target_path)
    except FileNotFoundError:
        try:
            with (open(source_file, "rb") as source,
                  open(target_path, "wb") as destination):
                while True:
                    chunk = source.read(4096)
                    if not chunk:
                        break
                    destination.write(chunk)
            os.remove(source_file)
        except FileNotFoundError:
            print(f"Error: Source file {source_file} not found.")
            return
        except OSError as e:
            print(f"Error: Could not move file {source_file} "
                  f"to {target_path}: {e}")
            return
        except Exception as e:
            print(f"An unexpected error occurred during file moving: {e}")
            return
    except OSError as e:
        print(f"Error: Could not rename file {source_file} "
              f"to {target_path}: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
