# zabot
Please Wait, still in development

Planning Features:
- MVC Pattern 🔄 
- SQL Query Builder 🔄 
- Migration ✅ (In Development Progress)
- Commander Console ✅

# Requirements Setups
For requirements run following commands:
```
$ python3 -m pip install -r requirements.txt
```

# Comander Console

## Generating Mysql Database Connection:
```
$ python3 comander.py create db:config
```

## Test Mysql Database Connection:
```
$ python3 comander.py testing db:config
```

## Generating Migrations:
```
$ python3 comander.py create migration:create_{TABLE_NANE}_table
```

## Running Migrations:
```
$ python3 comander.py run migration
```