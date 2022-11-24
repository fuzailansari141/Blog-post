import pymysql as p

def connect():
    return p.connect(host="localhost",user="root",password="",database="blogpost",port=3306)

def insert_a(t):
    con=connect()
    cur=con.cursor()
    sql="insert into author (Username,Password,Emailid,City) values(%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def insert_u(t):
    con=connect()
    cur=con.cursor()
    sql="insert into user (Username,Password,Emailid,City) values(%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def inspect_a(name):
    con=connect()
    cur=con.cursor()
    sql="select Username,Password from author where Username=%s"
    cur.execute(sql,name)
    data=cur.fetchall()
    con.commit()
    con.close()
    print(data)
    return data

def inspect_u(name):
    con=connect()
    cur=con.cursor()
    sql="select Username,Password from user where Username=%s"
    cur.execute(sql,name)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def insert_b(t):
    con=connect()
    cur=con.cursor()
    sql="insert into addpost (Authorname,Blogtitle,blog,posted) values(%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def post(u):
    con=connect()
    cur=con.cursor()
    sql="select * from addpost where Authorname=%s"
    cur.execute(sql,u)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data
    
def singleuser(id):
    con=connect()
    cur=con.cursor()
    sql="select * from addpost where id=%s"
    cur.execute(sql,id)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data[0]

def update(t):
    con=connect()
    cur=con.cursor()
    sql="update addpost set Authorname=%s,Blogtitle=%s,Blog=%s,Posted=%s where id=%s"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
def alldelete(blogtitle):
    con=connect()
    cur=con.cursor()
    sql="delete from addpost where Blogtitle=%s"
    cur.execute(sql,blogtitle)
    con.commit()
    con.close()

def allpost():
    con=connect()
    cur=con.cursor()
    sql="select * from addpost"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def nm():
    con=connect()
    cur=con.cursor()
    sql="select Username from author"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def nam():
    con=connect()
    cur=con.cursor()
    sql="select Username from user"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def ct(t):
    con=connect()
    cur=con.cursor()
    sql="insert into comments (Username,Comment,id_a) values(%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def ac(id_a):
    con=connect()
    cur=con.cursor()
    sql="select * from comments where id_a=%s"
    cur.execute(sql,id_a)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def del_c(id):
    con=connect()
    cur=con.cursor()
    sql="delete from comments where id=%s"
    cur.execute(sql,id)
    con.commit()
    con.close()

