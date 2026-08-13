# Doctor Finder REST API

Django REST Framework mini project for the TOPS Technologies assessment.

## Assessment coverage

- Doctor model with `name`, `specialization`, and `city`
- DRF `ModelSerializer`
- Custom field-level serializer validation
- `ModelViewSet`
- `DefaultRouter`
- `LimitOffsetPagination`
- `OrderingFilter`
- Atomic transactions for create and update
- DRF Browsable API
- Standard CRUD endpoints
- Postman-ready API examples

## 1. Create and activate a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run migrations

```bash
python manage.py migrate
```

## 4. Start the server

```bash
python manage.py runserver
```

API base URL:

`http://127.0.0.1:8000/api/`

Doctors endpoint:

`http://127.0.0.1:8000/api/doctors/`

Browsable API:

Open the doctors URL in a browser.

## CRUD examples

### GET
`GET /api/doctors/`

### GET with pagination
`GET /api/doctors/?limit=5&offset=0`

### GET with ordering
`GET /api/doctors/?ordering=name`

Descending name:

`GET /api/doctors/?ordering=-name`

Multiple ordering fields:

`GET /api/doctors/?ordering=city,-name`

### GET one doctor
`GET /api/doctors/1/`

### POST
`POST /api/doctors/`

```json
{
    "name": "Dr. Priya Patel",
    "specialization": "Cardiologist",
    "city": "Ahmedabad"
}
```

Expected success status: `201 Created`

### PUT
`PUT /api/doctors/1/`

```json
{
    "name": "Dr. Priya Patel",
    "specialization": "Cardiologist",
    "city": "Surat"
}
```

### PATCH
`PATCH /api/doctors/1/`

```json
{
    "city": "Surat"
}
```

### DELETE
`DELETE /api/doctors/1/`

Expected success status: `204 No Content`

## Postman

Create requests against:

`http://127.0.0.1:8000/api/doctors/`

For POST/PUT/PATCH use:

- Body
- raw
- JSON

The Browsable API and JSON responses can be used to verify status codes and payloads.
