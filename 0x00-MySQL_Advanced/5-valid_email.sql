-- 5. Email validation to sent
-- resets the attribute valid_email only when the
-- email has been changed.

DELIMITER $$ ;

DROP TRIGGER IF EXISTS reset_email_validation;
CREATE TRIGGER reset_email_validation BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF (OLD.email != NEW.email) THEN
    SET NEW.valid_email = 0;
    END IF;
END; $$

DELIMITER ; $$