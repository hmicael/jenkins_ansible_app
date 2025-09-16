import csv
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

def insertToDb(dict_values):
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cursor = connection.cursor()
        sql = "INSERT INTO utilisateurs (nom, email) VALUES (%s, %s)"
        cursor.execute(sql, (dict_values['nom'], dict_values['email']))
        connection.commit()
        cursor.close()
        connection.close() 
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")

def insertViaArgs(nom, email):
    dict_values = {'nom': nom, 'email': email}
    insertToDb(dict_values)
    
def insertViaCSV(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
                insertToDb(row)
    except FileNotFoundError:
        print(f"Le fichier {file_path} est introuvable.")
    except KeyError:
        print("Le fichier CSV doit contenir les colonnes 'nom' et 'email'.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")