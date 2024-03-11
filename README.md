# Personal Blog

This is a basic web development project by a beginner. I will be using HTML, CSS, and the Python Flask framework to create a basic blog.
It contains a landing page, an about page, and the blog page itself. Since the blog is meant to cover a variety of topic, readers
will be able to filter the posts by topic according to their interests.

The HTML files can be found in the **templates** folder. 
The CSS files can be found in the **static** folder.

Go through the following steps to install the requisite software and run the app:

1. ### Clone the repository
```
git clone https://github.com/Till1983/project-se19-ss24.git
```

2. ### Move to the project folder
```
cd project-se19-ss24
```

3. ### Create an virtual environment
```
python3 -m venv venv
```

4. ### Activate the virtual environment
On Linux/MacOS
```
source venv/bin/activate
````
On Windows
```
venv\Scripts\activate.bat
```
5. ### Install packages from requirements.txt
```
python -m pip install -r requirements.txt
```

6. ### Now you can run the server
```
python app.py
```

7. ### When you are finished, you can deactivate the virtual environment
```
deactivate
```