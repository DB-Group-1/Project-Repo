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

    def selectUserInfo(self, userId:int):
        sql = f"""
            select
                u.user_id uid,
                u.name name,
                u.profile_URL image,
                u.email email,
                u.phone_num phone,
                u.cash cash,
                u.payment_method payment
            from user_profile u
            where u.user_id = {userId};"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')

    def selectUserLikeContents(self, userId:int):
        sql = f"""
            SELECT
                cv.video_id AS video_id,
                cm.content_name AS name,
                cv.url AS image,
                cv.quantity AS runtime,
                ul.wish_time AS date
            FROM user_Like ul
            LEFT JOIN ContentVideo cv ON ul.content_id = cv.content_id
            LEFT JOIN Content_main cm ON ul.content_id = cm.content_id
            WHERE ul.like_onoff = 1 AND ul.user_id = {userId}
            ORDER BY ul.wish_time DESC;"""
        result = self.instance.execute(sql)
        result['date'] = result['date'].astype(str)
        return result.to_dict(orient='records')

    def selectUserPurchasingContents(self, userId:int):
        sql = f"""
            SELECT 
                cv.video_id AS video_id,
                cm.content_name AS name,
                cm.img_url AS image,
                up.purchase_type AS type,
                up_profile.cash AS price,
                cv.quantity AS runtime,
                up.purchase_time AS date
            FROM user_purchased up
            LEFT JOIN user_profile up_profile ON up.user_id = up_profile.user_id
            LEFT JOIN Content_main cm ON up.content_id = cm.content_id
            LEFT JOIN ContentVideo cv ON cm.content_id = cv.content_id
            WHERE up.user_id = {userId}
            ORDER BY up.purchase_time DESC;"""
        result = self.instance.execute(sql)
        result['date'] = result['date'].astype(str)
        return result.to_dict(orient='records')

    def selectUserWatchingContents(self, userId:int):
        sql = f"""
            SELECT 
                uw.video_id AS video_id,
                cm.content_name AS name,
                cm.img_url AS image,
                cv.quantity AS runtime,
                uw.view_time AS date
            FROM user_watched uw
            LEFT JOIN ContentVideo cv ON uw.video_id = cv.video_id
            LEFT JOIN Content_main cm ON cv.content_id = cm.content_id
            WHERE uw.user_id = {userId}
            ORDER BY uw.view_time DESC;"""
        result = self.instance.execute(sql)
        result['date'] = result['date'].astype(str)
        return result.to_dict(orient='records')

    def updateUserWatching(self, userId:int, videoId:int):
        sql = f"""
            INSERT INTO user_watched (user_id, video_id, view_time)
            VALUES ({userId}, "{videoId}", NOW())
            ON DUPLICATE KEY UPDATE view_time = NOW();"""
        result = self.instance.execute(sql)
        return f"update {result} row(s)"