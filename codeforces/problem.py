from .entity import *
from .contest import *
from .constants import *
from .submission import *


class Problem(Entity):
    __submissions = None

    def __init__(self, link):
        super().__init__(link)
    
    def get_contest(self):
        contest_link = self.__link
        index = contest_link.find("/problem")
        return Contest(contest_link[:index])
    
    def get_submissions(self, driver):
        if self.__submissions is not None:
            return self.__submissions
        driver.get(self.__link)
        links = driver.find_element_by_tag_name("a")
        submissions = []
        sequence = "submission/"
        for link in links:
            if sequence in link.href:
                submissions.append(Submission(CODEFORCES_URL + link.href))
        self.__submissions = submissions
        return self.__submissions