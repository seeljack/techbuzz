from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Users/jackseel/Documents/Documents/UMSI339/finalproject/templates/lottery.html')

def lottery():
    # Your Python code goes here
    # You can generate dynamic content or fetch data from a database
    # For simplicity, let's create a variable with some text
    python_output = "Hello from Python!"

    # Render an HTML template and pass the Python data to it
    return render_template('lottery.html', python_output=python_output)

if __name__ == '__main__':
    app.run(debug=True)

