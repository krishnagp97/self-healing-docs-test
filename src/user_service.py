class UserService:
    def get_user(self, user_id: int) -> str:
        return f"User {user_id}"

    def create_user(self, name: str) -> str:
        return f"Created user {name}"