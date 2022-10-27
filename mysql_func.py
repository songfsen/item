"""数据库的插入和查询方法"""

import datetime
import pymysql


class Function:

    # 初始化成员方法
    def __init__(self, id):
        self.id = id

    # 向数据库插入打卡数据
    def insert(self):
        # 连接数据库
        db = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1997106",
            db="record",
            charset="utf8"
        )
        # 创建游标
        cursor = db.cursor()

        name_list = ["初始", "宋福森", "罗足伍迁", "刘诚", "user"]
        # 获取打卡这一刻的时间
        time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 待执行的sql语句
        sql1 = f"insert into userInfo(name,time) values('{name_list[self.id]}','{str(time_now)}')"
        # 执行sql语句
        try:
            cursor.execute(sql1)
            db.commit()
        except Exception:
            db.rollback()
            print("打卡失败！请对准摄像头")

        cursor.close()
        db.close()
        return

    def query(self):
        db = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1997106",
            db="record",
            charset="utf8"
        )

        cursor = db.cursor()
        sql = "select * from userInfo order by id desc"

        try:
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchone()
        except Exception:
            db.rollback()
            print("查询失败")

        cursor.close()
        db.close()

        return result
