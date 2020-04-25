CREATE TABLE `restaurant` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `address` varchar(255),
  `latitute` real,
  `longitude` real,
  `rating` float,
  `cost_for_2` int,
  `image` varchar(255),
  `vegan` boolean,
  `vegetarian` boolean,
  `credit_card` boolean,
  `gluten_free` boolean,
  `takeaway` boolean,
  `phone_num1` varchar(255),
  `phone_num2` varchar(255),
  `timing` varchar(255),
  `menu` json
);

CREATE TABLE `cuisines` (
  `id` int  PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) UNIQUE NOT NULL
);

CREATE TABLE `restaurant_cuisine` (
  `restaurant_id` int,
  `cuisine_id` int,
  PRIMARY KEY(`restaurant_id`, `cuisine_id`),
  FOREIGN KEY (restaurant_id) REFERENCES restaurant(id),
  FOREIGN KEY (cuisine_id) REFERENCES cuisines(id)
);

CREATE PROCEDURE FindClosest (IN usr_lat REAL, IN usr_lon REAL)
SELECT
    id,
    name,
    (
        3959 
        * acos(
            cos( radians(usr_lat) ) 
            * cos( radians( latitute ) ) 
            * cos( radians( longitude ) - radians(usr_lon) ) 
            + sin( radians(usr_lat) ) 
            * sin( radians( latitute ) ) 
        ) 
    ) AS distance 
FROM restaurant 
ORDER BY distance
LIMIT 20;