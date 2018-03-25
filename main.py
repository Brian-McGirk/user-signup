from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("home.html", title="Sign-up")

@app.route("/", methods=["POST"])
def sign_up():

    user_name = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verifyPassword"]
    email = request.form["email"]

    name_error = ""
    password_error = ""
    match_error = ""
    email_error = ""

    if not user_name:
        name_error = "You must enter a Username"
        user_name = ""
    elif " " in user_name or len(user_name) < 3 or len(user_name) > 20:
        name_error = "Thats not a valid Username"
        user_name = ""
    
    if not password:
        password_error = "You must enter a Password"
    elif " " in password or len(password) < 3 or len(password) > 20:
        password_error = "Thats not a valid Username"

    if not verify_password or password != verify_password:
        match_error = "Passwords don't match"
    
    if email:
        if " " in email or len(email) < 3 or len(email) > 20 or email.count("@") > 1 or email.count(".") > 1 or email.count("@") < 1 or email.count(".") < 1:
            email_error = "Thats not a valid email"
            email = ""

    if not name_error and not password_error and not match_error and not email_error:
        return redirect("/welcome?username={0}".format(user_name))
    else:
        return render_template("home.html", title="Sign-up",name_error=name_error, password_error=password_error, match_error=match_error, email_error=email_error, user_name=user_name, email=email)
    
@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", title="Welcome", username=username)

app.run()






    



