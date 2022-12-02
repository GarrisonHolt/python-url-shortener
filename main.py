import pyshorteners

user_url = input("Enter your URL: ")

type_tiny = pyshorteners.Shortener()

short_url = type_tiny.tinyurl.short(user_url)

print(f"Your short url is: {short_url}")