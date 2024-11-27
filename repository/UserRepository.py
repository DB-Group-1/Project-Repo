from utils.DB import DB


class UserRepository:
    def __init__(self):
        self.instance = DB()

    def selectLikedContents(self, userId:int):
        sql = f"""
            select
                l.content_id content_id,
                l.wish_time date
            from user_like l
            where l.user_id = {userId} and l.like_onoff = 1"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')

    def selectWatchedContents(self, userId:int):
        sql = f"""
            select
                distinct vi.content_id content_id,
                w.view_time date
            from user_watched w
            join contentvideo vi on w.video_id = vi.video_id
            where w.user_id = {userId};"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')