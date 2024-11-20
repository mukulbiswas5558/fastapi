from app.database import get_db

async def create_product(product_data):
    """
    Inserts a new product into the database and returns the created product.
    """
    conn = await get_db()
    try:
        query = """
        INSERT INTO products (
            name, description, quantity, price, is_active, 
            category_id, supplier_id, sku, barcode, tax_rate
        )
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
        RETURNING *;
        """
        # Using positional parameters for binding: $1, $2, ..., $10
        created_product = await conn.fetchrow(
            query,
            product_data["name"],
            product_data.get("description"),
            product_data["quantity"],
            product_data["price"],
            product_data["is_active"],
            product_data.get("category_id"),
            product_data.get("supplier_id"),
            product_data.get("sku"),
            product_data.get("barcode"),
            product_data["tax_rate"]
        )
    finally:
        await conn.close()

    return created_product


async def get_product_from_db(product_id: int):
    """
    Retrieves a product from the database by its ID.
    """
    conn = await get_db()
    try:
        query = "SELECT * FROM products WHERE id = $1;"
        product = await conn.fetchrow(query, product_id)  # Bind product_id to $1
    finally:
        await conn.close()

    return product