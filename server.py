from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html',title='Home Page')

@app.route('/about')
def about():
    title = 'about Page'
    name = 'phuriphat sriwilat'
    email = 'phuri@gmail.com'
    mobile = '099 123 2133'
    age = 20
    return render_template('about.html',
                           title='about Page',
                           name=name,
                           email=email,
                           mobile=mobile,
                           age=age)

@app.route('/favorite/foods')
def favorite_foods():
  title = 'Favorite Foods Page'
  foods = ['กระเพราหมูสับ','กระเพราหมูกรอบ']
  return render_template('favorite_foods.html',
                        title=title,
                        foods=foods)
@app.route('/favorite/sports')
def favorite_sports():
  title = 'Favorite sports Page'
  sports = ['ฟุตบอล','ตะกร้อ','ฟุตซอล']
  return render_template('favorite_sports.html',
                        title=title,
                        sports=sports)

if __name__ == "__main__":
    app.run(debug=True)