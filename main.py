from flask import Flask,render_template,url_for,redirect
app=Flask(__name__)
@app.route('/')
def me():
    return render_template('index.html')
@app.route('/aboutus')
def saurabh():
    return("TERI BHEN KI CHUT SAURABH")
@app.route('/phone')
def you():
    return ('HELLO JI')
@app.route('/registratiom')
def master():
    return render_template ('registratiom.html')
@app.route('/success')
def prithu():
    return render_template('success.html')
app.run(debug=True)
