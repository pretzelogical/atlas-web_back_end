-- Creates a trigger that decreases the quantity of
-- an item after adding a new order

CREATE TRIGGER dequantity AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - 1
WHERE name = New.item_name
