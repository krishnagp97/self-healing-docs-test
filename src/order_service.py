class OrderService:
    def create_order(self, user_id: int, product_id: int, quantity: int = 1) -> dict:
        return {
            "user_id": user_id,
            "product_id": product_id,
            "quantity": quantity,
            "status": "created"
        }
    def get_order(self, order_id: int) -> dict:
        return {
            "id": order_id,
            "status": "created"
        }
    def update_order(self, order_id: int, status: str) -> bool:
        allowed = {"created", "processing", "shipped", "delivered"}
        return status in allowed
    def list_user_orders(self, user_id: int, limit: int = 20) -> list:
        return [
            {
                "id": index,
                "user_id": user_id,
                "status": "delivered"
            }
            for index in range(1, limit + 1)
        ]
    def calculate_total(self, price: float, quantity: int) -> float:
        return price * quantity
    def apply_discount(self, total: float, percentage: float) -> float:
        if percentage < 0 or percentage > 100:
            return total
        return total - (total * percentage / 100)
    def validate_order(self, user_id: int, product_id: int, quantity: int) -> bool:
        if user_id <= 0:
            return False
        if product_id <= 0:
            return False
        if quantity <= 0:
            return False
        return True
    def mark_as_shipped(self, order_id: int, tracking_id: str) -> bool:
        if not tracking_id:
            return False
        return True
    def mark_as_delivered(self, order_id: int) -> bool:
        return order_id > 0
    def get_order_summary(self, order_id: int) -> dict:
        return {
            "order_id": order_id,
            "items": 3,
            "subtotal": 1500,
            "discount": 100,
            "total": 1400
        }
