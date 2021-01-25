import mysql.connector
import sys

try:
    connection = mysql.connector.connect(
            user="bn_opencart",
            password="",
            host="0.0.0.0",
            port=3307,
            database = "bitnami_opencart"
)
except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)



with connection:
    cur = connection.cursor()
    cur.execute("SELECT * FROM oc_extension limit 20")

    version = cur.fetchone()

    print("Database version: {}".format(version))

