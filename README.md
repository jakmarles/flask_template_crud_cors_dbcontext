
# Flask CRUD Template
This is a template for creating a simple Flask application with full CRUD (Create, Read, Update, Delete) functionality, CORS support, and a DBcontext for database connections.

# Prerequisites
Flask
Flask-Cors
Flask-SQLAlchemy

#  Installing



Create a virtual environment and activate it
```bash
python -m venv myenv
source myenv/Scripts/activate (Windows)
```
Install the required packages
```bash
pip install -r requirements.txt
```
Run the migrations to create the necessary tables in the database
```bash
py app.py

```



# Endpoints
```bash
GET /items: Retrieve all items from the database
GET /items/<int:item_id>: Retrieve a specific item by its id from the database
POST /items: Create a new item in the database
PUT /items/<int:item_id>: Update an existing item in the database
DELETE /items/<int:item_id>: Delete an existing item from the database
```
# Database
```bash
The template uses SQLite as the database and the db.create_all() function to create the necessary table on the first run. 
The database file is located at ../instance/mydb.db
```
# Note
Make sure that you have the correct version of python (3.11) as well as the correct version of the modules you imported.

# Tips
You can replace the database URI with the database of your choice, also you can change the table name as well as the columns name as well as their types if you need to.
## Authors

- [@jakmarles](https://github.com/jakmarles) 

![Credits](https://img.shields.io/badge/Credits-Ilya%20Bronfman-green)
