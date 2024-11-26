from repository.GenreRepository import GenreRepository


class GenreService:
    def __init__(self):
        self.repo = GenreRepository()

    def getGenresByCategory(self, category:str):
        pass