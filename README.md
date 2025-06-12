# Flask, Vue application template

Full stack application template developed with Flask & SQLAlchemy ORM (using scaffolding), Vue & Axios, PostgrSQL, and Docker

## How to run

1. Clone the repository
2. Ensure Python and Docker Desktop are installed on your machine
3. In the terminal, run the command `docker-compose up --build`
4. Initialize the db using `docker-compose exec backend flask shell`
5. Create tables based on models.py by running the following inside the Flask shell:
    ```
    from app import db
    db.create_all()
    exit()
    ```

### Dev notes
- Use the command `docker-compose down -v` to reinstall dependencies

### Preview

![Dashboard default layout](docs/image.png)