CREATE DATABASE  IF NOT EXISTS `bdveterinaria` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bdveterinaria`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bdveterinaria
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `dni` int NOT NULL,
  `apellido` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nombre` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Direccion` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `telefono` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `estado` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`dni`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (12873501,'Platini','Maria Jose','Bv Ocampo 327','3515164899','santiagosmania@hotmail.com','deshabilitado'),(12873502,'Smania','Santiago','Bv Ocampo 327','3515164899','santiago.smania@gmail.com','habilitado'),(12873503,'Smania','Santiago','Bv Ocampo 327','3515164899','santiagosmania@hotmail.com','habilitado'),(12873506,'Smania','Santiago','Bv Ocampo 327','3515164899','santiagosmania@hotmail.com','habilitado'),(12873507,'Smania','Santiago','Bv Ocampo 327','3515164899','santiagosmania@hotmail.com','habilitado'),(43811733,'Smania','Santiago','Bv Ocampo 327','3515164899','santiagosmania@hotmail.com','habilitado'),(43811734,'SMANIA','Moreno','Bv Ocampo 327','2147483647','santiagosmania@hotmail.com','habilitado'),(89488196,'','','','0','','');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especies`
--

DROP TABLE IF EXISTS `especies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especies` (
  `idespecie` int NOT NULL AUTO_INCREMENT,
  `especie` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `idraza` int NOT NULL,
  PRIMARY KEY (`idespecie`),
  KEY `idraza` (`idraza`),
  CONSTRAINT `especies_ibfk_1` FOREIGN KEY (`idraza`) REFERENCES `razas` (`idraza`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especies`
--

LOCK TABLES `especies` WRITE;
/*!40000 ALTER TABLE `especies` DISABLE KEYS */;
INSERT INTO `especies` VALUES (1,'siames',1),(2,'Bulldog Ingles',3),(3,'Árabe',2),(4,'caniche',3),(5,'Pug',3),(6,'Bulldog Frances',3),(7,'Boxer',3),(8,'Criollo',3),(9,'Criollo',1),(10,'Persa',1),(11,'Birmano',1),(12,' Himalayo',1);
/*!40000 ALTER TABLE `especies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `examenclinico`
--

DROP TABLE IF EXISTS `examenclinico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `examenclinico` (
  `idexamenc` int NOT NULL AUTO_INCREMENT,
  `ganglios` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `mucosas` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `temperatura` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `cardiaca` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `pulso` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `respiratoria` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`idexamenc`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examenclinico`
--

LOCK TABLES `examenclinico` WRITE;
/*!40000 ALTER TABLE `examenclinico` DISABLE KEYS */;
INSERT INTO `examenclinico` VALUES (1,'alta','n','alta','alta','alta','normal'),(2,'alta','n','alta','alta','alta','normal'),(3,'alta','n','alta','alta','alta','normal'),(4,'alta','normal','normal','alta','alta','normal'),(5,'alta','n','alta','alta','alta','normal'),(6,'alta','n','alta','alta','alta','normal'),(7,'alta','n','alta','alta','alta','normal'),(8,'alta','n','alta','alta','alta','alta'),(9,'alta','normal','alta','alta','alta','normal');
/*!40000 ALTER TABLE `examenclinico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial`
--

DROP TABLE IF EXISTS `historial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial` (
  `idhistorial` int NOT NULL AUTO_INCREMENT,
  `idpaciente_id` int NOT NULL,
  `fechadesp` date NOT NULL,
  `productodesp` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `idvacuna` int NOT NULL,
  `lotev` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fechacelo` date NOT NULL,
  `fechapart` date NOT NULL,
  `estirilizado` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `consulta` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `hallazgo` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `idexamenc` int NOT NULL,
  `idpeso` int NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`idhistorial`),
  KEY `idpaciente` (`idpaciente_id`),
  KEY `idvacuna` (`idvacuna`),
  KEY `idexamenc` (`idexamenc`),
  KEY `idpeso` (`idpeso`),
  CONSTRAINT `historial_ibfk_1` FOREIGN KEY (`idpeso`) REFERENCES `peso` (`idpeso`) ON UPDATE CASCADE,
  CONSTRAINT `historial_ibfk_2` FOREIGN KEY (`idvacuna`) REFERENCES `vacunas` (`idvacuna`) ON UPDATE CASCADE,
  CONSTRAINT `historial_ibfk_3` FOREIGN KEY (`idexamenc`) REFERENCES `examenclinico` (`idexamenc`) ON UPDATE CASCADE,
  CONSTRAINT `historial_ibfk_4` FOREIGN KEY (`idpaciente_id`) REFERENCES `pacientes` (`idpaciente`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial`
--

LOCK TABLES `historial` WRITE;
/*!40000 ALTER TABLE `historial` DISABLE KEYS */;
INSERT INTO `historial` VALUES (1,1,'2024-02-20','kkk',1,'1100','2024-02-20','2023-02-20','si','sdf','sadf',1,1,'2024-01-14'),(2,4,'2024-02-20','pipeta',1,'1200','2024-02-20','2023-02-20','si','sadf','                saf',2,2,'2024-01-14'),(3,5,'2024-02-20','kkk',1,'1100','2024-02-20','2023-02-20','si','dfs','   sdf',3,3,'2024-01-14'),(4,2,'2023-02-20','hello',1,'1500','2022-02-20','2022-02-20','si',' hola','    hola',4,4,'2024-01-14'),(5,2,'2026-02-20','kkk',1,'1100','2024-02-20','2023-02-20','si','sdf','    sdf',5,5,'2024-01-14'),(6,5,'2024-02-20','pipeta',1,'1100','2024-02-20','2023-02-20','si','sdf','sdaf',6,6,'2024-01-14'),(7,1,'2024-02-20','kkk',1,'1100','2024-02-20','2023-02-20','si','sf','saf',7,7,'2024-01-14'),(8,6,'2024-02-20','kkk',1,'1100','2024-02-20','2023-02-20','si','sad','     sdf',8,8,'2024-01-17'),(9,1,'2024-02-20','kkk',1,'1200','2024-02-20','2023-02-20','si','sadf','  sadf',9,9,'2024-01-28');
/*!40000 ALTER TABLE `historial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pacientes`
--

DROP TABLE IF EXISTS `pacientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pacientes` (
  `idpaciente` int NOT NULL AUTO_INCREMENT,
  `dni` int NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `idraza` int NOT NULL,
  `sexo` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `estado` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `seniaspart` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `chip` int DEFAULT NULL,
  `idespecie` int NOT NULL,
  `fechana` date NOT NULL,
  PRIMARY KEY (`idpaciente`),
  KEY `dni` (`dni`),
  KEY `idespecie` (`idespecie`),
  KEY `idraza` (`idraza`),
  CONSTRAINT `pacientes_ibfk_1` FOREIGN KEY (`idespecie`) REFERENCES `especies` (`idespecie`) ON UPDATE CASCADE,
  CONSTRAINT `pacientes_ibfk_3` FOREIGN KEY (`dni`) REFERENCES `clientes` (`dni`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pacientes`
--

LOCK TABLES `pacientes` WRITE;
/*!40000 ALTER TABLE `pacientes` DISABLE KEYS */;
INSERT INTO `pacientes` VALUES (1,89488196,'felix',1,'M','habilitado','mancha',0,1,'2000-10-20'),(2,43811734,'Romelin',3,'M','habilitado','mancha',250202,2,'2004-06-27'),(3,12873501,'Santiago',1,'M','habilitado','mancha',0,1,'2000-10-20'),(4,43811733,'tucha',3,'F','habilitado','mancha',250202,2,'2000-10-20'),(5,43811734,'tucha',1,'M','habilitado','mancha',250202,1,'2000-10-20'),(6,12873506,'nina',1,'M','habilitado','mancha',0,3,'2000-10-20');
/*!40000 ALTER TABLE `pacientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peso`
--

DROP TABLE IF EXISTS `peso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peso` (
  `idpeso` int NOT NULL AUTO_INCREMENT,
  `peso` decimal(65,0) NOT NULL,
  PRIMARY KEY (`idpeso`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peso`
--

LOCK TABLES `peso` WRITE;
/*!40000 ALTER TABLE `peso` DISABLE KEYS */;
INSERT INTO `peso` VALUES (1,24),(2,35),(3,29),(4,26),(5,29),(6,24),(7,24),(8,27),(9,25);
/*!40000 ALTER TABLE `peso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `razas`
--

DROP TABLE IF EXISTS `razas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `razas` (
  `idraza` int NOT NULL AUTO_INCREMENT,
  `raza` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`idraza`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `razas`
--

LOCK TABLES `razas` WRITE;
/*!40000 ALTER TABLE `razas` DISABLE KEYS */;
INSERT INTO `razas` VALUES (1,'felino'),(2,'equino'),(3,'caninos');
/*!40000 ALTER TABLE `razas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sesion`
--

DROP TABLE IF EXISTS `sesion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sesion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `DNI` int NOT NULL,
  `contrasena` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sesion`
--

LOCK TABLES `sesion` WRITE;
/*!40000 ALTER TABLE `sesion` DISABLE KEYS */;
INSERT INTO `sesion` VALUES (1,43811734,'pepito123'),(2,35529056,'peito11'),(3,35529056,'pepito123'),(4,36125534,'pepito123'),(5,35529057,'pepoit'),(6,35529058,'pepito123'),(7,43811730,'pepito12'),(8,35529052,'pepiot');
/*!40000 ALTER TABLE `sesion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `turnos`
--

DROP TABLE IF EXISTS `turnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turnos` (
  `dni` int NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `celular` bigint NOT NULL,
  `fecha` date NOT NULL,
  `hora` time(6) NOT NULL,
  `tipo` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `idturno` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idturno`),
  KEY `dni` (`dni`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turnos`
--

LOCK TABLES `turnos` WRITE;
/*!40000 ALTER TABLE `turnos` DISABLE KEYS */;
INSERT INTO `turnos` VALUES (43811734,'santiagosmania@hotmail.com',2147483647,'2023-10-20','10:00:00.000000','',2),(12873501,'santiago.smania@gmail.com',2147483647,'2023-10-19','11:00:00.000000','',3),(43811733,'santiago.smania@gmail.com',45419856196,'2024-01-17','09:00:00.000000','Normal',21),(12873501,'santiago.smania@gmail.com',45419856196,'2024-01-18','09:00:00.000000','Emergencia',22),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',23),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',24),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',25),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',26),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',27),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',28),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',29),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',30),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',31),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',32),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-18','15:30:00.000000','Normal',33),(43811733,'santiago.smania@gmail.com',45419856196,'2024-01-18','12:30:00.000000','Emergencia',34),(43811733,'santiago.smania@gmail.com',45419856196,'2024-01-18','12:30:00.000000','Emergencia',35),(43811733,'santiagosmania@hotmail.com',45419856196,'2024-01-11','09:00:00.000000','Normal',36),(43811733,'platinimariajose@gmail.com',45419856196,'2024-01-18','09:00:00.000000','Emergencia',37),(43556887,'edugil2001@gmail.com',3516512949,'2024-01-16','10:30:00.000000','Emergencia',38);
/*!40000 ALTER TABLE `turnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacunas`
--

DROP TABLE IF EXISTS `vacunas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacunas` (
  `idvacuna` int NOT NULL AUTO_INCREMENT,
  `laboratorio` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `vacuna` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`idvacuna`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacunas`
--

LOCK TABLES `vacunas` WRITE;
/*!40000 ALTER TABLE `vacunas` DISABLE KEYS */;
INSERT INTO `vacunas` VALUES (1,'pepito','quintuple');
/*!40000 ALTER TABLE `vacunas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-06 12:34:34
