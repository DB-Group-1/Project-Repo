from utils.DB import DB


class SearchRepository:
    def __init__(self):
        self.instance = DB()

    def selectContentsByActor(self, actor: str):
        sql = f"""
            select
            	c.content_id id,
                c.content_name name,
                c.img_url image,
                c.category category,
                c.introduction description,
            	c.company_name publisher
            from content_main c
            where c.content_id in (
            	select ca.content_id
                from contentcast ca
                where ca.cast_name like "%{actor}%"
            )"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')

    def selectContentsByTitle(self, title: str):
        sql = f"""
            select
            	c.content_id id,
                c.content_name name,
                c.img_url image,
                c.category category,
                c.introduction description,
            	c.company_name publisher
            from content_main c
            where c.content_name like "%{title}%"
            """
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')

    def selectRealtimePopularContents(self):
        sql = """
            select
            	c.content_id id,
                c.content_name name,
                c.img_url image,
                c.category category,
                c.introduction description,
            	c.company_name publisher
            from content_main c
            join contentvideo vi on c.content_id = vi.content_id
            join content_viewershipbydate vs on vi.video_id = vs.video_id
            where timestampdiff(day, vs.updated_date, now()) <= 1
            order by vs.viewership desc
            limit 20;"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')

    def selectContentsByGenres(self, genres: tuple[int]):
        sql = f"""
            select
            	c.content_id id,
                c.content_name name,
                c.img_url image,
                c.category category,
                c.introduction description,
            	c.company_name publisher
            from content_main c
            join content_genre cg on c.content_id = cg.content_id
            join contentvideo vi on c.content_id = vi.content_id
            join content_viewershipbydate vs on vi.video_id = vs.video_id
            where cg.genre_id in {genres}
            order by vs.viewership desc
            limit 20;"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')
