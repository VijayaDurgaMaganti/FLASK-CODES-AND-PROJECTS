from flask import Flask,request,redirect,render_template,url_for

app=Flask(__name__)

@app.route('/index')
def home():
    l=[]
    name=request.args.get('marks')
    age=int(request.args.get('age'))
    pho=request.args.get('phno')
    l.extend([name,age,pho])
    return render_template('home.html',l=l)
@app.route('/result/<int:marks>')
def result(marks):
    if marks>=35 and marks<=100:
        return redirect(url_for('passes',marks=marks))
    else:
        return redirect(url_for('failed',marks=marks))
@app.route('/passes/<marks>')
def passes(marks):
    return f'Your are passed with the {marks} marks'
@app.route('/failed/<marks>')
def failed(marks):
    return f'Your are failed with the {marks} marks'

app.run(debug=True,use_reloader=True)
