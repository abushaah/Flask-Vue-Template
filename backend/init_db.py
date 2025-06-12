from app import create_app, db
from app.models import Item

app = create_app()

with app.app_context():
    db.create_all()  # create tables

    # adding mock initial data
    if Item.query.count() == 0:
        items = [
            Item(name="Item 1"),
            Item(name="Item 2"),
            Item(name="Item 3"),
        ]
        db.session.bulk_save_objects(items)
        db.session.commit()
        print("Database initialized with sample items.")
    else:
        print("Database already initialized.")