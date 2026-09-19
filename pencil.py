import json
from pathlib import Path


class Pencil:

    @classmethod
    def _perform_write(cls, file_name, data, mode="w"):
        try:
            file_path = Path(file_name)

            # Parent folder না থাকলে তৈরি করবে
            file_path.parent.mkdir(parents=True, exist_ok=True)

            with file_path.open(mode, encoding="utf-8") as file:

                if file_path.suffix.lower() == ".json":
                    json.dump(data, file, indent=4, ensure_ascii=False)

                else:
                    file.write(str(data))

            return True

        except OSError as error:
            print(f"File write error: {error}")
            return False

    @classmethod
    def rewrite(cls, file_name="example.txt", data="Pencil."):
        return cls._perform_write(file_name, data, "w")

    @classmethod
    def add(cls, file_name="example.txt", data="Pencil."):
        return cls._perform_write(file_name, data, "a")
