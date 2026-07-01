# ☕ Brew Haven

A modern full-stack café website built with **HTML, CSS, JavaScript, FastAPI, and MySQL**.

Brew Haven allows users to browse the café menu, explore the gallery, learn about the café, reserve a table, and contact the café through a responsive web interface.

---

## ✨ Features

- 🏠 Responsive landing page
- ☕ Menu page
- 🖼️ Gallery page
- 📖 About page
- 📞 Contact page
- 📅 Table reservation system
- ⚡ FastAPI REST API
- 🗄️ MySQL database integration
- 📚 Interactive API documentation using Swagger UI

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- FastAPI
- SQLAlchemy
- Pydantic

### Database
- MySQL

### Tools
- VS Code
- Git & GitHub
- Uvicorn

---

## 📂 Project Structure

```text
brew-haven/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   ├── services.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── css/
│   ├── images/
│   ├── js/
│   ├── index.html
│   ├── menu.html
│   ├── reserve.html
│   ├── gallery.html
│   ├── about.html
│   └── contact.html
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/brew-haven.git
cd brew-haven
```

### 2. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 3. Configure MySQL

Create a database named:

```sql
CREATE DATABASE brew_haven;
```

Create a `.env` file inside the `backend` folder:

```env
HOST=localhost
PORT=3306
NAME=brew_haven
USER=root
PASSWORD=your_password
```

### 4. Run the backend

```bash
cd backend
python -m uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📸 Screenshots

### Home Page

<img width="1436" height="692" alt="image" src="https://github.com/user-attachments/assets/7d6c422d-7faf-46a6-bd55-6b21b2728a90" />

### Menu Page

<img width="1367" height="692" alt="image" src="https://github.com/user-attachments/assets/b3baaff3-0d41-4358-8d19-5324626a2b4c" />
<img width="1437" height="692" alt="image" src="https://github.com/user-attachments/assets/1a347954-9b0d-4131-8522-a10b8a8c66b3" />

### Reservation Page

<img width="1392" height="692" alt="image" src="https://github.com/user-attachments/assets/d2aff5a1-ef3b-40f0-bf84-5d13dd14bc97" />


### About Page

<img width="1332" height="686" alt="image" src="https://github.com/user-attachments/assets/f6ea2478-b73a-41b8-ad2c-400f2d1692df" />


---

## 📚 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome route |
| POST | `/reservations` | Create a reservation |

---

## 🎯 Future Improvements

- User authentication
- Online payments
- Admin dashboard
- Reservation management
- Email confirmation
- Menu search & filtering

---

## 👩‍💻 What I Learned

Through this project I practiced:

- Building responsive web pages
- Designing REST APIs using FastAPI
- Using SQLAlchemy ORM
- Validating data with Pydantic
- Connecting a frontend to a backend using Fetch API
- Working with MySQL databases
- Organizing backend code using services and routes
- Using Git and GitHub for version control

---

## 📄 License

This project is for educational and portfolio purposes.
