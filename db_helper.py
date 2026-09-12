
import sqlite3
import hashlib
import secrets

DATABASE = "students.db"


# Connect to database
def create_connection():
    return sqlite3.connect(DATABASE)


# Create students table
def create_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Hash password
def hash_password(password):

    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100000
    )

    return salt.hex() + ":" + password_hash.hex()


# Check password
def verify_password(password, saved_password):

    try:

        salt_hex, hash_hex = saved_password.split(":")

        salt = bytes.fromhex(salt_hex)

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            100000
        )

        return secrets.compare_digest(
            password_hash.hex(),
            hash_hex
        )

    except Exception:

        return False


# Add student
def add_student(username, password, email):

    conn = create_connection()
    cursor = conn.cursor()

    password_hash = hash_password(password)

    try:

        cursor.execute("""
            INSERT INTO students
            (username, password, email)
            VALUES (?, ?, ?)
        """, (
            username,
            password_hash,
            email
        ))

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


# Verify student login
def verify_student(username, password):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT username, password, email
        FROM students
        WHERE username = ?
    """, (username,))

    student = cursor.fetchone()

    conn.close()

    if student is None:
        return None

    saved_username = student[0]
    saved_password = student[1]
    email = student[2]

    if verify_password(password, saved_password):

        return {
            "username": saved_username,
            "email": email
        }

    return None



