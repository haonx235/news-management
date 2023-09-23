CREATE DATABASE newsmanagement CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
CREATE USER 'newsmanagement'@'localhost' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON newsmanagement.* TO 'newsmanagement'@'localhost';