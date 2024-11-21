from common.config.Config import connect_db

class TempRepository:
    def getFriendList(self, cust_id):
        sql = """
            select c.name, ifnull(p.url, "images/o.png") url
            from t_friend f
            join t_customer c on f.friend_id = c.cust_id
            left join t_picture_update pu on c.cust_id = pu.cust_id
            left join t_picture p on pu.max_pic_id = p.pic_id
            where f.cust_id = %s
            order by c.name;""" % cust_id
        data = connect_db(sql)
        return data.to_dict(orient='records')

    def getUpdatedFriendList(self, cust_id):
        sql = """
            select c.name, p.url, p.update_time
            from t_friend f
            join t_customer c on f.friend_id = c.cust_id
            join t_picture_update pu on c.cust_id = pu.cust_id
            join t_picture p on pu.max_pic_id = p.pic_id
            where f.cust_id = %s and timestampdiff(MONTH, p.update_time, "2023-10-28") < 2
            order by c.name;""" % cust_id
        data = connect_db(sql)
        data['update_time'] = data['update_time'].astype(str)
        return data.to_dict(orient='records')

    def getNowBirthdayFriendList(self, cust_id):
        sql = """
            select c.name, c.birthday, ifnull(p.url, "images/o.png") url
            from t_friend f
            join t_customer c on f.friend_id = c.cust_id
            left join t_picture_update pu on c.cust_id = pu.cust_id
            left join t_picture p on pu.max_pic_id = p.pic_id
            where f.cust_id = %s and month(c.birthday) = month(curdate()) and day(c.birthday) = day(curdate())
            order by c.name;""" % cust_id
        data = connect_db(sql)
        data['birthday'] = data['birthday'].astype(str)
        return data.to_dict(orient='records')

    def getBeforeBirthdayFriendList(self, cust_id):
        sql = """
            select c.name, c.this_birthday, ifnull(p.url, "images/o.png") url
            from t_friend f
            join t_customer_birth c on f.friend_id = c.cust_id
            left join t_picture_update pu on c.cust_id = pu.cust_id
            left join t_picture p on pu.max_pic_id = p.pic_id
            where f.cust_id = %s and c.this_birthday between date_add(curdate(), interval -30 day) and curdate()
            order by c.name;""" % cust_id
        data = connect_db(sql)
        data['this_birthday'] = data['this_birthday'].astype(str)
        return data.to_dict(orient='records')

    def getAfterBirthdayFriendList(self, cust_id):
        sql = """
            select c.name, c.this_birthday, ifnull(p.url, "images/o.png") url
            from t_friend f
            join t_customer_birth c on f.friend_id = c.cust_id
            left join t_picture_update pu on c.cust_id = pu.cust_id
            left join t_picture p on pu.max_pic_id = p.pic_id
            where f.cust_id = %s and c.this_birthday between date_add(curdate(), interval 30 day) and curdate()
            order by c.name;""" % cust_id
        data = connect_db(sql)
        data['this_birthday'] = data['this_birthday'].astype(str)
        return data.to_dict(orient='records')

    def getRecommendedFriendList(self, cust_id):
        sql = """
            select f.cust_id
            from t_friend f
            where f.friend_id = %s
            and f.cust_id not in (
             select f.friend_id
                from t_friend f
                where f.cust_id = %s
            )""" % (cust_id, cust_id)
        data = connect_db(sql)
        return data.to_dict(orient='records')