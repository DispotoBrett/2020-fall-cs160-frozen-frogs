-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: localhost    Database: frogs
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_posting`
--

DROP TABLE IF EXISTS `app_posting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_posting` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` varchar(10000) NOT NULL,
  `buyer_id` int NOT NULL,
  `seller_id` int NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_posting_buyer_id_13bb9cef_fk_auth_user_id` (`buyer_id`),
  KEY `app_posting_seller_id_4af1b379_fk_auth_user_id` (`seller_id`),
  CONSTRAINT `app_posting_buyer_id_13bb9cef_fk_auth_user_id` FOREIGN KEY (`buyer_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `app_posting_seller_id_4af1b379_fk_auth_user_id` FOREIGN KEY (`seller_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_posting`
--

LOCK TABLES `app_posting` WRITE;
/*!40000 ALTER TABLE `app_posting` DISABLE KEYS */;
INSERT INTO `app_posting` VALUES (2,'The C Programming Language','An instant classic',1,1,12),(3,'FreeBSD Mastery: Advanced ZFS','Learn an obscure os and fs',1,1,72),(4,'AEPA Political Science/American Government (AZ006): Practice & Study Guide','An overpriced book, required for class',1,1,1000),(5,'Structure and Interpretation of Computer Programs','Another classic.',1,1,32),(6,'Introduction to Algorithms','I just want this book out of my sight!',1,1,2),(7,'Compilers: Principles, Techniques, and Tools','Uses yacc to make a compiler.',1,1,52);
/*!40000 ALTER TABLE `app_posting` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-27 16:01:47
