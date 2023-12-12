#!/bin/bash

# Create and activate a virtual environment (optional but recommended)
python -m venv venv

source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate

# Install dependencies
pip install -r requirement.text

