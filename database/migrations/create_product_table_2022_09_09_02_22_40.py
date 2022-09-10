from modules.databases.migration.migration import Migration
from modules.databases.migration.src.schema import Schema

class CreateProductTable(Migration):
	def up(self):
		Schema().create("product", [
			self.id(),
			self.timestamps()
		])




up_migration = CreateProductTable().up()