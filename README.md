# TODO-project-DP
Todo App in Streamlit
=====================

Welcome to the Todo App in Streamlit, a basic yet powerful application to manage your daily tasks. This application is developed using Streamlit and an SQLite database, and is written in Python 3.12.

Features
--------

*   **Read tasks**: Read tasks in your to-do list.
*   **User-friendly interface**: A simple and clean interface thanks to Streamlit.

Requirements
------------

*   Python 3.12
*   Streamlit
*   SQLite3

Installation
------------

1.  **Clone the repository**
    
        git clone https://github.com/EduardoVparga/TODO-project-DP.git
        cd DesignPatterns
    
2.  **Create a virtual environment**
    
        python3.12 -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
3.  **Install the dependencies**
    
        pip install -r requirements.txt
    
4.  **Run the application**
    
        streamlit run main.py
    

Usage
-----

1.  **Start the application** by following the installation steps.
2.  **See tasks** using the form at the top of the page.

Project Structure
-----------------

    todo-app-streamlit/
    │
    ├── app/               # Application-related files
    │   └── components/    # UI component files
    │       ├── card.py
    │       ├── modal.py
    │       ├── main.py
    │       └── utils.py
    ├── db/            # Database-related files (Singlenton Pattern)
    │    ├── init.py
    │    ├── StartDataScript.sql
    │    └── todo.db
    │
    ├── src/               # Source files
    │   ├── images/        # Image-related source files (Adapter Pattern)
    │   │   ├── animal_request.py
    │   │   ├── cat.py
    │   │   └── dog.py
    │   └── logger/        # Logger-related source files (Observer Pattern)
    │       ├── init.py
    │       ├── listeners.py
    │       └── logger.py
    │   
    ├── init.py 
    ├── main.py
    ├── requirements.txt   # Project dependencies
    └── README.md          # This file

Contributing
------------

Contributions are welcome! If you have any improvements or have found any bugs, feel free to open an issue or a pull request.

1.  **Fork the repository**
2.  **Create a new branch** (`git checkout -b feature/new-feature`)
3.  **Make your changes** and commit (`git commit -am 'Add new feature'`)
4.  **Push to the branch** (`git push origin feature/new-feature`)
5.  **Open a pull request**

License
-------

This project is licensed under the MIT License. See the `LICENSE` file for more details.

Developed with ❤️ by **catalinalopezb7**, **YasamanBadeli** & **EduardoVparga**  
