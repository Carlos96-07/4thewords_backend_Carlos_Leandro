CREATE DATABASE IF NOT EXISTS 4thewords_prueba_carlos_leandro;
USE 4thewords_prueba_carlos_leandro;

CREATE TABLE category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE province (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE canton (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    province_id INT,
    FOREIGN KEY (province_id) REFERENCES province(id)
);

CREATE TABLE district (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    canton_id INT,
    FOREIGN KEY (canton_id) REFERENCES canton(id)
);

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100),
    hashed_password VARCHAR(255)
);

CREATE TABLE legend (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    description TEXT,
    image_url VARCHAR(255),
    date DATETIME,
    category_id INT,
    province_id INT,
    canton_id INT,
    district_id INT,
    FOREIGN KEY (category_id) REFERENCES category(id),
    FOREIGN KEY (province_id) REFERENCES province(id),
    FOREIGN KEY (canton_id) REFERENCES canton(id),
    FOREIGN KEY (district_id) REFERENCES district(id)
);

-- Datos base
INSERT INTO category (name) VALUES ('Misterio'), ('Terror'), ('Tradición');

INSERT INTO province (name) VALUES ('San José');
INSERT INTO canton (name, province_id) VALUES ('Central', 1);
INSERT INTO district (name, canton_id) VALUES ('Carmen', 1);

-- 10 leyendas de ejemplo
INSERT INTO legend (name, description, image_url, date, category_id, province_id, canton_id, district_id)
VALUES 
('La Tulevieja', 'Leyenda sobre un espíritu que castiga a madres descuidadas.', '/uploads/tulevieja.jpg', '1980-05-01', 1, 1, 1, 1),
('El Cadejos', 'Un perro negro fantasma que protege a los borrachos.', '/uploads/cadejos.jpg', '1979-03-15', 1, 1, 1, 1),
('La Llorona', 'Espíritu de mujer que llora por sus hijos.', '/uploads/llorona.jpg', '1985-08-20', 2, 1, 1, 1),
('El Padre sin Cabeza', 'Fantasma de un sacerdote decapitado.', '/uploads/padre.jpg', '1970-09-13', 2, 1, 1, 1),
('La Mona', 'Bruja que se transforma en animal.', '/uploads/mona.jpg', '1982-11-10', 1, 1, 1, 1),
('La Cegua', 'Mujer hermosa que se transforma en monstruo.', '/uploads/cegua.jpg', '1983-07-05', 2, 1, 1, 1),
('El Portón Negro', 'Puerta maldita que cambia de lugar.', '/uploads/porton.jpg', '1981-10-25', 3, 1, 1, 1),
('La Siguanaba', 'Mujer que engaña hombres infieles.', '/uploads/siguanaba.jpg', '1984-02-22', 2, 1, 1, 1),
('El Duende', 'Pequeño ser que se lleva a los niños.', '/uploads/duende.jpg', '1987-06-30', 1, 1, 1, 1),
('La Casa Embrujada', 'Lugar con actividad paranormal.', '/uploads/casa.jpg', '1988-12-01', 3, 1, 1, 1);
