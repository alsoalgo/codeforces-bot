from .entity import *
from .contest import *
from .problem import *

class Submission(Entity):
    __problem = None

    def __init__(self, link):
        super().__init__(link)

    def get_contest(self):
        contest_link = self.__link
        index = contest_link.find("/submission")
        return Contest(contest_link[:index])
    
    def get_problem(self, driver):
        if self.__problem is not None:
            return self.__problem
        driver.get(self.__link)
        links = driver.find_element_by_tag_name("a")
        sequence = "problem/"
        for link in links:
            if sequence in link.href:
                self.__problem = Problem(CODEFORCES_URL + link.href)
                break
        return self.__problem
        

class SubmissionList(Entity):
    __submissions = None

    def __init__(self, link):
        super().__init__(link)

    def get_contest(self):
        contest_link = self.__link
        index = contest_link.find("/my")
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
