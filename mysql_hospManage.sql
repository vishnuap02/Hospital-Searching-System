CREATE DATABASE IF NOT EXISTS HOSPITAL;
USE HOSPITAL;

CREATE TABLE IF NOT EXISTS HOSPITALS(
ID INT(10) NOT NULL AUTO_INCREMENT,
HOSPITALNAME VARCHAR(25) NOT NULL,
PASSW VARCHAR(25) NOT NULL,
EMAIL VARCHAR(30) NOT NULL,
ADDRESS VARCHAR(100) NOT NULL,
CITY VARCHAR(50) NOT NULL,
STATE VARCHAR(25) NOT NULL,
COUNTRY VARCHAR(50) NOT NULL,
POSTCODE INT(6) NOT NULL,
ICUBEDS INT(3) ,
GENWARDBEDS INT(3),
OPETHEATER INT(3),
PRIMARY key (ID)
);

CREATE TABLE IF NOT EXISTS DOCTORS(
DID VARCHAR(10) NOT NULL,
FNAME VARCHAR(15) NOT NULL,
LNAME VARCHAR(15) NOT NULL,
RATING INT(2) NOT NULL,
SPL VARCHAR(20),
EXPERIENCE INT(2),
PRIMARY key (DID)
);

ALTER TABLE DOCTORS 
ADD COLUMN PASSW VARCHAR(25) AFTER DID;


ALTER TABLE DOCTORS 
ADD COLUMN HOSPID INT(10);

INSERT INTO HOSPITALS VALUES(10001,'ASTRA HOSPITAL','ASTRA@01','astra01@gamil.com','Plot 54 , main road , KANDIGAI',
'CHENNAI','TN','IND',600127,5,25,2);
INSERT INTO HOSPITALS VALUES(10002,'SPARSH HOSPITAL','SPARSH@02','sparsh02@gamil.com','MAMBAKKAM',
'CHENNAI','TN','IND',600129,10,30,5);
INSERT INTO HOSPITALS VALUES(10003,'APOLLO HOSPITAL','APOLLO@03','apollo03@gmail.com','KELLAMBAKKAM',
'CHENNAI','TN','IND',600130,20,20,0);

SELECT HOSPITALNAME,icubeds FROM HOSPITALS ;

INSERT INTO DOCTORS VALUES('D1001','HARI','KULKARNI',95,'GENERAL SURGEON',10);

INSERT INTO DOCTORS VALUES('20004','DHANU','DESAI',45,'PSYCHIATRIST',3,10001);

SELECT * FROM DOCTORS ;

SELECT * FROM HOSPITALS;

SELECT SUM(ICUBEDS) FROM HOSPITALS;

UPDATE HOSPITALS SET ADDRESS="PLOT-52, TAMBARAM",ICUBEDS=15 WHERE ID="10001";