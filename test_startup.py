#!/usr/bin/env python3
"""Test script to verify the app starts correctly"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

try:
    from app import app
    print("SUCCESS: App imported successfully")
    
    # Test health endpoint
    from fastapi.testclient import TestClient
    client = TestClient(app)
    response = client.get("/health")
    print(f"SUCCESS: Health check: {response.status_code} - {response.json()}")
    
    # Test servers list
    response = client.get("/api/v1/servers")
    print(f"SUCCESS: Servers list: {response.status_code} - Found {len(response.json())} servers")
    
    print("SUCCESS: All tests passed!")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)