/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - safekerala_final
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
USE `safekerala_final`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=81 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add criminal',7,'add_criminal'),
(26,'Can change criminal',7,'change_criminal'),
(27,'Can delete criminal',7,'delete_criminal'),
(28,'Can view criminal',7,'view_criminal'),
(29,'Can add labour',8,'add_labour'),
(30,'Can change labour',8,'change_labour'),
(31,'Can delete labour',8,'delete_labour'),
(32,'Can view labour',8,'view_labour'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add notification',10,'add_notification'),
(38,'Can change notification',10,'change_notification'),
(39,'Can delete notification',10,'delete_notification'),
(40,'Can view notification',10,'view_notification'),
(41,'Can add user',11,'add_user'),
(42,'Can change user',11,'change_user'),
(43,'Can delete user',11,'delete_user'),
(44,'Can view user',11,'view_user'),
(45,'Can add skill',12,'add_skill'),
(46,'Can change skill',12,'change_skill'),
(47,'Can delete skill',12,'delete_skill'),
(48,'Can view skill',12,'view_skill'),
(49,'Can add review',13,'add_review'),
(50,'Can change review',13,'change_review'),
(51,'Can delete review',13,'delete_review'),
(52,'Can view review',13,'view_review'),
(53,'Can add request',14,'add_request'),
(54,'Can change request',14,'change_request'),
(55,'Can delete request',14,'delete_request'),
(56,'Can view request',14,'view_request'),
(57,'Can add police station',15,'add_policestation'),
(58,'Can change police station',15,'change_policestation'),
(59,'Can delete police station',15,'delete_policestation'),
(60,'Can view police station',15,'view_policestation'),
(61,'Can add feedback',16,'add_feedback'),
(62,'Can change feedback',16,'change_feedback'),
(63,'Can delete feedback',16,'delete_feedback'),
(64,'Can view feedback',16,'view_feedback'),
(65,'Can add complaints',17,'add_complaints'),
(66,'Can change complaints',17,'change_complaints'),
(67,'Can delete complaints',17,'delete_complaints'),
(68,'Can view complaints',17,'view_complaints'),
(69,'Can add payemnt',18,'add_payemnt'),
(70,'Can change payemnt',18,'change_payemnt'),
(71,'Can delete payemnt',18,'delete_payemnt'),
(72,'Can view payemnt',18,'view_payemnt'),
(73,'Can add payment',18,'add_payment'),
(74,'Can change payment',18,'change_payment'),
(75,'Can delete payment',18,'delete_payment'),
(76,'Can view payment',18,'view_payment'),
(77,'Can add payments',19,'add_payments'),
(78,'Can change payments',19,'change_payments'),
(79,'Can delete payments',19,'delete_payments'),
(80,'Can view payments',19,'view_payments');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) DEFAULT NULL,
  `complaint` varchar(500) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `complaints_USER_id_eb97ca07_fk_login_id` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`id`,`date`,`complaint`,`reply`,`status`,`type`,`USER_id`) values 
(1,'2024-07-17','hh','hi','done',NULL,1),
(2,'2024-07-18','hereyy\n','scvhg','Done',NULL,1),
(3,'2024-07-19','The labour bhaskeren behavior is very bad. ','pending','pending',NULL,2),
(4,'2024-07-27','heyy','pending','pending',NULL,1);

/*Table structure for table `criminal` */

DROP TABLE IF EXISTS `criminal`;

CREATE TABLE `criminal` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `photo1` varchar(200) DEFAULT NULL,
  `photo2` varchar(200) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `adarcard` varchar(20) DEFAULT NULL,
  `fingerprint` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `criminal` */

insert  into `criminal`(`id`,`name`,`photo1`,`photo2`,`gender`,`place`,`district`,`state`,`post`,`dob`,`adarcard`,`fingerprint`) values 
(1,'Escobar','/media/criminals/criminal1/20241807235543.jpg','/media/criminals/criminal2/20241807235543.jpg','male','Haripad','Alappuzha','kerala','Muttom','1987-04-11','123456789041','/media/criminals/finger/20241807235543.jpg');

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'myapp','criminal'),
(8,'myapp','labour'),
(9,'myapp','login'),
(10,'myapp','notification'),
(11,'myapp','user'),
(12,'myapp','skill'),
(13,'myapp','review'),
(14,'myapp','request'),
(15,'myapp','policestation'),
(16,'myapp','feedback'),
(17,'myapp','complaints'),
(18,'myapp','payment'),
(19,'myapp','payments');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-07-16 07:09:56.093891'),
(2,'auth','0001_initial','2024-07-16 07:09:56.172393'),
(3,'admin','0001_initial','2024-07-16 07:09:56.362152'),
(4,'admin','0002_logentry_remove_auto_add','2024-07-16 07:09:56.419375'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-07-16 07:09:56.426554'),
(6,'contenttypes','0002_remove_content_type_name','2024-07-16 07:09:56.474468'),
(7,'auth','0002_alter_permission_name_max_length','2024-07-16 07:09:56.493550'),
(8,'auth','0003_alter_user_email_max_length','2024-07-16 07:09:56.517572'),
(9,'auth','0004_alter_user_username_opts','2024-07-16 07:09:56.526017'),
(10,'auth','0005_alter_user_last_login_null','2024-07-16 07:09:56.550915'),
(11,'auth','0006_require_contenttypes_0002','2024-07-16 07:09:56.557258'),
(12,'auth','0007_alter_validators_add_error_messages','2024-07-16 07:09:56.571671'),
(13,'auth','0008_alter_user_username_max_length','2024-07-16 07:09:56.597279'),
(14,'auth','0009_alter_user_last_name_max_length','2024-07-16 07:09:56.621027'),
(15,'auth','0010_alter_group_name_max_length','2024-07-16 07:09:56.637743'),
(16,'auth','0011_update_proxy_permissions','2024-07-16 07:09:56.652278'),
(17,'myapp','0001_initial','2024-07-16 07:09:56.859447'),
(18,'myapp','0002_auto_20240715_0001','2024-07-16 07:09:56.970296'),
(19,'myapp','0003_request_status','2024-07-16 07:09:57.006923'),
(20,'sessions','0001_initial','2024-07-16 07:09:57.025183'),
(21,'myapp','0004_auto_20240718_1221','2024-07-18 06:51:16.254562'),
(22,'myapp','0005_auto_20240718_1223','2024-07-18 06:53:32.753710'),
(23,'auth','0012_alter_user_first_name_max_length','2024-07-27 10:42:34.505271'),
(24,'myapp','0006_auto_20240727_1611','2024-07-27 10:42:34.758001'),
(25,'myapp','0007_request_work_status','2024-07-27 11:14:55.215073'),
(26,'myapp','0008_payemnt','2024-07-29 10:21:54.327388'),
(27,'myapp','0009_alter_payemnt_table','2024-07-29 10:24:35.224000'),
(28,'myapp','0010_auto_20240729_1555','2024-07-29 10:25:20.381455'),
(29,'myapp','0011_payments','2024-08-01 03:50:23.018508');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('zcluxwbqorwp3bz4829r7oc8i6wq5km2','N2UwMjYyYzAzMDdmMTQyM2Y3MWFmMDY5NTVkNDg4OWRiOGY0OTUyMjp7ImxpZCI6Mn0=','2024-07-30 07:21:49.160550'),
('jxt2ms9rl8cnwjidcksfoiywgicbj60b','N2UwMjYyYzAzMDdmMTQyM2Y3MWFmMDY5NTVkNDg4OWRiOGY0OTUyMjp7ImxpZCI6Mn0=','2024-08-02 10:08:30.994316'),
('rvlhurd88e73w5722j3fk52lbefw9ynu','eyJsaWQiOjJ9:1sYg3Q:B1ttmyAjgaAX51MWFKDhmV2slHGGLflHwjwMfvZ8o-Y','2024-08-13 06:09:48.092943');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `feedback_USER_id_580a1de9_fk_user_id` (`USER_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `labour` */

DROP TABLE IF EXISTS `labour`;

CREATE TABLE `labour` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `labourname` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `marital_status` varchar(50) DEFAULT NULL,
  `native_place` varchar(50) DEFAULT NULL,
  `native_city` varchar(50) DEFAULT NULL,
  `native_state` varchar(50) DEFAULT NULL,
  `native_pin` int(11) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `current_place` varchar(50) DEFAULT NULL,
  `current_district` varchar(50) DEFAULT NULL,
  `identification_mark1` varchar(50) DEFAULT NULL,
  `identification_mark2` varchar(50) DEFAULT NULL,
  `adarcard` bigint(20) DEFAULT NULL,
  `fingerprint` varchar(200) DEFAULT NULL,
  `job_type` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `idcard_no` varchar(20) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `labour_LOGIN_id_dcdc1d43_fk_login_id` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `labour` */

insert  into `labour`(`id`,`labourname`,`gender`,`dob`,`marital_status`,`native_place`,`native_city`,`native_state`,`native_pin`,`photo`,`current_place`,`current_district`,`identification_mark1`,`identification_mark2`,`adarcard`,`fingerprint`,`job_type`,`phone`,`status`,`email`,`idcard_no`,`LOGIN_id`) values 
(1,'kk','male','2005-01-01','good','h','h','h',454545,'/media/labours/labour/20240717=164236.jpg','u','h','head','hh',123456789012,'/media/labours/laboursign/2024,07,17=164236.jpg','electrician',9898989898,'Approved','ni@gmail.com','00000001',6),
(2,'NIRMAL S SAMSON','female','2024-07-11','hh','cheppad','kayamkulam','kk',676768,'/media/labours/labour/20241707164617.jpg','hh','jj','mark on head','mark on right hand',9400640939,'/media/labours/labour/20241707164617.jpg','Electrical',9400640939,'Approved','son12@gmail.com','00000002',7),
(3,'Bhaskeren','male','1985-01-24','married','Chavara','Kollam','karnataka',570942,'/media/labours/labour/20240719=112138.jpg','Pullepady','Ernakulam','below the nech','In the right hand',123456789013,'/media/labours/laboursign/2024,07,19=112138.jpg','Plumber',9445551234,'pending','bhas@gmail.com','0',8);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'admin@gmail.com','admin','admin'),
(2,'vipin17@gmail.com','1072','police'),
(7,'ss','123','labour'),
(4,'nn','123','user'),
(6,'kk','123','labour'),
(8,'bhas@gmail.com','123','labour'),
(9,'musk@gmail.com','123','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `notification` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`id`,`date`,`notification`) values 
(1,'2024-07-16','Electricion');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `payment` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `REQUEST_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_payemnt_REQUEST_id_902dbae2` (`REQUEST_id`),
  KEY `myapp_payemnt_USER_id_11024dc5` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`id`,`payment`,`date`,`REQUEST_id`,`USER_id`) values 
(1,'100','2024-07-31 05:40:05.864584+00:00',2,4);

/*Table structure for table `payments` */

DROP TABLE IF EXISTS `payments`;

CREATE TABLE `payments` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `payment` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `REQUEST_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Payments_REQUEST_id_3f28db22` (`REQUEST_id`),
  KEY `Payments_USER_id_9c40a471` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payments` */

insert  into `payments`(`id`,`payment`,`date`,`REQUEST_id`,`USER_id`) values 
(1,'1000','2024-08-01 03:51:31.411253+00:00',1,1),
(2,'500','2024-08-01 04:36:47.930577+00:00',1,1);

/*Table structure for table `police_station` */

DROP TABLE IF EXISTS `police_station`;

CREATE TABLE `police_station` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `station_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `police_station_LOGIN_id_09511df4_fk_login_id` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `police_station` */

insert  into `police_station`(`id`,`station_name`,`email`,`phone`,`place`,`post`,`district`,`pincode`,`LOGIN_id`) values 
(1,'Vipin','vipin17@gmail.com',7563421890,'Ayoor','Ayoor','Alappuzha',690505,2);

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `work_type` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `USER_id` bigint(20) NOT NULL,
  `WORKER_id` bigint(20) NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `work_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `request_USER_id_a6681d64_fk_user_id` (`USER_id`),
  KEY `request_WORKER_id_0d0d76c7_fk_labour_id` (`WORKER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`id`,`work_type`,`description`,`location`,`date`,`time`,`type`,`USER_id`,`WORKER_id`,`status`,`work_status`) values 
(1,'kk','123','kk','2024-07-31','15:13:33.285783','Labours',1,1,'Approve','Work Finished'),
(2,'k2','k2','ee','2024-07-31','15:15:15.333674','Labours',1,1,'pending','pending');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rating` varchar(50) DEFAULT NULL,
  `review` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `USER_id` bigint(20) NOT NULL,
  `WORKER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `review_USER_id_5f37438f_fk_user_id` (`USER_id`),
  KEY `review_WORKER_id_eeb2afbe_fk_labour_id` (`WORKER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`id`,`rating`,`review`,`date`,`type`,`USER_id`,`WORKER_id`) values 
(1,'2.0','','2024-07-17','worker',1,1),
(2,'3.0','heh','2024-07-17','worker',1,2),
(3,'3.0','hhh','2024-07-17','worker',1,1),
(4,'3.5','','2024-07-19','worker',2,1);

/*Table structure for table `skill` */

DROP TABLE IF EXISTS `skill`;

CREATE TABLE `skill` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `skill_type` varchar(50) DEFAULT NULL,
  `WORKER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `skill_WORKER_id_5e4fbd38_fk_labour_id` (`WORKER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `skill` */

insert  into `skill`(`id`,`skill_type`,`WORKER_id`) values 
(1,'hehhe',1),
(2,'Iam a professional plumber',3);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_LOGIN_id_709e2997` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`name`,`email`,`phone`,`gender`,`photo`,`place`,`post`,`district`,`pincode`,`LOGIN_id`) values 
(1,'nirmal','nirmalsamson1710@gmail.com',696969696,'male','/media/user/20240717-162329.jpg','jsje','jsje','kochi',696969,4),
(2,'Elon musk','musk@gmail.com',9445705421,'male','/media/user/20240719-121900.jpg','cheppad','haripad','alappuzha',690507,9);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
