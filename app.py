
from streamlit import Flask, request, redirect, session

from db_helper import (
    create_table,
    add_student,
    verify_student
)


app = Flask(__name__)

# Secret key for sessions
app.secret_key = "change-this-secret-key"


# Create database/table
create_table()


# =========================
# HOME
# =========================

@app.route("/")
def home():

    return """
    <h1>Student Login System</h1>

    <a href="/login">Login</a>

    <br><br>

    <a href="/register">Create Account</a>
    """


# =========================
# REGISTER
# =========================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if len(password) < 8:

            return """
            <h3>Password must be at least 8 characters.</h3>

            <a href="/register">
                Go Back
            </a>
            """

        success = add_student(
            username,
            password,
            email
        )

        if success:

            return """
            <h3>Account created successfully!</h3>

            <a href="/login">
                Login Now
            </a>
            """

        return """
        <h3>Username already exists.</h3>

        <a href="/register">
            Try Again
        </a>
        """

    return """
    <h1>Create Student Account</h1>

    <form method="POST">

        <input
            type="text"
            name="username"
            placeholder="Username"
            required
        >

        <br><br>

        <input
            type="email"
            name="email"
            placeholder="Email"
            required
        >

        <br><br>

        <input
            type="password"
            name="password"
            placeholder="Password"
            required
        >

        <br><br>

        <button type="submit">
            Create Account
        </button>

    </form>

    <br>

    <a href="/login">
        Already have an account?
    </a>
    """


# =========================
# LOGIN
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        student = verify_student(
            username,
            password
        )

        if student:

            session["username"] = student["username"]
            session["email"] = student["email"]

            return redirect("/dashboard")

        return """
        <h3>Invalid username or password.</h3>

        <a href="/login">
            Try Again
        </a>
        """

    return """
    <h1>Student Login</h1>

    <form method="POST">

        <input
            type="text"
            name="username"
            placeholder="Username"
            required
        >

        <br><br>

        <input
            type="password"
            name="password"
            placeholder="Password"
            required
        >

        <br><br>

        <button type="submit">
            Login
        </button>

    </form>

    <br>

    <a href="/register">
        Create Account
    </a>
    """


# =========================
# DASHBOARD
# =========================

@app.route("/dashboard")
def dashboard():

    if "username" not in session:

        return redirect("/login")

    username = session["username"]
    email = session["email"]

    return f"""
    <h1>Welcome {username} 👋</h1>

    <h2>Student Dashboard</h2>

    <p>
        Username: {username}
    </p>

    <p>
        Email: {email}
    </p>

    <br>

    <a href="/logout">
        Logout
    </a>
    """


# =========================
# LOGOUT
# =========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# =========================
# START SERVER
# =========================

if __name__ == "__main__":

    app.run(debug=True)
