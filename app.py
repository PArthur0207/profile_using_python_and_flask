from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/toUpperCase', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/areaOfcircle', methods = ['GET', 'POST'])
def area_of_circle():
    result = None
    while True:
        try:
            if request.method == 'POST':
                input_radius = request.form.get('inputRadius', '')
                result = 3.14 * (int(input_radius) ** 2)
            return render_template("Area of a Circle.html", result=result)
        except ValueError:
            return render_template("Area of a Circle.html", result="Invalid Input")

@app.route('/areaOfTriangle', methods = ['GET', 'POST'])
def area_of_triangle():
    result = None
    while True:
        try:
            if request.method == 'POST':
                input_base = request.form.get('inputBase', '')
                input_height = request.form.get('inputHeight', '')
                result = (int(input_base) * int(input_height)) / 2
            return render_template("Area of a Triangle.html", result=result)
        except ValueError:
            return render_template("Area of a Triangle.html", result="Invalid Input")

if __name__ == "__main__":
    app.run(debug=True)
