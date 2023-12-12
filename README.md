<h1 align="center">
  <b>In-Memory File System</b>
</h1>

## Overview

This project implements an in-memory file system with functionalities such as creating directories, navigating through directories, listing directory contents, creating files, writing to files, displaying file contents, and more. The project is divided into two main components: a Flask-based server and a command-line interface (CLI) for interacting with the server.

## Features

- **Server (`server.py`):**
  - Implemented using Flask.
  - Handles HTTP requests to perform file system operations.
  - Supports creating directories, listing contents, creating files, etc.
  - Provides RESTful endpoints for communication.

- **CLI (`cli.py`):**
  - Implements a command-line interface for interacting with the server.
  - Supports commands like `mkdir`, `ls`, `cd`, `touch`, `echo`, `cat`, and more.
  - Sends HTTP requests to the server to perform operations.
 
## Functions Implemented
  - **Handle Directory Creation (/mkdir endpoint):**
    - Accepts requests to create a new directory.
    - Manages the in-memory representation of the file system structure.
  - **Handle Listing Directory Contents (/ls endpoint):**
    - Processes requests to list the contents of a directory.
    - Retrieves and sends information about files and subdirectories.
  - **Handle Directory Navigation (/cd endpoint):**
    - Manages requests to change the current working directory.
    - Supports relative and absolute path navigation.
  - **Handle File Creation (/touch endpoint):**
    - Responds to requests for creating a new empty file.
    - Updates the file system structure accordingly.
  - **Handle Text Writing to a File (/echo endpoint):**
    - Processes requests to write text to a file.
    - Modifies the content of the specified file.
  - **Handle Displaying File Contents (/cat endpoint):**
    -   Manages requests to display the contents of a file.
    -   Retrieves and sends the content of the specified file.
  - **Handle Moving Files or Directories (/mv endpoint):**
    - Responds to requests for moving a file or directory to another location.
    - Updates the file system structure accordingly.
  - **Handle Copying Files or Directories (/cp endpoint):**
    - Processes requests to copy a file or directory to another location.
    - Creates a copy in the specified destination.
  - **Handle File or Directory Removal (/rm endpoint):**
    - Manages requests to remove a file or directory.
    - Updates the file system structure by removing the specified item.
  - **Handle Search for a Pattern in a File (/grep endpoint) [Bonus]:**
     -   Processes requests to search for a specified pattern in a file.
     -   Returns information about occurrences of the pattern.

## How It Works

1. **Server Setup:**
   - The server is implemented using Flask, a Python web framework.
   - Endpoints are defined to handle different file system operations.

2. **CLI Setup:**
   - The CLI is a script (`cli.py`) that interacts with the server.
   - Uses the `requests` library to send HTTP requests to the server.

3. **Server-Client Communication:**
   - The server and CLI communicate through HTTP requests.
   - Endpoints like `/mkdir`, `/ls`, `/cd`, etc., are defined for different operations.

4. **Data Structures:**
   - The file system structure is maintained in-memory.
   - Directories and files are represented using appropriate data structures.

## Setup

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Setup Commands

#### If `pip` is Not Installed

1. **Install `pip`:**

   - On Unix or MacOS, run the following command:
     ```
     sudo apt-get install python3-pip
     ```

   - On Windows, refer to the [official documentation](https://pip.pypa.io/en/stable/installation/) for instructions.

2. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/in-memory-file-system.git

3. **Navigate to the project directory**
   ```bash
   cd in-memory-file-system
4. **Create a virtual environment**
   ```bash
   python -m venv venv
5. **Activate the virtual enviroment**
   - on Windows
     ```bash
     .\venv\Scripts\activate```
   - on unix or macOS
     ```bash
     source venv/bin/activate```
  
6. **Install project dependencies**
   ```bash
   python -m pip install -r requirement.text```

## Running the Server and CLI
1. **Navigate to the server directory** ```cd server```
2. **Run the server** ```python server.py```
3. **Open a new terminal and navigate to the cli directory:** ```cd CLI```
4. **Run the CLI file** ```python cli.py

## Additional Notes
- **Data Storage:** Data is stored in-memory. Restarting the server will reset the file system state.
- **Endpoints:** Explore the server endpoints by referring to the filesystem_server.py file.
- **Contributions:** Contributions and improvements are welcome. Create a fork and submit a pull request.



  
  
  




