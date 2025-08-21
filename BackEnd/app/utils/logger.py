import logging
import sys

# Tạo logger
logger = logging.getLogger("assistant_logger")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# Format log
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
    "%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(formatter)

# Gắn handler nếu chưa có
if not logger.hasHandlers():
    logger.addHandler(console_handler)
