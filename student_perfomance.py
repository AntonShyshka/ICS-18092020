
class Student():
    name = None
    config = None
    marks = None
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.marks = {}
        for i in range(1, self.config['lab_num'] + 1):  
            self.marks[i] = 0
    def make_lab(self, m, n):
        if n <= self.config['lab_num']:  
            if float(m) > float(self.config['lab_max']):  
                self.marks[n] = self.config['lab_max']
            else:
                self.marks[n] = m  
        print(self.marks)
        return self  
    def make_exam(self, m):
        if m > self.config['exam_max']:  
            self.marks['exam'] = self.config['exam_max']
            print(self.config['exam_max'])
        else:
            self.marks['exam'] = m
        print(self.marks)
        return self
    def is_certified(self):
        if sum(self.marks.values()) >= self.config['k']*100:
            print(sum(self.marks.values()), True)
        else:
            print(sum(self.marks.values()), False)