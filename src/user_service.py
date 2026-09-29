class UserService:
    def get_user(self, user_id: int) -> str:
        return f"User {user_id}"

    def delete_user(self, user_id: int) -> bool:
        return True