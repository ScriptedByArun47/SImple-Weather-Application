import customtkinter as ctk
from tkinter import messagebox
import requests
import cv2
from PIL import Image, ImageTk

API_KEY = "your API KEY"  # Replace with your API key

# Video update function
def update_video():
    ret, frame = video_capture.read()
    if ret:
        # Resize the frame to match the window size dynamically
        frame = cv2.resize(frame, (app.winfo_width(), app.winfo_height()))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_image = ImageTk.PhotoImage(Image.fromarray(frame))

        # Store the image reference to prevent garbage collection
        video_label.image = frame_image
        video_label.configure(image=frame_image)  # Use 'configure' instead of 'config'
    else:
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video

    app.after(50, update_video)  # Repeat the video update every 50 ms


def fetch_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    try:
        # Fetch current weather and forecast
        url_current = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        url_forecast = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        
        response = requests.get(url_current)
        response_forecast = requests.get(url_forecast)

        if response.status_code == 200 and response_forecast.status_code == 200:
            # Parse the responses
            data = response.json()
            data_forecast = response_forecast.json()

            # Current weather details
            city_name = f"{data['name']}, {data['sys']['country']}"
            temp = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            # Update current weather UI
            location_label.configure(text=city_name)
            temp_label.configure(text=f"{temp}°C")
            desc_label.configure(text=weather_desc.capitalize())
            weather_details.configure(
                text=f"Humidity: {humidity}%\nWind Speed: {wind_speed} m/s"
            )

            # Forecast details
            forecast_data = data_forecast['list'] 
            daily_forecast = []
            weather_icons = {
                 "clear sky": "☀️",
                 "partly cloudy": "🌤️",
                  "scattered clouds": "🌥️",
                  "overcast clouds": "☁️",
                  "rain": "🌧️",
                  "light rain": "🌦️",
                   "thunderstorm": "⛈️",
                   "snow": "❄️",
                   "mist": "🌫️",
                   "haze": "🌫️",
                   "fog": "🌁"
}
            for entry in forecast_data:
                if "12:00:00" in entry['dt_txt']:
                    date = entry['dt_txt'].split(" ")[0]
                    temp = entry['main']['temp']
                    desc = entry['weather'][0]['description']
                    emoji = weather_icons.get(desc.lower(), "🌡️")  # Default emoji if no match
                    daily_forecast.append(f"{emoji} {date}: {temp}°C, {desc.capitalize()}")

            forecast_text = "\n".join(daily_forecast[:5])  # Limit to 5 days
            forecast_label.configure(text=forecast_text)
        elif response.status_code == 404 or response_forecast.status_code == 404:
            messagebox.showerror("Error", f"City '{city}' not found.")
        else:
            messagebox.showerror("Error", "An unexpected error occurred.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve weather data.\n{e}")

# Setup Main Window
app = ctk.CTk()
app.geometry("400x700")
app.wm_resizable(False, False)
app.title("Weather App")
app.configure(fg_color="#98AECF")  # Background color

# Video Setup
video_path = r"background.mp4"  # Path to your video file
video_capture = cv2.VideoCapture(video_path)

if not video_capture.isOpened():
    messagebox.showerror("Error", "Unable to open video file.")
    exit()

# Create a label to display video as the background
video_label = ctk.CTkLabel(app)
video_label.place(relwidth=1, relheight=1)  # Fill the entire window

# Start the video update loop
update_video()

# City Entry
city_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter the 🌇city.....",
    width=250,
    height=50,
    font=ctk.CTkFont(size=20),
    fg_color="#c0d0f0",
    text_color="black",
    placeholder_text_color="black"
)
city_entry.place(relx=0.055, rely=0.2, anchor="w")

# Fetch Weather Button
fetch_button = ctk.CTkButton(
    app,
    text="Get Weather",
    command=fetch_weather,
    width=70,
    height=40,
    font=ctk.CTkFont(size=20)
)
fetch_button.place(relx=0.999, rely=0.2, anchor="e")

# current Weather Frame
background_image=Image.open("glassmorphism_effect1.png")

current_weather_frame = ctk.CTkFrame(app, width=400, height=300, corner_radius=20,fg_color="transparent" )
current_weather_frame.place(relx=0.5, rely=0.5, anchor="center")
current_bg_label=ctk.CTkLabel(current_weather_frame,image=ctk.CTkImage(light_image=background_image,dark_image=background_image,size=(400,300)),text="",)
current_bg_label.place(relx=0.5,rely=0.5,anchor="center")


weather_frame = ctk.CTkFrame(app, width=400, height=300, corner_radius=20,fg_color="transparent" )
weather_frame.place(relx=0.5, rely=0.9, anchor="center")
weather_bg_label=ctk.CTkLabel(weather_frame,image=ctk.CTkImage(light_image=background_image,dark_image=background_image,size=(400,300)),text="",)
weather_bg_label.place(relx=0.5, rely=0.9, anchor="center")
# Weather Details Inside Frame
location_label = ctk.CTkLabel(current_weather_frame, text="", font=("Arial", 20, "bold"),text_color="black")
location_label.pack(pady=10, padx=0)

temp_label = ctk.CTkLabel(current_weather_frame, text="", font=("Arial", 30, "bold"),text_color="black")
temp_label.pack(pady=10, padx=0)

desc_label = ctk.CTkLabel(current_weather_frame, text="", font=("Arial", 20, "bold"),text_color="black")
desc_label.pack(pady=10, padx=0)

weather_details = ctk.CTkLabel(current_weather_frame, text="", font=("Arial", 20, "bold"), justify="left",text_color="black")
weather_details.pack(pady=10, padx=0)

forecast_label = ctk.CTkLabel(weather_frame, text="", font=("Arial", 20,"bold"), justify="left",text_color="black")
forecast_label.pack(pady=15, padx=0)

# Run App
app.mainloop()

# Release the video capture when the window is closed
video_capture.release()
