# -Azur_Developer_assessment
 Here is your complete and polished `README.md` file for the **Event Scheduler Flask API** project. It includes setup instructions, features, usage examples, and test commands — ideal for GitHub and submission.

---

### ✅ `README.md`

````markdown
# 🗓️ Event Scheduler System (Flask API)

This is a simple Python Flask-based REST API that allows users to manage scheduled events. Users can create, view, update, delete, search events, set recurring ones, and receive reminders.

---

## 📌 Features

- ✅ Add, view, update, and delete events
- 🔍 Search events by title or description
- 🔁 Recurring events (daily, weekly, monthly)
- 🔔 Get reminders for events due in the next hour
- 💾 Persistent storage using `events.json`
- 🧪 Unit testing with Pytest
- 📬 Postman collection included for API testing

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/venugopal7675/-Azur_Developer_assessment.git
cd -Azur_Developer_assessment
````

### 2️⃣ Install Dependencies

Make sure Python 3.10+ is installed.

```bash
python -m pip install -r requirements.txt
```

---

## 🛠️ Running the Application

```bash
python app.py
```

The server will start at: `http://127.0.0.1:5000/events`

---

## 📬 API Endpoints

### ▶️ Add Event

**POST** `/events`

```json
{
  "title": "Team Meeting",
  "description": "Sprint planning",
  "start_time": "2025-07-01T10:00:00",
  "end_time": "2025-07-01T11:00:00",
  "repeat": "none"
}
```

Values for `repeat`: `"none"`, `"daily"`, `"weekly"`, `"monthly"`

---

### 📃 Get All Events

**GET** `/events`

---

### ✏️ Update Event

**PUT** `/events/<event_id>`

```json
{
  "title": "Updated Meeting"
}
```

---

### ❌ Delete Event

**DELETE** `/events/<event_id>`

---

### 🔍 Search Events

**GET** `/search?q=meeting`

---

### 🔔 Reminders (Next 1 Hour)

**GET** `/reminders`

---

## 🧪 Running Unit Tests

```bash
pytest test_app.py
```

---

## 📂 Postman Collection

Import `event_scheduler.postman_collection.json` into Postman to test all endpoints directly.

---

## 📁 Data Persistence

All events are saved in a local file: `events.json`

Recurring events are auto-generated based on their repeat frequency.

---

## 🙌 Author

**Venugopal Mekala**
GitHub: [@venugopal7675](https://github.com/venugopal7675)

---

## 📄 License

MIT License – use freely with attribution.

```

---

✅ Save this as `README.md` in your project folder.

Next: I'll send you the updated `app.py`, `utils.py`, `test_app.py`, `events.json`, `requirements.txt`, and Postman collection. Ready?
```

