import os

"""
    In some case (OS's and/or Python versions a base directory is required when referencing the folder structure
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
