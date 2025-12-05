from abc import ABC, abstractmethod
from typing import List
from models import Product, CartItem

class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CashPayment(IPaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing Cash Payment: Rp {amount:,.0f}")
        return True

class DebitCardPayment(IPaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing Debit Card: Rp {amount:,.0f}")
        print("Connecting to EDC... PIN Verified.")
        return True

class CartService:
    def __init__(self):
        self.cart_items: List[CartItem] = []

    def add_product(self, product: Product, quantity: int):
        for item in self.cart_items:
            if item.product.id == product.id:
                item.quantity += quantity
                print(f"Updated quantity: {product.name}")
                return
        self.cart_items.append(CartItem(product, quantity))
        print(f"Added to cart: {product.name}")

    def get_all_items(self) -> List[CartItem]:
        return self.cart_items

    def calculate_total(self) -> float:
        return sum(item.subtotal for item in self.cart_items)

    def clear_cart(self):
        self.cart_items = []
        print("Cart cleared.")