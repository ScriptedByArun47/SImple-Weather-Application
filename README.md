# SImple-Weather-Application


Project Overview:
This project is a Weather App that provides real-time weather information and a 5-day forecast for a given city. The app features a dynamic video background for an immersive user experience. Users can enter a city name, and the app will fetch and display the current weather (temperature, description, humidity, wind speed) along with weather emojis representing the forecast.

Key Features:
Background Video: A video is played as the app’s background to create a dynamic and visually appealing user interface.
Weather Information: The app displays:
Current temperature in Celsius.
Weather description (e.g., clear sky, rain, snow).
Humidity and wind speed.
Weather Forecast: Displays a 5-day forecast, including temperature and weather conditions with emojis (e.g., ☀️ for clear skies, 🌧️ for rain).
City Input: Users can input the city name and get instant weather updates.
Technologies Used:
Python for development.
customtkinter for the user interface.
OpenCV for handling the background video.
PIL (Pillow) for image manipulation (e.g., for displaying weather icons).
Requests to fetch data from the OpenWeather API.
How It Works:
City Input: The user enters the name of the city.
Fetch Weather: The app calls the OpenWeather API to retrieve the weather data for that city.
Display Information: Weather details and emojis are displayed on the screen, with the current weather at the top and the 5-day forecast at the bottom.
Dynamic Video Background: A video (like a nature scene or cityscape) continuously plays in the background.
