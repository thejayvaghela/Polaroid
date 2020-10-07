-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 07, 2020 at 06:59 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `polaroid_test`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add post', 8, 'add_post'),
(30, 'Can change post', 8, 'change_post'),
(31, 'Can delete post', 8, 'delete_post'),
(32, 'Can view post', 8, 'view_post'),
(33, 'Can add friend', 9, 'add_friend'),
(34, 'Can change friend', 9, 'change_friend'),
(35, 'Can delete friend', 9, 'delete_friend'),
(36, 'Can view friend', 9, 'view_friend'),
(37, 'Can add like', 10, 'add_like'),
(38, 'Can change like', 10, 'change_like'),
(39, 'Can delete like', 10, 'delete_like'),
(40, 'Can view like', 10, 'view_like'),
(41, 'Can add comment', 11, 'add_comment'),
(42, 'Can change comment', 11, 'change_comment'),
(43, 'Can delete comment', 11, 'delete_comment'),
(44, 'Can view comment', 11, 'view_comment');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(11, 'polaroid', 'comment'),
(9, 'polaroid', 'friend'),
(10, 'polaroid', 'like'),
(8, 'polaroid', 'post'),
(7, 'polaroid', 'user'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-10-04 15:42:03.514441'),
(2, 'auth', '0001_initial', '2020-10-04 15:42:04.076936'),
(3, 'admin', '0001_initial', '2020-10-04 15:42:07.456958'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-10-04 15:42:08.361110'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-10-04 15:42:08.389605'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-10-04 15:42:09.329509'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-10-04 15:42:10.255218'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-10-04 15:42:10.552955'),
(9, 'auth', '0004_alter_user_username_opts', '2020-10-04 15:42:10.579299'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-10-04 15:42:10.738124'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-10-04 15:42:10.759702'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-10-04 15:42:10.784641'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-10-04 15:42:11.040358'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-10-04 15:42:11.297278'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-10-04 15:42:11.815855'),
(16, 'auth', '0011_update_proxy_permissions', '2020-10-04 15:42:11.843243'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2020-10-04 15:42:12.068369'),
(18, 'polaroid', '0001_initial', '2020-10-04 15:42:12.167980'),
(19, 'polaroid', '0002_auto_20200427_1417', '2020-10-04 15:42:14.582427'),
(20, 'polaroid', '0003_auto_20200427_1423', '2020-10-04 15:42:15.121029'),
(21, 'polaroid', '0004_auto_20200427_1436', '2020-10-04 15:42:16.270447'),
(22, 'polaroid', '0005_auto_20200427_1438', '2020-10-04 15:42:16.548811'),
(23, 'polaroid', '0006_auto_20200427_1535', '2020-10-04 15:42:16.875309'),
(24, 'polaroid', '0007_auto_20200427_1547', '2020-10-04 15:42:16.900933'),
(25, 'polaroid', '0008_auto_20200427_1858', '2020-10-04 15:42:17.091552'),
(26, 'polaroid', '0009_auto_20200427_1910', '2020-10-04 15:42:17.118293'),
(27, 'polaroid', '0010_auto_20200428_1250', '2020-10-04 15:42:17.145910'),
(28, 'polaroid', '0011_auto_20200428_1327', '2020-10-04 15:42:17.178839'),
(29, 'polaroid', '0012_auto_20200428_2308', '2020-10-04 15:42:19.386225'),
(30, 'polaroid', '0013_auto_20200430_1145', '2020-10-04 15:42:19.405593'),
(31, 'polaroid', '0014_auto_20200430_1146', '2020-10-04 15:42:19.448231'),
(32, 'polaroid', '0015_auto_20200430_1155', '2020-10-04 15:42:19.472528'),
(33, 'polaroid', '0016_auto_20200430_1156', '2020-10-04 15:42:19.499834'),
(34, 'polaroid', '0017_auto_20200430_1338', '2020-10-04 15:42:19.862617'),
(35, 'polaroid', '0018_auto_20200430_1342', '2020-10-04 15:42:19.889299'),
(36, 'polaroid', '0019_auto_20200430_1541', '2020-10-04 15:42:19.967490'),
(37, 'polaroid', '0020_auto_20200430_1546', '2020-10-04 15:42:20.119206'),
(38, 'polaroid', '0021_auto_20200430_1551', '2020-10-04 15:42:20.384673'),
(39, 'polaroid', '0022_auto_20200430_1552', '2020-10-04 15:42:21.246083'),
(40, 'polaroid', '0023_auto_20200430_1553', '2020-10-04 15:42:21.271717'),
(41, 'polaroid', '0024_user_bio', '2020-10-04 15:42:21.462283'),
(42, 'polaroid', '0025_auto_20200501_2302', '2020-10-04 15:42:21.497115'),
(43, 'polaroid', '0026_auto_20200501_2305', '2020-10-04 15:42:21.590894'),
(44, 'polaroid', '0027_auto_20200501_2306', '2020-10-04 15:42:21.657696'),
(45, 'polaroid', '0028_auto_20200501_2315', '2020-10-04 15:42:21.716315'),
(46, 'polaroid', '0029_auto_20200502_1117', '2020-10-04 15:42:21.749580'),
(47, 'polaroid', '0030_post', '2020-10-04 15:42:21.932108'),
(48, 'polaroid', '0031_friend', '2020-10-04 15:42:22.535335'),
(49, 'polaroid', '0032_delete_friend', '2020-10-04 15:42:24.295585'),
(50, 'polaroid', '0033_friend', '2020-10-04 15:42:24.416701'),
(51, 'polaroid', '0034_friend_request_pending', '2020-10-04 15:42:25.300643'),
(52, 'polaroid', '0035_auto_20200508_1756', '2020-10-04 15:42:26.760560'),
(53, 'polaroid', '0036_auto_20200510_1534', '2020-10-04 15:42:28.472230'),
(54, 'polaroid', '0037_like', '2020-10-04 15:42:28.734853'),
(55, 'polaroid', '0038_auto_20200514_1427', '2020-10-04 15:42:30.886216'),
(56, 'polaroid', '0039_auto_20200514_2329', '2020-10-04 15:42:32.325627'),
(57, 'polaroid', '0040_like_post_owner', '2020-10-04 15:42:34.497864'),
(58, 'polaroid', '0041_delete_like', '2020-10-04 15:42:36.310663'),
(59, 'polaroid', '0042_like', '2020-10-04 15:42:36.608393'),
(60, 'polaroid', '0043_auto_20200515_1219', '2020-10-04 15:43:09.627647'),
(61, 'polaroid', '0044_auto_20200515_1517', '2020-10-04 15:43:10.392717'),
(62, 'polaroid', '0045_delete_like', '2020-10-04 15:43:13.108403'),
(63, 'polaroid', '0046_post_likes', '2020-10-04 15:43:13.383800'),
(64, 'polaroid', '0047_auto_20200516_2214', '2020-10-04 15:43:15.835080'),
(65, 'polaroid', '0048_comment', '2020-10-04 15:43:17.966183'),
(66, 'polaroid', '0049_auto_20200518_1711', '2020-10-04 15:43:20.273892'),
(67, 'polaroid', '0050_auto_20200518_1714', '2020-10-04 15:43:20.332578'),
(68, 'polaroid', '0051_auto_20200518_1731', '2020-10-04 15:43:20.367547'),
(69, 'polaroid', '0052_auto_20200518_1936', '2020-10-04 15:43:20.409965'),
(70, 'polaroid', '0053_auto_20200518_1943', '2020-10-04 15:43:20.460925'),
(71, 'polaroid', '0054_auto_20200518_1946', '2020-10-04 15:43:20.511670'),
(72, 'polaroid', '0055_auto_20200518_2002', '2020-10-04 15:43:20.587379'),
(73, 'polaroid', '0056_auto_20200518_2003', '2020-10-04 15:43:20.667957'),
(74, 'polaroid', '0057_auto_20200519_1214', '2020-10-04 15:43:20.784346'),
(75, 'polaroid', '0058_auto_20200519_1216', '2020-10-04 15:43:20.927528'),
(76, 'polaroid', '0059_auto_20200519_1224', '2020-10-04 15:43:21.032532'),
(77, 'polaroid', '0060_auto_20200519_1230', '2020-10-04 15:43:21.099647'),
(78, 'polaroid', '0061_auto_20200519_1931', '2020-10-04 15:43:32.310392'),
(79, 'sessions', '0001_initial', '2020-10-04 15:43:32.462970'),
(80, 'polaroid', '0062_user_verified', '2020-10-07 13:16:57.323568');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2mhyzh28alguklbv2x8aqp31sudt232u', '.eJxFzMEKwjAMxvFXkZw32ApFsxcQdxW8SrR1rXSpdOlBxHc3PXnMj_-XD_iVYoKJa0odPGLZ5Mq0epjgvJuhg0R_udASfCJVl296j7gf-8H0xirdo7zV5sq0kAsqm5C02bE-qZC0JleW0rITu9gevULm1uDBWItocYDvD6OsLTE:1kQBxu:CYq1b96XECj6ZLKp0UTbLBZWvspxfx4azaRvQKvdbSM', '2020-10-21 16:06:54.958903'),
('e1ldgbsnnnypfb0f4y892l7ejvr8hz44', '.eJxFjEEKAjEMRe-StUrrIBZX7kQP4FbitLYdOq10UqGIdzfBhZDNf7yXN7gZY4IDUHAT9hf64BIevdDNWGZYwSPWhW4ZZ8faBTujhH9y_SVMbbnz3iql1krzMRojdalaRo82MFkISbJTm7AiiVNapiraOdsoj56hZHHU3mhj9KCHHXy-wzw1Pg:1kQAJ7:mT6BBtDMx4VQ5viF0t60-ZoW7YPPoXQQJ9i1JQOzJsM', '2020-10-21 14:20:41.860250');

-- --------------------------------------------------------

--
-- Table structure for table `polaroid_comment`
--

CREATE TABLE `polaroid_comment` (
  `commentid` int(11) NOT NULL,
  `content` varchar(100) DEFAULT NULL,
  `postid_id` int(11) NOT NULL,
  `userid_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `polaroid_friend`
--

CREATE TABLE `polaroid_friend` (
  `id` int(11) NOT NULL,
  `friends` tinyint(1) NOT NULL,
  `request_from_id` varchar(100) DEFAULT NULL,
  `request_pending` tinyint(1) NOT NULL,
  `user1_id` varchar(100) DEFAULT NULL,
  `user2_id` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `polaroid_like`
--

CREATE TABLE `polaroid_like` (
  `likeid` int(11) NOT NULL,
  `postid_id` int(11) NOT NULL,
  `userid_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `polaroid_post`
--

CREATE TABLE `polaroid_post` (
  `postid` int(11) NOT NULL,
  `postpic` varchar(100) NOT NULL,
  `postcaption` varchar(100) NOT NULL,
  `posttime` datetime(6) NOT NULL,
  `user_email_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `polaroid_user`
--

CREATE TABLE `polaroid_user` (
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `phone` varchar(128) DEFAULT NULL,
  `profilepic` varchar(100) NOT NULL,
  `bio` varchar(100) DEFAULT NULL,
  `verified` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `polaroid_comment`
--
ALTER TABLE `polaroid_comment`
  ADD PRIMARY KEY (`commentid`),
  ADD KEY `polaroid_comment_postid_id_b9ce8de1_fk_polaroid_post_postid` (`postid_id`),
  ADD KEY `polaroid_comment_userid_id_26e13a78_fk` (`userid_id`);

--
-- Indexes for table `polaroid_friend`
--
ALTER TABLE `polaroid_friend`
  ADD PRIMARY KEY (`id`),
  ADD KEY `polaroid_friend_request_from_id_ea09cd8c_fk` (`request_from_id`),
  ADD KEY `polaroid_friend_user1_id_8977d582_fk` (`user1_id`),
  ADD KEY `polaroid_friend_user2_id_f2aabcaa_fk` (`user2_id`);

--
-- Indexes for table `polaroid_like`
--
ALTER TABLE `polaroid_like`
  ADD PRIMARY KEY (`likeid`),
  ADD KEY `polaroid_like_postid_id_bc35061f_fk_polaroid_post_postid` (`postid_id`),
  ADD KEY `polaroid_like_userid_id_9c794a7e_fk` (`userid_id`);

--
-- Indexes for table `polaroid_post`
--
ALTER TABLE `polaroid_post`
  ADD PRIMARY KEY (`postid`),
  ADD KEY `polaroid_post_user_email_id_d869dbd7_fk` (`user_email_id`);

--
-- Indexes for table `polaroid_user`
--
ALTER TABLE `polaroid_user`
  ADD PRIMARY KEY (`user_email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `polaroid_comment`
--
ALTER TABLE `polaroid_comment`
  MODIFY `commentid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `polaroid_friend`
--
ALTER TABLE `polaroid_friend`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `polaroid_like`
--
ALTER TABLE `polaroid_like`
  MODIFY `likeid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `polaroid_post`
--
ALTER TABLE `polaroid_post`
  MODIFY `postid` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `polaroid_comment`
--
ALTER TABLE `polaroid_comment`
  ADD CONSTRAINT `polaroid_comment_postid_id_b9ce8de1_fk_polaroid_post_postid` FOREIGN KEY (`postid_id`) REFERENCES `polaroid_post` (`postid`),
  ADD CONSTRAINT `polaroid_comment_userid_id_26e13a78_fk` FOREIGN KEY (`userid_id`) REFERENCES `polaroid_user` (`user_email`);

--
-- Constraints for table `polaroid_friend`
--
ALTER TABLE `polaroid_friend`
  ADD CONSTRAINT `polaroid_friend_request_from_id_ea09cd8c_fk` FOREIGN KEY (`request_from_id`) REFERENCES `polaroid_user` (`user_email`),
  ADD CONSTRAINT `polaroid_friend_user1_id_8977d582_fk` FOREIGN KEY (`user1_id`) REFERENCES `polaroid_user` (`user_email`),
  ADD CONSTRAINT `polaroid_friend_user2_id_f2aabcaa_fk` FOREIGN KEY (`user2_id`) REFERENCES `polaroid_user` (`user_email`);

--
-- Constraints for table `polaroid_like`
--
ALTER TABLE `polaroid_like`
  ADD CONSTRAINT `polaroid_like_postid_id_bc35061f_fk_polaroid_post_postid` FOREIGN KEY (`postid_id`) REFERENCES `polaroid_post` (`postid`),
  ADD CONSTRAINT `polaroid_like_userid_id_9c794a7e_fk` FOREIGN KEY (`userid_id`) REFERENCES `polaroid_user` (`user_email`);

--
-- Constraints for table `polaroid_post`
--
ALTER TABLE `polaroid_post`
  ADD CONSTRAINT `polaroid_post_user_email_id_d869dbd7_fk` FOREIGN KEY (`user_email_id`) REFERENCES `polaroid_user` (`user_email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
