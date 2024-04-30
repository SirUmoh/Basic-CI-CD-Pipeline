# This is the package-level initialization for the 'app' package

# Optional: Print a message when the package is imported
print("Initializing the 'app' package")

# Importing the main Flask application from 'main.py'
from .app import app  # Importing the Flask app to make it accessible at the package level

__all__ = ['app']
