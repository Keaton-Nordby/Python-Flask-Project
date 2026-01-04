import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from website import create_app, db


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  
    app.config["WTF_CSRF_ENABLED"] = False 
     
    with app.app_context():
        db.create_all()  
        yield app        
        db.session.remove()
        db.drop_all()   
        
        
@pytest.fixture
def client(app):
    return app.test_client()