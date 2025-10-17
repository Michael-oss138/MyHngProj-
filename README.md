# 🧩 Dynamic Profile API — HNG Backend Wizards Stage 0  

A simple **Django REST Framework** API that returns my profile details and a **random cat fact** fetched dynamically from the public [Cat Facts API](https://catfact.ninja/fact).  

This project was built as part of **HNG 11 — Backend Wizards (Stage 0)** to demonstrate my understanding of RESTful endpoints, third-party API integration, and structured JSON responses.  

---

## 🚀 Endpoint  

### **GET /me**  

**URL:**  
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On Mac/Linux

pip install -r requirements.txt

python manage.py migrate

## Technologies Used

Python 3

Django 5

Django REST Framework

Requests Library

Django>=5.0
djangorestframework
requests

## Cat Fact API

"fact": "failed to get cat fact."


This API was developed as part of the HNG 11 Backend Wizards Stage 0 task.

### The goals were to:

Build a RESTful API endpoint.

Integrate a third-party API.

Return dynamic JSON with a current UTC timestamp.

Handle API failures gracefully

## Example
web-production-856bd.up.railway.app/me