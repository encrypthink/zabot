from modules.databases.migration.migration import Migration
from modules.databases.migration.src.schema import Schema

class CreateProductOrdersTable(Migration):
	def up(self):
		Schema().create("product_orders", [
			self.id(),
			self.timestamps()
		])




up_migration = CreateProductOrdersTable().up()