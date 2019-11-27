"""Update OpenFoodFact data"""
from catalog.update import Update_db
from django.core.management.base import BaseCommand
from django.db.utils import DataError, IntegrityError
from catalog.models import Category, Product

class Command(BaseCommand):
	help='Update data in database'

	def handle(self, *args, **options):
		update = Update_db()
		update.update()
		self.stdout.write('La base de données a bien été mise à jour.')
