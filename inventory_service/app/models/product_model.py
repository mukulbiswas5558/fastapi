from pydantic import BaseModel, Field
from typing import Optional

class CreateProduct(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int = Field(default=0, ge=0)  # Quantity must be >= 0
    price: float = Field(gt=0)             # Price must be > 0
    is_active: Optional[bool] = True
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None
    sku: Optional[str] = None
    barcode: Optional[str] = None
    tax_rate: Optional[float] = Field(default=0.0, ge=0.0)

class ResponseProduct(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    quantity: int
    price: float
    is_active: bool
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None
    sku: Optional[str] = None
    barcode: Optional[str] = None
    tax_rate: float