from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from collections import defaultdict
import time
from typing import Dict
from src.config import settings


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.requests = defaultdict(list)  # Store request times by identifier
    
    def _get_identifier(self, request: Request) -> str:
        """Get identifier for rate limiting - IP address for anonymous, user ID if authenticated."""
        # Get client IP address
        client_ip = request.client.host
        return client_ip
    
    def _clean_old_requests(self, identifier: str, now: float):
        """Remove request records older than the window."""
        window_start = now - settings.rate_limit_window
        self.requests[identifier] = [
            req_time for req_time in self.requests[identifier] 
            if req_time > window_start
        ]
    
    async def dispatch(self, request: Request, call_next):
        identifier = self._get_identifier(request)
        now = time.time()
        
        # Clean old requests
        self._clean_old_requests(identifier, now)
        
        # Check if request limit is exceeded
        if len(self.requests[identifier]) >= settings.rate_limit_requests:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Please try again later."
            )
        
        # Add current request to the list
        self.requests[identifier].append(now)
        
        response = await call_next(request)
        return response