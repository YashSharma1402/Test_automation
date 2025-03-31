FastAPI Test Automation Project

This project demonstrates how to set up a FastAPI server, write automated tests using requests and pytest, and integrate continuous testing using GitHub Actions.

Project Structure

├── apiserver.py             # FastAPI server with basic math operations
├── testAutomation.py        # Automated tests using requests
├── testAutomationPytest.py  # Automated tests using pytest
├── .github/workflows/test.yml  # GitHub Actions CI/CD workflow
├── README.md                # Project documentation

Task 1: Set Up the FastAPI Server

1️⃣ Install Required Packages

pip install fastapi uvicorn

2️⃣ Create FastAPI Server (apiserver.py)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    return {"result": num1 + num2}

@app.get("/subtract/{num1}/{num2}")
def subtract(num1: int, num2: int):
    return {"result": num1 - num2}

@app.get("/multiply/{num1}/{num2}")
def multiply(num1: int, num2: int):
    return {"result": num1 * num2}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("apiserver:app", host="0.0.0.0", port=8000, reload=True)

3️⃣ Run the Server

python apiserver.py

Server will be available at http://localhost:8000
<img width="896" alt="image" src="https://github.com/user-attachments/assets/65e415dc-cbc8-4a1d-977e-8b609aa79b4e" />


Task 2: Writing Automated Tests for the API

1️⃣ Install Requests Library

pip install requests

2️⃣ Create Test Script (testAutomation.py)

import requests

testcases = [
    {"url": "http://localhost:8000/add/2/2", "expected": 4, "description": "Test addition of 2 and 2"},
    {"url": "http://localhost:8000/subtract/2/2", "expected": 0, "description": "Test subtraction of 2 from 2"},
    {"url": "http://localhost:8000/multiply/2/2", "expected": 4, "description": "Test multiplication of 2 and 2"}
]

def test():
    for case in testcases:
        response = requests.get(case["url"])
        result = response.json()["result"]
        assert result == case["expected"], f"Test failed: {case['description']}. Expected {case['expected']}, got {result}"
        print(f"Test passed: {case['description']}")

test()
![Uploading image.png…]()


3️⃣ Run the Tests

python testAutomation.py

Task 3: Enhancing Tests with Pytest

1️⃣ Install Pytest

pip install pytest

2️⃣ Create pytest Test Script (testAutomationPytest.py)

import pytest
import requests

testcases = [
    ("http://localhost:8000/add/2/2", 4, "Test addition of 2 and 2"),
    ("http://localhost:8000/subtract/2/2", 0, "Test subtraction of 2 from 2"),
    ("http://localhost:8000/multiply/2/2", 4, "Test multiplication of 2 and 2"),
    ("http://localhost:8000/add/-1/1", 0, "Test addition of -1 and 1"),
    ("http://localhost:8000/multiply/0/5", 0, "Test multiplication by zero"),
]

@pytest.mark.parametrize("url, expected, description", testcases)
def test_api(url, expected, description):
    response = requests.get(url)
    result = response.json()["result"]
    assert result == expected, f"{description}. Expected {expected}, got {result}"
    <img width="864" alt="image" src="https://github.com/user-attachments/assets/15a196e7-0747-49a0-b228-951564b8195d" />


3️⃣ Run Tests with Pytest

pytest testAutomationPytest.py

Task 4: Integrating Test Automation with GitHub Actions

1️⃣ Create GitHub Actions Workflow (.github/workflows/test.yml)

name: API Tests

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install fastapi uvicorn pytest requests

      - name: Start FastAPI server
        run: |
          nohup python apiserver.py &
        env:
          PYTHONUNBUFFERED: 1

      - name: Wait for server to be ready
        run: sleep 5  # Wait to ensure the server is up

      - name: Run tests
        run: pytest testAutomationPytest.py

2️⃣ Commit and Push to GitHub

git add .
git commit -m "Add test automation and GitHub Actions"
git push origin main

3️⃣ View GitHub Actions Results

Go to the Actions tab in your GitHub repository to check test results.

Task 5: Expanding Automation for Real-World Projects

✅ Additional Features to Consider:

Database Integration: Use PostgreSQL or MongoDB and test database interactions.

Authentication & Authorization: Implement JWT, OAuth2, or API keys and test security.

Advanced Error Handling & Logging: Use logging frameworks and track API errors.

Performance Testing: Use locust.io or pytest-benchmark for load testing.

🎯 Conclusion

In this project, you have learned how to:
✅ Set up a FastAPI backend with basic API endpoints.
✅ Write automated tests using requests and pytest.
✅ Integrate test automation with GitHub Actions for continuous testing.
✅ Expand automation for real-world applications with authentication, databases, and performance testing.

This foundation is essential for ensuring reliable and scalable APIs in DevOps workflows. 🚀

