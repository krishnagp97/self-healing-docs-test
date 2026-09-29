class UserService:
    def get_user(self, user_id: int, include_email: bool = False) -> str:
        if include_email:
            return f"User {user_id} - email@example.com"

        return f"User {user_id}"

    def create_user(self, name: str) -> str:
        return f"Created user {name}"

    def update_user(
        self,
        user_id: int,
        name: str,
    ) -> bool:
        return True

    def delete_user(self, name: str) -> str:
            return f"delete user {name}"