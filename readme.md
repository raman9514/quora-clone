# 🧠 Quora Clone

A Django-based Question & Answer platform, inspired by Quora. Users can post questions, answer them, upvote/downvote, and interact with similar questions — all within a clean Bootstrap 5 UI.

## 🚀 Features

- User authentication (Sign up / Login)
- Ask and edit questions
- View and answer questions
- Upvote and downvote answers
- Similar question suggestion using HTMX
- Bootstrap 5 for responsive UI
- CKEditor 5 for rich text answers

---

## 💠 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/raman9514/quora-clone.git
cd quora-clone
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` does not exist, create one using:

```bash
pip freeze > requirements.txt
```

### 4. Set Up the Database

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to explore the app.

---

## 🔪 Testing (Optional)

If you’ve written any tests, you can run:

```bash
python manage.py test
```

---

## 📂 Project Structure

```bash
quora-clone/
├── discussion/        # Main app (Questions, Answers, Views)
├── templates/         # Base + app templates
├── static/            # CSS, JS, etc.
├── manage.py
├── requirements.txt
└── README.md
```

---

## ✨ Credits

Developed by [Raman](https://github.com/raman9514) — powered by Django, Bootstrap, HTMX, and CKEditor5.

---

## 📄 License

This project is licensed under the MIT License.

