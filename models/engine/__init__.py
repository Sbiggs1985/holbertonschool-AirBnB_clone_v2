#!/usr/bin/python3
import os
from models.storage import FileStorage, DBStorage


if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()