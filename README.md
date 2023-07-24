# Artist API using Django REST Framework

This project implements a customized Artist API using Django REST Framework. The API allows users to perform CRUD operations on artists and their works. Token-based authentication is implemented to ensure that only authenticated users can access the API endpoints.

## Requirements

+ Python 3.x
+ Django 3.x
+ Django REST Framework 3.x

### Setup

1. Clone the Repository

```bash
    https://github.com/Kodiererin/NSNCO.git
```

2. Change the Project Directory to ArtistAPI

```bash
    cd NSNO
```

3. Apply the database migrations:

```bash
    python manage.py migrate
```

4. Change the Project Directory to ArtistAPI

```bash
   python manage.py createsuperuser

```

5. Run the development server:

```bash
    python manage.py runserver
```

## API Reference

#### Get all items

```http
  http://127.0.0.1:8000/admin/
```

#### API Endpoints

| Parameter                         | Description                                                  |
| :-------------------------------- | :----------------------------------------------------------- |
| `GET /api/works/`               | Retrieve a list of all works.                                |
| `POST /api/works/`              | Create a new work.                                           |
| `GET /api/works/<int:pk>/`      | Retrieve details of a specific work.                         |
| `PUT /api/works/<int:pk>/:`     | Update a specific work.                                      |
| `GET /api/artists/`             | Delete a specific work.                                      |
| `POST /api/artists/`            | Retrieve a list of all artists.                              |
| `GET /api/artists/<int:pk>/`    | Create a new artist.                                         |
| `PUT /api/artists/<int:pk>/`    | Retrieve details of a specific artist.                       |
| `DELETE /api/artists/<int:pk>/` | Update a specific artist.                                    |
| `POST /api/register/`           | Register a new user account and get an authentication token. |

#### add(num1, num2)

Takes two numbers and returns the sum.

## Dummy Data

Upon user registration, the API automatically creates an associated Artist object and adds dummy Work objects for testing purposes.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, feel free to open an issue or submit a pull request.
