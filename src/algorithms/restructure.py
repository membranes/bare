import numpy as np

class Restructure:

    def __init__(self, string: str):

        self.__string = string

    def __splittings(self) -> list:

        points = enumerate(self.__string)
        text = ''
        place = np.empty(0, dtype=int)
        splittings = []
        
        for point in list(points):

            if point[1] == ' ' or point[1] == '(' or point[1] == ')':
                splittings.append({'start': place[0] if len(place) > 0 else np.nan, 'word': text})
                text = ''
                place = np.empty(0, dtype=int)
            else:
                place = np.append(place, point[0])
                text = ''.join([text, point[1]])

        return splittings
