from http.client import HTTPException
from typing import List, Optional
from sqlalchemy.orm import Session
from model.models import Customer, Address
from schema.schemas import CustomerCreate, AddressCreate

def create_customer(db: Session, customer: CustomerCreate) -> Customer:
    """
    Create a new customer in the database.

    Args:
        db (Session): SQLAlchemy database session.
        customer (CustomerCreate): Schema containing customer creation data.

    Returns:
        Customer: The created Customer ORM object.
    """
    db_customer = Customer(**customer.dict())

    # if check_customer_exist(db, db_customer):
    #     raise HTTPException(
    #         status_code=409,  # Conflict
    #         detail="Customer with this email already exists"
    #     )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def check_customer_exist(db: Session, customer: Customer) -> bool:
    all_emails = list(map(lambda el: el.email, db.query(Customer).all()))
    if customer.email in all_emails:
        return True
    return False
def get_customers(db: Session) -> List[Customer]:
    """
    Retrieve all customers from the database.

    Args:
        db (Session): SQLAlchemy database session.

    Returns:
        List[Customer]: A list of Customer ORM objects.
    """
    return db.query(Customer).all()

def get_customer(db: Session, customer_id: int) -> Optional[Customer]:
    """
    Retrieve a customer by ID from the database.

    Args:
        db (Session): SQLAlchemy database session.
        customer_id (int): ID of the customer to retrieve.

    Returns:
        Optional[Customer]: The Customer ORM object if found, else None.
    """
    return db.query(Customer).filter(Customer.id == customer_id).first()

def create_address_for_customer(db: Session, customer_id: int, address: AddressCreate) -> Address:
    """
    Create a new address for a given customer.

    Args:
        db (Session): SQLAlchemy database session.
        customer_id (int): ID of the customer to associate with the address.
        address (AddressCreate): Schema containing address creation data.

    Returns:
        Address: The created Address ORM object.
    """
    db_address = Address(**address.dict(), customer_id=customer_id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address
