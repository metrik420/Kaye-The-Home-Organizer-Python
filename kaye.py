import os
import requests
import logging
logging.basicConfig(level=logging.DEBUG)
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired
import sqlite3
from flask import send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

#get weather
def get_weather(city):
    api_key = 'Your_API_Key_Here'
    weather_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    
    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()
        
        # Extracting current weather data
        weather_info = {
            'city': weather_data['location']['name'],
            'temperature': weather_data['current']['temp_f'],
            'description': weather_data['current']['condition']['text'],
            'icon': weather_data['current']['condition']['icon']
        }

        # Extracting alerts if available
        alerts = []
        if 'alerts' in weather_data and weather_data['alerts']['alert']:
            for alert in weather_data['alerts']['alert']:
                alerts.append({
                    'headline': alert.get('headline'),
                    'msgtype': alert.get('msgtype'),
                    'severity': alert.get('severity'),
                    'urgency': alert.get('urgency'),
                    'areas': alert.get('areas'),
                    'event': alert.get('event'),
                    'desc': alert.get('desc'),
                    'instruction': alert.get('instruction'),
                    'expires': alert.get('expires')
                })

        # Add alerts to weather_info
        weather_info['alerts'] = alerts

        return weather_info
    else:
        return None



# Initialize the database
def init_db():
    conn = sqlite3.connect('organizer.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT,
            priority TEXT,
            due_date TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY,
            meal TEXT,
            recipe TEXT,
            frequency TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS grocery (
            id INTEGER PRIMARY KEY,
            item TEXT,
            quantity INTEGER,
            unit TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

# Flask Forms for adding items
class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    priority = SelectField('Priority', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    due_date = DateField('Due Date', format='%Y-%m-%d')
    submit = SubmitField('Add Task')

class MealForm(FlaskForm):
    meal = StringField('Meal', validators=[DataRequired()])
    recipe = StringField('Recipe')
    frequency = SelectField('Frequency', choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')])
    submit = SubmitField('Add Meal')

class GroceryForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    unit = StringField('Unit', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    submit = SubmitField('Add Grocery Item')

# Serve the Service Worker (for PWA)
@app.route('/service-worker.js')
def service_worker():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'service-worker.js')

# Home Route
@app.route('/')
def home():
    city = "Phoenix"  # You can use any city or let the user choose
    weather = get_weather(city)  # Fetch weather data	
    return render_template('home.html', weather=weather)

# Tasks Management Routes
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    form = TaskForm()
    conn = sqlite3.connect('organizer.db')
    c = conn.cursor()

    if form.validate_on_submit():
        c.execute("INSERT INTO tasks (task, priority, due_date) VALUES (?, ?, ?)",
                  (form.task.data, form.priority.data, form.due_date.data))
        conn.commit()

    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return render_template('tasks.html', tasks=tasks, form=form)

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    conn = sqlite3.connect('organizer.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tasks'))

# Meal Planner Routes
@app.route('/meal_planner', methods=['GET', 'POST'])
def meal_planner():
    form = MealForm()
    conn = sqlite3.connect('organizer.db')
    c = conn.cursor()

    if form.validate_on_submit():
        c.execute("INSERT INTO meals (meal, recipe, frequency) VALUES (?, ?, ?)",
                  (form.meal.data, form.recipe.data, form.frequency.data))
        conn.commit()

    c.execute("SELECT * FROM meals")
    meals = c.fetchall()
    conn.close()
    return render_template('meal_planner.html', meals=meals, form=form)

@app.route('/delete_meal/<int:meal_id>')
def delete_meal(meal_id):
    conn = sqlite3.connect('organizer.db')
    c = conn.cursor()
    c.execute("DELETE FROM meals WHERE id=?", (meal_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('meal_planner'))

# Grocery List Routes
@app.route('/grocery_list', methods=['GET', 'POST'])
def grocery_list():
    form = GroceryForm()
    conn = sqlite3.connect('organizer.db')
    c = conn.cursor()

    if form.validate_on_submit():
        c.execute("INSERT INTO grocery (item, quantity, unit, price) VALUES (?, ?, ?, ?)",
                  (form.item.data, form.quantity.data, form.unit.data, form.price.data))
        conn.commit()

    c.execute("SELECT * FROM grocery")
    grocery = c.fetchall()
    conn.close()
    return render_template('grocery.html', grocery=grocery, form=form)

@app.route('/delete_grocery_item/<int:item_id>')
def delete_grocery_item(item_id):
    conn = sqlite3.connect('organizer.db')
    c = conn.cursor()
    c.execute("DELETE FROM grocery WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('grocery_list'))

# API Endpoints (for Android App)
@app.route('/api/tasks', methods=['GET', 'POST'])
def api_tasks():
    conn = sqlite3.connect('organizer.db')
    c = conn.cursor()
    if request.method == 'GET':
        c.execute("SELECT * FROM tasks")
        tasks = c.fetchall()
        conn.close()
        return jsonify(tasks)
    elif request.method == 'POST':
        new_task = request.json.get('task')
        c.execute("INSERT INTO tasks (task) VALUES (?)", (new_task,))
        conn.commit()
        conn.close()
        return jsonify({'status': 'Task added!'})

@app.route('/api/meals', methods=['GET', 'POST'])
def api_meals():
    conn = sqlite3.connect('organizer.db')
    c = conn.cursor()
    if request.method == 'GET':
        c.execute("SELECT * FROM meals")
        meals = c.fetchall()
        conn.close()
        return jsonify(meals)
    elif request.method == 'POST':
        new_meal = request.json.get('meal')
        c.execute("INSERT INTO meals (meal) VALUES (?)", (new_meal,))
        conn.commit()
        conn.close()
        return jsonify({'status': 'Meal added!'})

@app.route('/api/grocery', methods=['GET', 'POST'])
def api_grocery():
    conn = sqlite3.connect('organizer.db')
    c = conn.cursor()
    if request.method == 'GET':
        c.execute("SELECT * FROM grocery")
        grocery = c.fetchall()
        conn.close()
        return jsonify(grocery)
    elif request.method == 'POST':
        new_item = request.json.get('item')
        c.execute("INSERT INTO grocery (item) VALUES (?)", (new_item,))
        conn.commit()
        conn.close()
        return jsonify({'status': 'Item added!'})

# Initialize the Database
init_db()

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9187, debug=True)
