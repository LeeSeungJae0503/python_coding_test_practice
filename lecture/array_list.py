# https://leetcode.com/problems/design-browser-history/description/
"""
class BrowserHistory(object):

    def __init__(self, homepage):
        self.list = [homepage]
        self.index = 0
        

    def visit(self, url):
        if self.index == len(self.list) - 1:
            self.list.append(url)
        else:
            for i in range(self.index+1, len(self.list)):
                self.list.pop()
            self.list.append(url)
        self.index += 1
        

    def back(self, steps):
        if self.index - steps < 0:
            self.index = 0
            return self.list[0]
        else:
            self.index -= steps
            return self.list[self.index]

    def forward(self, steps):
        if self.index + steps > len(self.list) - 1:
            self.index = len(self.list) - 1
            return self.list[self.index]
        else:
            self.index += steps
            return self.list[self.index]
"""

"""
class BrowserHistory(object):

    def __init__(self, homepage):
        self.list = [homepage]
        self.index = 0

    def visit(self, url):
        # 현재 인덱스 이후의 기록 제거
        self.list = self.list[:self.index + 1]
        # 새로운 URL 추가
        self.list.append(url)
        # 인덱스 갱신
        self.index += 1

    def back(self, steps):
        # steps 만큼 뒤로 이동
        self.index = max(0, self.index - steps)
        return self.list[self.index]

    def forward(self, steps):
        # steps 만큼 앞으로 이동
        self.index = min(len(self.list) - 1, self.index + steps)
        return self.list[self.index]
"""

class BrowserHistory(object):

    def __init__(self, homepage):
        self.list = [homepage]
        self.index = 0
        

    def visit(self, url):
        self.list = self.list[:self.index+1]
        self.list.append(url)
        self.index += 1
        

    def back(self, steps):
        self.index = max(0, self.index - steps)
        return self.list[self.index]

    def forward(self, steps):
        self.index = min(len(self.list)-1, self.index+steps)
        return self.list[self.index]