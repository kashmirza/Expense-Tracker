import json
import os


def load_data(filename):
    """
    Load data from a JSON file.
    Returns an empty dict if the file doesn't exist or is empty.
    """
    if not os.path.exists(filename):
        return {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read().strip()
            if not data:
                return {}
            return json.loads(data)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def save_data(filename, data):
    """
    Save data to a JSON file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)