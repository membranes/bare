import numpy as np
import pandas as pd


class Page:

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

    def __page(self, splittings: list) -> pd.DataFrame:

        page = pd.DataFrame.from_records(data=splittings)
        page = page.copy().loc[page['start'].notna(), :]

        # Setting the character indices as type integer
        page['start'] = page['start'].astype(dtype=int)
        page['end'] = page['start'] + page['word'].str.len()

        # Ascertaining the words order
        page.sort_values(by='start', inplace=True)

        return page

    def exc(self):

        splittings = self.__splittings()

        return self.__page(splittings=splittings)

