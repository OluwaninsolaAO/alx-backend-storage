-- 7. Average score
--  computes and store the average score for a student

DELIMITER $$ ;
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
    )
    BEGIN
        UPDATE users
        SET average_score = (
            SELECT SUM(score) / COUNT(user_id)
            FROM corrections
            WHERE corrections.user_id = user_id
        )
        WHERE id = user_id;
    END $$

DELIMITER ; $$