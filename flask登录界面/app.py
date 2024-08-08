import hashlib
from flask import Flask, render_template, request, redirect, session
from models import Users, db
import config

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
db.init_app(app)

# 时效性数据库
# with app.test_request_context():
#     db.drop_all()
#     db.create_all()


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # 在数据库中查询用户
        user = Users.query.filter_by(username=username)
        # 加密操作
        res = password + app.secret_key
        password = hashlib.md5(res.encode("utf-8")).hexdigest()

        # 验证用户名和密码是否匹配
        if user and password == password:
            return render_template("index.html")
    else:
        return render_template(
            "login-register.html", error="Invalid username or password"
        )


@app.route("/", methods=["GET", "POST"])
def loginregister():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        # 密码加密
        res = password + app.secret_key
        password = hashlib.md5(res.encode("utf-8")).hexdigest()

        new_user = Users(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
    return render_template("login-register.html")


if __name__ == "__main__":
    app.run(port=5050, debug=True)
