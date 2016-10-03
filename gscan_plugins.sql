-- phpMyAdmin SQL Dump
-- version 4.4.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2016-10-03 02:10:27
-- 服务器版本： 5.5.49-0+deb7u1
-- PHP Version: 5.4.45-0+deb7u2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `GScan`
--

-- --------------------------------------------------------

--
-- 表的结构 `gscan_plugins`
--

CREATE TABLE IF NOT EXISTS `gscan_plugins` (
  `id` int(11) NOT NULL,
  `path` longtext NOT NULL,
  `description` longtext NOT NULL,
  `name` longtext,
  `port` longtext NOT NULL,
  `type` longtext NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `gscan_plugins`
--

INSERT INTO `gscan_plugins` (`id`, `path`, `description`, `name`, `port`, `type`) VALUES
(1, 'ssh_crack.py', 'SSH_crack', 'SSH_crack', '80', 'Service'),
(2, 'ftp_crack.py', 'ftp_crack', 'ftp_crack', '21', 'Service'),
(3, 'mongodb_check.py', 'mongodb_check', 'mongodb_check', '27017', 'Service'),
(4, 'mysql_crack.py', 'mysql_crack', 'mysql_crack', '3306', 'Service'),
(5, 'pma_crack.py', 'pma_crack', 'pma_crack', '80', 'Web'),
(6, 'redis_crack.py', 'redis_crack', 'redis_crack', '6379', 'Service'),
(7, 'rsync_check.py', 'rsync_check', 'rsync_check', '873', 'Service');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gscan_plugins`
--
ALTER TABLE `gscan_plugins`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gscan_plugins`
--
ALTER TABLE `gscan_plugins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
