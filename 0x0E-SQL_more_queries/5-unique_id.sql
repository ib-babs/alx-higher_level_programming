-- Creates the table 'unique_id'
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
