#coding:utf8

'''
数据库的基本操作：增删改查
'''



"""
删除全部表操作
n [3]: db.drop_all()

创建表
In [4]: db.create_all()


创建数据
In [9]: role=Role(name='adm')

In [10]: db.session.add(role)

In [12]: db.session.commit()

创建外键数据
In [13]: user=Adminn(name='hah',role_id=role.id)

In [14]: db.session.add(user)

In [15]: db.session.commit()

修改数据
In [16]: user.name='chengxuyuan'

In [17]: db.session.commit()

删除数据
In [18]: db.session.delete(user)

In [19]: db.session.commit()




一对多关系的使用

新建一个角色
In [12]: role=Role(name='admin')

In [13]: db.session.add(role)

In [14]: db.session.commit()


新建一个用户user1
In [15]: user1=User(name='zhangsan',role_id=role.id)

In [16]: db.session.add(user1)

In [17]: user2=User(name='lisi',role_id=role.id)

新建另一个用户user2
In [18]: db.session.add(user2)

In [19]: db.session.commit()

通过role.users关联的User
In [20]: role.users
Out[20]: [<User:zhangsan 1 None None>, <User:lisi 2 None None>]

取第一个关联用户的名字
In [22]: role.users[0].name
Out[22]: 'zhangsan'


通过方向role查询用户关联的角色
In [23]: user1.role
Out[23]: <Role: admin 1>

In [24]: user1.role.name
Out[24]: 'admin'

"""


"""
查询数据库方法

In [4]: from app import models

In [6]: models.User.query.all()

[<User:zhangsna 1 zhang@163.com 123456>,
 <User:lisi 2 lisi@163.com 123456>,
 <User:wang 3 wang@163.com 111111>,
 <User:yuyi 4 yuyi@163.com 234561>,
 <User:limo 5 limo@163.com 876543>,
 <User:qianli 6 qian@163.com 908976>,
 <User:kankan 7 kan@163.com 665544>,
 <User:jiyu 8 ji@163.com 343555>]



In [7]: models.User.query.count()
        8

In [8]: models.User.query.first()
Out[8]: <User:zhangsna 1 zhang@163.com 123456>


查询id=4的三种方法
In [10]: models.User.query.get(4)    #主键id数字
     <User:yuyi 4 yuyi@163.com 234561>


In [13]: models.User.query.filter_by(id=4).first()
Out[13]: <User:yuyi 4 yuyi@163.com 234561>


In [15]: models.User.query.filter(models.User.id==4).first()
Out[15]: <User:yuyi 4 yuyi@163.com 234561>


filter_by:属性=
filter:对象.属性==
filter功能更强大，可以实现更多的一些查询，支持比较运算符
"""