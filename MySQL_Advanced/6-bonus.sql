-- Stored procedure AddBonus that adds a new correction for a student

DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE recordExists INT;

    SELECT COUNT(*) INTO recordExists
    FROM projects
    WHERE name = project_name;

    IF recordExists = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name LIMIT 1), score);
END//

DELIMITER ;
