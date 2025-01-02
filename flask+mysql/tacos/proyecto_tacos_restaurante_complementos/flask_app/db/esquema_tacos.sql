-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_tacos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_tacos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_tacos` DEFAULT CHARACTER SET utf8 ;
USE `esquema_tacos` ;

-- -----------------------------------------------------
-- Table `esquema_tacos`.`tacos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tacos`.`tacos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tortilla` VARCHAR(45) NULL,
  `guiso` VARCHAR(45) NULL,
  `salsa` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
