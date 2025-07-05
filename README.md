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
│ ├── urls.py
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

python manage.py createsuperuser

python manage.py runserver
Usage Guide







