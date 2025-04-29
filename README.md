# 📰 News Aggregator Website

A powerful and user-friendly web application that aggregates news articles from various sources, categorizes them by topic, and displays them in a clean and responsive interface. This project is ideal for users who want a centralized platform to stay updated on current events from multiple perspectives.

---

## 🔧 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **APIs:** News APIs (e.g., NewsAPI.org, The Guardian API, etc.)
- **Database:** SQLite (default for development)

---

## ✨ Features

- 🗞️ **Multi-Source Aggregation:** Fetches news from multiple reliable sources.
- 🗂️ **Category-Based Display:** News is categorized into topics like Business, Technology, Sports, Entertainment, etc.
- 🔍 **Search Functionality:** Users can search for news articles by keywords.
- 🌐 **Responsive Design:** Fully responsive layout using Bootstrap.
- 📅 **Recent Updates:** Displays the most recent news first.
- 💡 **Error Handling:** Graceful fallback for API errors or network issues.

---

## ✅ Prerequisites

Make sure you have the following installed:

- Python 3.8+
- Django
- Git ( for cloning)
- Virtual environment (recommended)

---

## 🚀 Project Setup

Follow the steps below to set up and run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/News-Aggregator-Website.git
cd News-Aggregator-Website

# 2. Create and activate a virtual environment
python -m venv env
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys in .env or settings file (as per your implementation)

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Start the development server
python manage.py runserver

# 7. Open your browser
Visit http://127.0.0.1:8000/
```
