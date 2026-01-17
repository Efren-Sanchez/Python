-- Crear base de datos y tabla para el GoogleBot
CREATE DATABASE IF NOT EXISTS googlebot CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE googlebot;

CREATE TABLE paginas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(1000) UNIQUE NOT NULL,
    titulo VARCHAR(300),
    contenido_texto LONGTEXT,
    palabras_clave JSON,
    enlaces JSON,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    profundidad INT DEFAULT 0,
    INDEX idx_url (url(100)),
    FULLTEXT(contenido_texto),
    FULLTEXT(titulo)
);
