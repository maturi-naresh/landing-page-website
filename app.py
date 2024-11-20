from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)