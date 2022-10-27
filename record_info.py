"""导出数据库全部打卡记录"""

import pymysql

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
    result = cursor.fetchall()
except Exception:
    db.rollback()
    print("查询出错")


for i in result:
    print(f"记录{i[0]}:\n{i[1]} {i[2]} 打卡成功！")
