import os
import shutil


def move_file(command: str) -> None:
    if command.startswith("mv"):
        command_list = command.split()
        if len(command_list) == 3:
            source, destination = command_list[1:]
            if not os.path.exists(source):
                print(f"Error: File '{source}' not exist!")
                return
            try:
                if "/" not in destination:
                    os.rename(source, destination)
                elif os.path.isdir(destination):
                    shutil.move(
                        source,
                        os.path.join(destination, os.path.basename(source))
                    )
                else:
                    os.makedirs(os.path.dirname(destination), exist_ok=True)
                    shutil.move(source, destination)
            except FileNotFoundError:
                print(
                    f"❌ File '{source}' "
                    f"or directory '{destination}' "
                    f"not found!"
                )
            except OSError as e:
                print(f"⚠️ System error: {e}")
            except Exception as e:
                print(f"💥 Unknown error: {e}")
