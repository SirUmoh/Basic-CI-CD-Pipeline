# Optionally, you can import all tests or specific test cases
from .test_app import test_homepage, client  # Example import of all test cases from 'test_main.py'

# You can define what gets imported with 'from tests import *'
__all__ = ['test_homepage, client']
