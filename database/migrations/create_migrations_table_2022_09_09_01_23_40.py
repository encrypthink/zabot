from modules.databases.migration.migration import Migration
from modules.databases.migration.src.schema import Schema

class CreateMigrationsTable(Migration):
	def up(self):
		Schema().create("migrations", [
			self.id(),
			self.string("migration"),
			self.integer("steps"),
			self.timestamps()
		])




up_migration = CreateMigrationsTable().up()