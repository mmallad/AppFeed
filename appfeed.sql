-- MySQL dump 10.13  Distrib 5.5.29, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: appfeed
-- ------------------------------------------------------
-- Server version	5.5.29-0ubuntu0.12.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tblAccessID`
--

DROP TABLE IF EXISTS `tblAccessID`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tblAccessID` (
  `ACCESSID` varchar(600) NOT NULL,
  `ACCESSNAME` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ACCESSID`),
  UNIQUE KEY `ACCESSNAME` (`ACCESSNAME`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblAccessID`
--

LOCK TABLES `tblAccessID` WRITE;
/*!40000 ALTER TABLE `tblAccessID` DISABLE KEYS */;
INSERT INTO `tblAccessID` VALUES ('3312','adasda'),('91c3bc1932bb0f8358c329e8b37e23e35b7a2b616085d760904468fb638740478d8b72b260e01f12ebb78d4e8e9f4322','Heklo'),('dd31ba98d58072a2465195a7c6267ecfb363093b45bf02c7259bfa71de4c3452f70a96cb7840ed731b89a0039e72d04f','Test');
/*!40000 ALTER TABLE `tblAccessID` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblPro`
--

DROP TABLE IF EXISTS `tblPro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tblPro` (
  `PROID` int(11) NOT NULL AUTO_INCREMENT,
  `PRONAME` varchar(200) DEFAULT NULL,
  `PROQRY` text,
  PRIMARY KEY (`PROID`),
  UNIQUE KEY `PRONAME` (`PRONAME`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblPro`
--

LOCK TABLES `tblPro` WRITE;
/*!40000 ALTER TABLE `tblPro` DISABLE KEYS */;
INSERT INTO `tblPro` VALUES (1,'Test','SELEC * FROM tblTest WHERE ID = %s'),(2,'asjkd','kjadkas'),(3,'aksjdas','sdjkf ajkdas'),(4,'aaaaaaaaaaaa','adsasdas');
/*!40000 ALTER TABLE `tblPro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblUser`
--

DROP TABLE IF EXISTS `tblUser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tblUser` (
  `UID` varchar(100) NOT NULL,
  `USERNAME` varchar(50) DEFAULT NULL,
  `PASSWORD` varchar(500) NOT NULL,
  PRIMARY KEY (`UID`),
  UNIQUE KEY `USERNAME` (`USERNAME`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblUser`
--

LOCK TABLES `tblUser` WRITE;
/*!40000 ALTER TABLE `tblUser` DISABLE KEYS */;
INSERT INTO `tblUser` VALUES ('88','admin','c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec');
/*!40000 ALTER TABLE `tblUser` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-03-12  1:58:23
