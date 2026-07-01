from db import engine

try:
    with engine.connect() as connection:
        print("✅ Successfully connected to MySQL!")
except Exception as e:
    print("❌ Connection failed")
    print(e)