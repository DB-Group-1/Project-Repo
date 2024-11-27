from utils.DB import DB


class GenreRepository:
    def __init__(self):
        self.instance = DB()

    def selectGenre(self, category: str):
        sql = """
            SELECT *
            FROM genre g;"""
        result = self.instance.execute(sql)
        return result.to_dict('records')