import speech_recognition as sr
import pyttsx3
import datetime
import requests
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Processing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("There seems to be an issue with the speech recognition service.")
        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
    return None

def get_weather(city):

    api_key = "77fd7d112a8ddc1fc9bd009f909788bf"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            speak(f"The weather in {city} is {weather} with a temperature of {temperature} degrees Celsius.")
        else:
            speak("I couldn't find the weather for that location.")
    except Exception as e:
        speak("I'm unable to fetch the weather details right now.")

def get_news():

    api_key = "df3d782d8e35493abb300208eed1f3d8"  # Replace with your NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    try:
        response = requests.get(url)
        articles = response.json()["articles"][:5]
        speak("Here are the top 5 news headlines:")
        for i, article in enumerate(articles, start=1):
            speak(f"Headline {i}: {article['title']}")
    except Exception as e:
        speak("I'm unable to fetch the news right now.")

def set_reminder(reminder_text, delay):

    speak(f"Reminder set for {delay} seconds from now.")
    time.sleep(delay)
    speak(f"Reminder: {reminder_text}")

def assistant():
    speak("Hello, I am your personal assistant. How can I help you?")
    while True:
        command = listen()
        if not command:
            continue

        if "weather" in command:
            speak("Which city?")
            city = listen()
            if city:
                get_weather(city)

        elif "news" in command:
            get_news()

        elif "reminder" in command:
            speak("What should I remind you about?")
            reminder_text = listen()
            if reminder_text:
                speak("In how many seconds?")
                try:
                    delay = int(listen())
                    set_reminder(reminder_text, delay)
                except ValueError:
                    speak("I couldn't understand the time duration.")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")

        elif "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    assistant()
