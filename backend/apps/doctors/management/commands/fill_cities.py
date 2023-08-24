import csv
from iranian_cities.management.commands.generate_city import Command
from iranian_cities.models import City


class Command(Command):
    def generate_shahr(self, path):
        with open(path, encoding="utf-8") as f:
            data = csv.DictReader(f)
            shahr_objs = [
                City(
                    name=row.get("name"),
                    amar_code=row.get("amar_code"),
                    ostan_id=int(row.get("ostan")),
                    shahrestan_id=int(row.get("shahrestan")),
                    bakhsh_id=int(row.get("bakhsh")),
                    shahr_type=row.get("shahr_type"),
                )
                for row in data
            ]
            City.objects.bulk_create(shahr_objs)
            print("Shahr Objects Created Successfully")
