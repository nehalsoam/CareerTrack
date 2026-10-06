from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# =========================
# CREATE DATABASE
# =========================

def create_database():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            location TEXT,
            status TEXT,
            applied_date TEXT
        )
    """)

    conn.commit()
    conn.close()


# =========================
# HOME
# =========================

@app.route("/")
def home():

    return render_template("home.html")


# =========================
# DASHBOARD
# =========================

@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM applications")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Applied'"
    )
    applied = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Shortlisted'"
    )
    shortlisted = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Interview'"
    )
    interview = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Rejected'"
    )
    rejected = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Selected'"
    )
    selected = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        total=total,
        applied=applied,
        shortlisted=shortlisted,
        interview=interview,
        rejected=rejected,
        selected=selected
    )


# =========================
# ADD APPLICATION
# =========================

@app.route("/add", methods=["GET", "POST"])
def add_application():

    if request.method == "POST":

        company = request.form["company"]
        role = request.form["role"]
        location = request.form["location"]
        status = request.form["status"]
        applied_date = request.form["applied_date"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO applications
            (company, role, location, status, applied_date)
            VALUES (?, ?, ?, ?, ?)
        """, (
            company,
            role,
            location,
            status,
            applied_date
        ))

        conn.commit()
        conn.close()

        return redirect("/applications")

    return render_template("add_application.html")


# =========================
# APPLICATIONS
# SEARCH + FILTER + PAGINATION
# =========================

@app.route("/applications")
def applications():

    search = request.args.get("search", "")
    status = request.args.get("status", "")

    page = request.args.get("page", 1, type=int)

    if page < 1:
        page = 1

    # 10 applications per page
    per_page = 10

    offset = (page - 1) * per_page

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # =========================
    # COUNT TOTAL APPLICATIONS
    # =========================

    count_query = """
        SELECT COUNT(*)
        FROM applications
        WHERE 1=1
    """

    count_parameters = []

    if search:

        count_query += """
            AND (company LIKE ? OR role LIKE ?)
        """

        count_parameters.append("%" + search + "%")
        count_parameters.append("%" + search + "%")

    if status:

        count_query += """
            AND status = ?
        """

        count_parameters.append(status)

    cursor.execute(
        count_query,
        count_parameters
    )

    total_applications = cursor.fetchone()[0]


    # =========================
    # GET APPLICATIONS
    # =========================

    query = """
        SELECT *
        FROM applications
        WHERE 1=1
    """

    parameters = []

    if search:

        query += """
            AND (company LIKE ? OR role LIKE ?)
        """

        parameters.append("%" + search + "%")
        parameters.append("%" + search + "%")

    if status:

        query += """
            AND status = ?
        """

        parameters.append(status)

    # IMPORTANT:
    # ASC = ID 1, 2, 3, 4...
    query += """
        ORDER BY id ASC
        LIMIT ? OFFSET ?
    """

    parameters.append(per_page)
    parameters.append(offset)

    cursor.execute(
        query,
        parameters
    )

    applications_list = cursor.fetchall()

    conn.close()


    # =========================
    # TOTAL PAGES
    # =========================

    if total_applications == 0:

        total_pages = 1

    else:

        total_pages = (
            total_applications + per_page - 1
        ) // per_page


    # =========================
    # INVALID PAGE CHECK
    # =========================

    if page > total_pages:

        return redirect(
            "/applications?page={}&search={}&status={}".format(
                total_pages,
                search,
                status
            )
        )


    # =========================
    # SHOWING NUMBER
    # =========================

    if total_applications == 0:

        start_number = 0
        end_number = 0

    else:

        start_number = offset + 1

        end_number = min(
            offset + per_page,
            total_applications
        )


    return render_template(
        "applications.html",

        applications=applications_list,

        page=page,

        total_pages=total_pages,

        total_applications=total_applications,

        start_number=start_number,

        end_number=end_number,

        search=search,

        status=status
    )


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_application(id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if request.method == "POST":

        company = request.form["company"]
        role = request.form["role"]
        location = request.form["location"]
        status = request.form["status"]
        applied_date = request.form["applied_date"]

        cursor.execute("""
            UPDATE applications
            SET company = ?,
                role = ?,
                location = ?,
                status = ?,
                applied_date = ?
            WHERE id = ?
        """, (
            company,
            role,
            location,
            status,
            applied_date,
            id
        ))

        conn.commit()
        conn.close()

        return redirect("/applications")

    cursor.execute(
        """
        SELECT *
        FROM applications
        WHERE id = ?
        """,
        (id,)
    )

    application = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_application.html",
        application=application
    )


# =========================
# DELETE APPLICATION
# =========================

@app.route("/delete/<int:id>")
def delete_application(id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM applications
        WHERE id = ?
        """,
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/applications")


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":

    create_database()

    app.run(debug=True)