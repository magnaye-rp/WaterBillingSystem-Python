-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2024 at 05:26 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wbs`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `BillingID` int(11) NOT NULL,
  `SerialID` int(11) NOT NULL,
  `DebtID` int(11) NOT NULL,
  `ChargeID` int(11) NOT NULL DEFAULT 0,
  `BaseAmount` float(10,2) NOT NULL,
  `BillingAmount` decimal(10,2) NOT NULL,
  `DueDate` date NOT NULL,
  `isPaid` tinyint(4) NOT NULL,
  `LateFeeMultiplier` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`BillingID`, `SerialID`, `DebtID`, `ChargeID`, `BaseAmount`, `BillingAmount`, `DueDate`, `isPaid`, `LateFeeMultiplier`) VALUES
(1, 1, 1, 0, 63.00, 63.00, '2024-12-01', 0, 0),
(2, 2, 14, 0, 39.00, 39.00, '2024-12-01', 0, 0),
(3, 3, 27, 0, 105.00, 105.00, '2024-12-01', 0, 0),
(4, 4, 39, 0, 97.50, 97.50, '2024-12-01', 0, 0),
(5, 5, 2, 0, 73.50, 73.50, '2024-12-01', 0, 0),
(6, 6, 15, 0, 182.00, 182.00, '2024-12-01', 0, 0),
(7, 7, 28, 0, 150.00, 150.00, '2024-12-01', 0, 0),
(8, 8, 40, 0, 107.25, 107.25, '2024-12-01', 0, 0),
(9, 9, 3, 0, 136.50, 136.50, '2024-12-01', 0, 0),
(10, 10, 16, 0, 52.00, 52.00, '2024-12-01', 0, 0),
(11, 11, 29, 0, 165.00, 165.00, '2024-12-01', 0, 0),
(12, 12, 41, 0, 107.25, 107.25, '2024-12-01', 0, 0),
(13, 13, 4, 0, 115.50, 115.50, '2024-12-01', 0, 0),
(14, 14, 17, 0, 78.00, 78.00, '2024-12-01', 0, 0),
(15, 15, 30, 0, 105.00, 105.00, '2024-12-01', 0, 0),
(16, 16, 42, 0, 87.75, 87.75, '2024-12-01', 0, 0),
(17, 17, 5, 0, 52.50, 52.50, '2024-12-01', 0, 0),
(18, 18, 18, 0, 221.00, 221.00, '2024-12-01', 0, 0),
(19, 19, 31, 0, 120.00, 120.00, '2024-12-01', 0, 0),
(20, 20, 43, 0, 146.25, 146.25, '2024-12-01', 0, 0),
(21, 21, 6, 0, 168.00, 168.00, '2024-12-01', 0, 0),
(22, 22, 19, 0, 78.00, 78.00, '2024-12-01', 0, 0),
(23, 23, 32, 0, 90.00, 90.00, '2024-12-01', 0, 0),
(24, 24, 44, 0, 107.25, 107.25, '2024-12-01', 0, 0),
(25, 25, 7, 0, 0.00, 0.00, '2024-12-01', 0, 0),
(26, 26, 20, 0, 78.00, 78.00, '2024-12-01', 0, 0),
(27, 27, 33, 0, 135.00, 135.00, '2024-12-01', 0, 0),
(28, 28, 45, 0, 107.25, 107.25, '2024-12-01', 0, 0),
(29, 29, 8, 0, 157.50, 157.50, '2024-12-01', 0, 0),
(30, 30, 21, 0, 117.00, 117.00, '2024-12-01', 0, 0),
(31, 31, 34, 0, 210.00, 210.00, '2024-12-01', 0, 0),
(32, 32, 46, 0, 136.50, 136.50, '2024-12-01', 0, 0),
(33, 33, 9, 0, 168.00, 168.00, '2024-12-01', 0, 0),
(34, 34, 22, 0, 91.00, 91.00, '2024-12-01', 0, 0),
(35, 35, 35, 0, 195.00, 195.00, '2024-12-01', 0, 0),
(36, 36, 47, 0, 29.25, 29.25, '2024-12-01', 0, 0),
(37, 37, 10, 0, 94.50, 94.50, '2024-12-01', 0, 0),
(38, 38, 23, 0, 39.00, 39.00, '2024-12-01', 0, 0),
(39, 39, 36, 0, 165.00, 165.00, '2024-12-01', 0, 0),
(40, 40, 48, 0, 126.75, 126.75, '2024-12-01', 0, 0),
(41, 41, 11, 0, 63.00, 63.00, '2024-12-01', 0, 0),
(42, 42, 24, 0, 143.00, 143.00, '2024-12-01', 0, 0),
(43, 43, 37, 0, 240.00, 240.00, '2024-12-01', 0, 0),
(44, 44, 49, 0, 48.75, 48.75, '2024-12-01', 0, 0),
(45, 45, 12, 0, 115.50, 115.50, '2024-12-01', 0, 0),
(46, 46, 25, 0, 117.00, 117.00, '2024-12-01', 0, 0),
(47, 47, 38, 0, 75.00, 75.00, '2024-12-01', 0, 0),
(48, 48, 50, 0, 87.75, 87.75, '2024-12-01', 0, 0),
(49, 49, 13, 0, 126.00, 126.00, '2024-12-01', 0, 0),
(50, 50, 26, 0, 156.00, 156.00, '2024-12-01', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `bill_generation_log`
--

CREATE TABLE `bill_generation_log` (
  `id` int(11) NOT NULL,
  `generation_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bill_generation_log`
--

INSERT INTO `bill_generation_log` (`id`, `generation_date`) VALUES
(1, '2024-11-01');

-- --------------------------------------------------------

--
-- Table structure for table `charge`
--

CREATE TABLE `charge` (
  `ChargeID` int(11) NOT NULL,
  `SerialID` int(11) NOT NULL,
  `ChargeAmount` decimal(10,2) NOT NULL,
  `DateIncurred` date NOT NULL,
  `Type` enum('Damages','Adjustment','Penalty','Repairs') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `concessionaire`
--

CREATE TABLE `concessionaire` (
  `ConcessionaireID` int(1) NOT NULL,
  `ConcessionaireName` varchar(30) NOT NULL,
  `PricePerCubicMeter` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `concessionaire`
--

INSERT INTO `concessionaire` (`ConcessionaireID`, `ConcessionaireName`, `PricePerCubicMeter`) VALUES
(1, 'NasugbuWaters', 10.50),
(2, 'BalayanWaterSystem', 13.00),
(3, 'LemeryWaterDistrict', 15.00),
(4, 'CalataganWaterElement', 9.75);

-- --------------------------------------------------------

--
-- Table structure for table `consumerinfo`
--

CREATE TABLE `consumerinfo` (
  `SerialID` int(11) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `FirstName` varchar(30) NOT NULL,
  `LastName` varchar(30) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `ContactNumber` varchar(20) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `MeterID` int(11) NOT NULL,
  `InspectorID` int(11) NOT NULL,
  `isConnected` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `consumerinfo`
--

INSERT INTO `consumerinfo` (`SerialID`, `Password`, `FirstName`, `LastName`, `Address`, `ContactNumber`, `Email`, `MeterID`, `InspectorID`, `isConnected`) VALUES
(1, 'Password1', 'Jared Jeffrey', 'Abellera', '123 Main St', '555-1234', 'jared.abellera@example.com', 1, 3, 1),
(2, 'Secure123', 'Clarence', 'Adrias', '456 Oak Ave', '555-5678', 'clarence.adrias@example.com', 2, 6, 1),
(3, 'MyPass45', 'Naicel', 'Apolona', '789 Pine Blvd', '555-9012', 'naicel.apolona@example.com', 3, 5, 1),
(4, 'Alpha@123', 'Lheoricke Miguel', 'Atienza', '101 Elm St', '555-3456', 'lheoricke.atienza@example.com', 4, 4, 1),
(5, 'Beta0987', 'Saipoden', 'Banto', '202 Maple St', '555-7890', 'saipoden.banto@example.com', 5, 2, 1),
(6, 'Gamma432', 'John Aldrie', 'Baquiran', '303 Pine St', '555-3210', 'john.baquiran@example.com', 6, 3, 1),
(7, 'Delta567', 'Jhon', 'Boiser', '404 Oak St', '555-6540', 'jhon.boiser@example.com', 7, 2, 1),
(8, 'Omega123', 'Clyde Allen', 'Brucal', '505 Elm St', '555-2340', 'clyde.brucal@example.com', 8, 1, 1),
(9, 'Zeta456', 'Jhayvic', 'Bugtong', '606 Maple St', '555-4560', 'jhayvic.bugtong@example.com', 9, 3, 0),
(10, 'Sigma789', 'Ivan', 'Cabatian', '707 Pine St', '555-7650', 'ivan.cabatian@example.com', 10, 3, 1),
(11, 'Epsilon9', 'Kaye Cee', 'Cagula', '808 Oak St', '555-1234', 'kaye.cagula@example.com', 11, 2, 1),
(12, 'Theta567', 'Kier Andrei', 'Catibog', '909 Elm St', '555-5678', 'kier.catibog@example.com', 12, 3, 1),
(13, 'Lambda42', 'Aj', 'Catli', '1010 Maple St', '555-9012', 'aj.catli@example.com', 13, 3, 1),
(14, 'Kappa987', 'Jomhar', 'Condicion', '1111 Pine St', '555-3456', 'jomhar.condicion@example.com', 14, 6, 1),
(15, 'PhiAlpha', 'Joyce Anne', 'Corpuz', '1212 Oak St', '555-7890', 'joyce.corpuz@example.com', 15, 1, 1),
(16, 'Omicron1', 'Eloisa Joyce', 'Creencia', '1313 Elm St', '555-3210', 'eloisa.creencia@example.com', 16, 3, 1),
(17, 'NuBeta56', 'Irish Kaye', 'Cuenca', '1414 Maple St', '555-6540', 'irish.cuenca@example.com', 17, 3, 1),
(18, 'XiDelta89', 'Jerome', 'Daluz', '1515 Pine St', '555-2340', 'jerome.daluz@example.com', 18, 3, 1),
(19, 'RhoGamma', 'King Exiquiel', 'Dando', '1616 Oak St', '555-4560', 'king.dando@example.com', 19, 4, 1),
(20, 'TauOmega1', 'Ian Jhon', 'Desuyo', '1717 Elm St', '555-7650', 'ian.desuyo@example.com', 20, 1, 1),
(21, 'Alpha77', 'Elon', 'Musk', '1 Innovation Ave', '555-1010', 'elon.musk@example.com', 21, 6, 1),
(22, 'Secure99', 'Jeff', 'Bezos', '2 Space Blvd', '555-2020', 'jeff.bezos@example.com', 22, 5, 1),
(23, 'MyCode88', 'Bill', 'Gates', '3 Tech Rd', '555-3030', 'bill.gates@example.com', 23, 2, 1),
(24, 'Techie21', 'Steve', 'Jobs', '4 Apple Ln', '555-4040', 'steve.jobs@example.com', 24, 2, 1),
(25, 'Quantum77', 'Marie', 'Curie', '5 Science St', '555-5050', 'marie.curie@example.com', 25, 4, 1),
(26, 'Relativity88', 'Albert', 'Einstein', '6 Physics Ave', '555-6060', 'albert.einstein@example.com', 26, 4, 1),
(27, 'Explorer33', 'Neil', 'Armstrong', '7 Moon Blvd', '555-7070', 'neil.armstrong@example.com', 27, 5, 1),
(28, 'Visionary44', 'Mark', 'Zuckerberg', '8 Meta Pl', '555-8080', 'mark.zuckerberg@example.com', 28, 6, 1),
(29, 'Author10', 'J.K.', 'Rowling', '9 Potter Ln', '555-9090', 'jk.rowling@example.com', 29, 1, 1),
(30, 'Imagine12', 'John', 'Lennon', '10 Beatle St', '555-1111', 'john.lennon@example.com', 30, 6, 1),
(31, 'Dynamic99', 'Taylor', 'Swift', '11 Music Blvd', '555-2222', 'taylor.swift@example.com', 31, 4, 1),
(32, 'Freedom22', 'Nelson', 'Mandela', '12 Peace St', '555-3333', 'nelson.mandela@example.com', 32, 5, 1),
(33, 'Artistic76', 'Leonardo', 'da Vinci', '13 Renaissance Pl', '555-4444', 'leonardo.davinci@example.com', 33, 2, 1),
(34, 'Playmaker5', 'Michael', 'Jordan', '14 Basketball Rd', '555-5555', 'michael.jordan@example.com', 34, 5, 1),
(35, 'Astrophile9', 'Carl', 'Sagan', '15 Cosmos Ave', '555-6666', 'carl.sagan@example.com', 35, 6, 1),
(36, 'Inspire66', 'Oprah', 'Winfrey', '16 Talkshow Ln', '555-7777', 'oprah.winfrey@example.com', 36, 2, 1),
(37, 'Classic77', 'Ludwig', 'Beethoven', '17 Symphony Blvd', '555-8888', 'ludwig.beethoven@example.com', 37, 5, 1),
(38, 'Legend10', 'Kobe', 'Bryant', '18 Mamba Dr', '555-9999', 'kobe.bryant@example.com', 38, 6, 1),
(39, 'King33', 'Martin', 'Luther King', '19 Dream St', '555-0000', 'martin.king@example.com', 39, 3, 1),
(40, 'Eloquent88', 'Maya', 'Angelou', '20 Poetic Pl', '555-1212', 'maya.angelou@example.com', 40, 3, 1),
(41, 'Pioneer77', 'Isaac', 'Newton', '21 Gravity Blvd', '555-1313', 'isaac.newton@example.com', 41, 4, 1),
(42, 'Bright123', 'Ada', 'Lovelace', '22 Programming Ln', '555-1414', 'ada.lovelace@example.com', 42, 4, 1),
(43, 'Explorer44', 'Christopher', 'Columbus', '23 Discovery St', '555-1515', 'christopher.columbus@example.com', 43, 1, 1),
(44, 'Resilient89', 'Malala', 'Yousafzai', '24 Education Ave', '555-1616', 'malala.yousafzai@example.com', 44, 6, 1),
(45, 'Nobel22', 'Alexander', 'Fleming', '25 Penicillin Blvd', '555-1717', 'alexander.fleming@example.com', 45, 3, 1),
(46, 'Classic91', 'Wolfgang', 'Mozart', '26 Melody Rd', '555-1818', 'wolfgang.mozart@example.com', 46, 1, 1),
(47, 'Inspire11', 'Amelia', 'Earhart', '27 Aviation Ln', '555-1919', 'amelia.earhart@example.com', 47, 2, 1),
(48, 'Artistic33', 'Vincent', 'van Gogh', '28 Starry Night Blvd', '555-2020', 'vincent.vangogh@example.com', 48, 6, 1),
(49, 'Innovate44', 'Thomas', 'Edison', '29 Lightbulb St', '555-2121', 'thomas.edison@example.com', 49, 4, 1),
(50, 'Champion66', 'Usain', 'Bolt', '30 Speed Blvd', '555-2222', 'usain.bolt@example.com', 50, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `debt`
--

CREATE TABLE `debt` (
  `DebtID` int(11) NOT NULL,
  `MeterID` int(11) NOT NULL,
  `FromDate` date NOT NULL,
  `PreviousReading` int(11) NOT NULL,
  `ToDate` date NOT NULL,
  `LatestReading` int(11) NOT NULL,
  `AmountDue` decimal(10,2) NOT NULL,
  `isBilled` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `debt`
--

INSERT INTO `debt` (`DebtID`, `MeterID`, `FromDate`, `PreviousReading`, `ToDate`, `LatestReading`, `AmountDue`, `isBilled`) VALUES
(1, 1, '2024-10-26', 7, '2024-11-26', 13, 63.00, 1),
(2, 5, '2024-10-26', 5, '2024-11-26', 12, 73.50, 1),
(3, 9, '2024-10-26', 5, '2024-11-26', 18, 136.50, 1),
(4, 13, '2024-10-26', 6, '2024-11-26', 17, 115.50, 1),
(5, 17, '2024-10-26', 7, '2024-11-26', 12, 52.50, 1),
(6, 21, '2024-10-26', 1, '2024-11-26', 17, 168.00, 1),
(7, 25, '2024-10-26', 10, '2024-11-26', 10, 0.00, 1),
(8, 29, '2024-10-26', 5, '2024-11-26', 20, 157.50, 1),
(9, 33, '2024-10-26', 2, '2024-11-26', 18, 168.00, 1),
(10, 37, '2024-10-26', 7, '2024-11-26', 16, 94.50, 1),
(11, 41, '2024-10-26', 9, '2024-11-26', 15, 63.00, 1),
(12, 45, '2024-10-26', 2, '2024-11-26', 13, 115.50, 1),
(13, 49, '2024-10-26', 5, '2024-11-26', 17, 126.00, 1),
(14, 2, '2024-10-26', 7, '2024-11-26', 10, 39.00, 1),
(15, 6, '2024-10-26', 1, '2024-11-26', 15, 182.00, 1),
(16, 10, '2024-10-26', 10, '2024-11-26', 14, 52.00, 1),
(17, 14, '2024-10-26', 7, '2024-11-26', 13, 78.00, 1),
(18, 18, '2024-10-26', 3, '2024-11-26', 20, 221.00, 1),
(19, 22, '2024-10-26', 7, '2024-11-26', 13, 78.00, 1),
(20, 26, '2024-10-26', 7, '2024-11-26', 13, 78.00, 1),
(21, 30, '2024-10-26', 3, '2024-11-26', 12, 117.00, 1),
(22, 34, '2024-10-26', 4, '2024-11-26', 11, 91.00, 1),
(23, 38, '2024-10-26', 7, '2024-11-26', 10, 39.00, 1),
(24, 42, '2024-10-26', 4, '2024-11-26', 15, 143.00, 1),
(25, 46, '2024-10-26', 1, '2024-11-26', 10, 117.00, 1),
(26, 50, '2024-10-26', 8, '2024-11-26', 20, 156.00, 1),
(27, 3, '2024-10-26', 5, '2024-11-26', 12, 105.00, 1),
(28, 7, '2024-10-26', 7, '2024-11-26', 17, 150.00, 1),
(29, 11, '2024-10-26', 7, '2024-11-26', 18, 165.00, 1),
(30, 15, '2024-10-26', 9, '2024-11-26', 16, 105.00, 1),
(31, 19, '2024-10-26', 5, '2024-11-26', 13, 120.00, 1),
(32, 23, '2024-10-26', 8, '2024-11-26', 14, 90.00, 1),
(33, 27, '2024-10-26', 4, '2024-11-26', 13, 135.00, 1),
(34, 31, '2024-10-26', 1, '2024-11-26', 15, 210.00, 1),
(35, 35, '2024-10-26', 2, '2024-11-26', 15, 195.00, 1),
(36, 39, '2024-10-26', 5, '2024-11-26', 16, 165.00, 1),
(37, 43, '2024-10-26', 4, '2024-11-26', 20, 240.00, 1),
(38, 47, '2024-10-26', 10, '2024-11-26', 15, 75.00, 1),
(39, 4, '2024-10-26', 2, '2024-11-26', 12, 97.50, 1),
(40, 8, '2024-10-26', 1, '2024-11-26', 12, 107.25, 1),
(41, 12, '2024-10-26', 3, '2024-11-26', 14, 107.25, 1),
(42, 16, '2024-10-26', 1, '2024-11-26', 10, 87.75, 1),
(43, 20, '2024-10-26', 3, '2024-11-26', 18, 146.25, 1),
(44, 24, '2024-10-26', 1, '2024-11-26', 12, 107.25, 1),
(45, 28, '2024-10-26', 7, '2024-11-26', 18, 107.25, 1),
(46, 32, '2024-10-26', 5, '2024-11-26', 19, 136.50, 1),
(47, 36, '2024-10-26', 9, '2024-11-26', 12, 29.25, 1),
(48, 40, '2024-10-26', 3, '2024-11-26', 16, 126.75, 1),
(49, 44, '2024-10-26', 9, '2024-11-26', 14, 48.75, 1),
(50, 48, '2024-10-26', 5, '2024-11-26', 14, 87.75, 1);

-- --------------------------------------------------------

--
-- Table structure for table `ledger`
--

CREATE TABLE `ledger` (
  `LedgerID` int(11) NOT NULL,
  `BillingID` int(11) NOT NULL,
  `SerialID` int(11) NOT NULL,
  `AmountPaid` decimal(10,2) NOT NULL,
  `PaymentDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `meterinspector`
--

CREATE TABLE `meterinspector` (
  `InspectorID` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `ContactNumber` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `meterinspector`
--

INSERT INTO `meterinspector` (`InspectorID`, `Name`, `ContactNumber`) VALUES
(1, 'Roberto Manapat', 2147483647),
(2, 'Godupredo Malucong', 2147483647),
(3, 'Fortunato Ipitipt', 2147483647),
(4, 'Felicensio Lalamunan', 2147483647),
(5, 'Manolo Lumapit', 2147483647),
(6, 'Josepe Cudiamat', 2147483647);

-- --------------------------------------------------------

--
-- Table structure for table `watermeter`
--

CREATE TABLE `watermeter` (
  `MeterID` int(11) NOT NULL,
  `PresentReading` decimal(10,2) NOT NULL,
  `ReadingDate` date NOT NULL,
  `PreviousReading` decimal(10,2) NOT NULL,
  `PreviousReadingDate` date DEFAULT NULL,
  `Consumption` decimal(10,2) GENERATED ALWAYS AS (`PresentReading` - `PreviousReading`) STORED,
  `ConcessionaireID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `watermeter`
--

INSERT INTO `watermeter` (`MeterID`, `PresentReading`, `ReadingDate`, `PreviousReading`, `PreviousReadingDate`, `ConcessionaireID`) VALUES
(1, 13.00, '2024-11-01', 7.00, '2024-12-10', 1),
(2, 10.00, '2024-11-01', 7.00, '2024-11-26', 2),
(3, 12.00, '2024-11-01', 5.00, '2024-11-26', 3),
(4, 12.00, '2024-11-01', 2.00, '2024-11-26', 4),
(5, 12.00, '2024-11-01', 5.00, '2024-11-26', 1),
(6, 15.00, '2024-11-01', 1.00, '2024-11-26', 2),
(7, 17.00, '2024-11-26', 7.00, '2024-10-26', 3),
(8, 12.00, '2024-11-26', 1.00, '2024-10-26', 4),
(9, 18.00, '2024-11-26', 5.00, '2024-10-26', 1),
(10, 14.00, '2024-11-26', 10.00, '2024-10-26', 2),
(11, 18.00, '2024-11-26', 7.00, '2024-10-26', 3),
(12, 14.00, '2024-11-26', 3.00, '2024-10-26', 4),
(13, 17.00, '2024-11-26', 6.00, '2024-10-26', 1),
(14, 13.00, '2024-11-26', 7.00, '2024-10-26', 2),
(15, 16.00, '2024-11-26', 9.00, '2024-10-26', 3),
(16, 10.00, '2024-11-26', 1.00, '2024-10-26', 4),
(17, 12.00, '2024-11-26', 7.00, '2024-10-26', 1),
(18, 20.00, '2024-11-26', 3.00, '2024-10-26', 2),
(19, 13.00, '2024-11-26', 5.00, '2024-10-26', 3),
(20, 18.00, '2024-11-26', 3.00, '2024-10-26', 4),
(21, 17.00, '2024-11-26', 1.00, '2024-10-26', 1),
(22, 13.00, '2024-11-26', 7.00, '2024-10-26', 2),
(23, 14.00, '2024-11-26', 8.00, '2024-10-26', 3),
(24, 12.00, '2024-11-26', 1.00, '2024-10-26', 4),
(25, 10.00, '2024-11-26', 10.00, '2024-10-26', 1),
(26, 13.00, '2024-11-26', 7.00, '2024-10-26', 2),
(27, 13.00, '2024-11-26', 4.00, '2024-10-26', 3),
(28, 18.00, '2024-11-26', 7.00, '2024-10-26', 4),
(29, 20.00, '2024-11-26', 5.00, '2024-10-26', 1),
(30, 12.00, '2024-11-26', 3.00, '2024-10-26', 2),
(31, 15.00, '2024-11-26', 1.00, '2024-10-26', 3),
(32, 19.00, '2024-11-26', 5.00, '2024-10-26', 4),
(33, 18.00, '2024-11-26', 2.00, '2024-10-26', 1),
(34, 11.00, '2024-11-26', 4.00, '2024-10-26', 2),
(35, 15.00, '2024-11-26', 2.00, '2024-10-26', 3),
(36, 12.00, '2024-11-26', 9.00, '2024-10-26', 4),
(37, 16.00, '2024-11-26', 7.00, '2024-10-26', 1),
(38, 10.00, '2024-11-26', 7.00, '2024-10-26', 2),
(39, 16.00, '2024-11-26', 5.00, '2024-10-26', 3),
(40, 16.00, '2024-11-26', 3.00, '2024-10-26', 4),
(41, 15.00, '2024-11-26', 9.00, '2024-10-26', 1),
(42, 15.00, '2024-11-26', 4.00, '2024-10-26', 2),
(43, 20.00, '2024-11-26', 4.00, '2024-10-26', 3),
(44, 14.00, '2024-11-26', 9.00, '2024-10-26', 4),
(45, 13.00, '2024-11-26', 2.00, '2024-10-26', 1),
(46, 10.00, '2024-11-26', 1.00, '2024-10-26', 2),
(47, 15.00, '2024-11-26', 10.00, '2024-10-26', 3),
(48, 14.00, '2024-11-26', 5.00, '2024-10-26', 4),
(49, 17.00, '2024-11-26', 5.00, '2024-10-26', 1),
(50, 20.00, '2024-11-26', 8.00, '2024-10-26', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`BillingID`),
  ADD KEY `Bill.SerialID_FK` (`SerialID`),
  ADD KEY `Bill.DebtID_FK` (`DebtID`),
  ADD KEY `Bill.ChargeID_FK` (`ChargeID`);

--
-- Indexes for table `bill_generation_log`
--
ALTER TABLE `bill_generation_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `charge`
--
ALTER TABLE `charge`
  ADD PRIMARY KEY (`ChargeID`),
  ADD KEY `Charge.SerialID_FK` (`SerialID`);

--
-- Indexes for table `concessionaire`
--
ALTER TABLE `concessionaire`
  ADD PRIMARY KEY (`ConcessionaireID`);

--
-- Indexes for table `consumerinfo`
--
ALTER TABLE `consumerinfo`
  ADD PRIMARY KEY (`SerialID`);

--
-- Indexes for table `debt`
--
ALTER TABLE `debt`
  ADD PRIMARY KEY (`DebtID`),
  ADD KEY `MeterID_FK` (`MeterID`);

--
-- Indexes for table `ledger`
--
ALTER TABLE `ledger`
  ADD PRIMARY KEY (`LedgerID`),
  ADD KEY `Ledger.SerialID_FK` (`SerialID`),
  ADD KEY `Ledger.BillID_FK` (`BillingID`);

--
-- Indexes for table `meterinspector`
--
ALTER TABLE `meterinspector`
  ADD PRIMARY KEY (`InspectorID`);

--
-- Indexes for table `watermeter`
--
ALTER TABLE `watermeter`
  ADD PRIMARY KEY (`MeterID`),
  ADD KEY `WaterMeter.ConcessionaireID_FK` (`ConcessionaireID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `BillingID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `bill_generation_log`
--
ALTER TABLE `bill_generation_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `charge`
--
ALTER TABLE `charge`
  MODIFY `ChargeID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `consumerinfo`
--
ALTER TABLE `consumerinfo`
  MODIFY `SerialID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `debt`
--
ALTER TABLE `debt`
  MODIFY `DebtID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT for table `ledger`
--
ALTER TABLE `ledger`
  MODIFY `LedgerID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `meterinspector`
--
ALTER TABLE `meterinspector`
  MODIFY `InspectorID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `watermeter`
--
ALTER TABLE `watermeter`
  MODIFY `MeterID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `Bill.SerialID_FK` FOREIGN KEY (`SerialID`) REFERENCES `consumerinfo` (`SerialID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `charge`
--
ALTER TABLE `charge`
  ADD CONSTRAINT `Charge.SerialID_FK` FOREIGN KEY (`SerialID`) REFERENCES `consumerinfo` (`SerialID`) ON DELETE CASCADE;

--
-- Constraints for table `debt`
--
ALTER TABLE `debt`
  ADD CONSTRAINT `MeterID_FK` FOREIGN KEY (`MeterID`) REFERENCES `watermeter` (`MeterID`) ON DELETE CASCADE;

--
-- Constraints for table `ledger`
--
ALTER TABLE `ledger`
  ADD CONSTRAINT `Ledger.BillID_FK` FOREIGN KEY (`BillingID`) REFERENCES `bill` (`BillingID`) ON DELETE CASCADE,
  ADD CONSTRAINT `Ledger.SerialID_FK` FOREIGN KEY (`SerialID`) REFERENCES `consumerinfo` (`SerialID`) ON DELETE CASCADE;

--
-- Constraints for table `watermeter`
--
ALTER TABLE `watermeter`
  ADD CONSTRAINT `WaterMeter.ConcessionaireID_FK` FOREIGN KEY (`ConcessionaireID`) REFERENCES `concessionaire` (`ConcessionaireID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
