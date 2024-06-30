CREATE TABLE IF NOT EXISTS user(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);


INSERT INTO user (username, email) VALUES 
('nazmul', 'nazmul.cse48@gmail.com'),
('masum', 'masum.pust43@gmail.com'),
('hasan', 'hasan@gmail.com');



SELECT * FROM user;