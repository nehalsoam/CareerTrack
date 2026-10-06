# CareerTrack – Job Application Tracker

A web-based Job Application Tracker built with **Python, Flask, SQLite, HTML, and CSS** to help users organize and monitor their job applications.

## 🚀 Live Demo

**[Open CareerTrack](https://careertrack-g11n.onrender.com/)**

## 📌 Features

* Add new job applications
* Edit application details
* Delete applications with confirmation
* Search applications by company or role
* Filter applications by status
* Dashboard with application status counts
* Pagination for application records
* Responsive design for desktop and mobile
* SQLite database for persistent data storage

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Database:** SQLite
* **Frontend:** HTML5, CSS3
* **Templating:** Jinja2
* **Deployment:** Render
* **Version Control:** Git, GitHub

## 📂 Project Structure

```text
CareerTrack/
│
├── app.py
├── database.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── home.html
│   ├── dashboard.html
│   ├── add_application.html
│   ├── applications.html
│   └── edit_application.html
│
└── static/
    └── style.css
```

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/nehalsoam/CareerTrack.git
cd CareerTrack
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

```text
http://127.0.0.1:5000
```

## 🗄️ Database

The application uses SQLite to store job application records.

Each application contains:

* Company
* Role
* Location
* Status
* Applied Date

## 🔄 Main Functionality

The application follows a simple CRUD workflow:

**Create → Read → Update → Delete**

Users can create applications, view stored applications, update existing records, and delete unwanted records.

## 🔎 Search & Filtering

Users can search applications by **company or role** and filter them according to application status such as:

* Applied
* Shortlisted
* Interview
* Rejected
* Selected

## 📊 Dashboard

The dashboard displays status-wise application counts, helping users quickly understand their job application progress.

## 📄 Pagination

Application records are displayed using pagination to keep the list organized and easier to navigate.

## 🌐 Deployment

The application is deployed using **Render** and is accessible through the Live Demo link above.

## 🔮 Future Improvements

* User authentication
* Application reminders
* Sorting and advanced filters
* Interview date tracking
* Application analytics
* PostgreSQL support for larger-scale usage

## 👨‍💻 Author

**Nehal Singh Soam**

MCA Student | Python & Backend Development

**GitHub:** https://github.com/nehalsoam
