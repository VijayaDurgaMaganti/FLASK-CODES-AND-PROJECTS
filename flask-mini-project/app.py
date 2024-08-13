from flask import Flask,request,redirect,url_for,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('welcome.html')
@app.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')
app.run(debug=True,use_reloader=True)