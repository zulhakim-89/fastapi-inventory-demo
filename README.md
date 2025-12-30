# 📦 FastAPI Inventory Management API

A simple RESTful API for managing inventory items, built with **FastAPI** and **Pydantic**. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations with automatic Swagger documentation.

## ✨ Features

- **Create** new inventory items
- **Read** all items or a specific item by ID
- **Update** existing items
- **Delete** items from inventory
- **Auto-generated API documentation** (Swagger UI)
- **Unit tests** with pytest

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Web framework |
| Pydantic | Data validation |
| Uvicorn | ASGI server |
| Pytest | Testing |

## 📁 Project Structure

```
simple api practice/
├── main.py           # FastAPI application with CRUD endpoints
├── test_main.py      # Unit tests for API endpoints
├── requirements.txt  # Python dependencies
├── .gitignore        # Git ignore rules
└── venv/             # Virtual environment
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "simple api practice"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the API

```bash
python main.py
```

The server will start at `http://127.0.0.1:8000` and automatically open the Swagger UI documentation in your browser.

## 📖 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/items` | Create a new item |
| `GET` | `/items` | Get all items |
| `GET` | `/items/{item_id}` | Get a specific item |
| `PUT` | `/items/{item_id}` | Update an item |
| `DELETE` | `/items/{item_id}` | Delete an item |

### Example Request Body

```json
{
  "id": 1,
  "name": "Laptop",
  "quantity": 10
}
```

## 🧪 Running Tests

```bash
pytest test_main.py -v
```

The test suite includes a complete CRUD lifecycle test that verifies:
- Item creation
- Item retrieval
- Item update
- Item deletion
- Confirmation of deletion (404 response)

## 📚 API Documentation

Once the server is running, access the interactive documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📝 License

This project is for educational purposes.
