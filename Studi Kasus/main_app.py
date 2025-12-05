from repositories import ProductRepository
# Import DebitCardPayment
from services import CartService, IPaymentProcessor, CashPayment, DebitCardPayment
from models import Product

class PosApp:
    def __init__(self, product_repo: ProductRepository, cart_service: CartService, payment_processor: IPaymentProcessor):
        self.repo = product_repo
        self.cart_service = cart_service
        self.payment_processor = payment_processor

    def show_products(self):
        print("\n--- PRODUCTS ---")
        for p in self.repo.get_all():
            print(f"{p.id}. {p.name} - Rp {p.price:,.0f}")

    def add_to_cart(self):
        try:
            p_id = int(input("Product ID: "))
            qty = int(input("Quantity: "))
            product = self.repo.find_by_id(p_id)
            if product:
                self.cart_service.add_product(product, qty)
            else:
                print("Product not found.")
        except ValueError:
            print("Invalid input.")

    def checkout(self):
        total = self.cart_service.calculate_total()
        if total == 0:
            print("Cart is empty.")
            return
        
        if self.payment_processor.process_payment(total):
            print("Transaction Success!")
            self.cart_service.clear_cart()

    def run(self):
        while True:
            print("\n1. List Products | 2. Add to Cart | 3. Checkout | 4. Exit")
            choice = input("Choice: ")
            if choice == '1': self.show_products()
            elif choice == '2': self.add_to_cart()
            elif choice == '3': self.checkout()
            elif choice == '4': break

if __name__ == "__main__":
    repo = ProductRepository()
    cart_svc = CartService()
    
    payment_method = DebitCardPayment() 
    
    app = PosApp(repo, cart_svc, payment_method)
    app.run()