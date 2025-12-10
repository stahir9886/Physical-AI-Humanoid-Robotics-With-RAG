import logging
import sys
from typing import Optional
from datetime import datetime


class Logger:
    def __init__(self, name: str, level: str = "INFO"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper()))
        
        # Create console handler with formatting
        if not self.logger.handlers:  # Prevent duplicate handlers
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def info(self, message: str):
        self.logger.info(message)
    
    def warning(self, message: str):
        self.logger.warning(message)
    
    def error(self, message: str, exc_info: bool = False):
        self.logger.error(message, exc_info=exc_info)
    
    def debug(self, message: str):
        self.logger.debug(message)


def get_logger(name: str, level: Optional[str] = None) -> Logger:
    """Get a configured logger instance."""
    from src.config import settings
    log_level = level or settings.log_level
    return Logger(name, log_level)