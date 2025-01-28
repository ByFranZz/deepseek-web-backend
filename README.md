# Deepseek Backend

This project is a backend service that utilizes the Deepseek API. It is built using FastAPI and provides a set of routes to interact with the Deepseek service.

## Project Structure

```
deepseek-web-backend
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   └── deepseek.py
│   ├── services
│   │   ├── __init__.py
│   │   └── deepseek_service.py
│   ├── models
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ByFranZz/deepseek-web-backend.git
   cd deepseek-web-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables in the `.env` file.

## Usage

To run the application, execute the following command:

```
uvicorn src.main:app --reload
```

Visit `http://localhost:8000/docs` to access the API documentation and test the endpoints.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.