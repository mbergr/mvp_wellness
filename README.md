# Wellness Check-In

A comprehensive mental health companion web application built with Flask, helping users track their daily moods and emotional well-being.

## Features

- 📝 Daily mood tracking with reflection
- 📊 Visual mood history and trends
- 👤 User authentication and profiles
- ⏰ Customizable reminders
- 🎨 Clean, minimalist interface

## Tech Stack

- **Backend**: Python/Flask
- **Database**: SQLAlchemy with SQLite
- **Frontend**: Bulma CSS, Chart.js
- **Authentication**: Flask-Login

## Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/mvp_wellness.git
cd mvp_wellness
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Unix/MacOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-super-secret-key
DATABASE_URL=sqlite:///wellness.db
```

5. Initialize the database:
```bash
flask db upgrade
```

6. Run the application:
```bash
flask run
```

Visit `http://127.0.0.1:5000` in your browser.

## Project Structure

```
mvp_wellness/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── user.py
│   ├── templates/
│   │   ├── auth/
│   │   ├── mood/
│   │   └── base.html
│   ├── utils/
│   │   └── ai_helper.py
│   ├── routes.py
│   └── auth.py
├── migrations/
├── instance/
├── venv/
├── .env
├── .gitignore
├── requirements.txt
└── run.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
