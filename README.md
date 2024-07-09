# Book Management Flask

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/8Nigel8/BooksInfo.git
   cd BooksInfo/

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the backend:
   ```bash
   start flask run
5. Open index.html in your browser:
    ```bash
   index.html
   
## Usage
Navigate to http://localhost:5000/api in your web browser to access the application.

### API Documentation

#### Get All Books

- **URL**: `http://127.0.0.1:5000/api/books`
- **Method**: GET
- **Description**: Fetches all books from the database.
- **Response**: 
  ```json
  {
    "data": [
      {
        "author": str,
        "id": int,
        "isbn": str,
        "pages": int,
        "published_date": str,
        "title": stt
      }
    ],
    "status": "success"
  }

#### Create a New Book

- **URL**: `http://127.0.0.1:5000/api/books`
- **Method**: POST
- **Description**: Creates a new book record in the database.
- **Request Body**:
    ```json
    {
    "author": str,
    "isbn": str,
    "pages": int,
    "published_date": date,
    "title": str
    }
- **Response**: 
  ```json
  {
  "data": {
    "author": str,
    "id": int,
    "isbn": str,
    "pages": int,
    "published_date": str,
    "title": str
  },
  "status": "success"
  }

#### Update an Existing Book

- **URL**: `http://127.0.0.1:5000/api/books/<int:id>`
- **Method**: PUT
- **Description**: Updates an existing book record identified by `<id>` in the database.
- **Request Body**:
    ```json
    {
    "author": str,
    "isbn": str,
    "pages": int,
    "published_date": date,
    "title": str
    }
- **Response**: 
  ```json
  {
  "data": {
    "author": str,
    "id": int,
    "isbn": str,
    "pages": int,
    "published_date": str,
    "title": str
  },
  "status": "success"
  }

#### Delete a Book

- **URL**: `http://127.0.0.1:5000/api/books/<int:id>`
- **Method**: DELETE
- **Description**: Deletes a book record identified by `<id>` from the database.
- **Response**: 
  ```json
  {
  "status": "success"
  }

#### Get a Book by ID

- **URL**: `http://127.0.0.1:5000/api/books/<int:id>`
- **Method**: GET
- **Description**: Retrieves a specific book record identified by `<id>` from the database.
- **Response**: 
  ```json
  {
  "data": {
    "author": str,
    "id": int,
    "isbn": str,
    "pages": int,
    "published_date": str,
    "title": str
  },
  "status": "success"
  }
  
## IMPORTANTLY
Enter isbn in isbn10 format

Here are some examples:
 - 0261103571
 - 0385504209
 - 0140283331
 - 0679783261
 - 0747532699
 - 0451524934
 - 0195153448
 - 0307474275
 - 067978327X
 - 0316769487