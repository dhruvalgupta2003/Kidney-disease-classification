import os
from pathlib import Path
from loguru import logger

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "logs/app.log",
    "tests/__init__.py",
    "conifg/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    ".gitignore",
    "docker-compose.yml",
    "Dockerfile",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logger.info(f"Creating directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logger.info(f"Creating empty file: {filepath}")
    
    else:
        logger.info(f"{filename} is already exists")

# setup logs
# Define log file path
log_file = os.path.join('logs', "app.log")

# Remove any previously configured handlers to prevent duplicate logs
logger.remove()

# Add new log configuration
logger.add(
    log_file,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{line} - {message}",
    level="DEBUG",
    rotation="5 MB",
    compression="zip",  # Compress old logs to save space
    enqueue=True  # Safe for multi-threading
)

# Now logging will work correctly
logger.info("Logging is set up! Logs will be stored in 'log/app.log'")
