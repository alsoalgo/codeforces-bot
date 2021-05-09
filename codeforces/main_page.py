from .entity import *
from .constants import *
from .group import *

class MainPage(Entity):
    __handle = None
    def __init__(self, handle, link=CODEFORCES_URL):
        super().__init__(link)
        self.__handle = handle

    def get_group_list(self):
        group_list_link = self.__link + "/groups/with/" + self.__handle
        return GroupList(group_list_link)

    