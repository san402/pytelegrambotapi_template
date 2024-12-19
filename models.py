from pydantic import BaseModel, Field
from pymongo import MongoClient
from typing import Optional
from re import search
from loguru import logger
from os import environ

class TelegramButton(BaseModel):
    name: str
    url: str = None
    callback_data: str = None

def sanitizer(input: str) -> str:
    match = search(r'[0-9a-zA-Z\.\-_]{1,50}', input)
    if match:
        return match[0]
    return ''


class TelegramUser(BaseModel):
    id: int
    username: Optional[str] = Field(default=None)
    full_name: Optional[str] =Field(default= None)
    menu_id: Optional[int] = Field(default=None)
    message_to_edit_id: Optional[tuple] = Field(default=None)
class User:
    def save_to_database(self):
        self.__users.update_one({'id': self.__telegram_user.id},
                                {"$set": self.__telegram_user.dict()},
                                upsert=True)

    def __init__(self, from_user):
        client = MongoClient(environ.get('DB_HOST'))
        self.__users = client[environ.get("DB_NAME",'example')][environ.get("DB_COLLECTION",'users')]
        if from_user.first_name is not None:
            from_user.first_name = sanitizer(from_user.first_name)
            if from_user.last_name is not None:
                from_user.last_name = sanitizer(from_user.last_name)
            else:
                from_user.last_name = ""
            full_name = f"{from_user.first_name} {from_user.last_name}"
        else:
            full_name = None

        initiated_user = TelegramUser(id=from_user.id, full_name=full_name,
                                      username=from_user.username)
        database_search = self.__users.find_one({"id": initiated_user.id})
        if database_search:
            self.__telegram_user = TelegramUser(**database_search)
        else:
            self.__telegram_user = initiated_user
        logger.debug(f'USER_INFO: {self.__telegram_user}')
        self.save_to_database()

    def set_menu(self, menu_id: int):
        self.__telegram_user.menu_id = menu_id
        self.save_to_database()
        return True

    def approve(self):
        self.__telegram_user.access = True
        self.save_to_database()

    @property
    def telegram_id(self):
        return self.__telegram_user.id

    @property
    def username(self):
        return self.__telegram_user.username

    @property
    def full_name(self):
        return self.__telegram_user.full_name

    @property
    def menu(self):
        return self.__telegram_user.menu_id

    @property
    def message_to_edit(self):
        return self.__telegram_user.message_to_edit_id

    @message_to_edit.setter
    def message_to_edit(self, value):
        self.__telegram_user.message_to_edit_id = value

    @property
    def short_info(self) -> str:
        info = self.__telegram_user.username if not self.__telegram_user.full_name else self.__telegram_user.full_name
        info = str(info)[:33] + " ({})".format(self.__telegram_user.id)
        info = info.replace(" ", "_")
        return info
