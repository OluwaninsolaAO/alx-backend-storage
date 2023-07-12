-- 0. We are all unique!
-- creates a table `users` with: id, email and name

CREATE TABLE IF NOT EXISTS `users` (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    email CHAR(255) NOT NULL UNIQUE,
    name CHAR(255)
);