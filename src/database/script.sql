-- Création de la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS demo_app;

-- Utilisation de la base
USE demo_app;

-- Création de la table principale
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
