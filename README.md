# Kaye-The-Home-Organizer-Python
"Kaye The Family Organizer is a user-friendly web application designed to simplify family management. It features a task manager, meal planner, and grocery list, all styled with vibrant animations and a sleek design. Users can easily add, view, and delete tasks and meals while staying updated with live weather information."

## Features

- **Task Management**: Add, view, and delete tasks with priority and due date.
- **Meal Planner**: Plan meals for the week, including recipes and frequency.
- **Grocery List**: Keep track of grocery items with quantity, unit, and price.
- **Live Weather Updates**: Displays current weather conditions and alerts on the home page.
- **Responsive Design**: Optimized for various screen sizes using Tailwind CSS and AOS (Animate On Scroll) for smooth animations.

## Technologies Used

- **Backend**: Python with Flask
- **Database**: SQLite for data storage
- **Frontend**: HTML, CSS (Tailwind CSS), and JavaScript
- **Animations**: AOS (Animate On Scroll)
- **Fonts**: Google Fonts - Orbitron
- **Weather API**: Integrated to fetch live weather data

## Installation

To set up Kaye The Family Organizer locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/kaye-the-family-organizer.git
   cd kaye-the-family-organizer
(Optional)Set up a virtual environment:
 ```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 ```
2. **Install the required packages**:
 ```
pip install -r requirements.txt
 ```
3. **Update wearther API key in kaye.py, You can get a API key from https://openweathermap.org/**:
```
def get_weather(city):
    api_key = 'Your_API_Key_Here'
```
4. **Run the application**:

 ```
python3 kaye.py
 ```
5. **Open your web browser and go to http://127.0.0.1:9187/.**

## Usage
- Tasks: Manage your family's tasks by adding new ones, setting priorities, and due dates. You can also delete completed tasks.
- Meal Planner: Input meals along with their recipes and frequency. This helps in organizing what to cook throughout the week.
- Weather Information: Check live weather updates, including alerts, right from the home page.

## Customization
- Feel free to customize the application by modifying the styles in static/styles.css or adding new features to enhance functionality.

## Contributing
- Contributions are welcome! If you would like to contribute to Kaye The Family Organizer, please fork the repository and submit a pull request. Ensure to follow the contribution guidelines.


## Thank you for checking out Kaye The Family Organizer! 
- We hope it helps make your family's life easier and more organized.





