from .entity import *
from .contest import *

class Group(Entity):
    __contests = None
    __name = None

    def __init__(self, link):
        super().__init__(link)
    
    def get_contests(self, driver):
        if self.__contests is not None:
            return self.__contests
        driver.get(self.__link)
        links = driver.find_element_by_tag_name("a")
        contests = []
        sequence = "contest/"
        for link in links:
            if sequence in link.href:
                index = link.href.find(sequence) + len(sequence)
                tail = link.href[index:]
                try:
                    int(tail)
                except ValueError:
                    continue
                contests.append(Contest(CODEFORCES_URL + link.href))
        self.__contests = contests
        return self.__contests

    def get_name(self, driver):
        if self.__name is not None:
            return self.__name
        pass
        
class GroupList(Entity):
    __groups = None

    def __init__(self, link):
        super().__init__(link)
    
    def get_groups(self, driver):
        if self.__groups is not None:
            return self.__groups
        links = driver.find_element_by_class_name("groupName")
        groups = []
        sequence = "group/"
        for link in links:
            if sequence in link.href:
                groups.append(Group(CODEFORCES_URL + link.href))
        self.__groups = groups
        return self.__groups
        
