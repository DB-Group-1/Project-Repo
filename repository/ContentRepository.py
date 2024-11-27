from utils.DB import DB


class ContentRepository:
    def __init__(self):
        self.db = DB()

    def selectActorInContent(self, contentId:int):
        sql = f"""
            select 
            	ca.cast_name name,
            	ca.role role
            from contentcast ca
            where ca.content_id = {contentId};"""
        result = self.db.execute(sql)
        return result.to_dict(orient='records')

    def selectEpisodeOfContent(self, contentId:int):
        sql = f"""
            select 
            	vi.video_id video_id,
            	vi.url url,
            	vi.quantity quantity,
                vi.uploaded_date uploaded_date
            from contentvideo vi
            where vi.content_id = {contentId}
            order by vi.uploaded_date asc;"""
        result = self.db.execute(sql)
        result['uploaded_date'] = result['uploaded_date'].astype(str)
        return result.to_dict(orient='records')

    def selectRelatedActor(self, contentId:int):
        sql = f"""
            select 
                ca.cast_id cast_id,
            	ca.cast_name name
            from contentcast ca
            where ca.content_id = {contentId};"""
        result = self.db.execute(sql)
        return result.to_dict(orient='records')

    def selectRelatedPublisher(self, contentId:int):
        sql = f"""
            select 
                c.company_name publisher
            from content_main c
            where c.content_id = {contentId};"""
        result = self.db.execute(sql)
        return result.to_dict(orient='records')

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
            order by vs.viewership desc
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
            order by vi.uploaded_date desc
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

    def selectContentInfo(self, contentId:int):
        sql = f"""
            select 
            	c.content_id content_id,
                c.content_name name,
                c.img_url image,
                c.limit_age limit_age,
                c.introduction description,
            	c.company_name publisher,
            	c.url url,
            	g.genre_name genre
            from content_main c
            join content_genre cg on c.content_id = cg.content_id
            join genre g on cg.genre_id = g.genre_id
            where c.content_id = {contentId};"""
        result = self.db.execute(sql)
        return result.to_dict(orient='records')

    def selectRelatedContent(self, contentId:int, genreId:int, actors:tuple[int], publisher:str):
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
            join contentcast ca on c.content_id = ca.content_id
            join contentvideo vi on c.content_id = vi.content_id
            join content_viewershipbydate vs on vi.video_id = vs.video_id
            where c.content_id != {contentId} and (
                cg.genre_id = {genreId} or
                ca.cast_id in {actors} or
                c.company_name = "{publisher}"
            )
            order by vs.viewership desc
            limit 20;"""
        result = self.db.execute(sql)
        return result.to_dict(orient='records')