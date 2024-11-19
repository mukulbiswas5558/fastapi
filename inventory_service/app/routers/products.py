from fastapi import APIRouter, Depends, HTTPException
from ..models.product_model import CreateProduct, ResponseProduct
from ..database import get_db
from ..services.product_service import create_product,get_product_from_db

router = APIRouter()

# Register new user
@router.post("/products", response_model=ResponseProduct)
async def register_product(product: CreateProduct, db=Depends(get_db)):
    # Prepare product data for insertion
    product_data = product.dict()

    # Insert the new product into the database
    new_product = await create_product(db, product_data)

    if not new_product:
        raise HTTPException(status_code=500, detail="Failed to create product")

    return dict(new_product)
    
@router.get("/products/{product_id}", response_model=ResponseProduct)
async def get_product_by_id(product_id: int, db=Depends(get_db)):
    """
    Retrieve a product by its ID.
    """
    # Fetch the product from the database
    product = await get_product_from_db(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return dict(product)
