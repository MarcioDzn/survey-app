class UserService:
    def __init__(self, user_repository, session):
        self.user_repository = user_repository
        self.session = session

    def create(self, user_data):
        return self.user_repository.create(user_data)

    def get_all(self):
        return self.user_repository.get_all()
