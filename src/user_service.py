class UserService:
    def get_user(
        self,
        user_id: int,
        include_email: bool = False,
        include_phone: bool = False
    ) -> str:
        if include_email and include_phone:
            return f"User {user_id} - email@example.com - 9876543210"

        if include_email:
            return f"User {user_id} - email@example.com"

        if include_phone:
            return f"User {user_id} - 9876543210"

        return f"User {user_id}"


    def update_user(
        self,
        user_id: int,
        include_email: bool,
        notify: bool = False
    ) -> bool:
        return True

    def delete_user(self, user_id: int) -> bool:
        return True


