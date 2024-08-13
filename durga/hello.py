from flask import Flask,redirect
app=Flask(__name__)
@app.route('/')
def home():
    return 'Hello World'
@app.route('/first')
def first():
    return '<h1>Tell me your name</h1>'
@app.route('/second')
def second():
    return '<h2>Tell me your graduation</h2>'
@app.route('/result/<marks>')
def result(marks):
    print(type(marks))
    print(int(marks))
    if int(marks)>=35:
        return 'pass'
    else:
        return 'fail'
@app.route('/grades/<marks>')
def grades(marks):
    if int(marks)>90 and int(marks)<=100:
        return 'A grade'
    elif int(marks)>80 and int(marks)<90:
        return 'B grade'
    elif int(marks)>70 and int(marks)<80:
        return 'C grade'
    elif int(marks)<70:
        return 'D grade'
    else:
        return 'Fail'
@app.route('/voter/<int:age>')
def voter(age):
    if age>=18:
        return redirect('http://127.0.0.1:5000/valid')
    else:
        return redirect('http://127.0.0.1:5000/invalid')
@app.route('/valid')
def valid():
    return 'you are eligible'
@app.route('/invalid')
def invalid():
    return 'you are not eligible'


app.run(debug=True)
