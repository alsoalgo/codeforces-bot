class Entity:
    __link = ""
    def __init__(self, link):
        self.__link = link
    
    @property
    def link(self):
        return self.__link
    
    @link.setter
    def link(self, value):
        self.__link = value

    def __str__(self):
        return self.__link
    
    def __eq__(self, other):
        return str(self) == str(other)