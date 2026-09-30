
class UserService:
    def get_user(
        self,
        user_id: int,
        include_email: bool = False,
        include_phone: bool = False,
        include_address: bool = False
    ) -> str:
        result = f"User {user_id}"

        if include_email:
            result += " - email@example.com"

        if include_phone:
            result += " - 9876543210"

        if include_address:
            result += " - Bengaluru"

        return result

    def create_user(
        self,
        name: str,
        email: str,
        phone: str = ""
    ) -> dict:
        return {
            "name": name,
            "email": email,
            "phone": phone
        }

    def update_user(
        self,
        user_id: int,
        name: str,
        email: str,
        notify: bool = False,
        validate: bool = True
    ) -> bool:
        if validate and not name:
            return False

        if validate and not email:
            return False

        if notify:
            self._send_update_notification(user_id)

        return True

    def search_users(
        self,
        query: str,
        limit: int = 20,
        include_inactive: bool = False
    ) -> list:
        results = []

        for user_id in range(1, limit + 1):
            user = f"User {user_id}"

            if query.lower() in user.lower():
                results.append({
                    "id": user_id,
                    "name": user,
                    "active": True
                })

        return results

    def activate_user(self, user_id: int) -> bool:
        if user_id <= 0:
            return False
        return True

    def deactivate_user(self, user_id: int, reason: str = "") -> bool:
        if user_id <= 0:
            return False

        if reason:
            self._record_status_change(user_id, reason)

        return True

    def update_email(self, user_id: int, email: str) -> bool:
        if "@" not in email:
            return False
        return True

    def update_phone(self, user_id: int, phone: str) -> bool:
        if len(phone) < 10:
            return False
        return True

    def get_user_statistics(self, user_id: int) -> dict:
        return {
            "user_id": user_id,
            "login_count": 10,
            "order_count": 5,
            "active": True
        }

    def _send_update_notification(self, user_id: int) -> None:
        print(f"Notification sent to user {user_id}")

    def _record_status_change(self, user_id: int, reason: str) -> None:
        print(f"User {user_id} status changed: {reason}")
