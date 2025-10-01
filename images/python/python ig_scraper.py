import instaloader
import os
from dotenv import load_dotenv

print("📦 Loading environment variables...")
load_dotenv()

USERNAME = os.getenv("almubskinconsults")
PASSWORD = os.getenv("Kakaka23$$")
TARGET = os.getenv("almubskinconsults")

print(f"Username from .env: {USERNAME}")
print("🔐 Logging into Instagram...")

L = instaloader.Instaloader()cd C:\Users\DELL\Downloads\python

try:
    L.login(USERNAME, PASSWORD)
    print("✅ Login successful")
except Exception as e:
    print("❌ Login failed:", e)
    exit()

print(f"📄 Fetching data for {TARGET}...")
profile = instaloader.Profile.from_username(L.context, TARGET)

print("✅ Profile info:")
print("Username:", profile.username)
print("Followers:", profile.followers)
