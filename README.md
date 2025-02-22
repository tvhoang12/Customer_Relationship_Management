# HGHGCRM
make a CRM application with Django

## Features

- Customer: CRUD Create, Read, Update, Delete
- Product: CRUD operations
- Employee: CRUD operations
- Task Board: CRUD, with filter function according to work status and assigned personnel.
- RESTful API with Django REST Framework
- JWT Authentication
- Customized Django Admin Interface
- API Documentation with Swagger UI
- Filtering and Search Capabilities

## Technical Stack

- Django
- Django REST Framework
- Django Filter
- Simple JWT
- drf-spectacular (Swagger/OpenAPI)
- SQLite (default database)

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/tvhoang12/Customer_Relationship_Management.git
cd Customer_Relationship_Management
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python crmp2/crmp2/manage.py makemigrations
python crmp2/crmp2/manage.py migrate
```

5. Create a superuser:
```bash
python crmp2/manage.py createsuperuser
```

6. Run the development server:
```bash
python crmp2/manage.py runserver
```

### Authentication
- `POST /api/token/`: Obtain JWT token pair
- `POST /api/token/refresh/`: Refresh JWT token

### Customers
- `GET /api/customers/`: List all customers
- `POST /api/customers/`: Create a new customer
- `GET /api/customers/{id}/`: Retrieve a customer
- `PUT /api/customers/{id}/`: Update a customer
- `DELETE /api/customers/{id}/`: Delete a customer

### Products
- `GET /api/products/`: List all products
- `POST /api/products/`: Create a new product
- `GET /api/products/{id}/`: Retrieve a product
- `PUT /api/products/{id}/`: Update a product
- `DELETE /api/products/{id}/`: Delete a product

### Employees
- `GET /api/employees/`: List all employees
- `POST /api/employees/`: Create a new employee
- `GET /api/employees/{id}/`: Retrieve an employee
- `PUT /api/employees/{id}/`: Update an employee
- `DELETE /api/employees/{id}/`: Delete an employee

### Tasks
- `GET /api/tasks/`: List all tasks
- `POST /api/tasks/`: Create a new task
- `GET /api/tasks/{id}/`: Retrieve a task
- `PUT /api/tasks/{id}/`: Update a task
- `DELETE /api/tasks/{id}/`: Delete a task

## API Documentation

- Swagger UI: `/api/docs/`
- ReDoc: `/api/redoc/`
- OpenAPI Schema: `/api/schema/`

## Filtering and Search

The API supports filtering and searching on various endpoints:

### Customers
- Filter by name
- Search by name and email

### Products
- Filter by stock and price
- Search by name, description

### Tasks
- Filter by status, priority, assigned employee
- Search by title and description

## Authentication

The API uses JWT (JSON Web Token) authentication. To authenticate:

1. Obtain a token pair:
```bash
curl -X POST /api/token/ -d "username=your_username&password=your_password"
```

2. Use the access token in subsequent requests:
```bash
curl -H "Authorization: Bearer your_access_token" /api/customers/
```

3. Refresh token when expired:
```bash
curl -X POST /api/token/refresh/ -d "refresh=your_refresh_token"
```

## Admin Interface

Access the admin interface at `/admin/` to manage:
- Customers
- Products
- Employees
- Tasks

The admin interface provides:
- Advanced filtering
- Search functionality
- Custom list displays
- Organized fieldsets
- Read-only fields

## Development

To run tests:
```bash
python crmp2/manage.py test
```

To generate schema:
```bash
python crmp2/manage.py spectacular --file schema.yml
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.