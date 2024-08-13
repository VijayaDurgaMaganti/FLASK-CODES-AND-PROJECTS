from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
accounts={'12345':{'pin':'111','balance':3000},
          '45678':{'pin':'222','balance':6000}}
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        accno=request.form["accno"]
        pinno=request.form["pinno"]
        initial_balance=request.form.get('balance',0)
        if accno in accounts:
            return 'Account Already existed',400
        accounts[accno]={'pin':pinno,'balance':initial_balance}
        return 'Account created successfully.'
    return render_template('index.html')

@app.route('/data')
def data():
    accounts_list=[{'account_id':accno,'balance':details['balance']} for accno,details in accounts.items()]
    return accounts_list
@app.route('/alreadyacc',methods=['GET','POST'])
def alreadyacc():
    if request.method=='POST':
        accno=request.form["accno"]
        pinno=request.form["pinno"]
        if accno in accounts:
            details=accounts[accno]
            accounts_list=[{'account_id': accno, 'pinno': details['pin']}]
            #accounts_list=[{'account_id':accno,'pinno':details['pin']} for accno,details in accounts.items()]
            if pinno==accounts_list[0]['pinno']:
                return redirect(url_for('panel',accno=accno,pinno=pinno))
            else:
                return 'Invalid pin_no'
        else:
            return 'Invalid account_no',400
    
    return render_template('login.html')

@app.route('/panel/<accno>/<pinno>')
def panel(accno,pinno):
    return render_template('options.html',accno=accno,pinno=pinno)

@app.route('/deposite/<accno>/<pinno>',methods=['GET','POST'])
def deposite(accno,pinno):
    if request.method=='POST':
        amount=int(request.form['depo'])
        print(amount)
        details=accounts[accno]
        accounts_list=[{'account_id':accno, 'pinno':details['pin']}]
        if accounts_list[0]['account_id']==accno:
            accounts[accno]['balance']+=amount
        #return redirect(url_for('panel',accno=accno,pinno=pinno))
        print(accounts)
    return render_template('depo.html')

@app.route('/withdraw/<accno>/<pinno>',methods=['GET','POST'])
def withdraw(accno,pinno):
    if request.method=='POST':
        amount=int(request.form['withds'])
        print(amount)
        details = accounts[accno]
        accounts_list=[{'account_id':accno, 'balance':details['balance']}]
        
        if accounts_list[0]['account_id']==accno:
            originalammount=accounts_list[0]['balance']
        if amount>originalammount:
            return 'Given amount is out of balance'
        else:
            accounts[accno]['balance']-=amount
        #return redirect(url_for('panel',accno=accno,pinno=pinno))
        print(accounts)
        
    return render_template('withdraw.html')

#balance
@app.route('/balance/<accno>/<pinno>',methods=['GET','POST'])
def balance(accno,pinno):
    details=accounts[accno]
    accounts_list=[{'account_id':accno, 'balance':details['balance']}]
    return render_template('balance.html',accounts_list=accounts_list)

app.run(debug=True,use_reloader=True)