class dictionary(object):

    def __init__(self, array):
        self._array = array

    @property
    def array(self):
        return self._array


def solution(dictionary a, int T):
    array = a.array

    if(array[0] == T):
        return 0
    