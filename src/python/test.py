import unittest
from myfunction import insertToDb, insertViaArgs, insertViaCSV
import os
import mysql.connector
import tempfile
import csv  

class TestMyFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup database connection for tests
        cls.connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cls.cursor = cls.connection.cursor()
        # Create a test table
        cls.cursor.execute("""
            CREATE TABLE IF NOT EXISTS utilisateurs (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL UNIQUE,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cls.connection.commit()

    @classmethod
    def tearDownClass(cls):
        # Drop the test table and close connection
        cls.cursor.execute("DROP TABLE IF EXISTS utilisateurs")
        cls.connection.commit()
        cls.cursor.close()
        cls.connection.close()

    def setUp(self):
        # Clear the table before each test
        self.cursor.execute("DELETE FROM utilisateurs")
        self.connection.commit()

    def test_insertToDb(self):
        data = {'nom': 'Test User', 'email': 'test@example.com'}
        insertToDb(data)
        self.cursor.execute("SELECT nom, email FROM utilisateurs WHERE nom=%s AND email=%s", (data['nom'], data['email']))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result, (data['nom'], data['email'])) 

    def test_insertViaArgs(self):
        nom = 'Arg User'
        email = 'test@example.com'
        insertViaArgs(nom, email)
        self.cursor.execute("SELECT nom, email FROM utilisateurs WHERE nom=%s AND email=%s", (nom, email))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result, (nom, email)) 