To-Do List Web App (Flask)

A simple To-Do List application built using Flask, HTML, CSS, and JSON file storage.
Users can add, edit, and delete tasks easily through a clean web interface.

Features

Add new tasks

Edit existing tasks

Delete tasks

Persistent storage using a tasks.json file

Lightweight backend using Flask

No database required

Tech Stack

Python 3

Flask

HTML / CSS

JSON (for storage)

Installation & Setup
1. Clone the project
git clone <https://github.com/thechhub/To-do-list-website>
cd todo-app

2. Install dependencies

Make sure you have Python installed, then run:

pip install flask

3. Start the Flask server
python app.py

4. Open the app

Visit the app in your browser:

http://127.0.0.1:5000

Project Structure
todo-app/
│── app.py              # Flask backend
│── tasks.json          # Task storage
│── templates/
│     └── index.html    # Frontend UI
│── static/
      └── style.css     # Styling

How It Works

Tasks are stored in tasks.json as a simple list.

Flask reads this file on page load and displays tasks.

When you add, edit, or delete tasks, the JSON file updates automatically.

No database, no complications — just straightforward functionality.

<img width="1600" height="800" alt="Screenshot (158)" src="https://github.com/user-attachments/assets/746d41d9-5d6e-4fc6-883a-8ecd00f8a15b" />

Feel free to customise anything in it
