from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"Login: {username} - {password}")
    return redirect('/')

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    appointment = request.form.get('appointment')
    print(f"Booking: {name} - {appointment}")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
