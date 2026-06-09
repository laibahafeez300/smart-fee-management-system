# 🎓 Smart Fee Management System

A web-based Smart Fee Management System developed using **Django Framework** for managing student fee records efficiently.

## 📌 Project Overview

The Smart Fee Management System allows administrators to:

* Add student fee records
* View all student records
* Update fee information
* Delete records
* Search student records
* Track fee status (Paid/Unpaid)

The system provides a user-friendly interface using Bootstrap and stores data using SQLite database.

---

## 🚀 Features

### ✅ CRUD Operations

* Create Student Fee Records
* Read/View All Records
* Update Existing Records
* Delete Records

### ✅ Search Functionality

* Search by Student Name
* Search by Roll Number

### ✅ User Interface

* Responsive Bootstrap Design
* Navigation Bar
* Dashboard/Home Page
* Professional Tables and Forms

### ✅ Validation

* JavaScript Form Validation
* Django Form Validation

---

## 🛠 Technologies Used

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Backend

* Python
* Django Framework

### Database

* SQLite3

### Development Tools

* Visual Studio Code
* GitHub

---

## 📂 Project Structure

```text
fee_management/
│
├── manage.py
├── db.sqlite3
│
├── fee_management/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── fees/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
└── templates/
    ├── base.html
    ├── home.html
    ├── add_fee.html
    ├── view_fee.html
    ├── edit_fee.html
    └── search.html
```

---

## 🗄 Database Model

### StudentFee

| Field      | Type      |
| ---------- | --------- |
| id         | AutoField |
| name       | CharField |
| roll_no    | CharField |
| semester   | CharField |
| fee_status | CharField |

---

## ⚙ Installation Guide

### Clone Repository

```bash
git clone https://github.com/laibahafeez300/smart-fee-management-system.git
```

### Move into Project Folder

```bash
cd smart-fee-management-system
```

### Install Django

```bash
pip install django
```

### Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

### Open Browser

```text
http://127.0.0.1:8000/
```

---


---

## 🎯 Learning Outcomes

Through this project I learned:

* Django Models
* Django Forms
* Django Templates
* CRUD Operations
* Bootstrap Integration
* URL Routing
* Database Management
* Web Application Development

---

## 👩‍💻 Developer

**Name:** Laiba Hafeez

**Course:** CYS-463L Web Engineering Lab

**Semester:** BS Cyber Security (6th Semester)

---

## 📄 License

This project is developed for educational and academic purposes.
