from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit',methods =['POST'])
def submit():
    uname = request.form['username']
    dob = request.form['date']
    gender = request.form.get('gender')
    return render_template('greetings.html',name = uname,dob = dob,gender = gender)
if(__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5000, debug=True)