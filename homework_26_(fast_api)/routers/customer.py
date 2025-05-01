from typing import Generator, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from model.models import Customer, Address
from database import SessionLocal
from schema import schemas
from crud import crud

router = APIRouter()

def get_db() -> Generator[Session, None, None]:
    """
    Dependency that provides a SQLAlchemy database session.
    Ensures the session is closed after the request is completed.

    Yields:
        Generator[Session, None, None]: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/customers/", response_model=schemas.CustomerRead)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)) -> schemas.CustomerRead:
    existing_customer = db.query(Customer).filter(Customer.email == customer.email).first()
    if existing_customer:
        raise HTTPException(
            status_code=409,
            detail="Customer with this email already exists"
        )
    return crud.create_customer(db, customer)

@router.get("/customers/", response_model=List[schemas.CustomerRead])
def read_customers(db: Session = Depends(get_db)) -> List[schemas.CustomerRead]:
    """
    Retrieve a list of all customers.

    Args:
        db (Session): Database session (injected).

    Returns:
        List[schemas.CustomerRead]: List of all customers.
    """
    return crud.get_customers(db)

@router.get("/customers/{customer_id}", response_model=schemas.CustomerRead)
def get_customer(customer_id: int, db: Session = Depends(get_db)) -> schemas.CustomerRead:
    """
    Retrieve a customer by their ID.

    Args:
        customer_id (int): ID of the customer.
        db (Session): Database session (injected).

    Raises:
        HTTPException: If the customer is not found.

    Returns:
        schemas.CustomerRead: The requested customer.
    """
    customer = crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.post("/customers/{customer_id}/addresses/", response_model=schemas.AddressRead)
def create_address(customer_id: int, address: schemas.AddressCreate, db: Session = Depends(get_db)) -> schemas.AddressRead:
    """
    Create a new address for a specific customer.

    Args:
        customer_id (int): ID of the customer to associate the address with.
        address (schemas.AddressCreate): Address creation payload.
        db (Session): Database session (injected).

    Returns:
        schemas.AddressRead: The created address.
    """
    return crud.create_address_for_customer(db, customer_id, address)
