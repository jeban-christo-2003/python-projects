import sqlite3

def create_user_table():
    conn = sqlite3.connect('authentication.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('authentication.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def authenticate(username, password):
    conn = sqlite3.connect('authentication.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False

def main():
    create_user_table()
    
    add_user("user1", "password1")
    add_user("user2", "password2")
    
    print("Welcome to the authentication system!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if authenticate(username, password):
        print("Authentication successful! You are logged in.")
    else:
        print("Authentication failed! Please check your username and password.")

if __name__ == "__main__":
    main()
