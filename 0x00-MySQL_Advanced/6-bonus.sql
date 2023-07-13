-- 6. Add bonus
-- creates a stored procedure AddBonus that adds a
-- new correction for a student.

DELIMITER $$ ;
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score FLOAT
    )
    BEGIN
        SET @project_id = IFNULL(
            (
                SELECT id 
                FROM projects
                WHERE name = project_name
                LIMIT 1
            ),
            'NULL'
        );

        IF (@project_id = 'NULL') THEN
            INSERT INTO projects (name)
            VALUES (project_name);
            SET @project_id = LAST_INSERT_ID();
        END IF;

        INSERT INTO corrections (`user_id`, `project_id`, `score`)
        VALUES (user_id, @project_id, score);
    END $$

DELIMITER ; $$