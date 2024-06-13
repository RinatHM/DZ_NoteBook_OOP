import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_content(self, new_content):
        self.content = new_content
        self.updated_at = datetime.now()
        logging.info(f'Заметка обновлена: {self.title}')

    def __str__(self):
        return f'Название: {self.title}\nТекст Заметки: {self.content}\nСоздана : {self.created_at}\nОбновлена: {self.updated_at}'
