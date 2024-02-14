-- Add 20 orders
SELECT * FROM items;
SELECT * FROM orders;

SELECT "--";

INSERT INTO orders (item_name, number) VALUES ('item 1', 2);
INSERT INTO orders (item_name, number) VALUES ('item 0', 1);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;

SELECT "--";

INSERT INTO orders (item_name, number) VALUES ('item 3', 5);
INSERT INTO orders (item_name, number) VALUES ('item 2', 7);
INSERT INTO orders (item_name, number) VALUES ('item 0', 2);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;

SELECT "--";

INSERT INTO orders (item_name, number) VALUES ('item 0', 1);
INSERT INTO orders (item_name, number) VALUES ('item 1', 2);
INSERT INTO orders (item_name, number) VALUES ('item 2', 3);
INSERT INTO orders (item_name, number) VALUES ('item 3', 4);
INSERT INTO orders (item_name, number) VALUES ('item 0', 5);
INSERT INTO orders (item_name, number) VALUES ('item 1', 6);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;

SELECT "--";

INSERT INTO orders (item_name, number) VALUES ('item 0', 1);
INSERT INTO orders (item_name, number) VALUES ('item 1', 2);
INSERT INTO orders (item_name, number) VALUES ('item 2', 3);
INSERT INTO orders (item_name, number) VALUES ('item 3', 4);
INSERT INTO orders (item_name, number) VALUES ('item 0', 5);
INSERT INTO orders (item_name, number) VALUES ('item 1', 6);
INSERT INTO orders (item_name, number) VALUES ('item 2', 4);
INSERT INTO orders (item_name, number) VALUES ('item 3', 5);
INSERT INTO orders (item_name, number) VALUES ('item 0', 6);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;
