-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 11, 2021 at 04:26 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `icd`
--

-- --------------------------------------------------------

--
-- Table structure for table `icd_codes`
--
DROP DATABASE IF EXISTS icd;
CREATE DATABASE icd;
use icd;
CREATE TABLE `icd_codes` (
  `id` int(11) NOT NULL,
  `category_code` varchar(100) NOT NULL,
  `icd_diagnosis_code` varchar(100) NOT NULL,
  `full_icd_code` varchar(100) NOT NULL,
  `abbreviated_description` text NOT NULL,
  `full_description` text NOT NULL,
  `category_title` text NOT NULL,
  `icd_type_id` int(11) NOT NULL,
  `status` char(10) NOT NULL DEFAULT 'active',
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `update_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `icd_codes`
--

INSERT INTO `icd_codes` (`id`, `category_code`, `icd_diagnosis_code`, `full_icd_code`, `abbreviated_description`, `full_description`, `category_title`, `icd_type_id`, `status`, `created_at`, `update_at`) VALUES
(1, 'A0', '1234', 'A01234', 'Comma-ind anal ret test', 'Comma-induced anal retention', 'Malignant neoplasm of anus and anal canal', 1, 'inactive', '2021-01-10 15:32:56', '2021-01-10 15:32:56'),
(2, 'A0', '1234', 'A01237', 'Comma-ind anal ret', 'Comma-induced anal retention', 'Malignant neoplasm of anus and anal canal', 1, 'inactive', '2021-01-10 15:33:40', '2021-01-10 15:32:56'),
(3, 'A0', '1234', 'A01239', 'Comma-ind anal ret', 'Comma-induced anal retention', 'Malignant neoplasm of anus and anal canal', 1, 'inactive', '2021-01-10 15:34:59', '2021-01-10 15:32:56'),
(4, 'A0', '1234', 'A01236', 'Comma-ind anal ret', 'Comma-induced anal retention', 'Malignant neoplasm of anus and anal canal', 1, 'inactive', '2021-01-10 15:35:45', '2021-01-10 15:32:56'),
(5, 'A00', '1235', 'A001235', 'Comma-ind anal dop', 'Comma-induced anal retention', 'Malignant neoplasm of anus and anal canal', 1, 'active', '2021-01-11 00:55:01', '2021-01-10 15:32:56'),
(6, 'A01', '1238', 'A011238', 'Comma-ind anal dop', 'Comma-induced anal retention', 'Malignant neoplasm of anus and anal canal', 1, 'active', '2021-01-11 01:05:22', '2021-01-10 15:32:56');

-- --------------------------------------------------------

--
-- Table structure for table `icd_records`
--

CREATE TABLE `icd_records` (
  `id` int(11) NOT NULL,
  `icd_name` char(20) NOT NULL,
  `icd_min_length` int(11) NOT NULL,
  `icd_max_length` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` date NOT NULL,
  `status` char(10) NOT NULL DEFAULT 'active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `icd_records`
--

INSERT INTO `icd_records` (`id`, `icd_name`, `icd_min_length`, `icd_max_length`, `created_at`, `updated_at`, `status`) VALUES
(1, 'ICD-10', 3, 7, '2021-01-09 22:01:36', '0000-00-00', 'active'),
(2, 'ICD-9', 3, 5, '2021-01-09 22:01:36', '0000-00-00', 'active');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `icd_codes`
--
ALTER TABLE `icd_codes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `icd_type_id` (`icd_type_id`);

--
-- Indexes for table `icd_records`
--
ALTER TABLE `icd_records`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `icd_name` (`icd_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `icd_codes`
--
ALTER TABLE `icd_codes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `icd_records`
--
ALTER TABLE `icd_records`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
