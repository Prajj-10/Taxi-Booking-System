-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2022 at 09:42 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `taxibooking`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking_information`
--

CREATE TABLE `booking_information` (
  `Booking_ID` int(11) NOT NULL,
  `Pickup_Location` varchar(100) DEFAULT NULL,
  `DropOff_Location` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  `Time` varchar(100) DEFAULT NULL,
  `Customer_ID` int(11) DEFAULT NULL,
  `Driver_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_information`
--

INSERT INTO `booking_information` (`Booking_ID`, `Pickup_Location`, `DropOff_Location`, `Date`, `Time`, `Customer_ID`, `Driver_ID`) VALUES
(1, 'SorhaKhutte', 'Lazimpat', '1/13/22', '10:15 AM', 1, 2),
(2, 'Kirtipur', 'RNAC', '1/14/22', '10:20 AM', 2, 3),
(3, 'Chhabail', 'Bhaktapur', '1/14/22', '12:30 PM', 3, 3),
(4, 'Patan', 'Godavari', '1/14/22', '12:50 PM', 4, 3),
(5, 'Budhanilkantha', 'Ratnapark', '1/15/22', '03:00 PM', 4, NULL),
(6, 'Chyasal', 'Kalanki', '1/16/22', '08:00 AM', 3, NULL),
(7, 'Sanepa', 'Pulchowk', '1/16/22', '12:30 PM', 5, NULL),
(8, 'Kupandole', 'Maitighar', '1/16/22', '01:00 PM', 5, NULL),
(9, 'Kamalpokhari', 'Dillibazar', '1/17/22', '02:35 PM', 6, NULL),
(10, 'Satdobato', 'Kalanki', '1/18/22', '03:22 PM ', 7, NULL),
(11, 'Dhulikhel', 'Koteshwor', '1/18/22', '04:45 PM', 7, NULL),
(12, 'Maharajgunj', 'Shivapuri', '1/19/22', '5:50 AM', 8, NULL),
(13, 'Chandragiri', 'Lagankhel', '1/19/22', '06:00 AM', 9, NULL),
(14, 'Naxal ', 'Gyaneshwor', '1/19/22', '07:35 AM', 9, NULL),
(15, 'Baluwatar', 'Hadigaun', '1/19/22', '10:00 AM', 10, NULL),
(16, 'Sundhara', 'Samakhusi', '1/19/22', '12:00 PM', 10, NULL),
(17, 'Ekantakuna', 'Basantapur', '1/19/22', '01:00 PM', 11, NULL),
(18, 'Jamal', 'Bouddha', '1/19/22', '02:30 PM', 12, NULL),
(19, 'New Baneshwor', 'Kakani', '1/19/22', '04:00 PM', 13, NULL),
(20, 'Swayambu', 'Narayanthan', '1/19/22', '06:00 PM', 14, NULL),
(21, 'Bansbari', 'Kantipath', '1/20/22', '05:45 AM', 15, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `customer_data`
--

CREATE TABLE `customer_data` (
  `Customer_ID` int(11) NOT NULL,
  `Customer_Name` varchar(100) DEFAULT NULL,
  `Customer_Address` varchar(100) DEFAULT NULL,
  `Telephone_No` varchar(100) DEFAULT NULL,
  `Customer_Email` varchar(100) DEFAULT NULL,
  `Customer_Password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_data`
--

INSERT INTO `customer_data` (`Customer_ID`, `Customer_Name`, `Customer_Address`, `Telephone_No`, `Customer_Email`, `Customer_Password`) VALUES
(1, 'Justin Shakya', 'Sorhakhutte', '9872536587', 'jushakya@gmail.com', 'justin3245'),
(2, 'Diwas Suyal', 'Ranibari', '9826462648', 'suyaldiwas@yahoo.com', 'diwas123'),
(3, 'Sanjeet Chaudhary', 'Thasikhel', '98264628471', 'sanjeet@rediff.com', 'sanjeet234'),
(4, 'Prajjwal Veer Basnet', 'Kirtipur-02', '9808201266', 'prajjwalveerbasnet10@gmail.com', 'Prajjwal@1'),
(5, 'Abhishek Yadav', 'Kuleshwor', '9856374658', 'abijeasonyadav@gmail.com', 'abhishek321'),
(6, 'Deepak Karna', 'Bhaktapur', '9846473648', 'deepakKarna@hotmail.com', 'dpk1234'),
(7, 'Shreeya Chetani', 'Soltimode', '9826462847', 'shreeyaChetani@yahoo.com', 'shreeya123'),
(8, 'Sahil Tiwari ', 'Godavari', '9856374846', 'SahilT34@outlook.com', 'IamSahil'),
(9, 'Astha Shrestha', 'Bhaktapur', '9846473647', 'Asthaaa@kec.edu.np', 'shrAstha2233'),
(10, 'Shikshya Risal', 'Bhaisepati', '9846483648', 'shikshya@hotmail.com', 'shikshya789'),
(11, 'Deepti Khatri', 'USA', '2758575947', 'khatrideepti67@gmail.com', 'pokemon123'),
(12, 'Yatharth Shrestha', 'Balkumari', '9726485758', 'yatharthshr@gmail.com', 'genSkid'),
(13, 'Nirvik RajBhandari', 'Sanepa', '9872648474', 'nirvik66@hotmail.com', 'nirvike455'),
(14, 'Sanskar Sapkota', 'Kalanki', '9846584638', 'sanskar334@live.com', 'sanskar43'),
(15, 'Abhi Ramtel', 'Ranibari', '9846563868', 'ramtelabhi@gmail.com', 'abhi123456');

-- --------------------------------------------------------

--
-- Table structure for table `driver_information`
--

CREATE TABLE `driver_information` (
  `Driver_ID` int(11) NOT NULL,
  `Driver_Name` varchar(100) DEFAULT NULL,
  `Driver_Address` varchar(100) DEFAULT NULL,
  `Driver_Telephone` varchar(100) DEFAULT NULL,
  `Driver_Email` varchar(100) DEFAULT NULL,
  `Driver_Password` varchar(100) DEFAULT NULL,
  `License_Plate` varchar(100) DEFAULT NULL,
  `Car_Model` varchar(100) DEFAULT NULL,
  `Status` varchar(100) DEFAULT 'Pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `driver_information`
--

INSERT INTO `driver_information` (`Driver_ID`, `Driver_Name`, `Driver_Address`, `Driver_Telephone`, `Driver_Email`, `Driver_Password`, `License_Plate`, `Car_Model`, `Status`) VALUES
(1, 'Benjamin Ale', 'Budhanilkantha', '9843782727', 'aalebenjamin@gmail.com', 'benji123', 'FH9-DN9-987', 'Ford F-150', 'Active'),
(2, 'Sumedha Shakya', 'Patan', '9826454537', 'sumedha@hotmail.com', 'sumedh231', 'JD8-HNB-782', 'Tesla', 'Active'),
(3, 'Ram Kumar ', 'Lainchaur', '9856472647', 'RamKumar32@gmail.com', 'RamKumar213', 'PTY-87G-G8J', 'Maruti Suzuki', 'Active'),
(4, 'Atyush Chaudhary', 'Patan', '9826483638', 'Atyush@hotmail.com', 'atyush@456', 'PT8-FJ7-987', 'Alto', 'Active'),
(5, 'Gaurav Nepal', 'Lazimpat', '9856382746', 'GauravNepal@yahoo.com', 'Gaurav54', 'PF8-F97-FJK', 'Tesla Roadster', 'Active'),
(6, 'Harsh Agrawal', 'Chhauni', '9826485628', 'Harsh@gmail.com', 'harshTiktok23', '666-JFN-TRI', 'Tata Nano', 'Active'),
(7, 'Silan Panthi', 'Baneshwor', '9856374836', 'Iamsilan6@hotmail.com', 'malaisabaiaaucha', 'IFH-28U-FHJ', 'Tata Nano', 'Active'),
(8, 'Santosh Rokaya', 'Balkhu', '9846583648', 'rokaya@gmail.com', 'rokayasantosh123', 'IF9-FJK-DHJ', 'Maruti Suzuki', 'Active'),
(9, 'Ashim Panta', 'Kalopul', '9875646484', 'asim@hotmail.com', 'ashimGod@11', 'OF9-FH7-HFN', 'BMW', 'Active'),
(10, 'Abin Pradhananga', 'Bhaktapur', '9846846582', 'abinpradhan33@yahoo.com', 'nangaabin@34', 'OR7-FJ1-24J', 'Peugot', 'Active'),
(11, 'Santos Lamichanne', 'Swayambhu', '9846104811', 'santosboka@gmail.com', 'santosBoks', 'ES0-JHF-42P', 'Scorpio', 'Active'),
(12, 'Kshitiz Bartaula', 'Dhading', '9264917481', 'kshitiz@gmail.com', 'ksitiz123@456', 'IF9-FND-67F', 'Renault', 'Active');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking_information`
--
ALTER TABLE `booking_information`
  ADD PRIMARY KEY (`Booking_ID`),
  ADD KEY `Customer_ID` (`Customer_ID`),
  ADD KEY `booking_information_ibfk_2` (`Driver_ID`);

--
-- Indexes for table `customer_data`
--
ALTER TABLE `customer_data`
  ADD PRIMARY KEY (`Customer_ID`);

--
-- Indexes for table `driver_information`
--
ALTER TABLE `driver_information`
  ADD PRIMARY KEY (`Driver_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking_information`
--
ALTER TABLE `booking_information`
  MODIFY `Booking_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `customer_data`
--
ALTER TABLE `customer_data`
  MODIFY `Customer_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `driver_information`
--
ALTER TABLE `driver_information`
  MODIFY `Driver_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking_information`
--
ALTER TABLE `booking_information`
  ADD CONSTRAINT `booking_information_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `customer_data` (`Customer_ID`),
  ADD CONSTRAINT `booking_information_ibfk_2` FOREIGN KEY (`Driver_ID`) REFERENCES `driver_information` (`Driver_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
