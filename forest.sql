# HeidiSQL Dump 
#
# --------------------------------------------------------
# Host:                 127.0.0.1
# Database:             forest
# Server version:       5.4.3-beta-community
# Server OS:            Win32
# Target-Compatibility: Standard ANSI SQL
# HeidiSQL version:     3.1 RC1 Revision: 1064
# --------------------------------------------------------

/*!40100 SET CHARACTER SET latin1;*/
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ANSI';*/
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;*/


#
# Database structure for database 'forest'
#

CREATE DATABASE /*!32312 IF NOT EXISTS*/ "forest" /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_bin */;

USE "forest";


#
# Table structure for table 'fire'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "fire" (
  "Cameraid" varchar(50) DEFAULT NULL,
  "Location" varchar(50) DEFAULT NULL,
  "mail" varchar(50) DEFAULT NULL
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'fire'
#

/*!40000 ALTER TABLE "fire" DISABLE KEYS;*/
LOCK TABLES "fire" WRITE;
REPLACE INTO "fire" ("Cameraid", "Location", "mail") VALUES
	('1','coimbatore','covai.id');
REPLACE INTO "fire" ("Cameraid", "Location", "mail") VALUES
	('2','chennai','chennai.com');
REPLACE INTO "fire" ("Cameraid", "Location", "mail") VALUES
	('3','chennai','che@gmail.com');
UNLOCK TABLES;
/*!40000 ALTER TABLE "fire" ENABLE KEYS;*/
/*!40101 SET SQL_MODE=@OLD_SQL_MODE;*/
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;*/
