from .entity import *
from .problem import *
from .constants import *
from .submission import *

class Contest(Entity):
    __problems = None # [[letter1, link1], [letter2, link2], ...]

    def __init__(self, link):
        super().__init__(link)
    
    def get_problem_list(self, driver):
        if self.__problems is not None:
            return self.__problems
        driver.get(self.__link)
        links = driver.find_element_by_tag_name("a")
        problems = []
        sequence = "problem/"
        for link in links:
            if sequence in link.href:
                index = link.href.find(sequence) + len(sequence)
                letter = link.href[index:]
                problem = [letter, Problem(CODEFORCES_URL + link.href)]
                if problem not in problems:
                    problems.append(problem)
        self.__problems = problems
        return self.__problems
    
    def get_group(self):
        if "group" not in self.__link:
            return None
        group_link = self.__link
        index = group_link.find("/contest")
        return Group(group_link[:index])
    
    def get_submission_list(self):
        submission_list_link = self.__link + "/my"
        return SubmissionList(submission_list_link) 