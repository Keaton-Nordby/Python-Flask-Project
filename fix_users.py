from website import create_app, db
from website.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Find users with no password
    users_without_password = User.query.filter((User.password == None) | (User.password == '')).all()
    
    print(f"Found {len(users_without_password)} users with no password.")

    for user in users_without_password:
        # Option 1: Delete the user
        print(f"Deleting user: {user.email}")
        db.session.delete(user)

        # Option 2 (safer alternative): set a temporary password
        # temp_pass = "Temp1234!"
        # user.password = generate_password_hash(temp_pass)
        # print(f"Set temporary password for {user.email}")

    db.session.commit()
    print("Cleanup done!")
