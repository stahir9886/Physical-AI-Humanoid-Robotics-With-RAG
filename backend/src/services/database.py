import asyncpg
import os
from typing import Optional
from contextlib import asynccontextmanager


class DatabaseService:
    def __init__(self):
        self.pool = None
        self.database_url = os.getenv("NEON_DATABASE_URL")
    
    async def connect(self):
        """Initialize the database connection pool."""
        if not self.database_url:
            raise ValueError("NEON_DATABASE_URL environment variable is not set")
        
        self.pool = await asyncpg.create_pool(
            dsn=self.database_url,
            min_size=1,
            max_size=10,
            command_timeout=60
        )
    
    async def disconnect(self):
        """Close the database connection pool."""
        if self.pool:
            await self.pool.close()
    
    @asynccontextmanager
    async def get_connection(self):
        """Get a connection from the pool."""
        if not self.pool:
            raise RuntimeError("Database connection pool not initialized")
        
        conn = await self.pool.acquire()
        try:
            yield conn
        finally:
            await self.pool.release(conn)
    
    async def execute_query(self, query: str, *args):
        """Execute a query and return the result."""
        async with self.get_connection() as conn:
            return await conn.fetch(query, *args)
    
    async def execute_query_row(self, query: str, *args):
        """Execute a query and return a single row."""
        async with self.get_connection() as conn:
            return await conn.fetchrow(query, *args)
    
    async def execute_command(self, command: str, *args):
        """Execute a command (INSERT, UPDATE, DELETE) and return affected rows."""
        async with self.get_connection() as conn:
            return await conn.execute(command, *args)