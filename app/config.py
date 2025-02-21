import os


class Config:
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = False
    DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', 'data', 'projects.json')