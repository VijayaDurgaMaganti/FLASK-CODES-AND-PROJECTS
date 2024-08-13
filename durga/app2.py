from flask import Flask,redirect
app=Flask(__name__)
@app.route('/veg/<int:menu>')
def veg(menu):
        if menu>=20:
                return redirect('http://127.0.0.1:5000/vegmenu')
        else:
                return redirect('http://127.0.0.1:5000/nonvegmenu')
                
@app.route('/vegmenu')
def vegmenu():
        return 'order vegmenu'
@app.route('/nonvegmenu')
def nonvegmenu():
        return 'order nonvegmenu'

    
app.run(debug=True)
