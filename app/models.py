from app import db

class Username(db.Model):

    #定义表名
    __tablename__ = 'username'
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


"""
角色（管理员/普通用户）
用户（角色ID）
"""

class Role(db.Model):
    #定义表名
    __tablename__ = 'roles'

    #定义字段
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)

    #在一的一方，写关联
    #users = db.db.RelationshipProperty('User');表示和User模型发生了关联，增加了一个user属性
    #backref ='role':表示role是User要用的属性
    users=db.RelationshipProperty("User",backref='role')

    # repr()方法显示一个可读字符串
    def __repr__(self):
        return '<Role: %s %s>' % (self.name,self.id)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(32))

    #db.ForeignKey('roles.id) 表示外键.表名.id
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))   #外键的表名是依据 __tablename__ = 'roles'找的，切记切记！
    #User希望有role属性，但是这个属性的定义，需要再另一个模型定义

    def __repr__(self):
        return '<User:%s %s %s %s>' % (self.name,self.id,self.email,self.password)




'''
数据库的基本操作
db.session.add(role) 添加到数据库的session中
db.session.add_all([user1,user2])    添加多个信息到session中
db.session.commit()    提交数据库的修改（包括增/删/改)
db.session.rollback()   数据库的回滚操作
db.session.delete(user)  删除数据库（需跟上commit)
db.create_all()
db.drop_all()
'''