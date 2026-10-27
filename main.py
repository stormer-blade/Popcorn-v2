from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "gsavdVsagdvdfgj"


@app.route("/login", methods=["GET", "POST"])
def login():
    name = request.form.get("username")
    roll = request.form.get("roll")
    password = request.form.get("password")

    try:
        name.title()

        # Checking user in database 
        with open("Data.txt", "r") as file:
            data = file.read().split("\n")[1:-1]
        for i in range(len(data)):
            if f"{name.title()} {roll} {password}" == data[i]:
                session["username"] = name.title()
                return redirect("home")
    except:
        pass
    return render_template("login.html")


@app.route("/home", methods=["GET", "POST"])
def home():
    message = request.form.get("message")
    name = session.get("username")
    you = []
    others = []
    print(message)
    if message != None:
        with open("chat.txt", "a") as file:
            chats = file.write(f"{name} {message}\n")
    with open("chat.txt", "r") as file:
        chats = file.read().splitlines()
    for i in range(len(chats)):
        chat = chats[i]
        for x in range(len(chat)):
            if chat[x] == " ":
                chat = [chat[0:int(x)], f"{chat[int(x+1): -1]}{chat[-1]}"]
                break
        try:
            if chat[0].lower() == name.lower():
                you.append([chat, i])
            else:
                others.append([chat, i])
        except:
            pass
    return render_template("main.html", you=you, others=others, lenght=range(len(chats)))

if __name__ == "__main__":
    app.run(debug=True, port=8080)