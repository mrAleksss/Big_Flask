from flask import Flask, request, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

conn = sqlite3.connect("database.db")
conn.execute('CREATE TABLE IF NOT EXISTS Participants ( name TEXT, \
             email TEXT, city TEXT, country TEXT, phone TEXT )')


@app.route("/join", methods=['POST', 'GET'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        country = request.form['country']
        phone = request.form['phone']

        with sqlite3.connect('database.db') as users:
            cursor = users.cursor()
            cursor.execute('INSERT INTO Participants \
                           (name, email, city, country, phone) VALUES (?, ?, ?, ?, ?)', \
                           (name, email, city, country, phone))
            users.commit()

        return render_template("index.html")
    else:
        return render_template("join.html")
    

@app.route('/participants')
def participants():
    conn = sqlite3.connect("database.db")
    curr = conn.cursor()
    curr.execute('SELECT * FROM Participants')
    data = curr.fetchall()
    return render_template("participants.html", data=data)










if __name__ == '__main__':
    app.run(debug=True)