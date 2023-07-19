from typing import Dict, Type
from inventory_report.product import Product
from abc import ABC, abstractmethod
import json
import csv


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        products = []
        with open(self.path, 'r') as file:
            data = json.load(file)

            for i in data:
                product = Product(
                    id=i['id'],
                    product_name=i['product_name'],
                    company_name=i['company_name'],
                    manufacturing_date=i['manufacturing_date'],
                    expiration_date=i['expiration_date'],
                    serial_number=i['serial_number'],
                    storage_instructions=i['storage_instructions']
                )
                products.append(product)
        return products


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        products = []
        with open(self.path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                product = Product(
                    id=row['id'],
                    product_name=row['product_name'],
                    company_name=row['company_name'],
                    manufacturing_date=row['manufacturing_date'],
                    expiration_date=row['expiration_date'],
                    serial_number=row['serial_number'],
                    storage_instructions=row['storage_instructions']
                )
                products.append(product)
        return products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
