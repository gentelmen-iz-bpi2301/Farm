import json
import os

def save_to_file(data, filename='farm_data.json'):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Ошибка сохранения: {e}")

def load_from_file(filename='farm_data.json'):
    if not os.path.exists(filename):
        return None
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return None