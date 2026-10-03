# 🐾 Pet Adoption & Rescue Platform

A Django-based Pet Adoption and Rescue Platform where users can browse pets,
submit adoption requests, and track their adoption status.

## Features

- User Registration
- User Login & Logout
- User Profile
- Pet Listing
- Pet Details
- Pet Search
- Pet Filtering
- Adoption Requests
- User Adoption Dashboard
- Admin Pet Management
- Admin Adoption Management
- Adoption Approval/Rejection
- JWT Authentication
- REST API
- API Search and Filtering
- API Pagination
- PostgreSQL Database
- Image Upload
- Responsive Custom CSS UI

## Technologies

- Python
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL
- HTML
- CSS
- JavaScript

## API Endpoints

### Authentication

POST `/api/token/`

POST `/api/token/refresh/`

POST `/api/accounts/register/`

GET `/api/accounts/profile/`

PUT `/api/accounts/profile/`

### Pets

GET `/api/pets/`

GET `/api/pets/<id>/`

POST `/api/pets/`

PUT `/api/pets/<id>/`

DELETE `/api/pets/<id>/`

### Adoption

GET `/api/adoptions/`

POST `/api/adoptions/`

GET `/api/adoptions/<id>/`

PUT `/api/adoptions/<id>/`

## Search & Filtering

Example:

`/api/pets/?search=golden`

`/api/pets/?animal_type=Dog`

`/api/pets/?gender=Male`

`/api/pets/?location=Dhaka`

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt