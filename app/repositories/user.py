from sqlalchemy.exc import IntegrityError

from app.models import User


class UserRepository:
    def __init__(self, session):
        self.session = session

    def create(self, user_data):
        user_db = User(
            name=user_data.name, email=user_data.email, password=user_data.password
        )

        self.session.add(user_db)

        try:
            self.session.commit()
            self.session.refresh(user_db)
            return user_db

        except IntegrityError:
            self.session.rollback()
            raise ValueError("E-mail já cadastrado")

    def get_all(self):
        return self.session.query(User).all()
