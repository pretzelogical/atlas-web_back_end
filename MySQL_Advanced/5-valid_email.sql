-- Resets attribute valid_email when email has been changed

DELIMITER FUNNI

CREATE TRIGGER reset_valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF New.email != Old.email THEN
        SET New.valid_email = 0;
    END IF;
END FUNNI
