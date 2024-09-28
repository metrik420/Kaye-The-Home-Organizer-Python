# Kaye-The-Home-Organizer-Python
"Kaye The Family Organizer" is a user-friendly web application designed to simplify family management. It features task management, a meal planner, a grocery list, a calendar, and live weather updates. The app is designed with a modern interface, vibrant animations, and responsive design, making it easy for families to organize their daily activities."

## Features

- **Task Management**: Add, view, and delete tasks with priority levels and due dates.
- **Meal Planner**: Plan meals for the week, including recipes and frequency.
- **Grocery List**: Keep track of grocery items with quantity, unit, and price.
- **Calendar: Organize** events and view them in a user-friendly calendar interface.
- **Live Weather Updates**: Displays current weather conditions and alerts on the home page.
- **Progressive Web App (PWA)**: Installable web app with offline functionality for basic features.
- **Responsive Design**: Optimized for various screen sizes using Tailwind CSS and AOS (Animate On Scroll) for smooth animations.
- **Security**: Built-in authentication, input validation, and CSRF protection for secure user interactions.

## Technologies Used

- **Backend**: Python with Flask, modularized with Flask Blueprints for better code management.
- **Database**: SQLite for local data storage with optimized queries and relationships.
- **Frontend**: HTML, CSS (Tailwind CSS), and JavaScript with progressive enhancements for modern browsers.
- **Animations**: AOS (Animate On Scroll) for user-friendly animations.
- **Fonts**: Google Fonts - Orbitron
- **Weather API**: Integrated with WeatherAPI to fetch live weather data.
- **Progressive Web App**: Utilizes a service worker and manifest file for offline functionality and installability.

## Optimizations
- **Modular Code Structure**: The app has been divided into blueprints for task management, meal planning, calendar, and grocery lists for better scalability and organization.
- **Database Optimization**: Queries are now more efficient with appropriate indexing and lazy loading of relationships.
- **Caching**: Integrated Flask-Caching to reduce redundant API calls and speed up frequently accessed routes.
- **Service Worker**: Improved offline functionality by caching static assets and handling fallback requests.

## File structure
```
kaye-the-family-organizer/
│
├── app/                           # Main application folder
│   ├── blueprints/                # Flask blueprints for different features
│   │   ├── tasks.py               # Task management routes
│   │   ├── calendar.py            # Calendar feature routes
│   │   ├── meal_planner.py        # Meal planner routes
│   │   ├── grocery.py             # Grocery list routes
│   │   └── profile.py             # Profile management routes
│   ├── templates/                 # HTML templates for the application
│   │   ├── home.html              # Home page template
│   │   ├── tasks.html             # Tasks management template
│   │   ├── calendar.html          # Calendar template
│   │   ├── meal_planner.html      # Meal planner template
│   │   └── grocery.html           # Grocery list template
│   ├── static/                    # Static files (CSS, JavaScript, images)
│   │   ├── styles.css             # Custom styles for the application
│   │   ├── manifest.json          # Manifest for Progressive Web App (PWA)
│   │   ├── service-worker.js      # Service worker for offline support
│   │   └── (other static assets)  # Any additional static assets (images, JS files)
│   ├── models.py                  # Database models
│   ├── forms.py                   # Flask-WTF forms
│   ├── routes.py                  # Main routes for the app
│   ├── config.py                  # App configuration (dev, prod settings)
│   └── extensions.py              # Flask extensions initialization (e.g., db, cache)
│
├── tests/                         # Unit tests for the application
├── migrations/                    # Database migration files
├── kaye.py                        # Main application entry point
├── requirements.txt               # Python package dependencies
├── README.md                      # Project documentation
└── LICENSE                        # License file (e.g., GNU GPL v3.0)
```

## Installation

To set up Kaye The Family Organizer locally, follow these steps:

1. **Clone the repository**:
```bash
   git clone https://github.com/yourusername/kaye-the-family-organizer.git
   cd kaye-the-family-organizer
```
(Optional)Set up a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
2. **Install the required packages**:
```
pip install -r requirements.txt
```
3. **Update wearther API key in config.py or kaye.py : You can get a API key from https://openweathermap.org/**:
```
def get_weather(city):
    api_key = 'Your_API_Key_Here'
```
4. **Update loction for weather in config.py or kaye.py**
```
def home():
    city = "Add_Location_here"  # You can use any city
```
5. **Run the application**:

 ```
python3 kaye.py
 ```
6. **Open your web browser and go to http://127.0.0.1:9187/.**

## Usage
- **Tasks**: Manage your family's tasks by adding new ones, setting priorities, and due dates. You can also delete completed tasks.
- **Meal Planner**: Input meals along with their recipes and frequency. This helps in organizing what to cook throughout the week.
- **Grocery List**: Keep track of your grocery needs with item names, quantities, units, and prices.
- **Calendar**: Organize events using the calendar feature and view all upcoming family events.
- **Weather Information**: Check live weather updates, including alerts, right from the home page.

## Customization
- Feel free to customize the application by modifying the styles in static/styles.css or adding new features to enhance functionality.

## Deployment
- For production, use a WSGI server like Gunicorn or uWSGI, and run the app behind a reverse proxy like Nginx.
- You can containerize the app using Docker for easier deployment.

## Contributing
- Contributions are welcome! If you would like to contribute to Kaye The Family Organizer, please fork the repository and submit a pull request. Ensure to follow the contribution guidelines.

## License
- This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

## Thank you for checking out Kaye The Family Organizer! 
- We hope it helps make your family's life easier and more organized.
