from src.logger.logger import (
    Logger,
)

from src.logger.listeners import (
    ConsoleLogger,
    FileLogger,
)

def initialize_logger():
    logger = Logger()
    console_logger = ConsoleLogger()
    file_logger = FileLogger()
    
    logger.register_listener(console_logger)
    logger.register_listener(file_logger)
    
    return logger

logger = initialize_logger()