from decimal import Decimal

from django.core.management.base import BaseCommand

from store.models import Product

SAMPLE_PRODUCTS = [
    ("Wireless Headphones", "Over-ear Bluetooth headphones with 30-hour battery life and deep bass.", "2499.00", True),
    ("Smart Watch Series 5", "Track steps, heart rate and sleep. Water resistant with a bright AMOLED display.", "3999.00", True),
    ("Running Shoes", "Lightweight, breathable running shoes with a cushioned sole for daily miles.", "1899.00", True),
    ("Leather Backpack", "Everyday backpack with a padded laptop sleeve and three inner pockets.", "2199.00", False),
    ("Stainless Steel Bottle", "1 litre insulated bottle. Keeps drinks cold for 24 hours, hot for 12.", "749.00", False),
    ("Mechanical Keyboard", "Compact 87-key keyboard with tactile switches and white backlighting.", "3299.00", False),
    ("Sunglasses", "UV400 polarised sunglasses with a lightweight metal frame.", "999.00", False),
    ("Desk Lamp", "LED desk lamp with three colour temperatures and a USB charging port.", "1299.00", False),
    ("Cotton T-Shirt", "Soft 100% cotton crew-neck t-shirt in a relaxed everyday fit.", "499.00", False),
    ("Bluetooth Speaker", "Portable speaker with 12 hours of playtime and an IPX6 splash-proof body.", "1599.00", False),
    ("Yoga Mat", "6 mm non-slip yoga mat with a carry strap.", "699.00", False),
    ("Coffee Mug Set", "Set of four ceramic mugs, dishwasher and microwave safe.", "849.00", False),
]


class Command(BaseCommand):
    help = "Insert sample products into the Product table."

    def add_arguments(self, parser):
        parser.add_argument("--reset", action="store_true", help="Delete existing products first.")

    def handle(self, *args, **options):
        if options["reset"]:
            Product.objects.all().delete()
        created = 0
        for index, (title, description, price, featured) in enumerate(SAMPLE_PRODUCTS, start=1):
            _, was_created = Product.objects.get_or_create(
                title=title,
                defaults={
                    "description": description,
                    "price": Decimal(price),
                    "image_url": f"https://picsum.photos/seed/shop{index}/800/600",
                    "is_featured": featured,
                },
            )
            created += int(was_created)
        self.stdout.write(self.style.SUCCESS(f"Added {created} product(s)."))