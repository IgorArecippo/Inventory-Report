from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        id="123",
        product_name="Test Product",
        company_name="Test Company",
        manufacturing_date="13-07-2023",
        expiration_date="13-07-2023",
        serial_number="ABC123",
        storage_instructions="Store in a cool place."
    )

    assert product.id == "123"
    assert product.product_name == "Test Product"
    assert product.company_name == "Test Company"
    assert product.manufacturing_date == "13-07-2023"
    assert product.expiration_date == "13-07-2023"
    assert product.serial_number == "ABC123"
    assert product.storage_instructions == "Store in a cool place."
