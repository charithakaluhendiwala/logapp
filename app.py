from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

def generate_random_log():
    log_levels = ["INFO", "WARNING", "ERROR"]
    log_messages = [
        "Application started",
        "Processing data",
        "Error occurred",
        "Task completed successfully",
        "Connection lost",
        "Debugging information"
    ]

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_level = random.choice(log_levels)
    log_message = random.choice(log_messages)

    return f"{timestamp} - {log_level}: {log_message}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_logs')
def generate_logs():
    number_of_logs = 10  # Adjust as needed
    logs = [generate_random_log() for _ in range(number_of_logs)]
    return "<br>".join(logs)

@app.route('/save_logs')
def save_logs():
    number_of_logs = 10  # Adjust as needed
    logs = [generate_random_log() for _ in range(number_of_logs)]
    log_file_name = "logs.log"

    with open(log_file_name, 'w') as file:
        for log in logs:
            file.write(log + '\n')

    return "Logs saved to 'logs.log'."

if __name__ == '__main__':
    port_number = 8081  # Specify your desired port
    app.run(debug=True, port=port_number)