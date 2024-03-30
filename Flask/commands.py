import click
from flask.cli import with_appcontext
from typing import Type


@click.command("add-admin")
@click.option("--admin-email", help="Email of admins to add")
@with_appcontext
def add_admin(admin_email: str):
    """
    Add a service administrator.
    python -m flask add-admin --admin-email "xyz@gmail.com"
    """
    from app import db, User
    try:
        user = User(username = admin_email,
            password = admin_email,
            email = admin_email,
            is_active = True)
        db.session.add(user)
        db.session.commit()
        print(f"Sucessfully added administrator {admin_email}")
    except Exception as e:
        print("Error adding administrator %s: %s" % (admin_email, str(e)))
