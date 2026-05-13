# storage.py
import json
import os

STORAGE_FILE = "users.json"

def _load_users() -> list:
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)