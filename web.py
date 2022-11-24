
import datetime as dt
from database import *
from flask import *
web=Flask(__name__)
web.secret_key='asdsdfsdfs13sdf_df%&'

@web.route("/")
def home():
    return render_template("home.html")

@web.route("/reg_a")
def reg_a():
    return render_template("register_a.html")

@web.route("/reg_u")
def reg_u():
    return render_template("register_u.html")

@web.route("/log_a")
def log_a():
    return render_template("login_a.html")
    
@web.route("/log_u")
def log_u():
    return render_template("login_u.html")

@web.route("/logout")
def logout():
    return redirect("/")

@web.route("/author/<username>")
def author(username):
        return render_template("author.html",username=username)

@web.route("/user/<user>")
def user(user):
    data=allpost()
    return render_template("user.html",i=data,user=user)

@web.route("/addpost/<username>")
def addpost(username):
    now=dt.datetime.now()
    now=now.date()
    return render_template("addpost.html",username=username,now=now)

@web.route("/viewpost/<username>")
def viewpost(username):    
    data=post(username)
    return render_template("viewpost.html",i=data,username=username)

@web.route("/edit")
def edit():
    id=request.args.get("id")
    info=singleuser(id)
    now=dt.datetime.now()
    now=now.date()
    return render_template("edit.html",i=info,id=id,now=now)

@web.route("/delete/<username>/<blogtitle>")
def delete(username,blogtitle):
    alldelete(blogtitle)
    return redirect(url_for('viewpost',username=username))

@web.route("/insert_a",methods=["post"])
def ins_a():
    name=request.form["Username"]
    password=request.form["Password"]
    email=request.form["Emailid"]
    city=request.form["City"]
    
    a=nm()
    b=[]
    for i in range (len(a)):
        b.append(a[i][0])
    if name==name.upper():
        if name not in b:
            t=(name,password,email,city)
            insert_a(t)
            return redirect("/log_a")
        else:
            flash("The Username already exist!","info")
            return redirect("/reg_a")
    else:
        flash("The entered Username must be in capital letters!","info")
        return redirect("/reg_a")


@web.route("/insert_u",methods=["post"])
def ins_u():
    name=request.form["Username"]
    password=request.form["Password"]
    email=request.form["Emailid"]
    city=request.form["City"]
    
    c=nam()
    d=[]    
    for i in range (len(c)):
        d.append(c[i][0])
    if name==name.lower():
        if name not in d:
            t=(name,password,email,city)
            insert_u(t)
            return redirect("/log_u")
        else:
            flash("The Username already exist!","info")
            return redirect("/reg_u")
    else:
        flash("The entered Username must be in small letters!","info")
        return redirect("/reg_u")


@web.route("/check_a",methods=["post"])
def check_a():
    name=request.form["Username"]
    password=request.form["Password"]
    t=(name,password)
    t1=inspect_a(name)

    if t in t1 :
        return redirect(url_for('author',username=name))
    else:
        flash("Incorrect Username or Password!","info")
        return redirect("/log_a")


@web.route("/check_u",methods=["post"])
def check_u():
    name=request.form["Username"]
    password=request.form["Password"]
    t=(name,password)
    t1=inspect_u(name)

    if t in t1:
        return redirect(url_for('user',user=name))
    else:
        flash("Incorrect Username or Password!","info")
        return redirect("/log_u")


@web.route("/insert_b/<now>/<username>",methods=["post"])
def ins_b(now,username):
    name=request.form["Authorname"]
    title=request.form["Blog title"]
    blog=request.form["Blog"]
    t=(name,title,blog,now)
    
    if name==username:
        insert_b(t)
        return redirect(url_for('viewpost',username = name))
    else:
        flash("Authorname must be Username","info")
        return redirect(url_for('addpost',username=username))


@web.route("/insagain/<id>/<now>/<username>",methods=["post"])
def insagain(id,now,username):
    name=request.form["Authorname"]
    title=request.form["Blog title"]
    blog=request.form["Blog"]
    
    if name==username:
        t=(name,title,blog,now,id)
        update(t)
        return redirect(url_for('viewpost',username = name))
    else:
        flash("Authorname must be Username","info")
        return redirect(url_for('edit',id=id))

@web.route("/comment/<user>/<id_a>",methods=['post'])
def comment(user,id_a):
    com=request.form["comment"]
    t=(user,com,id_a)
    ct(t)
    return redirect(url_for('allcomments',user=user,id_a=id_a))

@web.route("/allcomments/<user>/<id_a>")
def allcomments(user,id_a):
    data=ac(id_a)
    return render_template ("allcomments.html",user=user,id_a=id_a,i=data)

@web.route("/coms/<id_a>/<username>")
def coms(id_a,username):
    data=ac(id_a)
    return render_template ("coms.html",username=username,id_a=id_a,i=data)

@web.route("/del_a/<id>/<username>/<id_a>")
def dela(id,username,id_a):
    del_c(id)
    return redirect(url_for('coms',username=username,id_a=id_a))

@web.route("/del_c/<id>/<user>/<id_a>")
def delc(id,user,id_a):
    del_c(id)
    return redirect(url_for('allcomments',user=user,id_a=id_a))

if __name__=="__main__":
    web.run(debug=True)
