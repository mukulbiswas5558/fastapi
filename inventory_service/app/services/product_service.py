
async def create_product(db, product_data):
    query = """
    INSERT INTO products (name, description, quantity, price, is_active, category_id, supplier_id, sku, barcode, tax_rate)
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
    RETURNING *;
    """
    return await db.fetchrow(
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
async def get_product_from_db(db, product_id: int):
    query = """
    SELECT * FROM products WHERE id = $1;
    """
    return await db.fetchrow(query, product_id)