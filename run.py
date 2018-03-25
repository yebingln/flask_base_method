#!flask/bin/python
from app import app,db

# #先删除表结构
# db.drop_all()
#
# #再创建表结构
# db.create_all()


app.run(debug = True)