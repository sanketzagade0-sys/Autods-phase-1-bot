from database import SessionLocal, Order

def create_order(data):
    db = SessionLocal()
    order = Order(
        product_id=data.get("product_id"),
        user_id=data.get("user_id"),
        amount=data.get("amount"),
        status="pending"
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_daily_report():
    db = SessionLocal()
    orders = db.query(Order).all()
    total_orders = len(orders)
    total_revenue = sum(o.amount for o in orders)
    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue
  }
