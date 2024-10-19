# Porter Martin
# 10/17/2024
# Secured Login Application Homework #2
# This program encrypts and decrypts the given passwords/usernames using a "Caesar Cipher", and stores them in a database.
import string
import DBConnector
import tkinter as tk
from tkinter import messagebox

# Restructured the original Caesar Cipher we used in class to fit into this program for both the encrypt and decrypt portions.
def encrypt_password(message):
    # Alphabet creation: uppercase English letters
    key = 15
    chars = string.ascii_uppercase

    # Convert the message to uppercase
    encrypt = message.upper()

    # To store the final encrypted result
    result = ""

    # Loop through each character in the message
    for char in encrypt:
        if char in chars:
            # Find the current character's position in the alphabet
            index = (chars.find(char) + key) % 26

            # Append the shifted character to the result
            result += chars[index]
        else:
            # If it's not an alphabet character, add it as is
            result += char

    return result


def decrypt_password(message):
    # Alphabet creation: uppercase English letters
    key = 15
    chars = string.ascii_uppercase

    # Convert the message to uppercase
    decrypt = message.upper()

    # To store the final decrypted result
    result = ""

    # Loop through each character in the message
    for char in decrypt:
        if char in chars:
            # Find the current character's position in the alphabet and shift backwards by the key
            index = (chars.find(char) - key) % 26

            # Append the shifted character to the result
            result += chars[index]
        else:
            # If it's not an alphabet character, add it as is
            result += char

    return result


# This method creates user tables in the database
def create_users_table(db):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Martin_Porter_HW2 (

        username VARCHAR NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    """
    db.query(create_table_query, '')

# Inserts the given username and password into the database
def insert_user(db, username, password):
        encrypted_username = encrypt_password(username)
        encrypted_password = encrypt_password(password)
        # Ensure the encrypted password is stored as a string
        insert_user_query = "INSERT INTO Martin_Porter_HW2 (username, password) VALUES (%s, %s);"
        db.query(insert_user_query, (encrypted_username, encrypted_password))

# Authenticates the user comparing the given password and username to the stored variants
def authenticate_user(db, username, password):

        fetch_user_query = "SELECT username, password FROM Martin_Porter_HW2;"
        results = db.query(fetch_user_query, ())

        # iterate through records in the db
        for row in results:
            encrypted_username_str = row[0]
            encrypted_password_str = row[1]


            # Decrypt the saved encrypted username
            decrypted_username = decrypt_password(encrypted_username_str)


            # Compare decrypted usernames with the provided username
            if decrypted_username == username:
                # Decrypt the stored password
                decrypted_password = decrypt_password(encrypted_password_str)

                # compare decrypted passwords with the provided password
                if decrypted_password == password:
                    print("Successful Login!")
                    return True

                    # If the password does not match
                print("Failed Login! Please try again.")
                return False

    # GUI for Login Screen
def create_login_screen(db):
        def attempt_login():
            username = entry_username.get().upper()
            password = entry_password.get().upper()
            if authenticate_user(db, username, password):
                messagebox.showinfo("Login Success", "Welcome!")
            else:
                messagebox.showerror("Login Failed", "Invalid credentials!")

        root = tk.Tk()
        root.title("Secure Login Screen")

        label_username = tk.Label(root, text="Username")
        label_username.grid(row=0, column=0)
        entry_username = tk.Entry(root)
        entry_username.grid(row=0, column=1)

        label_password = tk.Label(root, text="Password")
        label_password.grid(row=1, column=0)
        entry_password = tk.Entry(root, show="*")
        entry_password.grid(row=1, column=1)

        login_button = tk.Button(root, text="Login", command=attempt_login)
        login_button.grid(row=2, columnspan=2)

        root.mainloop()

def main():

        # Connect to the database
        db = DBConnector.MyDB()

        # Create the users table
        create_users_table(db)

        # Insert sample users (comment this out after running once to avoid duplicate users)
        user_name = input("Give me a username to store in the database:")
        password = input("Give me a password to store in the database:")
        insert_user(db, user_name, password)

        # Launch the login screen
        create_login_screen(db)

if __name__ == "__main__":
        main()
