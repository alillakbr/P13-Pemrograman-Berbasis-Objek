from repositories import ProductRepository
from services import CartService, IPaymentProcessor, CashPayment
from models import Product

class PosApp:
    def __init__(self, product_repo: ProductRepository, cart_service: CartService, payment_processor: IPaymentProcessor):
        self.repo = product_repo
        self.cart_service = cart_service
        self.payment_processor = payment_processor

    def run(self):
        print("--- POS SYSTEM (PURE C) ---")
        products = self.repo.get_all()
        for p in products:
            print(f"{p.name} - {p.price}")
        
        p1 = self.repo.find_by_id(1)
        if p1:
            self.cart_service.add_product(p1, 1)
            total = self.cart_service.calculate_total()
            print(f"Total: {total}")
            self.payment_processor.process_payment(total)

if __name__ == "__main__":
    repo = ProductRepository()
    cart_svc = CartService()
    
    payment_method = CashPayment() 
    
    app = PosApp(repo, cart_svc, payment_method)
    app.run()