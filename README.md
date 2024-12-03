# SMS Messaging App

## Overview

Welcome to the **SMS Messaging App**! This project is a simple, locally-hosted web application that simulates sending and receiving SMS messages. It's built using **Python**, **Flask**, and **Flask-SocketIO**. The app provides a web-based interface where you can interact with a simulated phone number and send/receive messages in real-time.

With this app, you’ll get hands-on experience with:
- Web application development using **Flask**
- Real-time messaging via **Socket.IO**
- Simulating SMS-like interactions within a web browser

---

## Key Features

- **Real-time Messaging**: Messages are sent and received instantly using WebSockets (via Flask-SocketIO), without the need to refresh the page.
- **Interactive Web Interface**: A user-friendly, minimalistic interface to interact with the simulated messaging system.
- **Local Simulation**: Everything runs locally, meaning there is no need for external APIs or services. It’s all self-contained.

---

## Prerequisites

Before you start, you'll need to ensure that you have the following software installed:

- **Python 3.x** (preferably Python 3.6 or higher)
- **Git** (for cloning the repository and managing the project version)

Additionally, we will need to install several Python libraries that the app depends on.

---

## Step-by-Step Guide

### Step 1: Install Python

First, you need to have Python installed on your machine. To check if it's already installed, run the following command in your terminal (Command Prompt on Windows, Terminal on macOS/Linux):

```bash
python --version
```

If Python isn't installed, you can download it from the official website:

- [Download Python](https://www.python.org/downloads/)

Make sure to add Python to your system’s PATH during installation.

---

### Step 2: Clone the Repository

Clone the repository to your local machine using Git. Open your terminal and run the following command:

```bash
git clone https://github.com/developerofcodes/SMS-Messaging-App.git
```

After cloning the repo, navigate to the project folder:

```bash
cd SMS-Messaging-App
```

---

### Step 3: Install Dependencies

This project requires several Python libraries, such as Flask and Flask-SocketIO. These can be easily installed using **pip**.

In the project folder, run:

```bash
pip install -r requirements.txt
```

This will automatically install the required dependencies.

- **Flask**: A web framework used to create the web application.
- **Flask-SocketIO**: A Python library for real-time communication using WebSockets.
- **Other dependencies**: Flask's extensions for working with the server, and others required for the app.

---

### Step 4: Run the Application

Once all dependencies are installed, you’re ready to start the app.

Run the following command to launch the Flask server:

```bash
python app.py
```

This will start the Flask web server, and you should see output in your terminal like:

```
 * Running on http://127.0.0.1:5000
```

This indicates that the app is running locally at `http://127.0.0.1:5000`.

---

### Step 5: Open the Web Interface

Now that the server is running, open your web browser and visit the following address:

```
http://127.0.0.1:5000
```

You should see the **SMS Messaging App** interface, where you can begin interacting with the app.

---

### Step 6: Send and Receive Messages

- **Sending a Message**: On the homepage, enter a phone number and a message in the provided input fields. Then click the “Send” button. Your message will appear instantly in the inbox.
- **Receiving a Message**: Any messages sent to your virtual phone number will automatically appear in the inbox. The inbox updates in real-time, so you don’t need to refresh the page.

---

## Understanding the Code

The app is built using the following components:

### `app.py` - Main Application File

- **Flask** is used to create the web server and handle HTTP requests.
- **Flask-SocketIO** is integrated to enable real-time, bi-directional communication. This allows messages to be sent and received instantly, without the need to refresh the page.

#### Key Components of `app.py`:
- **WebSocket Handling**: The app uses SocketIO to emit and listen for real-time messages. When a message is sent, it is emitted to the client, which displays it in the chat.
- **Routes**: The app defines several routes (URLs) for serving the HTML page, sending messages, and receiving messages via WebSockets.

### `templates/index.html` - Web Interface

The HTML file provides the user interface of the messaging app. It includes:
- **Input fields** for entering a phone number and message.
- **Message display area** where sent and received messages appear.
- **JavaScript (Socket.IO)** to handle real-time updates.

The app uses **Socket.IO** to listen for new messages and update the UI without a page refresh.

---

## Troubleshooting

Here are some common issues you might encounter, along with solutions:

### Issue 1: Missing dependencies
If you see an error like `ModuleNotFoundError: No module named 'flask'`, it means that one of the required libraries isn’t installed.

**Solution**: Make sure you run the following to install all dependencies:
```bash
pip install -r requirements.txt
```

### Issue 2: Flask Server Not Running
If the Flask server fails to start or crashes with an error, ensure that:
- You’re in the correct directory (where `app.py` is located).
- You don’t have any other applications running on port 5000. If you do, you can change the port in `app.py` by modifying the line:
  ```python
  app.run(debug=True)
  ```
  to:
  ```python
  app.run(debug=True, port=5001)
  ```

### Issue 3: WebSocket Connection Issues
If the real-time messaging feature is not working, ensure that **Flask-SocketIO** is properly installed and configured.

Check if you see any errors in the browser's Developer Tools (press F12 in most browsers).

---

## Conclusion

This project is an excellent way to explore web development with Flask, real-time communication with Socket.IO, and basic messaging simulation. You can further extend the app to include features like:
- Storing messages in a database
- Simulating multiple phone numbers
- Adding a user authentication system

Feel free to fork and customize this project as you wish!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
