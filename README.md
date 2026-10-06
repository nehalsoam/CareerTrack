# Job Application Tracker

A web-based Job Application Tracker developed using Python, Flask, SQLite, HTML and CSS.

The application helps users manage and track their job applications in one place. Users can add, view, search, filter, edit and delete applications and monitor their application status through a dashboard.

## Features

- Add new job applications
- View all job applications
- Search applications by company or job role
- Filter applications by status
- Edit application details
- Delete applications with confirmation
- Dashboard with application statistics
- Pagination for application records
- Form validation
- Responsive design for mobile and desktop

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- Jinja2

## Application Status

The tracker supports the following application statuses:

- Applied
- Shortlisted
- Interview
- Rejected
- Selected

## Project Structure

```text
Job-Application-Tracker/
│
├── app.py
├── database.db
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