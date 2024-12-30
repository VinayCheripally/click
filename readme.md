# task-manager

This is a project where you can add tasks and it will remind you before the due time.

---

## Features

- There are two ways to add tasks either by command line interface or by voice assistant.
- While reminding you it will use a library which turns text into voice and also it pops up a window with a 'got it' button and if you don't press it in ten seconds it will send a message to your phone.

---

## Installation

### Prerequisites

- Python

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/VinayCheripally/task-manager.git
   cd task-manager
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Create a .env file with the following variables
   ```bash
   TWILIO_ACCOUNT_SID=<Your Twilio Account SID>
   TWILIO_AUTH_TOKEN=<Your Twilio Auth Token>
   TWILIO_SENDER=<Twilio Sender Number>
   TWILIO_RECEIVER=<Your Phone Number>
   ```
4. Initialize the database:
   ```bash
   python main.py initialize-db
   ```
5. Run the program
   for reminding the due tasks
   ```bash
   python alert.py
   ```
   for voice assistant
   ```bash
   python voiceassistant.py
   ```
   The wake word for voice assistant is 'hey'
   and for using command line interface just use the command

```bash
 python main.py add-todo -n <name of the task> -d <description of thr task> --due<due date and time in ISO 8601-like format> <priority>
```
