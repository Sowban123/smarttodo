# 🧠 Smart Todo List

Smart Todo List is an AI-powered task management web app built with Django (backend) and HTML/CSS/JavaScript (frontend). It allows users to create tasks, get AI suggestions for better task planning, and manage context entries such as emails, notes, and messages — all in one place.

---

## 📌 Features

- ✅ Add, view, and manage tasks
- 🧠 AI suggestions for:
  - Enhanced task descriptions
  - Priority classification (low, medium, high)
  - Smart deadlines
- 📝 Add contextual entries (email, WhatsApp, note) that influence tasks
- 📂 Task filtering by category
- 🌐 Responsive, simple UI (no external frameworks)

---

## 📁 Project Structure

smarttodo/
├── smarttodo/
│ ├── settings.py
│ ├── urls.py
├── todo/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py!
│ ├── templates/
│ │ ├── dashboard.html
│ │ ├── add-task.html
│ │ └── add-context.html
├── static/
│ └── ...
├── manage.py



##



Usage Guide
 Dashboard
Shows all tasks.

Accessible at /

 Add Task
URL: /add-task/

Inputs: title, description, context (comma-separated)

AI will suggest priority, enhanced description, and deadline.

 Add Context
URL: /add-context/

Inputs: text + source (email, WhatsApp, or note)

Used for AI context in task suggestions.

 AI Suggestion Flow (Simulated)
When submitting a new task:

Context and title/description are sent to /api/ai/suggestions/

Server returns:

priority: "low" / "medium" / "high"

deadline: auto-generated future date

enhanced_description: improved summary

Task is saved to /api/tasks/ using AI suggestions.
  ##


SCREENSHOTS:

![Screenshot 2025-07-05 201930](https://github.com/user-attachments/assets/82cbe056-2f1a-4f8a-b2f5-6ba0f6eab3e0)

![Screenshot 2025-07-05 200116](https://github.com/user-attachments/assets/0f2d1bf6-4c8f-4f78-9497-269023aa0bb4)
![Screenshot 2025-07-05 200146](https://github.com/user-attachments/assets/13420726-7390-40bf-882f-bcf681d76ac0)
---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smarttodo.git
cd smarttodo



python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

pip install -r requirements.txt

pip install django djangorestframework

python manage.py makemigrations
python manage.py migrate
![Screenshot 2025-07-05 201930](https://github.com/user-attachments/assets/6ca582a8-01da-4a32-b2e7-bb683abfe6e9)

python manage.py createsuperuser

python manage.py runserver
Usage Guide







