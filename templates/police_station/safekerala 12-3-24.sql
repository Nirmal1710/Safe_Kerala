/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 8.0.31 : Database - safekerala
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`safekerala` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `safekerala`;

/*Data for the table `action_plan` */

insert  into `action_plan`(`plan_id`,`login_id`,`description`,`file`,`from_year`,`to_year`,`upload_by`) values 
(8,1,'Unorganized Workers Welfare Board-reg','/static/actionplan/230417-114405.pdf','2021-10-26','2022-10-26','Admin'),
(9,1,'Code on Wages','/static/actionplan/230417-114716.pdf','2021-12-15','2022-12-15','Admin'),
(10,14,'Code on Wages','/static/dlwactionplan/230417-122055.pdf','2021-12-30','2022-07-30','DLW_Officer');

/*Data for the table `adharcard` */

insert  into `adharcard`(`adid`,`enrollment_no`,`name`,`adhar_no`,`dob`,`gender`,`house_name`,`place`,`post`,`city`,`sub_district`,`district`,`state`,`pin`,`mobile`,`email`,`fathername`,`photo`,`issue_date`,`print_date`) values 
(1,'2001/2012/3031','Ravi R K',111122223333,'1960-05-05','Male','RK House','Guwahati','Guwahati G.P.O','Guwahati','Kamrup','Kamrup','Assam(AS)',781001,9867569751,'ravidasass@gmail.com','Ram K',NULL,'2011-09-19','2011-12-06'),
(2,'2002/2013/3032','Raju Karnav',111122223334,'1971-06-16','Male','Karnav ','Tajpur','Binnyakhata','Tajpur','kokrajhar','Kokrajhar','Assam(AS)',783336,9456783421,'rajmkokk@gmail.com','Linkesh Karnav',NULL,'2011-11-24','2012-01-03'),
(3,'2003/2014/3033','Basker Bose',111122223335,'1979-10-27','Male','Kesav','Anantapur','Ramachandra Nagar','Anantapur','Ananthapur','Ananthapur','Andhra Pradesh(Ap)',515001,9646763328,'BasBos79@gmail.com','Bose Keasav',NULL,'2012-06-12','2012-06-11'),
(4,'2003/2015/3034','Mahesh Das',111122223336,'1981-04-19','Male','KPP House','excel college of instution','Pallakkapalayam','excel college of instutions','Salem','Salem','Tamil Nadu(TN)',637303,8526414130,'mahi112233@gmail.com','Selva Raj',NULL,'2012-03-01','2012-03-08'),
(5,'2003/2016/3035','Lokesh',111122223337,'1980-12-31','Male','Nilambari','CHINNA SADAYAMPALAYAM','Eroad Railway Colony','CHINNA SADAYAMPALAYAM','Erode','Erode','Tamil Nadu(TN)',638002,7986543891,'lokeshrev2222@gmail.com','Murukan',NULL,'2012-07-05','2012-07-30'),
(6,'2003/2017/3036','Amritha T K',111122223338,'1995-04-06','Female','Revath','Ezhakadavu','Ezhakadavu','Ezhakadavu','Mavelikkara','Alappuzha','Kerala(KL)',690104,7540412076,'amritha@gmail.com','Manoj Nair',NULL,'2013-01-02','2013-02-01'),
(7,'2003/2018/3037',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Data for the table `child_labor` */

insert  into `child_labor`(`child_id`,`user_lid`,`report`,`spot`,`evidence`,`time`,`date`,`status`,`reply`,`report_date`) values 
(1,5,'a complaint against child labor ','Near Koyilandi bus stand',NULL,'03:00:00','2023-02-16','Done','will take action','2023-02-16'),
(2,5,'cgnmm','calicut ','/static/childlabour/20230508=113326.jpg','08:00:00','2022-03-08','Done','We will take necessary action','2023-05-08'),
(3,5,'child work in site','kuttpuram','/static/childlabour/20230508=161307.jpg','06:00:00','2023-05-12','pending','pending','2023-05-08');

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`date`,`complaint`,`reply`,`status`,`user_lid`,`login_id`,`con_lid`,`type`) values 
(1,'2023-05-09','This is a complaint against an unknown person who always came with a duplicate id card to my work si','pending','pending',NULL,NULL,28,'contractor'),
(3,'2023-05-09','Unknown person roaming around with a duplicate id','pending','pending',34,0,0,'user'),
(4,'2023-05-09','valare mosham sameepanam','This the last warning for this contractor','Done',0,33,28,'lab_cont'),
(5,'2023-05-09','It is a complaint against the user who request me for a work. that is a fake request.','pending','pending',0,33,6002,'lab_user'),
(6,'2023-05-09','An unauthorized person went my house, he lies he is a authorized worker from this application ','ok will','Done',8,0,0,'user'),
(7,'2024-02-12','gyfyf','pending','pending',34,0,0,'user'),
(8,'2024-02-13','hfugg','ok','Done',8,0,0,'user');

/*Data for the table `contractor` */

insert  into `contractor`(`con_id`,`con_lid`,`name`,`gender`,`dob`,`place`,`post`,`pin`,`district`,`work_type`,`photo`,`phone`,`adharcard`,`status`,`Email`) values 
(1,17,'Rahul','Male','1970-01-01','Kollam','Kollam',673307,'Kozhikode','Construction',NULL,7564372233,854623452345,'Approved','rahulcon@gmail.com'),
(2,18,'Ravi','Male','1984-11-29','Koyilandi','Koyilandi',673337,'Kozhikode','Painting',NULL,8086345623,543676589756,'Approved','ravikk84@gmail.com'),
(4,28,'eeeeeeeeeeee','Male','2023-03-29','jhhhh','iiiii',543678,'kozhikode','eeeeee','static/contractor/20230425112017.jpg',7560614453,333344445556,'Approved','eeee@gmail.com'),
(5,29,'aaaaaaaaaa','Female','2023-03-27','dddddd','ddddd',333444,'kozhikode','eeeeeeeeeee','static/contractor/20230425113535.jpg',7654678767,333322221111,'Approved','wwww@gmail.com'),
(6,32,'lab','Male','2023-04-04','Bengal','pvgv',67768,'kozhikode','ssssssssssssssssss','static/contractor/20230429141733.jpg',676878,333344445556,'pending','l@gmail'),
(7,37,'riya','Female','2023-05-25','KOZHIKODE','calicut',345678,'Kozhikode','painter','static/contractor/20230508175801.jpg',9897567856,234567893456,'Approved','riya@gmail.com');

/*Data for the table `criminal` */

insert  into `criminal`(`criminal_id`,`name`,`photo1`,`photo2`,`gender`,`place`,`district`,`state`,`post`,`dob`,`adarcard`,`fingerprint`) values 
(21,'bilal','/static/criminal/20240213183658.jpg','/static/criminal1/20240213183658.jpg','male','bangaldesh','bangla','bandra','east bangal','2024-02-16','987456321455','/static/criminalsign/20240213183658.jpg'),
(22,'mohanlal','/static/criminal/20240213184014.jpg','/static/criminal1/20240213184014.jpg','male','kottarakara','kollam','kerala','kottooli','2024-02-16','987456321456','/static/criminalsign/20240213184014.jpg'),
(23,'mamoty','/static/criminal/20240213184138.jpg','/static/criminal1/20240213184138.jpg','male','chennai','madras','tamilnadu','madura','2024-02-17','987456321456','/static/criminalsign/20240213184138.jpg'),
(24,'vasu','/static/criminal/20240308113106.jpg','/static/criminal1/20240308113106.jpg','male','house','north paravur','city','qsqs','2024-03-14','789456654789','/static/criminalsign/20240308113106.jpg');

/*Data for the table `dlw_officer` */

insert  into `dlw_officer`(`officer_id`,`officer_lid`,`name`,`pen_no`,`photo`,`phone`,`email`,`place`,`post`,`pin`,`district`) values 
(5,23,'K RANI',88889999,'/static/dlw/230417102824.jpg',8547655274,'dlckkd.lc@kerala.gov.in','KOZHIKODE LABOUR OFFICE','CIVIL STATION',673020,'KOZHIKODE'),
(7,24,'NIVEED N K',77778888,'/static/dlw/230417104402.jpg',8547655265,'dlcekm.lc@kerala.gov.in','KAKKANAD','ERNAKULAM',682030,'ERNAKULAM');

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`date`,`user_lid`,`feedback`) values 
(0,'0000-00-00',0,''),
(1,'2022-08-26',6001,'good'),
(2,'2022-08-30',6020,'good'),
(3,'2022-09-03',6004,'bad'),
(4,'2022-09-05',6011,'good'),
(5,'2022-11-15',8,'sgdhdydufu'),
(6,'2022-11-15',8,'good'),
(8,'2022-11-21',11,'average'),
(9,'2022-11-21',8,'very good'),
(10,'2023-05-06',5,'dhhdsafchhfdd'),
(11,'2023-05-07',5,'fhdhf');

/*Data for the table `job_wage` */

insert  into `job_wage`(`wage_id`,`skill_type`,`minimum_wage`) values 
(1,'painter','800'),
(2,'carpenter','1000'),
(3,'electrician','1000'),
(4,'Driver','2000'),
(5,'Plumber','1231');

/*Data for the table `labour` */

insert  into `labour`(`labour_id`,`login_id`,`labourname`,`gender`,`dob`,`marital_status`,`native_place`,`native_city`,`native_state`,`native_pin`,`photo`,`current_place`,`current_district`,`identification_mark1`,`identification_mark2`,`adarcard`,`fingerprint`,`job_type`,`phone`,`status`,`con_lid`,`email`,`idcard_no`) values 
(6,55,'mammutty','male','2024-02-23','vbnm','vbnm','dfghnm','cvbn',456123,'/static/labour/240213154803.jpg','ernamkulam','ernamkulam','cvbn','cvbnm',789456789456,'/static/laboursign/240213154803.jpg','Construction',789456789456,'Approved',NULL,'core@gmail.com','00000002'),
(7,59,'bhaskar','male','2024-02-17','single','nepal','nepot','nepal',789541,'/static/labour/240213183331.jpg','ernamkulam','ernamkulam','a reddish mole on the left cheek','a white wound on the right hand',123456789784,'/static/laboursign/240213183331.jpg','Construction',123456789784,'pending',NULL,'bhaskar@gmail.com','0'),
(8,61,'vasu annan','male','2024-03-09','single','punnakkad','kottayam','kerala',987456,'/static/labour/240308112524.jpg','kundara','kollam','the both eyes are red','a bold koman pakada mustache',789456123787,'/static/laboursign/240308112524.jpg','Driving',789456123787,'Approved',NULL,'vasuannan@gmail.com','00000003');

/*Data for the table `laws` */

insert  into `laws`(`law_id`,`title`,`law`,`discription`) values 
(3,'Kerala labours Welfare Fund','ACTII of 1977','An Act to provide for the constitution of a fund for promoting the welfare of labour and for certain'),
(4,'Employee Compensation ','ACT 1923','An Act to provide the payment by certain classes of employers to their workmen of compensation for i');

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(4,'admin@gmail.com','admin1','admin'),
(5,'reema@gmail.com','123','user'),
(6,'labour@gmail.com','123456','labour'),
(7,'kakkodi@gmail.com','9532','police'),
(8,'navaneeth@gmail.com','2233','user'),
(9,'Payyolistation@gmail.com','9738','police'),
(10,'akansha@gmail.com','7016','user'),
(11,'bindu@gmail.com','3344','user'),
(12,'kannurstation@gmail.com','1735','police'),
(14,'bh@gmail.com','7788','DLW OFFICER'),
(15,'new@g','3163','DLW OFFICER'),
(19,'shoknrtwnknr.pol@kerala.gov.in','9503','police'),
(20,'siksdps.pol@kerala.gov.in','7665','police'),
(21,'shopdjwynd.pol@kerala.gov.in','8989','police'),
(22,'shompmpsmpm.pol@kerala.gov.in','4547','police'),
(23,'dlckkd.lc@kerala.gov.in','5579','DLW OFFICER'),
(24,'dlcekm.lc@kerala.gov.in','2585','DLW OFFICER'),
(25,'asdawe@gmail.com','7286','DLW OFFICER'),
(26,'ddd@gmail.com','2840','DLW OFFICER'),
(28,'eeee@gmail.com','5566','contractor'),
(29,'wwww@gmail.com','6677','contractor'),
(32,'l@gmail','123','pending'),
(34,'a','123','user'),
(35,'john@gmail1.com','123','user'),
(36,'arun@gmail.com','123','user'),
(37,'riya@gmail.com','123','contractor'),
(38,'shocentralekm.pol@kerala.gov.in','1155','police'),
(39,'rrrrr@gmail.com','6516','police'),
(42,'asd@gmail.com','7244','DLW OFFICER'),
(43,'dff3t5@gmail.com','308','DLW OFFICER'),
(44,'northpolice@gmail.com','5950','police'),
(45,'kaloor@gmail.com','9796','police'),
(46,'\"++\"','\"++\"','\"++\"'),
(47,'shaji@gmail.com','1','labour'),
(48,'core@gmail.com','789456123789','labour'),
(49,'core@gmail.com','789456123789','labour'),
(50,'core@gmail.com','789456123456','labour'),
(51,'core@gmail.com','789456123123','labour'),
(52,'core@gmail.com','789456123123','labour'),
(53,'core@gmail.com','789456123123','labour'),
(54,'kappela@gmail.com','1','labour'),
(55,'mamuty@gmail.com','123','labour'),
(56,'malappurampolice@gmail.com','7493','police'),
(57,'payannur@gmail.com','9655','police'),
(58,'mavoorpolice@gmail.com','2925','police'),
(59,'bhaskar@gmail.com','123456789784','labour'),
(60,'n@gmail.com','833','police'),
(61,'vasuannan@gmail.com','1','labour');

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`date`,`notification`) values 
(2,'2022-09-15','hello the people of ernamkulam city'),
(15,'2024-02-12','some kind of people are came to enter the city of ernamkulam...the citizens of ernamkulam city  dont'),
(16,'2024-02-13','Many countries have government departments or agencies dedicated to labor and migration. They often '),
(17,'2024-02-13','Some organizations or services offer subscription-based updates on labor migration news and developm'),
(18,'2024-02-13','here are mobile applications available that provide updates and notifications on labor migration new'),
(19,'2024-02-13',' Some websites and news outlets offer RSS feeds that you can subscribe to using RSS reader apps or s'),
(20,'2024-03-08','sdfghjkl');

/*Data for the table `police_station` */

insert  into `police_station`(`station_id`,`login_id`,`station_name`,`email`,`phone`,`place`,`post`,`district`,`pincode`) values 
(1008,19,'KANNUR TOWN POLICE STATION','shoknrtwnknr.pol@kerala.gov.in',9497980893,'KANNUR','KANNUR CIVIL STATION','KANNUR',670002),
(1009,20,'KASARAGOD POLICE STATIONSS','siksdps.pol@kerala.gov.in',9497987217,'THE STATION HOUSE OFFICER,KASARAGOD','KASARAGOD','Alappuzha',671121),
(1010,21,'PADINJARATHARA POLICE STATION','shopdjwynd.pol@kerala.gov.in',9436273401,'PADINJARATHARA POLICE STATION','PADINJARATHARA','WAYANAD',673575),
(1011,22,'MALAPPURAM POLICE STATION','shompmpsmpm.pol@kerala.gov.in',9497987162,'MALAPPURAM','DOWN HILL','MALAPPURAM',676519),
(1012,38,'ERNAKULAM CENTRAL POLICE STATION','shocentralekm.pol@kerala.gov.in',9497980427,'The Station House Officer, Ernakulam','Ernakulam Central PS','Ernakulam',682018),
(1016,56,'MALAPPURAM DISTRICT POLICE STATION','malappurampolice@gmail.com',9874563218,'MALAPPURAM','MALAPPURAM TOWN','Malappuram',987452),
(1017,57,'PAYANNUR SOUTH POLICE STATION','payannur@gmail.com',9874587463,'PAYYANNUR','PAYYANNUR','Kannur',654782),
(1019,60,'north','n@gmail.com',9874563254,'noth stat','townhalls','Alappuzha',654782);

/*Data for the table `report` */

insert  into `report`(`report_id`,`user_lid`,`report_title`,`report_descripton`,`date`,`labour_id`,`type`) values 
(1,6001,'misbhv','mmm','2022-10-04',5002,NULL),
(2,6002,'nnn','nddd','2022-10-06',5004,NULL),
(3,0,'\"++\"','\"++\"','2022-10-22',0,NULL),
(4,6,'pending','gdjjdjdd','2022-11-14',5002,NULL),
(5,8,'pending','ghh','2022-11-15',5002,NULL),
(6,8,'pending','vhkll','2022-11-15',5002,NULL),
(7,8,'pending','bdjdjjdd','2022-11-15',5002,NULL),
(8,8,'pending','hdjdjdkd','2022-11-15',5002,NULL),
(9,8,'pending','hdhdhhdd','2022-11-15',5005,NULL),
(10,8,'pending','aaaaaaaaa\n','2022-11-15',0,NULL),
(11,8,'pending','fhiioop','2022-11-15',0,NULL),
(12,8,'pending','sssssssssss','2022-11-15',8,NULL),
(13,8,'pending','He is not a good labour','2022-11-20',8,NULL),
(15,5,'pending','shhjfdss','2023-05-06',7,'labours'),
(16,5,'pending','fkl','2023-05-07',14,'labours'),
(17,5,'work ','sssddddhbhnhjfgh','2023-05-08',17,'labours'),
(18,17,'hi ','Hhh','2023-05-09',0,'Contractor'),
(19,34,'po','jjsk','2023-05-09',33,'labours'),
(20,34,'jzj','jjj','2023-05-09',33,'labours'),
(21,8,'Misbehavior ','This Contractor misbehaving with their workers\n','2023-05-09',17,'Contractor'),
(22,8,'kkk','rrrrrrrt\n','2023-05-09',33,'labours');

/*Data for the table `request` */

insert  into `request`(`request_id`,`user_id`,`labourr_lid`,`work_type`,`discription`,`location`,`date`,`time`,`type`,`status`) values 
(1,5,31,'paint','2 dats work','Amaravala','2023-05-02','9','contractor',NULL),
(2,0,0,'\"++\"','\"++\"','\"++\"','0000-00-00','\"++\"','\"++\"',NULL),
(3,5,1,'painting ','chnmmm','chnmm','2023-05-08','09:48:33','Labours',NULL),
(4,34,33,'nmm','kk','kk','2023-05-09','07:04:05','Labours','Approve'),
(5,8,33,'Electrical','Room Modification lite fitting dfdfdf','Vadakara','2023-05-09','17:13:42','Labours','Approve'),
(6,8,55,'hshsh','hshahs','hzhzhs','2024-03-08','15:08:38','Labours','Approve');

/*Data for the table `review` */

insert  into `review`(`review_id`,`rating`,`review`,`date`,`user_lid`,`about_id`,`type`) values 
(1,'eeeee','iiiiiii','2023-05-04',5,33,'labour'),
(2,'rrrr','ooo','2023-05-04',5,17,'labour'),
(3,'','','0000-00-00',0,0,''),
(4,'','gjjf','2024-02-12',34,36,'worker');

/*Data for the table `skill` */

insert  into `skill`(`skill_id`,`skill_type`,`labour_id`) values 
(1,'\"++\"',0),
(2,'mechanical ',17),
(3,'electric ',33),
(5,'construction ',40),
(8,'excellent ',6);

/*Data for the table `user` */

insert  into `user`(`user_id`,`user_lid`,`name`,`email`,`phone`,`gender`,`photo`,`place`,`post`,`district`,`pincode`) values 
(1,6001,'Amritha','amritha@gmail.com',7540412076,'female','/static/criminal1/20221002121014.jpg','moodadi','moodadi','ernamkulam',673307),
(2,6002,'Ravi','rv1980@gmail.com',9826517130,'male',NULL,'nandi','kadalur','ernamkulam',673529),
(3,6011,'Abhishek','abhi@gmail.com',7530414150,'male',NULL,'arangad','melur','ernamkulam',673306),
(4,5,'Reema','reema@gmail.com',8086765628,'m','/static/criminal1/20221002121014.jpg','payyoli','payyoli','ernamkulam',673426),
(5,36,'Mamtha','mamtha@gmail.com',9645745869,'m','/static/user/20221114-152736.jpg','calicut','calicut','ernamkulam',679850),
(6,8,'Navaneeth','navaneeth@gmail.com',9747360170,'m','/static/user/20221120-230928.jpg','Kakkodi','Kizhakkummuri','ernamkulam',673611),
(7,10,'Akansha R','akansha@gmail.com',7528105166,'m','/static/user/20221115-175500.jpg','Moodadi','Moodadi','ernamkulam',673307),
(8,11,'Bindu','bindu@gmail.com',8525863914,'female','/static/user/20221115-180052.jpg','palakulam','moodadi','ernamkulam',673307),
(9,34,'john','john@gmail.com',9685232655,'male','/static/user/20230507-224846.jpg','calicut ','alghj','ernamkulam',586457),
(10,35,'john','john@gmail.com',9685236958,'male','/static/user/20230507-225419.jpg','fhjj','gjkk','ernamkulam',2586);

/*Data for the table `wage_con` */

insert  into `wage_con`(`wc_id`,`con_lid`,`labour_lid`,`skill_type`,`wage_given`,`job_discription`,`date`) values 
(2,28,31,'snfjds',0,'jhdhsj','2023-05-04'),
(3,28,31,'kjfksj',0,'ijeirj','2023-05-04'),
(4,28,33,'aaaaaaa',800,'rrrrrrrr','2023-05-04');

/*Data for the table `wage_issue` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
