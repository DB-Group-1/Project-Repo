from utils.DB import DB


class ContentRepository:
    def __init__(self):
        self.db = DB()

    def selectPopularContent(self):
        sql = f"""
            select 
            	c.content_id content_id,
                c.content_name name,
                c.img_url image,
                c.category category,
                c.introduction description,
                c.company_name publisher
            from content_main c
            join contentvideo vi on c.content_id = vi.content_id
            join content_viewershipbydate vs on vi.video_id = vs.video_id
            order by vs.viewership asc
            limit 20;"""
        result = self.db.execute(sql)
        return result.to_dict(orient='records')

    def selectRecentlyContent(self):
        sql = f"""select 
            	c.content_id id,
                c.content_name name,
                c.img_url image,
                c.category category,
                c.introduction description,
            	c.company_name publisher
            from content_main c
            join contentvideo vi on c.content_id = vi.content_id
            order by vi.uploaded_date asc
            limit 20;"""
        result = self.db.execute(sql)
        return result.to_dict(orient='records')

    def selectContentListByGenre(self, genre:str):
        sql = f"""select 
            	c.content_id id,
                c.content_name name,
                c.img_url image,
                c.category category,
                c.introduction description,
            	c.company_name publisher
            from content_main c
            join content_genre cg on c.content_id = cg.content_id
            join genre g on cg.genre_id = g.genre_id and g.genre_name = "{genre}"
            order by name asc
            limit 20;"""
        result = self.db.execute(sql)
        return result.to_dict(orient='records')