import numpy as np

class Restructure:

    def __init__(self, string: str):

        self.__string = string

    def __splittings(self):

        indices = enumerate(self.__string)
        text = ''
        place = np.empty(0, dtype=int)
        reference = []
        for term in list(indices):

            if term[1] == ' ' or term[1] == '(' or term[1] == ')':
                reference.append({'start': place[0] if len(place) > 0 else np.nan, 'word': text})
                text = ''
                place = np.empty(0, dtype=int)
            else:
                place = np.append(place, term[0])
                text = ''.join([text, term[1]])
