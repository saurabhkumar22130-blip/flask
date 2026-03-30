from flask import Flask,render_template,url_for,redirect,request
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
@app.route('/success' ,methods=['POST'])
def prithu():
    name=request.form['fullname']
    return "welome "+name
@app.route('/add')
def prantak():
    return render_template ('add.html')
@app.route('/result', methods=['POST'])
def mama():
    a = int(request.form.get('num1'))
    b = int(request.form.get('num2'))
    c = a + b
    return render_template('result.html',answer=c)
@app.route('/series')
def series():
    return render_template('series.html')
@app.route('/pass')
def pass():
    return render_template('pass.html')
app.run(debug=True)

