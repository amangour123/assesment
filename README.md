==========================
Task Management System (DRF + Role-Based Access + Auto Deactivation)
==========================

Description:
------------
This is a secure RESTful web application built using Django REST Framework (DRF), with JWT authentication and role-based access control. The system supports full CRUD operations for users and tasks with the following features:

Roles:
------
1. **Admin**
   - Full unrestricted access.
   - Can create/update/delete users and tasks.
   - Can reactivate users.

2. **Manager**
   - Can assign tasks to users with deadlines.
   - Can view all tasks.
   - Can monitor missed task alerts via a scheduled background job.
   - Can reactivate users.

3. **User**
   - Can view and update the status of their own tasks only.
   - Cannot create/delete tasks or users.

Key Features:
-------------
JWT-based secure authentication  
Role-based access control (Admin, Manager, User)  
Task assignment with deadlines  
Automatic task status update to "missed" via scheduled command
Auto-deactivation of users with 5+ missed tasks in a week via scheduled command
Manual user reactivation by Admin/Manager  
Alerts for Managers: API endpoint to view missed tasks

Project Setup:
--------------
1. **Clone the repository**
git clone https://github.com/amangour123/assesment.git
cd assesment


2. **Create virtual environment & activate it**
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows


3. **Install dependencies**
pip install -r requirements.txt


4. **Skip migrations**
The SQLite database with initial data is already included



5. **Superuser Credentials**
#already created
username:admin
password:admin


6. **Run server**
python manage.py runserver


Scheduled Missed Task Checker:
------------------------------
Missed task status is **not updated manually by users**. Instead, we use a background process that runs every hour using one of the following:

### Option 1: APScheduler (for dev)
Run this file as a background Python process:
cd assesment(after activating virtual env in new terminal)
python schedule_runner.py

This will automatically(running every minute):

-Mark overdue tasks as "missed"

-Deactivate users with 5+ missed tasks in 7 days


### Option 2: Cron Job (Linux/macOS production setup)
1. Edit the crontab:
crontab -e
2. Add this line to run the task every hour:
0 * * * * /absolute/path/to/venv/bin/python /absolute/path/to/project/manage.py auto_update_tasks >> /tmp/auto_update_tasks.log 2>&1
- Replace /absolute/path/to/venv/ and /absolute/path/to/project/ with your actual paths.
3. Save and exit. Cron will now run your command every hour and log output to /tmp/auto_update_tasks.log.


Postman Collection:
Include a Postman collection demonstrating:

JWT login

Create/update users (Admin)

Create/assign tasks (Manager)

View/update task status (User)

Missed alerts (Manager)

Reactivate user

postman collection link:
https://amangour-65796.postman.co/workspace/Aman-Gour's-Workspace~e897b74c-c56f-430d-8481-514c6ea645e6/collection/45781481-009a301f-03be-4ef7-8f40-9e82586e1453?action=share&creator=45781481

Security Notes:
Permissions are enforced using custom permission classes.

All APIs are protected with JWT.

Managers can assign and monitor tasks; Admins have full control.

Users cannot see others’ tasks.

