import logging
from datetime import datetime
from pathlib import Path
from pencil import Pencil

# Set up standard logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class FileSystem:
    """Manages file structure creation and categorization in the Downloads folder."""

    DOWNLOADS = Path.home() / "Downloads"
    LOG_FILE = Path.cwd() / "logs" / "file_system.log"
    DATABASE_DIR = Path.cwd() / "database"

    # Pre-computed sets for fast O(1) lookup speed
    SUB_FOLDERS: dict[str, set[str]] = {
        "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
        "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"},
        "Audio": {".mp3", ".wav", ".aac", ".flac", ".m4a"},
        "Video": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
        "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
        "Executables": {".exe", ".msi", ".bat"},
    }

    @classmethod
    def _normalize_category(cls, category: str) -> str | None:
        """Normalizes input strings (e.g. 'image', 'video', 'images') to match official keys."""
        if not category:
            return None
        
        cat_lower = category.strip().lower()
        for key in cls.SUB_FOLDERS:
            # Matches exact key, or singular form (e.g., 'image' -> 'Images')
            if key.lower() == cat_lower or key.lower().rstrip("s") == cat_lower.rstrip("s"):
                return key
        return None

    @classmethod
    def _write_log(cls, message: str) -> bool:
        """Writes a log entry to the log file."""
        try:
            cls.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with cls.LOG_FILE.open("a", encoding="utf-8") as file:
                file.write(f"[{timestamp}] {message}\n")
            return True
        except OSError as error:
            logger.error(f"Log write error: {error}")
            return False

    @classmethod
    def create_subfolders(cls) -> bool:
        """Creates predefined subfolders inside the Downloads directory."""
        try:
            cls.DOWNLOADS.mkdir(parents=True, exist_ok=True)
            for folder_name in cls.SUB_FOLDERS:
                (cls.DOWNLOADS / folder_name).mkdir(parents=True, exist_ok=True)

            cls._write_log("Created subfolders")
            return True
        except OSError as error:
            logger.error(f"Error creating folders: {error}")
            return False

    @classmethod
    def get_files(cls, folder_type: str = "Images") -> list[str]:
        """Retrieves relative file paths matching the extension list for a folder category."""
        category = cls._normalize_category(folder_type)
        if not category:
            logger.warning(f"Unknown folder type: {folder_type}")
            return []

        folder_path = cls.DOWNLOADS / category
        if not folder_path.exists():
            cls.create_subfolders()

        allowed_extensions = cls.SUB_FOLDERS[category]

        try:
            return [
                f"{category}/{file.name}"
                for file in folder_path.iterdir()
                if file.is_file() and file.suffix.lower() in allowed_extensions
            ]
        except OSError as error:
            logger.error(f"Error reading directory '{folder_path}': {error}")
            return []

    @classmethod
    def add_to_database(cls, folder_type: str = "Images") -> bool:
        """Exports file list metadata to a JSON file via Pencil."""
        category = cls._normalize_category(folder_type)
        if not category:
            logger.warning(f"Invalid or empty category provided: '{folder_type}'")
            return False

        files = cls.get_files(category)
        now = datetime.now()

        payload = {
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S"),
            "count": len(files),
            "files": files,
        }

        # Ensure database parent directory exists
        cls.DATABASE_DIR.mkdir(parents=True, exist_ok=True)
        database_path = cls.DATABASE_DIR / f"{category}.json"

        try:
            return Pencil.rewrite(database_path, payload)
        except Exception as error:
            logger.error(f"Failed to update database for '{category}': {error}")
            return False


def create_databases():
    """Batch processes a list of categories and adds them to the database."""
    database_names = ["image", "video", "archive", "document", "music", "executable"]
    
    results = {}
    for name in database_names:
        success = FileSystem.add_to_database(name)
        results[name] = success
    return results


try:
    create_databases()
except Exception as error:
    print(error)