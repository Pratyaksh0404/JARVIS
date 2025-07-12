# 🧠 JARVIS - A Python Based Voice Assistant

A Python-based **offline virtual assistant** that can listen to your commands, speak responses, open websites, search Wikipedia, tell the time, and even send emails — all through voice.

---

## 🚀 Features

- 🎙️ Voice-controlled commands
- 🔊 Text-to-speech responses
- 🧾 Wikipedia search integration
- 🕒 Tells current system time
- 🌐 Opens popular websites (Google, YouTube, Udemy, LinkedIn)
- 📝 Opens Notepad or Spotify
- 📧 Sends emails via Gmail (requires app password)
- 🎤 Greets the user based on time of day

---

## 🛠️ Technologies Used

- Python 3.x
- `pyttsx3` – Text-to-Speech (offline)
- `speech_recognition` – Voice recognition (requires internet)
- `wikipedia` – Wikipedia summary API
- `smtplib` – For sending emails
- `webbrowser`, `os`, `datetime` – Standard libraries

---

## 📁 File Structure

```
voice-assistant/
├── assistant.py        # Main script (all logic)
├── requirements.txt    # Required Python packages
└── README.md           
```

---

## ▶️ How to Run

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Run the assistant**

```bash
python assistant.py
```

3. **Say commands like**:
- `"Wikipedia Elon Musk"`
- `"Open YouTube"`
- `"What is the time"`
- `"Email to [name]"`
- `"Goodbye"`

> 💡 Make sure your mic is on and your internet is connected (for voice recognition and Wikipedia).

---

## 📦 `requirements.txt`

```txt
pyttsx3
speechrecognition
wikipedia
requests
```

---

## 🔐 Email Configuration

To use the email feature:
- Enable **2-Step Verification** in your Google account.
- Create an **App Password** from [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
- Replace the login line in the code:

```python
server.login('your_email@gmail.com', 'your_app_password')
```

> ⚠️ **NEVER share or commit your real email/password in code.**

---

## 💡 Example Commands

| You Say                      | Assistant Does                          |
|-----------------------------|------------------------------------------|
| `"Wikipedia machine learning"` | Reads summary from Wikipedia          |
| `"Open YouTube"`            | Launches YouTube in browser              |
| `"What is the time"`        | Tells current time                       |
| `"Open Notepad"`            | Opens Windows Notepad                    |
| `"Send email to XYZ"`       | Sends an email via Gmail                 |
| `"Goodbye"`                 | Says farewell and exits                  |

---

## 🔒 Disclaimer

- Voice commands rely on Google Speech Recognition — it requires internet.
- Email sending requires an app-specific password for Gmail.
- Make sure external apps (like Spotify, Notepad) exist on your system for those commands.

---

## 👤 Author

**Pratyaksh Agrawal**

---

## 📄 License

This project is free to use for educational and personal purposes.

