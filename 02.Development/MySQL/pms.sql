-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: pms
-- ------------------------------------------------------
-- Server version	8.0.27

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
  `category_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a_category`
--

LOCK TABLES `a_category` WRITE;
/*!40000 ALTER TABLE `a_category` DISABLE KEYS */;
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
  `priority_id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`priority_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a_priority`
--

LOCK TABLES `a_priority` WRITE;
/*!40000 ALTER TABLE `a_priority` DISABLE KEYS */;
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
  `milestone_category` int NOT NULL,
  `action_id` int NOT NULL,
  `action_desc` longtext,
  `owner_id` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `deadline` date DEFAULT NULL,
  `finish_date` date DEFAULT NULL,
  `priority_id` int NOT NULL,
  `comment` longtext,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`action_id`),
  KEY `fk_e_action_e_employee1_idx` (`owner_id`),
  KEY `fk_e_action_e_Priority1_idx` (`priority_id`),
  KEY `fk_e_action_r_project_schedule1_idx` (`project_id`,`milestone_id`,`milestone_category`),
  CONSTRAINT `fk_e_action_e_employee1` FOREIGN KEY (`owner_id`) REFERENCES `e_employee` (`id`),
  CONSTRAINT `fk_e_action_e_Priority1` FOREIGN KEY (`priority_id`) REFERENCES `a_priority` (`priority_id`),
  CONSTRAINT `fk_e_action_r_project_schedule1` FOREIGN KEY (`project_id`, `milestone_id`, `milestone_category`) REFERENCES `r_project_schedule` (`project_id`, `milestone_id`, `milestone_category`)
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_area`
--

LOCK TABLES `e_area` WRITE;
/*!40000 ALTER TABLE `e_area` DISABLE KEYS */;
INSERT INTO `e_area` VALUES (1,'US','2022-05-19','2022-05-19'),(2,'JP','2022-05-19','2022-05-19'),(3,'EU','2022-05-19','2022-05-19'),(4,'CN','2022-05-19','2022-05-19');
/*!40000 ALTER TABLE `e_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_compliance_version`
--

DROP TABLE IF EXISTS `e_compliance_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_compliance_version` (
  `version_no` varchar(45) NOT NULL,
  `operator_id` int NOT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `doc_url` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`version_no`,`operator_id`),
  KEY `fk_e_version_e_operator1_idx` (`operator_id`),
  CONSTRAINT `fk_e_version_e_operator1` FOREIGN KEY (`operator_id`) REFERENCES `e_operator` (`id`)
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
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `cpm` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `is_alpha` tinyint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_customer_e_employee_idx` (`cpm`),
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
  `id` int NOT NULL,
  `priority` int DEFAULT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `description` longtext,
  `doc_loc` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `note` varchar(2048) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `structure_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`operator_id`,`version_no`,`id`),
  KEY `fk_e_device_requirement_e_priority1_idx` (`priority`),
  KEY `fk_e_device_requirement_e_compliance_version1_idx` (`version_no`,`operator_id`),
  KEY `fk_e_device_requirement_e_doc_structure1_idx` (`operator_id`,`version_no`,`structure_id`),
  CONSTRAINT `fk_e_device_requirement_e_compliance_version1` FOREIGN KEY (`version_no`, `operator_id`) REFERENCES `e_compliance_version` (`version_no`, `operator_id`),
  CONSTRAINT `fk_e_device_requirement_e_doc_structure1` FOREIGN KEY (`operator_id`, `version_no`, `structure_id`) REFERENCES `e_doc_structure` (`operator_id`, `version_no`, `id`),
  CONSTRAINT `fk_e_device_requirement_e_priority1` FOREIGN KEY (`priority`) REFERENCES `a_priority` (`priority_id`)
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
-- Table structure for table `e_doc_structure`
--

DROP TABLE IF EXISTS `e_doc_structure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_doc_structure` (
  `operator_id` int NOT NULL,
  `version_no` varchar(45) NOT NULL,
  `id` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `tagId` varchar(45) DEFAULT NULL,
  `category` int NOT NULL,
  `parent_structure_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`operator_id`,`version_no`,`id`),
  KEY `fk_e_doc_structure_e_doc_structure_category1_idx` (`category`),
  KEY `fk_e_doc_structure_e_compliance_version1_idx` (`version_no`,`operator_id`),
  KEY `fk_doc_structure_has_parent_doc_structure_idx` (`operator_id`,`version_no`,`parent_structure_id`),
  CONSTRAINT `fk_compliance_version_has_doc_structures` FOREIGN KEY (`version_no`, `operator_id`) REFERENCES `e_compliance_version` (`version_no`, `operator_id`),
  CONSTRAINT `fk_doc_structure_has_parent_doc_structure` FOREIGN KEY (`operator_id`, `version_no`, `parent_structure_id`) REFERENCES `e_doc_structure` (`operator_id`, `version_no`, `id`),
  CONSTRAINT `fk_doc_structure_is_doc_structure_category` FOREIGN KEY (`category`) REFERENCES `e_doc_structure_category` (`id`)
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
  `id` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `chinese_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
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
-- Table structure for table `e_milestone`
--

DROP TABLE IF EXISTS `e_milestone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_milestone` (
  `milestone_id` int NOT NULL,
  `category_id` int NOT NULL,
  `milestone_name` longtext,
  `deliverable` longtext,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `estimated` double DEFAULT NULL,
  `estimated_baseline` int DEFAULT NULL,
  PRIMARY KEY (`milestone_id`,`category_id`),
  KEY `fk_e_milestone_a_category1_idx` (`category_id`),
  KEY `fk_estimated_basedon_idx` (`estimated_baseline`),
  CONSTRAINT `fk_e_milestone_a_category1` FOREIGN KEY (`category_id`) REFERENCES `a_category` (`id`),
  CONSTRAINT `fk_e_milestone_a_category2` FOREIGN KEY (`estimated_baseline`) REFERENCES `a_category` (`id`)
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
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `area_id` int NOT NULL,
  `url` longtext,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_operator_e_area1_idx` (`area_id`),
  CONSTRAINT `fk_e_operator_e_area1` FOREIGN KEY (`area_id`) REFERENCES `e_area` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_operator`
--

LOCK TABLES `e_operator` WRITE;
/*!40000 ALTER TABLE `e_operator` DISABLE KEYS */;
INSERT INTO `e_operator` VALUES (1,'ATT',1,'Z:\\AT_and_T','2022-05-19','2022-05-19');
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
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `ppm` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `platform_family_id` int NOT NULL,
  `code_name` varchar(45) DEFAULT NULL,
  `category` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_platform_e_employee1_idx` (`ppm`),
  KEY `fk_e_platform_e_platform_family1_idx` (`platform_family_id`),
  KEY `fk_e_platform_a_category1_idx` (`category`),
  CONSTRAINT `fk_e_platform_a_category1` FOREIGN KEY (`category`) REFERENCES `a_category` (`id`),
  CONSTRAINT `fk_e_platform_e_employee1` FOREIGN KEY (`ppm`) REFERENCES `e_employee` (`id`),
  CONSTRAINT `fk_e_platform_e_platform_family1` FOREIGN KEY (`platform_family_id`) REFERENCES `e_platform_family` (`id`)
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
  `name` varchar(45) DEFAULT NULL,
  `create_Date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
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
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
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
  `id` int NOT NULL,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `pm` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `alpha_project` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_e_project_e_employee1_idx` (`pm`),
  CONSTRAINT `fk_e_project_e_employee1` FOREIGN KEY (`pm`) REFERENCES `e_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `version` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `ta_id` int DEFAULT NULL,
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
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
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
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `test_description` varchar(2048) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`operator_id`,`version_no`,`test_id`),
  KEY `fk_e_test_plan_e_compliance_version1_idx` (`version_no`,`operator_id`),
  CONSTRAINT `fk_e_test_plan_e_compliance_version1` FOREIGN KEY (`version_no`, `operator_id`) REFERENCES `e_compliance_version` (`version_no`, `operator_id`)
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
  `requirement_operator_id` int NOT NULL,
  `requirement_version_no` varchar(45) NOT NULL,
  `requirement_id` int NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`requirement_operator_id`,`requirement_version_no`,`requirement_id`,`category_id`),
  KEY `fk_e_requirement_category_has_e_device_requirement_e_requir_idx` (`category_id`),
  CONSTRAINT `fk_e_requirement_category_has_e_device_requirement_e_device_r1` FOREIGN KEY (`requirement_operator_id`, `requirement_version_no`, `requirement_id`) REFERENCES `e_device_requirement` (`operator_id`, `version_no`, `id`),
  CONSTRAINT `fk_e_requirement_category_has_e_device_requirement_e_requirem1` FOREIGN KEY (`category_id`) REFERENCES `e_requirement_category` (`id`)
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
  `milestone_category` int NOT NULL,
  `plan_start_dt` date DEFAULT NULL,
  `plan_end_dt` date DEFAULT NULL,
  `actual_start_dt` date DEFAULT NULL,
  `actual_end_dt` date DEFAULT NULL,
  PRIMARY KEY (`product_id`,`milestone_id`,`milestone_category`),
  KEY `fk_e_milestone_has_e_product_e_product1_idx` (`product_id`),
  KEY `fk_e_milestone_has_e_product_e_milestone1_idx` (`milestone_id`,`milestone_category`),
  CONSTRAINT `fk_e_milestone_has_e_product_e_milestone1` FOREIGN KEY (`milestone_id`, `milestone_category`) REFERENCES `e_milestone` (`milestone_id`, `category_id`),
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
  PRIMARY KEY (`customer_id`,`project_id`),
  KEY `fk_e_customer_has_e_project_e_project1_idx` (`project_id`),
  KEY `fk_e_customer_has_e_project_e_customer1_idx` (`customer_id`),
  CONSTRAINT `fk_e_customer_has_e_project_e_customer1` FOREIGN KEY (`customer_id`) REFERENCES `e_customer` (`id`),
  CONSTRAINT `fk_e_customer_has_e_project_e_project1` FOREIGN KEY (`project_id`) REFERENCES `e_project` (`id`)
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
  `version` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
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
  PRIMARY KEY (`project_id`,`platform_id`),
  KEY `fk_e_project_has_e_platform_e_platform1_idx` (`platform_id`),
  KEY `fk_e_project_has_e_platform_e_project1_idx` (`project_id`),
  CONSTRAINT `fk_e_project_has_e_platform_e_platform1` FOREIGN KEY (`platform_id`) REFERENCES `e_platform` (`id`),
  CONSTRAINT `fk_e_project_has_e_platform_e_project1` FOREIGN KEY (`project_id`) REFERENCES `e_project` (`id`)
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
  `milestone_category` int NOT NULL,
  `plan_start_dt` date DEFAULT NULL,
  `plan_end_dt` date DEFAULT NULL,
  `actual_start_dt` date DEFAULT NULL,
  `actual_end_dt` date DEFAULT NULL,
  `note` longtext,
  `create_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`project_id`,`milestone_id`,`milestone_category`),
  KEY `fk_e_project_has_e_milestone_e_project1_idx` (`project_id`),
  KEY `fk_e_project_has_e_milestone_e_milestone1_idx` (`milestone_id`,`milestone_category`),
  CONSTRAINT `fk_e_project_has_e_milestone_e_milestone1` FOREIGN KEY (`milestone_id`, `milestone_category`) REFERENCES `e_milestone` (`milestone_id`, `category_id`),
  CONSTRAINT `fk_e_project_has_e_milestone_e_project1` FOREIGN KEY (`project_id`) REFERENCES `e_project` (`id`)
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
  CONSTRAINT `fk_e_technical_acceptance_has_e_device_requirement_e_device_r1` FOREIGN KEY (`operator_id`, `version_no`, `requirement_id`) REFERENCES `e_device_requirement` (`operator_id`, `version_no`, `id`),
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
  KEY `fk_e_device_requirement_has_e_test_plan_e_device_requiremen_idx` (`operator_id`,`version_no`,`requirement_id`),
  KEY `fk_e_device_requirement_has_e_test_plan_e_test_plan1_idx` (`operator_id`,`version_no`,`test_id`),
  CONSTRAINT `fk_e_device_requirement_has_e_test_plan_e_device_requirement1` FOREIGN KEY (`operator_id`, `version_no`, `requirement_id`) REFERENCES `e_device_requirement` (`operator_id`, `version_no`, `id`),
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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-19  9:47:40
