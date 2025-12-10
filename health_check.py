#!/usr/bin/env python3
"""
Health check script for the Textbook Generation API.
This script verifies that all components of the system are functioning properly.
"""

import asyncio
import httpx
import sys
import os
from typing import Dict, List, Tuple

# Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
TIMEOUT = 10.0  # seconds


async def check_health_status() -> Tuple[bool, str]:
    """Check the health status of the API."""
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.get(f"{API_BASE_URL}/health")
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "healthy":
                    return True, f"Health check passed: {data.get('message', 'Service operational')}"
                else:
                    return False, f"Health check failed: {data}"
            else:
                return False, f"Health check returned status code: {response.status_code}"
    except Exception as e:
        return False, f"Health check failed with exception: {str(e)}"


async def check_readiness_status() -> Tuple[bool, str]:
    """Check the readiness of the API."""
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.get(f"{API_BASE_URL}/ready")
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "ready":
                    return True, f"Readiness check passed: {data.get('message', 'Service ready')}"
                else:
                    return False, f"Readiness check failed: {data}"
            else:
                return False, f"Readiness check returned status code: {response.status_code}"
    except Exception as e:
        return False, f"Readiness check failed with exception: {str(e)}"


async def check_chapters_endpoint() -> Tuple[bool, str]:
    """Check that the chapters endpoint is working."""
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.get(f"{API_BASE_URL}/api/chapters")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and len(data) > 0:
                    return True, f"Chapters endpoint working, returned {len(data)} chapters"
                else:
                    return False, f"Chapters endpoint returned unexpected data: {data}"
            else:
                return False, f"Chapters endpoint returned status code: {response.status_code}"
    except Exception as e:
        return False, f"Chapters endpoint check failed with exception: {str(e)}"


async def check_chat_endpoint() -> Tuple[bool, str]:
    """Check that the chat endpoint is working."""
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            # This is a mock request since we don't have a real session to test with
            # In a real scenario, you'd need to create a valid session first
            test_data = {
                "query_id": "test-query-123",
                "session_id": "test-session-456",
                "query_text": "What is Physical AI?",
                "timestamp": "2023-10-01T10:00:00Z"
            }
            response = await client.post(f"{API_BASE_URL}/api/chat/query", json=test_data)
            if response.status_code in [200, 422]:  # 422 is validation error which is expected for test
                return True, f"Chat endpoint reachable (status: {response.status_code})"
            else:
                return False, f"Chat endpoint returned unexpected status code: {response.status_code}"
    except Exception as e:
        return False, f"Chat endpoint check failed with exception: {str(e)}"


async def run_all_checks() -> bool:
    """Run all health checks and return True if all pass."""
    print("Starting health checks for Textbook Generation API...")
    print(f"Target API URL: {API_BASE_URL}")
    print("-" * 50)
    
    checks = [
        ("Health Status", check_health_status),
        ("Readiness Status", check_readiness_status),
        ("Chapters Endpoint", check_chapters_endpoint),
        ("Chat Endpoint", check_chat_endpoint),
    ]
    
    results = []
    for check_name, check_func in checks:
        print(f"Running {check_name} check...")
        success, message = await check_func()
        results.append((check_name, success))
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"  {status}: {message}")
        print()
    
    print("-" * 50)
    print("Health Check Summary:")
    all_passed = True
    for check_name, success in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"  {check_name}: {status}")
        if not success:
            all_passed = False
    
    print()
    if all_passed:
        print("🎉 All health checks passed! The API is ready for use.")
        return True
    else:
        print("❌ Some health checks failed. Please review the issues above.")
        return False


if __name__ == "__main__":
    # Allow custom API URL from command line
    if len(sys.argv) > 1:
        API_BASE_URL = sys.argv[1]
    
    # Run the health checks
    success = asyncio.run(run_all_checks())
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)