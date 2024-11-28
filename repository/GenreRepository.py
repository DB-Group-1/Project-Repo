from utils.DB import DB


class GenreRepository:
    def __init__(self):
        self.instance = DB()

    def selectGenre(self):
        sql = """SELECT * FROM genre g;"""
        result = self.instance.execute(sql)
        return result.to_dict('records')

    def selectFavorGenres(self, contents: tuple[int]):
        sql = f"""
            select
            	cg.genre_id genre_id,
            	g.genre_name name,
                count(*) count
            from content_genre cg
            join genre g on cg.genre_id = g.genre_id
            where cg.content_id in {contents}
            group by cg.genre_id
            order by count desc
            limit 3;"""
        result = self.instance.execute(sql)
        return result.to_dict('records')

    def selectRelatedGenre(self, contentId:int):
        sql = f"""
            select
            	cg.genre_id genre_id,
            	g.genre_name name
            from content_genre cg
            join genre g on cg.genre_id = g.genre_id
            where cg.content_id = {contentId};"""
        result = self.instance.execute(sql)
        return result.to_dict('records')