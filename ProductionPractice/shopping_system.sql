/*>>mysql -u root -p < shopping_system.sql */

DROP DATABASE IF EXISTS shoppingSystem;
CREATE DATABASE shoppingSystem CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
USE shoppingSystem;

CREATE TABLE AdminUser (
    username CHAR(5) NOT NULL,
    password VARCHAR(32) NOT NULL,

    PRIMARY KEY(username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE User (
    username VARCHAR(255) NOT NULL,
    password VARCHAR(32) NOT NULL,
    phone VARCHAR(11) NOT NULL,
    addr VARCHAR(1024) NOT NULL,

    PRIMARY KEY(username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Commodity (
    id CHAR(8) NOT NULL,
    name VARCHAR(1024) NOT NULL,
    price INTEGER NOT NULL DEFAULT 0,
    store INTEGER NOT NULL DEFAULT 0,
    info VARCHAR(10240),
    PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Image (
    id INTEGER NOT NULL AUTO_INCREMENT,
    commodity_id VARCHAR(8) NOT NULL,
    img_path VARCHAR(1024) NOT NULL,

    PRIMARY KEY(id),
    FOREIGN KEY(commodity_id) REFERENCES Commodity(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Orders (
    order_id CHAR(8) NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    counter INTEGER NOT NULL DEFAULT 1,
    status INTEGER NOT NULL DEFAULT 0,
    username VARCHAR(255) NOT NULL,
    commodity_id CHAR(8) NOT NULL,

    PRIMARY KEY(order_id),
    FOREIGN KEY(username) REFERENCES User(username) ON DELETE CASCADE,
    FOREIGN KEY(commodity_id) REFERENCES Commodity(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE ShoppingCart(
    username VARCHAR(255) NOT NULL,
    commodity_id CHAR(8) NOT NULL,
    counter INTEGER NOT NULL DEFAULT 1,

    PRIMARY KEY(username, commodity_id, counter),
    FOREIGN KEY(username) REFERENCES User(username) ON DELETE CASCADE,
    FOREIGN KEY(commodity_id) REFERENCES Commodity(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO AdminUser(username, password) VALUES ('admin', '21232f297a57a5a743894a0e4a801fc3');
