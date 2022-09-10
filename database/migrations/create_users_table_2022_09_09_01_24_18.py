from modules.databases.migration.migration import Migration
from modules.databases.migration.src.schema import Schema

class CreateUsersTable(Migration):
	def up(self):
		Schema().create("users", [
			self.id(),
			self.string("fullname").not_null(),
			self.string("email").not_null(),
			self.string("password").not_null(),
			self.string("phone").not_null(),
			self.timestamps()
		])




up_migration = CreateUsersTable().up()