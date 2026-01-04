from flask import redirect
import pytest
from website.models import User
from werkzeug.security import generate_password_hash

# successful sign in test
def test_signup_success(client):
    # send data
    form_data = {
        "email": "keaton@gmail.com",
        "firstName": "Keaton",
        "password1": "keaton123",
        "password2": "keaton123"
    }    
    # assert submitting a post request
    res = client.post("/sign-up", data=form_data, follow_redirects=True)
    
    # Response
    assert b"Account created successfully!" in res.data
    
    # assert user into db
    user = User.query.filter_by(email="keaton@gmail.com").first()
    assert user is not None
    assert user.first_name == "Keaton"
    
def test_signup_with_short_password(client):
    res = client.post("/sign-up", data={
        "email": "test2@example.com",
        "firstName": "Keaton",
        "password1": "123",
        "password2": "123"
    }, follow_redirects=True)
    
    assert b"Password must be at least 7 characters" in res.data
 