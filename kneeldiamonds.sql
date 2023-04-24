CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Types`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `type_id` INTEGER NOT NULL,
    `timestamp` CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metal`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Size`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Style`(`id`),
    FOREIGN KEY(`type_id`) REFERENCES `type`(`id`)
);

INSERT INTO `Metals` VALUES (null, "Sterling Silver", 405);
INSERT INTO `Metals` VALUES (null, "14K Gold", 782);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1470);
INSERT INTO `Metals` VALUES (null, "Platinum", 1997);
INSERT INTO `Metals` VALUES (null, "Palladium", 3638);

INSERT INTO `Sizes` VALUES (null, .5, 1000);
INSERT INTO `Sizes` VALUES (null, .75, 2000);
INSERT INTO `Sizes` VALUES (null, 1, 3000);
INSERT INTO `Sizes` VALUES (null, 1.5, 4000);
INSERT INTO `Sizes` VALUES (null, 2, 5000);

INSERT INTO `Styles` VALUES (null, "Classic", 500);
INSERT INTO `Styles` VALUES (null, "Modern", 710);
INSERT INTO `Styles` VALUES (null, "Vintage", 965);

INSERT INTO `Types` VALUES (null, "Ring", 250);
INSERT INTO `Types` VALUES (null, "Earring", 350);
INSERT INTO `Types` VALUES (null, "Necklace", 450);

INSERT INTO `Orders` VALUES (null, 2, 4, 2, 3, 20230421);
INSERT INTO `Orders` VALUES (null, 4, 3, 1, 1, 20230420);
INSERT INTO `Orders` VALUES (null, 3, 1, 2, 2, 20230419);
INSERT INTO `Orders` VALUES (null, 1, 5, 3, 1, 20230418);
INSERT INTO `Orders` VALUES (null, 5, 2, 1, 3, 20230417);

SELECT
        o.id,
        o.metal_id,
        o.size_id,
        o.style_id,
        o.type_id,
        o.timestamp
    FROM orders o

SELECT
        o.id,
        o.metal_id,
        o.size_id,
        o.style_id,
        o.type_id,
        o.timestamp,
        m.id metal_id,
        m.metal metal_metal,
        m.price metal_price,
        st.id style_id,
        st.style style_style,
        st.price style_price,
        si.id size_id,
        si.carets size_carets,
        si.price size_price,
        t.id type_id,
        t.name type_name,
        t.price type_price
    FROM orders o
    JOIN metals m
        ON m.id = o.metal_id
    JOIN styles st
        ON st.id = o.style_id
    JOIN sizes si
        ON si.id = o.size_id
    JOIN types t
        ON t.id = o.type_id