from inventory_report.product import Product
from unittest.mock import patch
import pytest


@pytest.fixture
def product() -> Product:
    return Product(
        id="123",
        product_name="Test Product",
        company_name="Test Company",
        manufacturing_date="13-07-2023",
        expiration_date="13-07-2023",
        serial_number="ABC123",
        storage_instructions="Store in a cool place"
    )


def test_product_report(product: Product) -> None:
    # product = Product(
    #     id="123",
    #     product_name="Test Product",
    #     company_name="Test Company",
    #     manufacturing_date="13-07-2023",
    #     expiration_date="13-07-2023",
    #     serial_number="ABC123",
    #     storage_instructions="Store in a cool place."
    # )

    expected_output = (
        "The product 123 - Test Product with serial number ABC123 "
        "manufactured on 13-07-2023 by the company Test Company "
        "valid until 13-07-2023 must be stored according to the "
        "following instructions: Store in a cool place."
    )

    with patch("builtins.print") as mock_print:
        print(str(product))
        mock_print.assert_called_with(expected_output)
