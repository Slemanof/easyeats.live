CREATE TABLE `restaurant` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `address` varchar(255),
  `rating` float,
  `cost_for_2` int,
  `image` varchar(255),
  `vegan` boolean,
  `vegetarian` boolean,
  `credit_card` boolean,
  `gluten_free` boolean,
  `Takeaway` boolean,
  `phone_num1` int,
  `phone_num2` int,
  `menu` json
);

CREATE TABLE `cuisines` (
  `id` int  PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) UNIQUE NOT NULL
);

CREATE TABLE `restaurant_cuisine` (
  `restaurant_id` int,
  `cuisine_id` int
);
INSERT INTO restaurant ( id, name) VALUES (1, "Test")