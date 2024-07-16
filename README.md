* * * * *

TweetApp
========

Welcome to TweetApp! This application allows users to log in and create posts with images, which are displayed on the homepage. It is built using Django.

Table of Contents
-----------------

-   [Features](#features)
-   [Folder Structure](#folder-structure)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Contributing](#contributing)
-   [License](#license)
-   [Contact](#contact)

Features
--------

-   User authentication: Register and log in to your account.
-   Create posts: Share your thoughts along with images.
-   Homepage: View all posts created by users in a clean and organized layout.

#Screenshots
![image](https://github.com/user-attachments/assets/5bcd1539-ba4f-4c25-8b5a-bc06d66172c8)


Folder Structure
----------------

The folder structure of the project is as follows:

![image](https://github.com/user-attachments/assets/638d5615-199b-4f2e-bd87-24dc6c63003e)

Installation
------------

To get a local copy up and running, follow these simple steps:

1.  **Clone the repository:**

    ```
     git clone https://github.com/Oviyan007/TweetApp.git
    ```
    ```
    cd TweetApp
    ```

3.  **Create a virtual environment:**

    ```
    python -m venv venv
    ```
     

5.  **Activate the virtual environment:**

    -   On Windows:

      

        ```
        venv\Scripts\activate
        ```

    -   On macOS/Linux:



        ```
        source venv/bin/activate
        ```

6.  **Install dependencies:**

  

    ```
    pip install -r requirements.txt
    ```

8.  **Apply migrations:**




    ```
    python manage.py migrate
    ```

10.  **Run the development server:**



    ```
    python manage.py runserver
    
    ```
    

Usage
-----

1.  Open your web browser and go to `http://127.0.0.1:8000/`.
2.  Register a new account or log in with an existing account.
3.  Create new posts by clicking on the "New Post" button.
4.  Upload an image and share your thoughts.
5.  View all posts on the homepage.

Contributing
------------

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

License
-------

Distributed under the MIT License. See `LICENSE` for more information.

Contact
-------

Oviyan S - oviyan.btech@gmail.com

Project Link: <https://github.com/Oviyan007/TweetApp>
