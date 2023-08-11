-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: vista2
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `cview_services_master`
--

DROP TABLE IF EXISTS `cview_services_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cview_services_master` (
  `CV_Service_ID` int NOT NULL AUTO_INCREMENT,
  `Cv_Service_Name` varchar(45) NOT NULL,
  `Cv_Service_Description` varchar(45) DEFAULT NULL,
  `Created_By` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Visa_Location` varchar(45) DEFAULT NULL,
  `Service_Amount` float NOT NULL,
  PRIMARY KEY (`CV_Service_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=440 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Service master shall have the data about the services we are offering to our customer there shall be a sub master for further division of services';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cview_services_master`
--

LOCK TABLES `cview_services_master` WRITE;
/*!40000 ALTER TABLE `cview_services_master` DISABLE KEYS */;
INSERT INTO `cview_services_master` VALUES (432,'experience 0-1 years','package description','admin','2023-02-24 12:02:11',NULL,3111),(433,'experience 1-5 years','package description','admin','2023-02-24 12:02:11',NULL,4000),(434,'experience 5-10 years','package description','admin','2023-02-24 12:02:11',NULL,5500),(435,'experience 10+ years','package description','admin','2023-02-24 12:02:11',NULL,6560),(436,'student-undergraduation','package description','admin','2023-02-24 12:02:11',NULL,4200),(437,'student-graduation','package description','admin','2023-02-24 12:02:11',NULL,5150),(438,'student-phd/mba/doctorate','package description','admin','2023-02-24 12:02:11',NULL,5800),(439,'visa application','package description','admin','2023-02-24 12:02:11',NULL,6200);
/*!40000 ALTER TABLE `cview_services_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `idfeedback` int NOT NULL,
  `platform` varchar(45) DEFAULT NULL,
  `visit_again` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `rating` int DEFAULT NULL,
  `feedback_editor` varchar(45) DEFAULT NULL,
  `feedback_website` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idfeedback`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,'google','yes','mohan@gmail.com',4,'',''),(2,'friend','yes','kiran@gmail.com',10,'Did an excellent job','Good');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_ats_score`
--

DROP TABLE IF EXISTS `tbl_ats_score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_ats_score` (
  `Ats_Score_Id` int NOT NULL AUTO_INCREMENT,
  `Ats_Score_Parameter` varchar(45) NOT NULL,
  `Ats_Score_Operator` varchar(2) NOT NULL,
  `Ats_Score_Value` float NOT NULL,
  `Created_By` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL,
  PRIMARY KEY (`Ats_Score_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This table stores + or - value parameters for calculating the ats score';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_ats_score`
--

LOCK TABLES `tbl_ats_score` WRITE;
/*!40000 ALTER TABLE `tbl_ats_score` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_ats_score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_history_resume`
--

DROP TABLE IF EXISTS `tbl_history_resume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_history_resume` (
  `Resume_History_Id` int NOT NULL AUTO_INCREMENT,
  `Resume_Identifier` varchar(45) NOT NULL COMMENT 'This we insert like where from we stored \n1. ATS\n2. Completed\n3. In process and sent to customer\n',
  `User_Id` int NOT NULL,
  `Created_By` int NOT NULL COMMENT 'this is foreignkey from tbl_user_master user id\n',
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'system date',
  PRIMARY KEY (`Resume_History_Id`),
  KEY `User_ID_idx` (`User_Id`),
  KEY `created_by_idx` (`Created_By`),
  CONSTRAINT `created_by` FOREIGN KEY (`Created_By`) REFERENCES `tbl_user_master` (`User_Id`),
  CONSTRAINT `User_ID` FOREIGN KEY (`User_Id`) REFERENCES `tbl_user_master` (`User_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='All history resumes stored as PDF';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_history_resume`
--

LOCK TABLES `tbl_history_resume` WRITE;
/*!40000 ALTER TABLE `tbl_history_resume` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_history_resume` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_report1_temp`
--

DROP TABLE IF EXISTS `tbl_report1_temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_report1_temp` (
  `User_First_Name` varchar(45) DEFAULT NULL,
  `User_Id` int DEFAULT NULL,
  `Records_assigned` int DEFAULT '0',
  `User_Last_Name` varchar(45) DEFAULT NULL,
  `User_eMail` varchar(45) DEFAULT NULL,
  `User_Mobile` bigint DEFAULT NULL,
  `status_id` int DEFAULT NULL,
  `role_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_report1_temp`
--

LOCK TABLES `tbl_report1_temp` WRITE;
/*!40000 ALTER TABLE `tbl_report1_temp` DISABLE KEYS */;
INSERT INTO `tbl_report1_temp` VALUES ('sagar',101,2,'munjam','sagar@gmail.com',9652502657,7,2),('srinivas',100,0,'c','srinuc@gmail.com',9000000000,2,2),('sagar',101,0,'munjam','sagar@gmail.com',9652502657,2,2),('karthik',102,0,'swaminathan','contact@karthikswaminathan.com',8096675401,2,2);
/*!40000 ALTER TABLE `tbl_report1_temp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_resume`
--

DROP TABLE IF EXISTS `tbl_resume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_resume` (
  `Resume_Id` int NOT NULL AUTO_INCREMENT COMMENT 'It is auto generated number. May be used to created just resume ID',
  `User_Id` int NOT NULL COMMENT 'Foreign key with tbl_user_master',
  `Status_ID` int NOT NULL COMMENT 'column used as foreign key from Status Table',
  `Assign_to` int NOT NULL COMMENT 'this is  basically user_id of Internal Users',
  `Assigned_By` int NOT NULL COMMENT 'This column is also foreign key to tbl_user_master table',
  `Assigned_Date_Time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Previous_Status` int NOT NULL COMMENT 'Previous status is status ID from Status table',
  `comments` varchar(100) DEFAULT NULL,
  `package_id` int NOT NULL DEFAULT '432',
  PRIMARY KEY (`Resume_Id`),
  KEY `Resume_Userid_idx` (`User_Id`),
  KEY `Assigned_by_user_idx` (`Assigned_By`),
  KEY `Assigned_to_user_idx` (`Assign_to`),
  KEY `Current_Status_idx` (`Status_ID`),
  KEY `Previous_Status_idx` (`Previous_Status`),
  CONSTRAINT `Assigned_by_user` FOREIGN KEY (`Assigned_By`) REFERENCES `tbl_user_master` (`User_Id`),
  CONSTRAINT `Assigned_to_user` FOREIGN KEY (`Assign_to`) REFERENCES `tbl_user_master` (`User_Id`),
  CONSTRAINT `Current_Status` FOREIGN KEY (`Status_ID`) REFERENCES `tbl_resume_status` (`Status_Id`),
  CONSTRAINT `Previous_Status` FOREIGN KEY (`Previous_Status`) REFERENCES `tbl_resume_status` (`Status_Id`),
  CONSTRAINT `Resume_Userid` FOREIGN KEY (`User_Id`) REFERENCES `tbl_user_master` (`User_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=1027 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This table is created to have Resume and its status';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_resume`
--

LOCK TABLES `tbl_resume` WRITE;
/*!40000 ALTER TABLE `tbl_resume` DISABLE KEYS */;
INSERT INTO `tbl_resume` VALUES (1026,1,2,200,300,'2023-02-24 15:13:54',11,NULL,434);
/*!40000 ALTER TABLE `tbl_resume` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_resume_status`
--

DROP TABLE IF EXISTS `tbl_resume_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_resume_status` (
  `Status_Id` int NOT NULL AUTO_INCREMENT,
  `Status_Description` varchar(45) NOT NULL,
  `Status_time` int NOT NULL COMMENT 'Please specify how many days the resume can be in this status. for example assign to editor shall have only 14 hours then trigger to fire. ',
  `Created_by` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'is the system date and time',
  PRIMARY KEY (`Status_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_resume_status`
--

LOCK TABLES `tbl_resume_status` WRITE;
/*!40000 ALTER TABLE `tbl_resume_status` DISABLE KEYS */;
INSERT INTO `tbl_resume_status` VALUES (1,'form filling',48,'admin','2023-02-20 11:51:55'),(2,'pending for assignment',12,'admin','2023-02-20 11:51:55'),(3,'pending for acceptance',12,'admin','2023-02-20 11:51:55'),(4,'pending for editing',48,'admin','2023-02-20 11:51:55'),(5,'editing in progress',48,'admin','2023-02-20 11:51:55'),(6,'pending for review',48,'admin','2023-02-20 11:51:55'),(7,'completed',72,'admin','2023-02-20 11:51:55'),(10,'package',80,'admin','2023-02-20 11:51:55'),(11,'registered',180,'admin','2023-02-20 11:51:55');
/*!40000 ALTER TABLE `tbl_resume_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_role_master`
--

DROP TABLE IF EXISTS `tbl_role_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_role_master` (
  `Role_ID` int NOT NULL AUTO_INCREMENT,
  `Role_Description` varchar(45) NOT NULL,
  `Role_Assign_ScreenIDs` varchar(45) DEFAULT NULL,
  `Created_By` varchar(45) NOT NULL DEFAULT 'ADMIN',
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Role_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Create Roles Screen ID column is future use to add logic for assigning any particular screens';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_role_master`
--

LOCK TABLES `tbl_role_master` WRITE;
/*!40000 ALTER TABLE `tbl_role_master` DISABLE KEYS */;
INSERT INTO `tbl_role_master` VALUES (1,'customer','user1','ADMIN','2023-02-17 17:32:13'),(2,'editor','user2','ADMIN','2023-02-17 17:32:13'),(3,'super editor','user3','ADMIN','2023-02-17 17:32:13'),(4,'admin','user4','ADMIN','2023-02-17 17:32:13');
/*!40000 ALTER TABLE `tbl_role_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_screens`
--

DROP TABLE IF EXISTS `tbl_screens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_screens` (
  `User_Screen_Id` int NOT NULL AUTO_INCREMENT,
  `User_Screen_Name` varchar(45) NOT NULL,
  `Created_By` varchar(45) DEFAULT NULL,
  `Created_Date` datetime DEFAULT NULL,
  PRIMARY KEY (`User_Screen_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This shall allow CEO level to assign screens example if internal user wants to use customer entry screen he should be able to do it';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_screens`
--

LOCK TABLES `tbl_screens` WRITE;
/*!40000 ALTER TABLE `tbl_screens` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_screens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_un_registered_user`
--

DROP TABLE IF EXISTS `tbl_un_registered_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_un_registered_user` (
  `Ur_User_Id` int NOT NULL AUTO_INCREMENT,
  `Ur_User_Name` varchar(45) DEFAULT NULL,
  `Ur_User_Mobile` bigint DEFAULT NULL,
  `Ur_eMail` varchar(45) NOT NULL,
  `Ur_Resume` longblob COMMENT 'Uploads his resume',
  `Created_By` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Ur_User_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This table is to handle Un registered user who comes to check their ATS. He may opt for our services and we need to move them into regular user later.\nThere will not be any user name and password for this person.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_un_registered_user`
--

LOCK TABLES `tbl_un_registered_user` WRITE;
/*!40000 ALTER TABLE `tbl_un_registered_user` DISABLE KEYS */;
INSERT INTO `tbl_un_registered_user` VALUES (1,NULL,NULL,'pothurajulakarthik50@gmail.com',NULL,'pothurajulakarthik50@gmail.com','2023-02-23 12:35:06');
/*!40000 ALTER TABLE `tbl_un_registered_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_activities`
--

DROP TABLE IF EXISTS `tbl_user_activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_activities` (
  `User_Activity_Id` int NOT NULL AUTO_INCREMENT,
  `User_ID` int NOT NULL,
  `User_Activity_name` varchar(45) DEFAULT NULL,
  `User_Activity_Description` varchar(1000) DEFAULT NULL,
  `User_Awards` varchar(1000) DEFAULT NULL,
  `User_Papers_Submitted` varchar(1000) DEFAULT NULL,
  `User_AnyOther_Information` varchar(1000) DEFAULT NULL,
  `User_Languages_Known` varchar(45) DEFAULT NULL,
  `User_Known_Tools` varchar(45) DEFAULT NULL COMMENT 'Fill any tools if he known may be software or Hardware',
  `User_Known_Computer_Languages` varchar(45) DEFAULT NULL COMMENT 'any software languages hardware and software boath',
  `tbl_user_activitiescol` varchar(45) DEFAULT NULL,
  `Created_By` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`User_Activity_Id`),
  KEY `User_Activities_masterID_idx` (`User_ID`),
  CONSTRAINT `User_Activities_masterID` FOREIGN KEY (`User_ID`) REFERENCES `tbl_user_master` (`User_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='User inputs of any activity shall be stored here.\n1. Indoor 2.outdoor 3.sports 4.Games 5.Papers 6.Awards 7.Clubs';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_activities`
--

LOCK TABLES `tbl_user_activities` WRITE;
/*!40000 ALTER TABLE `tbl_user_activities` DISABLE KEYS */;
INSERT INTO `tbl_user_activities` VALUES (1,1,'travelling','i love travelling','','','','','','','','1','2023-02-24 15:53:24'),(2,302,'singing','','','','','','','','','302','2023-02-23 12:41:34');
/*!40000 ALTER TABLE `tbl_user_activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_education`
--

DROP TABLE IF EXISTS `tbl_user_education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_education` (
  `Education_Id` int NOT NULL AUTO_INCREMENT,
  `User_Id` int NOT NULL,
  `User_Education` varchar(45) NOT NULL,
  `User_Education_Inistitute_Name` varchar(45) NOT NULL,
  `User_Educatin_Inistitute_City` varchar(45) NOT NULL,
  `User_Educatin_Inistitute_Country` varchar(45) NOT NULL,
  `User_Education_Grade_Percentage` varchar(4) NOT NULL,
  `User_Education_Passout_Start_Date` date NOT NULL,
  `User_Education_Passout_End_Year` date DEFAULT NULL,
  `User_Education_Mode` varchar(45) NOT NULL DEFAULT 'Online; Regular',
  `Created_By` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Education_Id`),
  KEY `User_Master_UserID_idx` (`User_Id`),
  CONSTRAINT `User_Master_UserID` FOREIGN KEY (`User_Id`) REFERENCES `tbl_user_master` (`User_Id`) ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This table is created for storing Customer Education Details. The user ID is foreign key referred to Tbl_User_Master';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_education`
--

LOCK TABLES `tbl_user_education` WRITE;
/*!40000 ALTER TABLE `tbl_user_education` DISABLE KEYS */;
INSERT INTO `tbl_user_education` VALUES (1,1,'ssc','zphs','Mancherial','India','80','2022-01-01','2022-01-01','offline','1','2023-02-24 15:53:24'),(2,302,'ssc','th','h','hh','H','2022-01-01','2022-01-01','FTH','302','2023-02-23 12:41:33');
/*!40000 ALTER TABLE `tbl_user_education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_experience`
--

DROP TABLE IF EXISTS `tbl_user_experience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_experience` (
  `User_Exp_ID` int NOT NULL AUTO_INCREMENT,
  `User_Id` int NOT NULL,
  `User_Work_Exp_Company` varchar(45) DEFAULT NULL,
  `User_Work_Exp_Disignation` varchar(45) DEFAULT NULL,
  `User_Work_Exp_From_Date` date DEFAULT NULL,
  `User_Work_Exp_To_Date` date DEFAULT NULL,
  `User_Exp_Type` varchar(45) NOT NULL DEFAULT 'Virtual; Internship; Training; Regular Job' COMMENT 'The column should be a drop down to select the kind of work / project experience.',
  `Created_By` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`User_Exp_ID`),
  KEY `User_Exp_User_Id_Master_Userid_idx` (`User_Id`),
  CONSTRAINT `User_Exp_User_Id_Master_Userid` FOREIGN KEY (`User_Id`) REFERENCES `tbl_user_master` (`User_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This table sotres data regarding user experience';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_experience`
--

LOCK TABLES `tbl_user_experience` WRITE;
/*!40000 ALTER TABLE `tbl_user_experience` DISABLE KEYS */;
INSERT INTO `tbl_user_experience` VALUES (1,1,'vista','developer','2022-01-01','2022-01-01','fresher','1','2023-02-24 15:53:24'),(2,302,'vista','developer','2022-01-01','2022-01-01','','302','2023-02-23 12:41:33');
/*!40000 ALTER TABLE `tbl_user_experience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_master`
--

DROP TABLE IF EXISTS `tbl_user_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_master` (
  `User_Id` int NOT NULL AUTO_INCREMENT,
  `User_Type` varchar(45) NOT NULL DEFAULT 'Customer, Internal',
  `User_Role` int NOT NULL,
  `User_Last_Name` varchar(45) NOT NULL,
  `User_First_Name` varchar(45) DEFAULT NULL,
  `User_Middle_Name` varchar(45) DEFAULT NULL,
  `User_eMail` varchar(45) NOT NULL,
  `User_Mobile_Number` bigint NOT NULL,
  `User_Alternative_Number` bigint DEFAULT NULL,
  `Created_By` varchar(45) NOT NULL DEFAULT 'admin',
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `User_Password` varchar(45) NOT NULL DEFAULT 'password',
  PRIMARY KEY (`User_Id`),
  UNIQUE KEY `User_Id_UNIQUE` (`User_Id`),
  KEY `Role_master_id_idx` (`User_Role`),
  CONSTRAINT `Role_master_id` FOREIGN KEY (`User_Role`) REFERENCES `tbl_role_master` (`Role_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=307 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This is a User Master table where initial details shall be stored';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_master`
--

LOCK TABLES `tbl_user_master` WRITE;
/*!40000 ALTER TABLE `tbl_user_master` DISABLE KEYS */;
INSERT INTO `tbl_user_master` VALUES (1,'customer',1,'Alli','Ramesh','None','alliramesh1990@gmail.com',91985855890,8096675401,'admin','2023-02-24 15:53:24','password'),(2,'customer',1,'V','SAIRAMA','CHAITANYA','ram9151@gmail.com',9866323870,NULL,'admin','2023-02-17 17:33:28','password'),(3,'customer',1,'Pathak','Omkar','None','omkarpathak27@gmail.com',8087996634,NULL,'admin','2023-02-17 17:33:28','password'),(4,'customer',1,'Nakka','Geetha','Sree','geethasri719@gmail.com',9390707130,NULL,'admin','2023-02-17 17:33:28','password'),(6,'customer',1,'pothurajula','charan',NULL,'charan@gmail.com',7032648102,NULL,'admin','2023-02-17 17:33:28','password'),(7,'customer',1,'pothurajula','mounika','None','mounika2222@gmail.com',9121517326,NULL,'admin','2023-02-17 17:33:28','password'),(8,'customer',1,'swaminathan','sirisha',NULL,'sirishaswaminathan@gmail.com',9346828042,NULL,'admin','2023-02-17 17:33:28','password'),(9,'customer',1,'j','chatrapathi',NULL,'chatrapathi.j@gmail.com',9121517540,NULL,'admin','2023-02-17 17:33:28','password'),(10,'customer',1,'peddy','pavan',NULL,'peddypavan@gmail.com',8688928043,NULL,'admin','2023-02-17 17:33:28','password'),(11,'customer',1,'bathuka','shankar',NULL,'shankarbathuka@gmail.com',7032675401,NULL,'admin','2023-02-17 17:33:28','password'),(12,'customer',1,'bhukya','raja',NULL,'raja@gmail.com',9123478945,NULL,'admin','2023-02-17 17:33:28','password'),(13,'customer',1,'md','shakeel',NULL,'shakeelmd12@gmail.com',8456129876,NULL,'admin','2023-02-17 17:33:28','password'),(14,'customer',1,'thangella','vinay','None','vinayvinnu@gmail.com',7894532165,NULL,'admin','2023-02-17 17:33:28','password'),(15,'customer',1,'mm','mohan',NULL,'mohan@vistaispl.com',7894512365,NULL,'admin','2023-02-17 17:33:28','password'),(16,'customer',1,'kotrange','srikanth',NULL,'srik.k@gmail.com',8456998725,NULL,'admin','2023-02-17 17:33:28','password'),(17,'customer',1,'yadav','manoj',NULL,'manoj@gmail.com',7984548965,NULL,'admin','2023-02-17 17:33:28','password'),(18,'customer',1,'krishna','vamshi','None','vamshikrishna@gmail.com',9876514256,NULL,'admin','2023-02-17 17:33:28','password'),(19,'customer',1,'sai','venkat','None','saivenkat@gmail.com',6281789654,NULL,'admin','2023-02-17 17:33:28','password'),(20,'customer',1,'marripalli','lavanya',NULL,'lavanya@gmail.com',6281521593,NULL,'admin','2023-02-17 17:33:28','password'),(21,'customer',1,'v','kavitha',NULL,'kavithav@gmail.com',7896541234,NULL,'admin','2023-02-17 17:33:28','password'),(100,'editor',2,'c','srinivas',NULL,'srinuc@gmail.com',9000000000,NULL,'admin','2023-02-17 17:33:28','password'),(101,'editor',2,'munjam','sagar',NULL,'sagar@gmail.com',9652502657,NULL,'admin','2023-02-17 17:33:28','password'),(102,'editor',2,'swaminathan','karthik',NULL,'contact@karthikswaminathan.com',8096675401,NULL,'admin','2023-02-17 17:33:28','password'),(200,'super editor',3,'n','moorthy',NULL,'moorthy@gmail.com',9000000001,NULL,'admin','2023-02-17 17:33:28','password'),(300,'admin',4,'agarwal','chavi',NULL,'chaviagarwal@gmail.com',9123456987,NULL,'admin','2023-02-17 17:33:28','password'),(301,'customer',1,'pothurajula','sravan','kumar','sravanp@gmail.com',6302811345,NULL,'admin','2023-02-17 17:33:28','password'),(302,'customer',1,'krishna','hari','','hari@gmail.com',9121519875,789456123,'admin','2023-02-17 17:33:28','password'),(303,'customer',1,'saashtri','vijay','kumar','vijay@gmail.com',8096675401,NULL,'admin','2023-02-17 17:33:28','password'),(304,'customer',1,'bhargav','charan','','charanbhargav@gmail.com',7032648102,NULL,'admin','2023-02-17 17:33:28','password'),(305,'customer',1,'s','abhi','kumar','abhi@gmail.com',8465067895,NULL,'admin','2023-02-17 17:33:28','password'),(306,'customer',1,'naidu','prashanthi','','prashanthi@gmail.com',7032648102,NULL,'admin','2023-02-17 17:33:28','password');
/*!40000 ALTER TABLE `tbl_user_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_prof`
--

DROP TABLE IF EXISTS `tbl_user_prof`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_prof` (
  `User_Prof_Id` int NOT NULL AUTO_INCREMENT,
  `User_id` int NOT NULL,
  `User_Prof_summary` varchar(1000) DEFAULT NULL,
  `User_Profcol` varchar(45) DEFAULT NULL,
  `Created_By` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`User_Prof_Id`),
  KEY `Prof_User_link_user_master_idx` (`User_id`),
  CONSTRAINT `Prof_User_link_user_master` FOREIGN KEY (`User_id`) REFERENCES `tbl_user_master` (`User_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This table is to store profissional summary of user';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_prof`
--

LOCK TABLES `tbl_user_prof` WRITE;
/*!40000 ALTER TABLE `tbl_user_prof` DISABLE KEYS */;
INSERT INTO `tbl_user_prof` VALUES (1,1,'i have 3 years of carreer in the it and worked on AI and ML',NULL,'1','2023-02-24 15:53:24'),(2,302,'i have 3 years of carreer in the it and worked on AI and ML',NULL,'302','2023-02-23 12:41:34');
/*!40000 ALTER TABLE `tbl_user_prof` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_projects`
--

DROP TABLE IF EXISTS `tbl_user_projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_projects` (
  `User_Project_ID` int NOT NULL AUTO_INCREMENT,
  `User_ID` int NOT NULL,
  `User_Project_Title` varchar(45) DEFAULT NULL,
  `User_Role_Responsibilities` varchar(1000) DEFAULT NULL,
  `User_Technology_Used` varchar(45) DEFAULT NULL,
  `User_Project_Description` varchar(1000) DEFAULT NULL,
  `User_Project_client` varchar(45) DEFAULT NULL,
  `User_Project_Start_Date` date DEFAULT NULL,
  `User_Project_End_Date` date DEFAULT NULL,
  `Created_By` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`User_Project_ID`),
  KEY `User_Projects_User_Id_User_masterid_idx` (`User_ID`),
  CONSTRAINT `User_Projects_User_Id_User_masterid` FOREIGN KEY (`User_ID`) REFERENCES `tbl_user_master` (`User_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This table stores data about the user projects - multiples';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_projects`
--

LOCK TABLES `tbl_user_projects` WRITE;
/*!40000 ALTER TABLE `tbl_user_projects` DISABLE KEYS */;
INSERT INTO `tbl_user_projects` VALUES (1,1,'web ecommerce','intern','AI-ML-NLP','major project in college','college','2022-01-01','2022-01-01','1','2023-02-24 15:53:24'),(2,302,'major','leader','','major project in college','group','2022-01-01','2022-01-01','302','2023-02-23 12:41:33');
/*!40000 ALTER TABLE `tbl_user_projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_scocial_media`
--

DROP TABLE IF EXISTS `tbl_user_scocial_media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_scocial_media` (
  `User_SocMedia_Id` int NOT NULL AUTO_INCREMENT,
  `User_id` int NOT NULL,
  `User_ScMedia_Description` varchar(45) DEFAULT 'Twitter, LinkDin',
  `User_ScMedia_link` varchar(45) DEFAULT NULL,
  `Created_By` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`User_SocMedia_Id`),
  KEY `User_ScMedia_User_Master_id_idx` (`User_id`),
  CONSTRAINT `User_ScMedia_User_Master_id` FOREIGN KEY (`User_id`) REFERENCES `tbl_user_master` (`User_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This table stores data regarding the Social Media links like linkdin, twitter, facebook...etc';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_scocial_media`
--

LOCK TABLES `tbl_user_scocial_media` WRITE;
/*!40000 ALTER TABLE `tbl_user_scocial_media` DISABLE KEYS */;
INSERT INTO `tbl_user_scocial_media` VALUES (1,1,'instagram','thehimalayandreamer','1','2023-02-24 15:53:24'),(2,302,'instagram','FTUFT','302','2023-02-23 12:41:34');
/*!40000 ALTER TABLE `tbl_user_scocial_media` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_tech_skills`
--

DROP TABLE IF EXISTS `tbl_user_tech_skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_tech_skills` (
  `Tech_Skills_ID` int NOT NULL AUTO_INCREMENT,
  `User_Id` int NOT NULL,
  `Tech_Skill_Description` varchar(100) DEFAULT NULL,
  `Created_By` varchar(45) NOT NULL,
  `Created_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Tech_Skills_ID`),
  KEY `User_tech-skills_user_master_idx` (`User_Id`),
  CONSTRAINT `User_tech-skills_user_master` FOREIGN KEY (`User_Id`) REFERENCES `tbl_user_master` (`User_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This table stores data regarding individual user Technical Skills';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_tech_skills`
--

LOCK TABLES `tbl_user_tech_skills` WRITE;
/*!40000 ALTER TABLE `tbl_user_tech_skills` DISABLE KEYS */;
INSERT INTO `tbl_user_tech_skills` VALUES (1,1,'django expert','1','2023-02-24 15:53:24'),(2,302,'django expert','302','2023-02-23 12:41:34');
/*!40000 ALTER TABLE `tbl_user_tech_skills` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-27 10:22:13
