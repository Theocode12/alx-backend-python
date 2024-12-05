-- creates a prodev user

CREATE USER 'prodev'@'localhost' IDENTIFIED BY '0';
GRANT ALL PRIVILEGES ON *.* TO 'prodev'@'localhost';
FLUSH PRIVILEGES;
