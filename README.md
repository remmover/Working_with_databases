# Working_with_databases 

```
# Database Seed and Query Example

This repository contains a Python script that demonstrates how to seed a database with sample data and execute various SQL queries on the seeded database.

## Requirements

- Python 3.x
- PostgreSQL
- Psycopg2 library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

2. Install the required dependencies:

```bash
poetry install
```

3. Configure the database connection:

Modify the `creating_and_filling_DB/connection.py` file to provide the necessary database connection details, such as host, port, database name, username, and password.

## Usage

1. Seed the database with sample data:

Run the `creating_and_filling_DB/seed.py` script to create the necessary database tables and populate them with sample data.

```bash
python creating_and_filling_DB/seed.py
```

2. Execute SQL queries:

The `query.py` script contains several pre-defined SQL queries that can be executed on the seeded database. You can modify or add your own queries as needed.

```bash
python query.py
```

## Example Queries

The `query.py` script already contains several example queries. You can uncomment and execute them to retrieve specific information from the database. Each query is assigned to a variable named `sql_expressionX`, where X is a number.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
