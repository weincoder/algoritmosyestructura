from flask import Flask, request, make_response, redirect, render_template, url_for

# se crea un objeto del tipo app
app = Flask(__name__)

@app.route('/')
def homeRoute():
    user_ip = request.remote_addr
    response = make_response(redirect('hello'))
    response.set_cookie('ip',user_ip)
    response.set_cookie('gato','Lior Herrera')
    return render_template('home.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/hello')
def helloRoute():
    gato = request.cookies.get('gato')
    ip = request.cookies.get('ip')
    return render_template('hello.html', 
    mascota = gato, userIp = ip)
@app.route('/hey')
def heyRoute():
    return render_template('hey.html')



if __name__ == '__main__':
    app.run()
