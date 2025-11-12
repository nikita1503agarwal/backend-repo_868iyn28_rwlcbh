"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class ClothingProduct(BaseModel):
    """
    Pakistani women's clothing products
    Collection name: "clothingproduct" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in PKR")
    category: str = Field(..., description="Category e.g., Lawn, Pret, Abaya, Kurti")
    sizes: List[str] = Field(default_factory=list, description="Available sizes e.g., XS,S,M,L,XL,Free")
    fabric: Optional[str] = Field(None, description="Fabric type e.g., Lawn, Cotton, Chiffon")
    color: Optional[str] = Field(None, description="Primary color")
    images: List[HttpUrl] = Field(default_factory=list, description="Image URLs")
    in_stock: bool = Field(True, description="Whether product is in stock")
    city: str = Field("Karachi", description="City where available")
    brand: Optional[str] = Field(None, description="Brand name")
    tags: List[str] = Field(default_factory=list, description="Search tags")
