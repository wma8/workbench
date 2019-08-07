class student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be Integer')
        if not 0 <= value <= 100:
            raise ValueError('Must between 0 to 100')
        self._score = value

    
    
if __name__ == '__main__':
    s = student()
    s.score = 100
    print(s.score)