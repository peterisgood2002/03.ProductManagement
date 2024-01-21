-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: pms
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `a_category`
--

DROP TABLE IF EXISTS `a_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `a_category` (
  `id` int NOT NULL,
  `category_name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `note` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `parent` int DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_a_category_a_category1_idx` (`parent`) /*!80000 INVISIBLE */,
  CONSTRAINT `fk_a_category_a_category1` FOREIGN KEY (`parent`) REFERENCES `a_category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a_category`
--

LOCK TABLES `a_category` WRITE;
/*!40000 ALTER TABLE `a_category` DISABLE KEYS */;
INSERT INTO `a_category` VALUES (1,'Platform',NULL,NULL,NULL,NULL),(2,'Customer',NULL,NULL,NULL,NULL),(3,'Product',NULL,NULL,NULL,NULL),(4,'Milestone',NULL,NULL,NULL,NULL),(10,'Modem',NULL,1,NULL,NULL),(11,'Connectivity',NULL,1,NULL,NULL),(12,'RF',NULL,1,NULL,NULL),(13,'PMIC',NULL,1,NULL,NULL),(14,'AP',NULL,1,NULL,NULL),(20,'HOME','MAIN',2,NULL,NULL),(21,'ODM','MAIN',2,NULL,NULL),(22,'T2','MAIN',2,NULL,NULL),(23,'T1','INDIRCT',2,NULL,NULL),(24,'OEM','INDIRCT',2,NULL,NULL),(30,'Smartphone',NULL,3,NULL,NULL),(31,'CPE',NULL,3,NULL,NULL),(32,'DataCard',NULL,3,NULL,NULL),(33,'Telematics',NULL,3,NULL,NULL),(34,'Wearable',NULL,3,NULL,NULL);
/*!40000 ALTER TABLE `a_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `a_compliance`
--

DROP TABLE IF EXISTS `a_compliance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `a_compliance` (
  `compliance_id` int NOT NULL,
  `compliance_name` varchar(45) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `compliance_desc` longtext,
  PRIMARY KEY (`compliance_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a_compliance`
--

LOCK TABLES `a_compliance` WRITE;
/*!40000 ALTER TABLE `a_compliance` DISABLE KEYS */;
/*!40000 ALTER TABLE `a_compliance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `a_priority`
--

DROP TABLE IF EXISTS `a_priority`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `a_priority` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a_priority`
--

LOCK TABLES `a_priority` WRITE;
/*!40000 ALTER TABLE `a_priority` DISABLE KEYS */;
INSERT INTO `a_priority` VALUES (1,'Mandatory','2023-11-14','2023-11-14');
/*!40000 ALTER TABLE `a_priority` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_action`
--

DROP TABLE IF EXISTS `e_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_action` (
  `project_id` int NOT NULL,
  `milestone_id` int NOT NULL,
  `schedule_id` int NOT NULL,
  `action_id` int NOT NULL,
  `action_desc` longtext,
  `owner_id` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `deadline` date DEFAULT NULL,
  `finish_date` date DEFAULT NULL,
  `priority_id` int NOT NULL,
  `comment` longtext,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`action_id`),
  KEY `fk_e_action_e_employee1_idx` (`owner_id`),
  KEY `fk_e_action_e_Priority1_idx` (`priority_id`),
  KEY `fk_e_action_r_project_schedule1_idx` (`project_id`,`milestone_id`,`schedule_id`),
  CONSTRAINT `fk_e_action_e_employee1` FOREIGN KEY (`owner_id`) REFERENCES `e_employee` (`id`),
  CONSTRAINT `fk_e_action_e_Priority1` FOREIGN KEY (`priority_id`) REFERENCES `a_priority` (`id`),
  CONSTRAINT `fk_e_action_r_project_schedule1` FOREIGN KEY (`project_id`, `milestone_id`, `schedule_id`) REFERENCES `r_project_schedule` (`project_id`, `milestone_id`, `schedule_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_action`
--

LOCK TABLES `e_action` WRITE;
/*!40000 ALTER TABLE `e_action` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_area`
--

DROP TABLE IF EXISTS `e_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_area` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_area`
--

LOCK TABLES `e_area` WRITE;
/*!40000 ALTER TABLE `e_area` DISABLE KEYS */;
INSERT INTO `e_area` VALUES (1,'NA','2022-05-19','2023-11-16'),(2,'JP','2022-05-19','2023-11-21'),(3,'EU','2022-05-19','2023-11-21'),(4,'CN','2022-05-19','2023-11-21'),(5,'TW',NULL,NULL);
/*!40000 ALTER TABLE `e_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_compliance_version`
--

DROP TABLE IF EXISTS `e_compliance_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_compliance_version` (
  `operator_id` int NOT NULL,
  `version_no` varchar(45) NOT NULL,
  `doc_url` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`operator_id`,`version_no`),
  KEY `fk_e_version_e_operator1_idx` (`operator_id`),
  CONSTRAINT `fk_e_version_e_operator1` FOREIGN KEY (`operator_id`) REFERENCES `e_operator` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_compliance_version`
--

LOCK TABLES `e_compliance_version` WRITE;
/*!40000 ALTER TABLE `e_compliance_version` DISABLE KEYS */;

/*!40000 ALTER TABLE `e_compliance_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_customer`
--

DROP TABLE IF EXISTS `e_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_customer` (
  `id` int NOT NULL,
  `name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `area` int NOT NULL,
  `cpm` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `is_alpha` tinyint NOT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_customer_e_employee_idx` (`cpm`),
  KEY `fk_e_customer_e_area1_idx` (`area`),
  CONSTRAINT `fk_e_customer_e_area1` FOREIGN KEY (`area`) REFERENCES `e_area` (`id`),
  CONSTRAINT `fk_e_customer_e_employee` FOREIGN KEY (`cpm`) REFERENCES `e_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_customer`
--

LOCK TABLES `e_customer` WRITE;
/*!40000 ALTER TABLE `e_customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_device_requirement`
--

DROP TABLE IF EXISTS `e_device_requirement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_device_requirement` (
  `operator_id` int NOT NULL,
  `version_no` varchar(45) NOT NULL,
  `desc_id` int NOT NULL,
  `priority` int DEFAULT NULL,
  `structure_id` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `tag_id` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`operator_id`,`version_no`,`desc_id`),
  UNIQUE KEY `fk_e_device_requirement_e_doc_structure1_idx` (`operator_id`,`version_no`,`structure_id`) /*!80000 INVISIBLE */,
  KEY `fk_e_device_requirement_e_priority1_idx` (`priority`),
  KEY `fk_e_device_requirement_e_device_requirement_desc1_idx` (`desc_id`) /*!80000 INVISIBLE */,
  CONSTRAINT `fk_e_device_requirement_e_compliance_version1` FOREIGN KEY (`operator_id`, `version_no`) REFERENCES `e_compliance_version` (`operator_id`, `version_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_e_device_requirement_e_device_requirement_desc1` FOREIGN KEY (`desc_id`) REFERENCES `e_device_requirement_desc` (`id`),
  CONSTRAINT `fk_e_device_requirement_e_doc_structure1` FOREIGN KEY (`operator_id`, `version_no`, `structure_id`) REFERENCES `e_doc_structure` (`operator_id`, `version_no`, `doc_id`),
  CONSTRAINT `fk_e_device_requirement_e_priority1` FOREIGN KEY (`priority`) REFERENCES `a_priority` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_device_requirement`
--

LOCK TABLES `e_device_requirement` WRITE;
/*!40000 ALTER TABLE `e_device_requirement` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_device_requirement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_device_requirement_desc`
--

DROP TABLE IF EXISTS `e_device_requirement_desc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_device_requirement_desc` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `description` longtext,
  `doc_loc` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `note` varchar(2048) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_device_requirement_desc`
--

LOCK TABLES `e_device_requirement_desc` WRITE;
/*!40000 ALTER TABLE `e_device_requirement_desc` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_device_requirement_desc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_device_requirement_question`
--

DROP TABLE IF EXISTS `e_device_requirement_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_device_requirement_question` (
  `desc_id` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `question` longtext,
  `answer` longtext,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `create_user` varchar(45) DEFAULT NULL,
  `answer_user` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`,`desc_id`),
  KEY `fk_e_device_requirement_question_e_device_requirement_desc1_idx` (`desc_id`),
  CONSTRAINT `fk_e_device_requirement_question_e_device_requirement_desc1` FOREIGN KEY (`desc_id`) REFERENCES `e_device_requirement_desc` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_device_requirement_question`
--

LOCK TABLES `e_device_requirement_question` WRITE;
/*!40000 ALTER TABLE `e_device_requirement_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_device_requirement_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_doc_structure`
--

DROP TABLE IF EXISTS `e_doc_structure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_doc_structure` (
  `operator_id` int NOT NULL,
  `version_no` varchar(45) NOT NULL,
  `doc_id` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `category` int NOT NULL,
  `parent_structure_id` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`operator_id`,`version_no`,`doc_id`),
  KEY `fk_e_doc_structure_e_doc_structure_category1_idx` (`category`),
  KEY `fk_doc_structure_has_parent_doc_structure_idx` (`operator_id`,`version_no`,`parent_structure_id`) /*!80000 INVISIBLE */,
  CONSTRAINT `fk_compliance_version_has_doc_structures` FOREIGN KEY (`operator_id`, `version_no`) REFERENCES `e_compliance_version` (`operator_id`, `version_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_doc_structure_has_parent_doc_structure` FOREIGN KEY (`operator_id`, `version_no`, `parent_structure_id`) REFERENCES `e_doc_structure` (`operator_id`, `version_no`, `doc_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_doc_structure_is_doc_structure_category` FOREIGN KEY (`category`) REFERENCES `e_doc_structure_category` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_doc_structure`
--

LOCK TABLES `e_doc_structure` WRITE;
/*!40000 ALTER TABLE `e_doc_structure` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_doc_structure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_doc_structure_category`
--

DROP TABLE IF EXISTS `e_doc_structure_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_doc_structure_category` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_doc_structure_category`
--

LOCK TABLES `e_doc_structure_category` WRITE;
/*!40000 ALTER TABLE `e_doc_structure_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_doc_structure_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_employee`
--

DROP TABLE IF EXISTS `e_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_employee` (
  `id` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `chinese_name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `english_name` varchar(255) DEFAULT NULL,
  `nt_account` varchar(255) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_employee`
--

LOCK TABLES `e_employee` WRITE;
/*!40000 ALTER TABLE `e_employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_feature`
--

DROP TABLE IF EXISTS `e_feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_feature` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_feature`
--

LOCK TABLES `e_feature` WRITE;
/*!40000 ALTER TABLE `e_feature` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_generation`
--

DROP TABLE IF EXISTS `e_generation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_generation` (
  `id` int NOT NULL,
  `name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `external_name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_generation`
--

LOCK TABLES `e_generation` WRITE;
/*!40000 ALTER TABLE `e_generation` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_generation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_milestone`
--

DROP TABLE IF EXISTS `e_milestone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_milestone` (
  `id` int NOT NULL,
  `category_id` int NOT NULL,
  `milestone_name` longtext,
  `deliverable` longtext,
  `parent_milestone` int DEFAULT NULL,
  `estimated_baseline` int DEFAULT NULL,
  `estimated` double DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_milestone_a_category1_idx` (`category_id`),
  KEY `fk_estimated_basedon_idx` (`estimated_baseline`),
  KEY `fk_e_milestone_e_milestone1_idx` (`parent_milestone`),
  CONSTRAINT `fk_e_milestone_a_category1` FOREIGN KEY (`category_id`) REFERENCES `a_category` (`id`),
  CONSTRAINT `fk_e_milestone_a_category2` FOREIGN KEY (`estimated_baseline`) REFERENCES `a_category` (`id`),
  CONSTRAINT `fk_e_milestone_e_milestone1` FOREIGN KEY (`parent_milestone`) REFERENCES `e_milestone` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_milestone`
--

LOCK TABLES `e_milestone` WRITE;
/*!40000 ALTER TABLE `e_milestone` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_milestone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_operator`
--

DROP TABLE IF EXISTS `e_operator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_operator` (
  `id` int NOT NULL,
  `name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `area_id` int NOT NULL,
  `url` longtext,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_operator_e_area1_idx` (`area_id`),
  CONSTRAINT `fk_e_operator_e_area1` FOREIGN KEY (`area_id`) REFERENCES `e_area` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_operator`
--

LOCK TABLES `e_operator` WRITE;
/*!40000 ALTER TABLE `e_operator` DISABLE KEYS */;
INSERT INTO `e_operator` VALUES (101,'ATT',1,'Z:\\AT_and_T','2022-05-19','2022-05-19'),(102,'TMO',1,NULL,'2022-02-22','2022-02-22');
/*!40000 ALTER TABLE `e_operator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_platform`
--

DROP TABLE IF EXISTS `e_platform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_platform` (
  `id` int NOT NULL,
  `name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `external_name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `ppm` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `platform_family_id` int NOT NULL,
  `category` int NOT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_platform_e_employee1_idx` (`ppm`),
  KEY `fk_e_platform_e_platform_family1_idx` (`platform_family_id`),
  KEY `fk_e_platform_a_category1_idx` (`category`),
  CONSTRAINT `fk_e_platform_a_category1` FOREIGN KEY (`category`) REFERENCES `a_category` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_e_platform_e_employee1` FOREIGN KEY (`ppm`) REFERENCES `e_employee` (`id`),
  CONSTRAINT `fk_e_platform_e_platform_family1` FOREIGN KEY (`platform_family_id`) REFERENCES `e_platform_family` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_platform`
--

LOCK TABLES `e_platform` WRITE;
/*!40000 ALTER TABLE `e_platform` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_platform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_platform_family`
--

DROP TABLE IF EXISTS `e_platform_family`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_platform_family` (
  `id` int NOT NULL,
  `name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `external_name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `generation_id` int NOT NULL,
  `create_Date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_platform_family_e_generation1_idx` (`generation_id`),
  CONSTRAINT `fk_e_platform_family_e_generation1` FOREIGN KEY (`generation_id`) REFERENCES `e_generation` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_platform_family`
--

LOCK TABLES `e_platform_family` WRITE;
/*!40000 ALTER TABLE `e_platform_family` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_platform_family` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_product`
--

DROP TABLE IF EXISTS `e_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_product` (
  `id` int NOT NULL,
  `name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `category_id` int NOT NULL,
  `ta_id` int DEFAULT NULL,
  `forecast_qty` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_product_e_category1_idx` (`category_id`),
  KEY `fk_e_product_e_technical_acceptance1_idx` (`ta_id`),
  CONSTRAINT `fk_e_product_e_category1` FOREIGN KEY (`category_id`) REFERENCES `a_category` (`id`),
  CONSTRAINT `fk_e_product_e_technical_acceptance1` FOREIGN KEY (`ta_id`) REFERENCES `e_technical_acceptance` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_product`
--

LOCK TABLES `e_product` WRITE;
/*!40000 ALTER TABLE `e_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_project`
--

DROP TABLE IF EXISTS `e_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_project` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `alpha_project` tinyint DEFAULT NULL,
  `priority` int DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_project_a_priority1_idx` (`priority`),
  CONSTRAINT `fk_e_project_a_priority1` FOREIGN KEY (`priority`) REFERENCES `a_priority` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_project`
--

LOCK TABLES `e_project` WRITE;
/*!40000 ALTER TABLE `e_project` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_project_fwversion`
--

DROP TABLE IF EXISTS `e_project_fwversion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_project_fwversion` (
  `project_id` int NOT NULL,
  `version` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `ta_id` int DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`project_id`,`version`),
  KEY `fk_e_platform_version_e_technical_acceptance1_idx` (`ta_id`),
  KEY `fk_e_project_fwversion_e_project1_idx` (`project_id`),
  CONSTRAINT `fk_e_platform_version_e_technical_acceptance1` FOREIGN KEY (`ta_id`) REFERENCES `e_technical_acceptance` (`id`),
  CONSTRAINT `fk_e_project_fwversion_e_project1` FOREIGN KEY (`project_id`) REFERENCES `e_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_project_fwversion`
--

LOCK TABLES `e_project_fwversion` WRITE;
/*!40000 ALTER TABLE `e_project_fwversion` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_project_fwversion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_requirement_category`
--

DROP TABLE IF EXISTS `e_requirement_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_requirement_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `parent` int NOT NULL,
  PRIMARY KEY (`id`,`parent`),
  KEY `fk_e_requirement_category_a_category1_idx` (`parent`),
  CONSTRAINT `fk_e_requirement_category_a_category1` FOREIGN KEY (`parent`) REFERENCES `a_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_requirement_category`
--

LOCK TABLES `e_requirement_category` WRITE;
/*!40000 ALTER TABLE `e_requirement_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_requirement_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_technical_acceptance`
--

DROP TABLE IF EXISTS `e_technical_acceptance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_technical_acceptance` (
  `id` int NOT NULL,
  `issue_date` date DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_technical_acceptance`
--

LOCK TABLES `e_technical_acceptance` WRITE;
/*!40000 ALTER TABLE `e_technical_acceptance` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_technical_acceptance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_test_plan`
--

DROP TABLE IF EXISTS `e_test_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_test_plan` (
  `operator_id` int NOT NULL,
  `version_no` varchar(45) NOT NULL,
  `test_id` int NOT NULL,
  `title` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `test_description` varchar(2048) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`operator_id`,`version_no`,`test_id`),
  CONSTRAINT `fk_e_test_plan_e_compliance_version1` FOREIGN KEY (`operator_id`, `version_no`) REFERENCES `e_compliance_version` (`operator_id`, `version_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_test_plan`
--

LOCK TABLES `e_test_plan` WRITE;
/*!40000 ALTER TABLE `e_test_plan` DISABLE KEYS */;
/*!40000 ALTER TABLE `e_test_plan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_device_requirement_category`
--

DROP TABLE IF EXISTS `r_device_requirement_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_device_requirement_category` (
  `desc_id` int NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`desc_id`,`category_id`),
  KEY `fk_e_requirement_category_has_e_device_requirement_e_requir_idx` (`category_id`),
  KEY `fk_r_device_requirement_category_e_device_requirement_desc1_idx` (`desc_id`),
  CONSTRAINT `fk_e_requirement_category_has_e_device_requirement_e_requirem1` FOREIGN KEY (`category_id`) REFERENCES `e_requirement_category` (`id`),
  CONSTRAINT `fk_r_device_requirement_category_e_device_requirement_desc1` FOREIGN KEY (`desc_id`) REFERENCES `e_device_requirement_desc` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_device_requirement_category`
--

LOCK TABLES `r_device_requirement_category` WRITE;
/*!40000 ALTER TABLE `r_device_requirement_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_device_requirement_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_employee_role_project`
--

DROP TABLE IF EXISTS `r_employee_role_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_employee_role_project` (
  `e_project_id` int NOT NULL,
  `e_employee_id` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `role` int NOT NULL,
  PRIMARY KEY (`e_project_id`,`e_employee_id`),
  KEY `fk_e_project_has_e_employee_e_employee1_idx` (`e_employee_id`),
  KEY `fk_e_project_has_e_employee_e_project1_idx` (`e_project_id`),
  KEY `fk_r_employee_role_project_a_category1_idx` (`role`),
  CONSTRAINT `fk_e_project_has_e_employee_e_employee1` FOREIGN KEY (`e_employee_id`) REFERENCES `e_employee` (`id`),
  CONSTRAINT `fk_e_project_has_e_employee_e_project1` FOREIGN KEY (`e_project_id`) REFERENCES `e_project` (`id`),
  CONSTRAINT `fk_r_employee_role_project_a_category1` FOREIGN KEY (`role`) REFERENCES `a_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_employee_role_project`
--

LOCK TABLES `r_employee_role_project` WRITE;
/*!40000 ALTER TABLE `r_employee_role_project` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_employee_role_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_op_rfp`
--

DROP TABLE IF EXISTS `r_op_rfp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_op_rfp` (
  `operator_id` int NOT NULL,
  `product_id` int NOT NULL,
  `version_no` varchar(45) NOT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL COMMENT 'This tables records the RFP',
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`operator_id`,`product_id`,`version_no`),
  KEY `fk_e_operator_has_e_product_e_product1_idx` (`product_id`),
  KEY `fk_e_operator_has_e_product_e_operator1_idx` (`operator_id`),
  CONSTRAINT `fk_e_operator_has_e_product_e_operator1` FOREIGN KEY (`operator_id`) REFERENCES `e_operator` (`id`),
  CONSTRAINT `fk_e_operator_has_e_product_e_product1` FOREIGN KEY (`product_id`) REFERENCES `e_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_op_rfp`
--

LOCK TABLES `r_op_rfp` WRITE;
/*!40000 ALTER TABLE `r_op_rfp` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_op_rfp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_operator_schedule`
--

DROP TABLE IF EXISTS `r_operator_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_operator_schedule` (
  `operator_id` int NOT NULL,
  `milestone_id` int NOT NULL COMMENT 'Operator has its own schedule to release document',
  `version` varchar(45) DEFAULT NULL,
  `plan_release_date` date DEFAULT NULL,
  `actual_release_date` date DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`operator_id`,`milestone_id`),
  KEY `fk_e_operator_has_e_milestone_e_milestone1_idx` (`milestone_id`),
  KEY `fk_e_operator_has_e_milestone_e_operator1_idx` (`operator_id`),
  CONSTRAINT `fk_e_operator_has_e_milestone_e_milestone1` FOREIGN KEY (`milestone_id`) REFERENCES `e_milestone` (`id`),
  CONSTRAINT `fk_e_operator_has_e_milestone_e_operator1` FOREIGN KEY (`operator_id`) REFERENCES `e_operator` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_operator_schedule`
--

LOCK TABLES `r_operator_schedule` WRITE;
/*!40000 ALTER TABLE `r_operator_schedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_operator_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_product_feature`
--

DROP TABLE IF EXISTS `r_product_feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_product_feature` (
  `product_id` int NOT NULL,
  `feature_id` int NOT NULL,
  `parameters` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`product_id`,`feature_id`),
  KEY `fk_e_product_has_e_feature_e_feature1_idx` (`feature_id`),
  KEY `fk_e_product_has_e_feature_e_product1_idx` (`product_id`),
  CONSTRAINT `fk_e_product_has_e_feature_e_feature1` FOREIGN KEY (`feature_id`) REFERENCES `e_feature` (`id`),
  CONSTRAINT `fk_e_product_has_e_feature_e_product1` FOREIGN KEY (`product_id`) REFERENCES `e_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_product_feature`
--

LOCK TABLES `r_product_feature` WRITE;
/*!40000 ALTER TABLE `r_product_feature` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_product_feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_product_schedule`
--

DROP TABLE IF EXISTS `r_product_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_product_schedule` (
  `product_id` int NOT NULL,
  `milestone_id` int NOT NULL,
  `plan_start_dt` date DEFAULT NULL,
  `plan_end_dt` date DEFAULT NULL,
  `actual_start_dt` date DEFAULT NULL,
  `actual_end_dt` date DEFAULT NULL,
  PRIMARY KEY (`product_id`,`milestone_id`),
  KEY `fk_e_milestone_has_e_product_e_product1_idx` (`product_id`),
  KEY `fk_e_milestone_has_e_product_e_milestone1_idx` (`milestone_id`),
  CONSTRAINT `fk_e_milestone_has_e_product_e_milestone1` FOREIGN KEY (`milestone_id`) REFERENCES `e_milestone` (`id`),
  CONSTRAINT `fk_e_milestone_has_e_product_e_product1` FOREIGN KEY (`product_id`) REFERENCES `e_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_product_schedule`
--

LOCK TABLES `r_product_schedule` WRITE;
/*!40000 ALTER TABLE `r_product_schedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_product_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_project_customer`
--

DROP TABLE IF EXISTS `r_project_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_project_customer` (
  `customer_id` int NOT NULL,
  `project_id` int NOT NULL,
  `relationship` int NOT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`customer_id`,`project_id`),
  KEY `fk_e_customer_has_e_project_e_project1_idx` (`project_id`),
  KEY `fk_r_project_customer_a_category1_idx` (`relationship`),
  KEY `fk_r_project_customer_e_customer1_idx` (`customer_id`),
  CONSTRAINT `fk_e_customer_has_e_project_e_project1` FOREIGN KEY (`project_id`) REFERENCES `e_project` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_r_project_customer_a_category1` FOREIGN KEY (`relationship`) REFERENCES `a_category` (`id`),
  CONSTRAINT `fk_r_project_customer_e_customer1` FOREIGN KEY (`customer_id`) REFERENCES `e_customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_project_customer`
--

LOCK TABLES `r_project_customer` WRITE;
/*!40000 ALTER TABLE `r_project_customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_project_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_project_fwversion_feature`
--

DROP TABLE IF EXISTS `r_project_fwversion_feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_project_fwversion_feature` (
  `project_id` int NOT NULL,
  `version` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `feature` int NOT NULL,
  PRIMARY KEY (`project_id`,`version`,`feature`),
  KEY `fk_e_project_fwversion_has_e_feature_e_feature1_idx` (`feature`),
  KEY `fk_e_project_fwversion_has_e_feature_e_project_fwversion1_idx` (`project_id`,`version`),
  CONSTRAINT `fk_e_project_fwversion_has_e_feature_e_feature1` FOREIGN KEY (`feature`) REFERENCES `e_feature` (`id`),
  CONSTRAINT `fk_e_project_fwversion_has_e_feature_e_project_fwversion1` FOREIGN KEY (`project_id`, `version`) REFERENCES `e_project_fwversion` (`project_id`, `version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_project_fwversion_feature`
--

LOCK TABLES `r_project_fwversion_feature` WRITE;
/*!40000 ALTER TABLE `r_project_fwversion_feature` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_project_fwversion_feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_project_platform`
--

DROP TABLE IF EXISTS `r_project_platform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_project_platform` (
  `project_id` int NOT NULL,
  `platform_id` int NOT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`project_id`,`platform_id`),
  KEY `fk_e_project_has_e_platform_e_platform1_idx` (`platform_id`),
  KEY `fk_e_project_has_e_platform_e_project1_idx` (`project_id`),
  CONSTRAINT `fk_e_project_has_e_platform_e_platform1` FOREIGN KEY (`platform_id`) REFERENCES `e_platform` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_e_project_has_e_platform_e_project1` FOREIGN KEY (`project_id`) REFERENCES `e_project` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_project_platform`
--

LOCK TABLES `r_project_platform` WRITE;
/*!40000 ALTER TABLE `r_project_platform` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_project_platform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_project_schedule`
--

DROP TABLE IF EXISTS `r_project_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_project_schedule` (
  `project_id` int NOT NULL,
  `milestone_id` int NOT NULL,
  `schedule_id` int NOT NULL,
  `note` longtext,
  `plan_start_dt` date DEFAULT NULL,
  `plan_end_dt` date DEFAULT NULL,
  `actual_start_dt` date DEFAULT NULL,
  `actual_end_dt` date DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`project_id`,`milestone_id`,`schedule_id`),
  KEY `fk_e_project_has_e_milestone_e_project1_idx` (`project_id`),
  KEY `fk_e_project_has_e_milestone_e_milestone1_idx` (`milestone_id`),
  CONSTRAINT `fk_e_project_has_e_milestone_e_milestone1` FOREIGN KEY (`milestone_id`) REFERENCES `e_milestone` (`id`),
  CONSTRAINT `fk_e_project_has_e_milestone_e_project1` FOREIGN KEY (`project_id`) REFERENCES `e_project` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_project_schedule`
--

LOCK TABLES `r_project_schedule` WRITE;
/*!40000 ALTER TABLE `r_project_schedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_project_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_project_target_product`
--

DROP TABLE IF EXISTS `r_project_target_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_project_target_product` (
  `project_id` int NOT NULL,
  `product_id` int NOT NULL,
  PRIMARY KEY (`project_id`,`product_id`),
  KEY `fk_e_project_has_e_product_e_product1_idx` (`product_id`),
  KEY `fk_e_project_has_e_product_e_project1_idx` (`project_id`),
  CONSTRAINT `fk_e_project_has_e_product_e_product1` FOREIGN KEY (`product_id`) REFERENCES `e_product` (`id`),
  CONSTRAINT `fk_e_project_has_e_product_e_project1` FOREIGN KEY (`project_id`) REFERENCES `e_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_project_target_product`
--

LOCK TABLES `r_project_target_product` WRITE;
/*!40000 ALTER TABLE `r_project_target_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_project_target_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_ta_comply_device_requirement`
--

DROP TABLE IF EXISTS `r_ta_comply_device_requirement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_ta_comply_device_requirement` (
  `operator_id` int NOT NULL,
  `version_no` varchar(45) NOT NULL,
  `requirement_id` int NOT NULL,
  `technical_acceptance_id` int NOT NULL,
  `compliance` int NOT NULL,
  PRIMARY KEY (`operator_id`,`version_no`,`requirement_id`,`technical_acceptance_id`),
  KEY `fk_e_technical_acceptance_has_e_device_requirement_e_techni_idx` (`technical_acceptance_id`),
  KEY `fk_r_ta_comply_device_requirement_a_compliance1_idx` (`compliance`),
  CONSTRAINT `fk_e_technical_acceptance_has_e_device_requirement_e_device_r1` FOREIGN KEY (`operator_id`, `version_no`, `requirement_id`) REFERENCES `e_device_requirement` (`operator_id`, `version_no`, `desc_id`),
  CONSTRAINT `fk_e_technical_acceptance_has_e_device_requirement_e_technica1` FOREIGN KEY (`technical_acceptance_id`) REFERENCES `e_technical_acceptance` (`id`),
  CONSTRAINT `fk_r_ta_comply_device_requirement_a_compliance1` FOREIGN KEY (`compliance`) REFERENCES `a_compliance` (`compliance_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_ta_comply_device_requirement`
--

LOCK TABLES `r_ta_comply_device_requirement` WRITE;
/*!40000 ALTER TABLE `r_ta_comply_device_requirement` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_ta_comply_device_requirement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_ta_comply_test_plan`
--

DROP TABLE IF EXISTS `r_ta_comply_test_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_ta_comply_test_plan` (
  `technical_acceptance_id` int NOT NULL,
  `test_id` int NOT NULL,
  `version_no` varchar(45) NOT NULL,
  `operator_id` int NOT NULL,
  PRIMARY KEY (`technical_acceptance_id`,`test_id`,`version_no`,`operator_id`),
  KEY `fk_e_technical_acceptance_has_e_test_plan_e_technical_accep_idx` (`technical_acceptance_id`),
  KEY `fk_e_technical_acceptance_has_e_test_plan_e_test_plan1_idx` (`operator_id`,`version_no`,`test_id`),
  CONSTRAINT `fk_e_technical_acceptance_has_e_test_plan_e_technical_accepta1` FOREIGN KEY (`technical_acceptance_id`) REFERENCES `e_technical_acceptance` (`id`),
  CONSTRAINT `fk_e_technical_acceptance_has_e_test_plan_e_test_plan1` FOREIGN KEY (`operator_id`, `version_no`, `test_id`) REFERENCES `e_test_plan` (`operator_id`, `version_no`, `test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_ta_comply_test_plan`
--

LOCK TABLES `r_ta_comply_test_plan` WRITE;
/*!40000 ALTER TABLE `r_ta_comply_test_plan` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_ta_comply_test_plan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_test_plan_examine_device_requirement`
--

DROP TABLE IF EXISTS `r_test_plan_examine_device_requirement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_test_plan_examine_device_requirement` (
  `operator_id` int NOT NULL,
  `version_no` varchar(45) NOT NULL,
  `requirement_id` int NOT NULL,
  `test_id` int NOT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`operator_id`,`version_no`,`requirement_id`,`test_id`),
  KEY `fk_e_device_requirement_has_e_test_plan_e_test_plan1_idx` (`operator_id`,`version_no`,`test_id`),
  CONSTRAINT `fk_e_device_requirement_has_e_test_plan_e_device_requirement1` FOREIGN KEY (`operator_id`, `version_no`, `requirement_id`) REFERENCES `e_device_requirement` (`operator_id`, `version_no`, `desc_id`),
  CONSTRAINT `fk_e_device_requirement_has_e_test_plan_e_test_plan1` FOREIGN KEY (`operator_id`, `version_no`, `test_id`) REFERENCES `e_test_plan` (`operator_id`, `version_no`, `test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_test_plan_examine_device_requirement`
--

LOCK TABLES `r_test_plan_examine_device_requirement` WRITE;
/*!40000 ALTER TABLE `r_test_plan_examine_device_requirement` DISABLE KEYS */;
/*!40000 ALTER TABLE `r_test_plan_examine_device_requirement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `v_milestone`
--

DROP TABLE IF EXISTS `v_milestone`;
/*!50001 DROP VIEW IF EXISTS `v_milestone`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_milestone` AS SELECT 
 1 AS `category_name`,
 1 AS `milestone_id`,
 1 AS `milestone_name`,
 1 AS `deliverable`,
 1 AS `ESTIMATED_BASE`,
 1 AS `estimated`,
 1 AS `PARENT_MILESTONE`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_operator_doc_structure`
--

DROP TABLE IF EXISTS `v_operator_doc_structure`;
/*!50001 DROP VIEW IF EXISTS `v_operator_doc_structure`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_operator_doc_structure` AS SELECT 
 1 AS `operator_id`,
 1 AS `version_no`,
 1 AS `ChapterId`,
 1 AS `Chapter`,
 1 AS `SectionId`,
 1 AS `Section`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_operator_requirement`
--

DROP TABLE IF EXISTS `v_operator_requirement`;
/*!50001 DROP VIEW IF EXISTS `v_operator_requirement`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_operator_requirement` AS SELECT 
 1 AS `area`,
 1 AS `operatorId`,
 1 AS `operator`,
 1 AS `version_no`,
 1 AS `SectionId`,
 1 AS `tag_id`,
 1 AS `title`,
 1 AS `name`,
 1 AS `description`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_operator_requirement_with_structure`
--

DROP TABLE IF EXISTS `v_operator_requirement_with_structure`;
/*!50001 DROP VIEW IF EXISTS `v_operator_requirement_with_structure`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_operator_requirement_with_structure` AS SELECT 
 1 AS `area`,
 1 AS `operator`,
 1 AS `version_no`,
 1 AS `tag_id`,
 1 AS `ChapterId`,
 1 AS `Chapter`,
 1 AS `SectionId`,
 1 AS `Section`,
 1 AS `title`,
 1 AS `name`,
 1 AS `description`,
 1 AS `priority`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_platform`
--

DROP TABLE IF EXISTS `v_platform`;
/*!50001 DROP VIEW IF EXISTS `v_platform`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_platform` AS SELECT 
 1 AS `G_ID`,
 1 AS `Generation`,
 1 AS `G_External`,
 1 AS `F_ID`,
 1 AS `Family`,
 1 AS `F_External`,
 1 AS `P_ID`,
 1 AS `Platform`,
 1 AS `Category`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_project_customer`
--

DROP TABLE IF EXISTS `v_project_customer`;
/*!50001 DROP VIEW IF EXISTS `v_project_customer`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_project_customer` AS SELECT 
 1 AS `P_ID`,
 1 AS `Project`,
 1 AS `A_ID`,
 1 AS `Area`,
 1 AS `C_ID`,
 1 AS `Customer`,
 1 AS `category_name`,
 1 AS `note`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_project_platform`
--

DROP TABLE IF EXISTS `v_project_platform`;
/*!50001 DROP VIEW IF EXISTS `v_project_platform`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_project_platform` AS SELECT 
 1 AS `P_ID`,
 1 AS `Project`,
 1 AS `Generation`,
 1 AS `Family`,
 1 AS `Platform`,
 1 AS `Category`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_milestone`
--

/*!50001 DROP VIEW IF EXISTS `v_milestone`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_milestone` AS select `c`.`category_name` AS `category_name`,(case when (`e`.`parent_milestone` is null) then `e`.`id` else (`e`.`id` / (round((`e`.`id` / `e`.`category_id`),0) / 10)) end) AS `milestone_id`,`e`.`milestone_name` AS `milestone_name`,`e`.`deliverable` AS `deliverable`,`b`.`category_name` AS `ESTIMATED_BASE`,`e`.`estimated` AS `estimated`,`p`.`milestone_name` AS `PARENT_MILESTONE` from (((`e_milestone` `e` join `a_category` `c` on((`e`.`category_id` = `c`.`id`))) left join `a_category` `b` on((`e`.`estimated_baseline` = `b`.`id`))) left join `e_milestone` `p` on((`e`.`parent_milestone` = `p`.`id`))) order by (case when (`e`.`parent_milestone` is null) then `e`.`id` else (`e`.`id` / (round((`e`.`id` / `e`.`category_id`),0) / 10)) end) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_operator_doc_structure`
--

/*!50001 DROP VIEW IF EXISTS `v_operator_doc_structure`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_operator_doc_structure` AS select `section`.`operator_id` AS `operator_id`,`section`.`version_no` AS `version_no`,`chapter`.`doc_id` AS `ChapterId`,`chapter`.`name` AS `Chapter`,`section`.`doc_id` AS `SectionId`,`section`.`name` AS `Section` from (`e_doc_structure` `chapter` join `e_doc_structure` `section`) where ((`chapter`.`operator_id` = `section`.`operator_id`) and (`chapter`.`version_no` = `section`.`version_no`) and (`section`.`parent_structure_id` = `chapter`.`doc_id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_operator_requirement`
--

/*!50001 DROP VIEW IF EXISTS `v_operator_requirement`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_operator_requirement` AS select `a`.`name` AS `area`,`o`.`id` AS `operatorId`,`o`.`name` AS `operator`,`v`.`version_no` AS `version_no`,`r`.`structure_id` AS `SectionId`,`r`.`tag_id` AS `tag_id`,`d`.`title` AS `title`,`d`.`name` AS `name`,`d`.`description` AS `description` from ((((`e_area` `a` join `e_operator` `o`) join `e_compliance_version` `v`) join `e_device_requirement` `r`) join `e_device_requirement_desc` `d`) where ((`a`.`id` = `o`.`area_id`) and (`o`.`id` = `v`.`operator_id`) and (`v`.`operator_id` = `r`.`operator_id`) and (`v`.`version_no` = `r`.`version_no`) and (`r`.`desc_id` = `d`.`id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_operator_requirement_with_structure`
--

/*!50001 DROP VIEW IF EXISTS `v_operator_requirement_with_structure`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_operator_requirement_with_structure` AS select `a`.`name` AS `area`,`o`.`name` AS `operator`,`v`.`version_no` AS `version_no`,`r`.`tag_id` AS `tag_id`,`chapter`.`doc_id` AS `ChapterId`,`chapter`.`name` AS `Chapter`,`section`.`doc_id` AS `SectionId`,`section`.`name` AS `Section`,`d`.`title` AS `title`,`d`.`name` AS `name`,`d`.`description` AS `description`,`p`.`name` AS `priority` from (((((((`e_area` `a` join `e_operator` `o` on((`a`.`id` = `o`.`area_id`))) join `e_compliance_version` `v` on((`o`.`id` = `v`.`operator_id`))) join `e_device_requirement` `r` on(((`v`.`operator_id` = `r`.`operator_id`) and (`v`.`version_no` = `r`.`version_no`)))) left join `a_priority` `p` on((`r`.`priority` = `p`.`id`))) join `e_device_requirement_desc` `d` on((`r`.`desc_id` = `d`.`id`))) join `e_doc_structure` `section` on(((`r`.`operator_id` = `section`.`operator_id`) and (`r`.`version_no` = `section`.`version_no`) and (`r`.`structure_id` = `section`.`doc_id`)))) join `e_doc_structure` `chapter` on(((`chapter`.`operator_id` = `section`.`operator_id`) and (`chapter`.`version_no` = `section`.`version_no`) and (`section`.`parent_structure_id` = `chapter`.`doc_id`)))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_platform`
--

/*!50001 DROP VIEW IF EXISTS `v_platform`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_platform` AS select `g`.`id` AS `G_ID`,`g`.`name` AS `Generation`,`g`.`external_name` AS `G_External`,`f`.`id` AS `F_ID`,`f`.`name` AS `Family`,`f`.`external_name` AS `F_External`,`p`.`id` AS `P_ID`,`p`.`name` AS `Platform`,`c`.`category_name` AS `Category` from (((`e_generation` `g` join `e_platform_family` `f` on((`f`.`generation_id` = `g`.`id`))) join `e_platform` `p` on((`p`.`platform_family_id` = `f`.`id`))) join `a_category` `c` on((`c`.`id` = `p`.`category`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_project_customer`
--

/*!50001 DROP VIEW IF EXISTS `v_project_customer`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_project_customer` AS select `p`.`id` AS `P_ID`,`p`.`name` AS `Project`,`a`.`id` AS `A_ID`,`a`.`name` AS `Area`,`pc`.`customer_id` AS `C_ID`,`c`.`name` AS `Customer`,`category`.`category_name` AS `category_name`,`category`.`note` AS `note` from ((((`e_project` `p` join `r_project_customer` `pc` on((`pc`.`project_id` = `p`.`id`))) join `e_customer` `c` on((`c`.`id` = `pc`.`customer_id`))) join `e_area` `a` on((`a`.`id` = `c`.`area`))) join `a_category` `category` on((`category`.`id` = `pc`.`relationship`))) order by `pc`.`relationship` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_project_platform`
--

/*!50001 DROP VIEW IF EXISTS `v_project_platform`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_project_platform` AS select `p`.`id` AS `P_ID`,`p`.`name` AS `Project`,`platform`.`Generation` AS `Generation`,`platform`.`Family` AS `Family`,`platform`.`Platform` AS `Platform`,`platform`.`Category` AS `Category` from ((`e_project` `p` join `r_project_platform` `pp` on((`p`.`id` = `pp`.`project_id`))) join `v_platform` `platform` on((`platform`.`P_ID` = `pp`.`platform_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-21 12:45:03
