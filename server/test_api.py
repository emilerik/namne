#!/usr/bin/env python3
"""
Test script to verify the API is working correctly
"""
import requests
from requests.auth import HTTPBasicAuth

# API base URL
BASE_URL = "http://localhost:8000"

# Test credentials
USERNAME = "emil"
PASSWORD = "950615"


def test_health():
    """Test health endpoint (no auth required)"""
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    print("✓ Health check passed\n")


def test_root():
    """Test root endpoint"""
    print("Testing root endpoint...")
    response = requests.get(BASE_URL)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    print("✓ Root endpoint passed\n")


def test_authenticate():
    """Test authentication"""
    print("Testing authentication...")
    auth = HTTPBasicAuth(USERNAME, PASSWORD)
    response = requests.get(f"{BASE_URL}/authenticate", auth=auth)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    print("✓ Authentication passed\n")


def test_get_names():
    """Test getting names"""
    print("Testing get names...")
    auth = HTTPBasicAuth(USERNAME, PASSWORD)
    response = requests.get(f"{BASE_URL}/names", auth=auth)
    print(f"Status: {response.status_code}")
    print(f"Response preview: {response.json()}")
    assert response.status_code == 200
    print("✓ Get names passed\n")


def main():
    print("Starting API tests...\n")

    try:
        test_health()
        test_root()
        test_authenticate()
        test_get_names()

        print("All tests passed! ✓")

    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API. Is the server running?")
        print("Start the server with: python start.py")
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
