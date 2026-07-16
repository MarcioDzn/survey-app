from app.models import User


class UserRepository:
    def __init__(self, session):
        self.session = session

    def create(self, user_data):
        pass

    def get_all(self):
        return self.session.query(User).all()
