/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80025
 Source Host           : localhost:3306
 Source Schema         : materials_system

 Target Server Type    : MySQL
 Target Server Version : 80025
 File Encoding         : 65001

 Date: 29/08/2022 09:55:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
BEGIN;
INSERT INTO `auth_group` (`id`, `name`) VALUES (5, '主管科室');
INSERT INTO `auth_group` (`id`, `name`) VALUES (3, '仓库管理员');
INSERT INTO `auth_group` (`id`, `name`) VALUES (4, '供应商');
INSERT INTO `auth_group` (`id`, `name`) VALUES (1, '分管领导');
INSERT INTO `auth_group` (`id`, `name`) VALUES (2, '局长');
COMMIT;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
BEGIN;
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (56, 1, 41);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (58, 1, 45);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (60, 1, 49);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (67, 1, 95);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (66, 1, 97);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (55, 1, 101);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (57, 1, 105);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (59, 1, 109);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (63, 1, 113);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (61, 1, 114);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (62, 1, 115);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (64, 1, 117);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (65, 1, 121);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (1, 2, 12);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (2, 2, 16);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (3, 2, 20);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (4, 2, 24);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (5, 2, 29);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (6, 2, 33);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (7, 2, 37);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (8, 2, 41);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (9, 2, 53);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (10, 2, 57);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (11, 2, 65);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (12, 2, 69);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (13, 2, 73);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (14, 2, 77);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (15, 2, 81);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (16, 2, 85);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (17, 2, 89);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (18, 2, 93);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (68, 2, 95);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (19, 2, 97);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (20, 2, 101);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (69, 2, 103);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (21, 2, 105);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (22, 2, 109);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (23, 2, 113);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (70, 2, 115);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (24, 2, 117);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (25, 2, 121);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (30, 3, 57);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (161, 3, 65);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (26, 3, 69);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (160, 3, 73);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (27, 3, 74);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (28, 3, 75);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (29, 3, 77);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (162, 3, 85);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (31, 3, 90);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (32, 3, 91);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (33, 3, 92);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (34, 3, 93);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (51, 4, 17);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (52, 4, 18);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (53, 4, 19);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (54, 4, 20);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (49, 4, 21);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (50, 4, 22);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (48, 4, 24);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (47, 4, 29);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (35, 4, 33);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (37, 4, 37);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (38, 4, 38);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (39, 4, 39);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (40, 4, 40);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (41, 4, 41);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (42, 4, 42);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (43, 4, 43);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (44, 4, 44);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (45, 4, 45);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (46, 4, 49);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (71, 5, 17);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (72, 5, 18);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (73, 5, 19);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (74, 5, 20);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (75, 5, 21);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (76, 5, 22);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (77, 5, 23);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (78, 5, 24);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (79, 5, 25);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (80, 5, 26);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (81, 5, 27);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (82, 5, 28);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (83, 5, 29);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (84, 5, 30);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (85, 5, 31);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (86, 5, 32);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (87, 5, 33);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (88, 5, 34);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (89, 5, 35);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (90, 5, 36);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (91, 5, 37);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (92, 5, 38);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (93, 5, 39);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (94, 5, 40);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (95, 5, 41);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (96, 5, 42);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (97, 5, 43);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (98, 5, 44);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (99, 5, 45);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (100, 5, 46);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (101, 5, 47);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (102, 5, 48);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (103, 5, 49);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (104, 5, 50);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (105, 5, 51);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (106, 5, 52);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (107, 5, 53);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (108, 5, 57);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (109, 5, 61);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (110, 5, 62);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (111, 5, 63);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (112, 5, 64);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (113, 5, 65);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (114, 5, 66);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (115, 5, 67);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (116, 5, 68);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (117, 5, 69);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (118, 5, 70);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (119, 5, 71);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (120, 5, 72);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (121, 5, 73);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (122, 5, 74);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (123, 5, 75);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (124, 5, 76);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (125, 5, 77);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (126, 5, 78);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (127, 5, 79);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (128, 5, 80);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (129, 5, 81);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (130, 5, 82);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (131, 5, 83);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (132, 5, 84);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (133, 5, 85);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (134, 5, 90);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (135, 5, 91);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (136, 5, 92);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (137, 5, 93);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (138, 5, 94);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (139, 5, 95);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (140, 5, 96);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (141, 5, 97);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (142, 5, 98);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (143, 5, 99);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (144, 5, 100);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (145, 5, 101);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (146, 5, 102);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (147, 5, 103);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (148, 5, 104);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (149, 5, 105);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (150, 5, 106);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (151, 5, 107);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (152, 5, 108);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (153, 5, 109);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (154, 5, 113);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (155, 5, 114);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (156, 5, 115);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (157, 5, 116);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (158, 5, 117);
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES (159, 5, 121);
COMMIT;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (1, 'Can add permission', 1, 'add_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (2, 'Can change permission', 1, 'change_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (3, 'Can delete permission', 1, 'delete_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (4, 'Can view permission', 1, 'view_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (5, 'Can add group', 2, 'add_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (6, 'Can change group', 2, 'change_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (7, 'Can delete group', 2, 'delete_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (8, 'Can view group', 2, 'view_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (9, 'Can add user', 3, 'add_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (10, 'Can change user', 3, 'change_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (11, 'Can delete user', 3, 'delete_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (12, 'Can view user', 3, 'view_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (17, 'Can add 物料库存', 5, 'add_locallabrarymaterials');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (18, 'Can change 物料库存', 5, 'change_locallabrarymaterials');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (19, 'Can delete 物料库存', 5, 'delete_locallabrarymaterials');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (20, 'Can view 物料库存', 5, 'view_locallabrarymaterials');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (21, 'Can add 入库单', 6, 'add_locallibrary');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (22, 'Can change 入库单', 6, 'change_locallibrary');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (23, 'Can delete 入库单', 6, 'delete_locallibrary');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (24, 'Can view 入库单', 6, 'view_locallibrary');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (25, '是否可以审核入库单', 6, 'can_approve');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (26, 'Can add 地方库库出库单', 7, 'add_localoutboundorder');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (27, 'Can change 地方库库出库单', 7, 'change_localoutboundorder');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (28, 'Can delete 地方库库出库单', 7, 'delete_localoutboundorder');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (29, 'Can view 地方库库出库单', 7, 'view_localoutboundorder');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (30, 'Can add 地方库库出库单详情', 8, 'add_localoutboundorderdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (31, 'Can change 地方库库出库单详情', 8, 'change_localoutboundorderdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (32, 'Can delete 地方库库出库单详情', 8, 'delete_localoutboundorderdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (33, 'Can view 地方库库出库单详情', 8, 'view_localoutboundorderdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (34, 'Can add 地方库', 9, 'add_suppliermessage');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (35, 'Can change 地方库', 9, 'change_suppliermessage');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (36, 'Can delete 地方库', 9, 'delete_suppliermessage');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (37, 'Can view 地方库', 9, 'view_suppliermessage');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (38, 'Can add (供应商附件)', 10, 'add_supplierfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (39, 'Can change (供应商附件)', 10, 'change_supplierfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (40, 'Can delete (供应商附件)', 10, 'delete_supplierfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (41, 'Can view (供应商附件)', 10, 'view_supplierfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (42, 'Can add (采购计划、政府采购批复、投标手续)', 11, 'add_localwarehousingfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (43, 'Can change (采购计划、政府采购批复、投标手续)', 11, 'change_localwarehousingfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (44, 'Can delete (采购计划、政府采购批复、投标手续)', 11, 'delete_localwarehousingfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (45, 'Can view (采购计划、政府采购批复、投标手续)', 11, 'view_localwarehousingfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (46, 'Can add 审批记录', 12, 'add_localoutboundorderhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (47, 'Can change 审批记录', 12, 'change_localoutboundorderhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (48, 'Can delete 审批记录', 12, 'delete_localoutboundorderhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (49, 'Can view 审批记录', 12, 'view_localoutboundorderhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (50, 'Can add 入库明细', 13, 'add_centerlabrarymaterials');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (51, 'Can change 入库明细', 13, 'change_centerlabrarymaterials');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (52, 'Can delete 入库明细', 13, 'delete_centerlabrarymaterials');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (53, 'Can view 入库明细', 13, 'view_centerlabrarymaterials');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (54, 'Can add 物料库存', 14, 'add_centerlabraryquantity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (55, 'Can change 物料库存', 14, 'change_centerlabraryquantity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (56, 'Can delete 物料库存', 14, 'delete_centerlabraryquantity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (57, 'Can view 物料库存', 14, 'view_centerlabraryquantity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (58, 'Can add 中央库基本信息', 15, 'add_centerlibrary');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (59, 'Can change 中央库基本信息', 15, 'change_centerlibrary');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (60, 'Can delete 中央库基本信息', 15, 'delete_centerlibrary');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (61, 'Can view 中央库基本信息', 15, 'view_centerlibrary');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (62, 'Can add 中央库附件', 16, 'add_centerlibraryfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (63, 'Can change 中央库附件', 16, 'change_centerlibraryfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (64, 'Can delete 中央库附件', 16, 'delete_centerlibraryfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (65, 'Can view 中央库附件', 16, 'view_centerlibraryfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (66, 'Can add 中央库出库单', 17, 'add_centeroutboundorder');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (67, 'Can change 中央库出库单', 17, 'change_centeroutboundorder');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (68, 'Can delete 中央库出库单', 17, 'delete_centeroutboundorder');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (69, 'Can view 中央库出库单', 17, 'view_centeroutboundorder');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (70, 'Can add 中央库出库单详情', 18, 'add_centeroutboundorderdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (71, 'Can change 中央库出库单详情', 18, 'change_centeroutboundorderdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (72, 'Can delete 中央库出库单详情', 18, 'delete_centeroutboundorderdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (73, 'Can view 中央库出库单详情', 18, 'view_centeroutboundorderdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (74, 'Can add 入库单', 19, 'add_centerwarehousingapplication');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (75, 'Can change 入库单', 19, 'change_centerwarehousingapplication');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (76, 'Can delete 入库单', 19, 'delete_centerwarehousingapplication');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (77, 'Can view 入库单', 19, 'view_centerwarehousingapplication');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (78, 'Can add (采购计划、政府采购批复、投标手续)等附件', 20, 'add_centerwarehousingfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (79, 'Can change (采购计划、政府采购批复、投标手续)等附件', 20, 'change_centerwarehousingfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (80, 'Can delete (采购计划、政府采购批复、投标手续)等附件', 20, 'delete_centerwarehousingfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (81, 'Can view (采购计划、政府采购批复、投标手续)等附件', 20, 'view_centerwarehousingfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (82, 'Can add 审批记录', 21, 'add_centeroutboundorderhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (83, 'Can change 审批记录', 21, 'change_centeroutboundorderhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (84, 'Can delete 审批记录', 21, 'delete_centeroutboundorderhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (85, 'Can view 审批记录', 21, 'view_centeroutboundorderhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (86, 'Can add 单号自增表', 22, 'add_codenumber');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (87, 'Can change 单号自增表', 22, 'change_codenumber');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (88, 'Can delete 单号自增表', 22, 'delete_codenumber');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (89, 'Can view 单号自增表', 22, 'view_codenumber');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (90, 'Can add 物料种类', 23, 'add_materialstype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (91, 'Can change 物料种类', 23, 'change_materialstype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (92, 'Can delete 物料种类', 23, 'delete_materialstype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (93, 'Can view 物料种类', 23, 'view_materialstype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (94, 'Can add 出库申请', 24, 'add_exwarehousingapplication');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (95, 'Can change 出库申请', 24, 'change_exwarehousingapplication');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (96, 'Can delete 出库申请', 24, 'delete_exwarehousingapplication');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (97, 'Can view 出库申请', 24, 'view_exwarehousingapplication');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (98, 'Can add 地方库研判', 25, 'add_localassessmentdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (99, 'Can change 地方库研判', 25, 'change_localassessmentdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (100, 'Can delete 地方库研判', 25, 'delete_localassessmentdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (101, 'Can view 地方库研判', 25, 'view_localassessmentdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (102, 'Can add 申请资料', 26, 'add_exapplicationfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (103, 'Can change 申请资料', 26, 'change_exapplicationfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (104, 'Can delete 申请资料', 26, 'delete_exapplicationfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (105, 'Can view 申请资料', 26, 'view_exapplicationfile');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (106, 'Can add 中央库研判', 27, 'add_centerassessmentdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (107, 'Can change 中央库研判', 27, 'change_centerassessmentdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (108, 'Can delete 中央库研判', 27, 'delete_centerassessmentdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (109, 'Can view 中央库研判', 27, 'view_centerassessmentdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (110, 'Can add 审批记录', 28, 'add_applicationhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (111, 'Can change 审批记录', 28, 'change_applicationhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (112, 'Can delete 审批记录', 28, 'delete_applicationhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (113, 'Can view 审批记录', 28, 'view_applicationhistory');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (114, 'Can add 领用详情', 29, 'add_applicationdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (115, 'Can change 领用详情', 29, 'change_applicationdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (116, 'Can delete 领用详情', 29, 'delete_applicationdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (117, 'Can view 领用详情', 29, 'view_applicationdetail');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (118, 'Can add 台账', 30, 'add_accounts');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (119, 'Can change 台账', 30, 'change_accounts');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (120, 'Can delete 台账', 30, 'delete_accounts');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (121, 'Can view 台账', 30, 'view_accounts');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (122, 'Can add log entry', 31, 'add_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (123, 'Can change log entry', 31, 'change_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (124, 'Can delete log entry', 31, 'delete_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (125, 'Can view log entry', 31, 'view_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (126, 'Can add session', 32, 'add_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (127, 'Can change session', 32, 'change_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (128, 'Can delete session', 32, 'delete_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (129, 'Can view session', 32, 'view_session');
COMMIT;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
BEGIN;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES (1, 'pbkdf2_sha256$390000$hEzGAdVGGngMgvEGc6wFb4$PHVoerzuXRDf3bfOSSxxphbRIwvwqmSXQh++hBMc83A=', '2022-08-28 22:55:14.440379', 1, 'admin', 'admin', '', 'admin@qq.com', 1, 1, '2022-08-27 17:45:50.513497');
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES (2, 'pbkdf2_sha256$390000$x1pRHJ4dhpma7F0izNvILP$/MCLTOSFP+IRu3ESOZhauCO/ci2pHD6c3i91y+l85Sg=', '2022-08-27 18:43:10.512844', 0, 'ybkb', 'ybkb', '', 'ybkb@qq.com', 1, 1, '2022-08-27 17:45:00.000000');
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES (3, 'pbkdf2_sha256$390000$pXMH6fcIQOhKyW1qWdn6Y8$5oS23kuUIR3UP/PbvIiK8deGHE5lmKdeeaTBpn4OYvM=', '2022-08-27 19:43:04.067440', 0, 'ybkb1', 'ybkb1', '', 'ybkb1@qq.com', 1, 1, '2022-08-27 17:45:00.000000');
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES (4, 'pbkdf2_sha256$390000$IbL4R6OogKpGC23LZMwwo7$hI0dSH6GqYY1i45Sy5vJjvWMQ2ASxcLVH8KiuYf5dJM=', '2022-08-27 20:28:41.378775', 0, 'ybkb2', 'ybkb2', '', 'ybkb2@qq.com', 1, 1, '2022-08-27 17:45:00.000000');
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES (5, 'pbkdf2_sha256$390000$uLx8gN9wu9uaDlrhMy6NTN$qM0kMd8oTGNCufvWus4iHU8IlDU8aGv5mSdVR389ikc=', '2022-08-28 18:01:31.960757', 0, 'ybkb3', 'ybkb3', '', 'ybkb3@qq.com', 1, 1, '2022-08-27 17:45:00.000000');
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES (6, 'pbkdf2_sha256$390000$vjvbm7Jsk56JyAglLQ5l1R$Snqry4BZrH3x80t7k7MHNq4N2Kk5bJ1gCwD+bF9r644=', '2022-08-27 17:45:00.000000', 0, 'ybkb4', 'ybkb4', '', 'ybkb4@qq.com', 1, 1, '2022-08-27 17:45:00.000000');
COMMIT;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
BEGIN;
INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES (1, 2, 4);
INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES (2, 3, 1);
INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES (3, 4, 2);
INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES (4, 5, 5);
INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES (5, 6, 3);
COMMIT;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for center_library_centerlabrarymaterials
-- ----------------------------
DROP TABLE IF EXISTS `center_library_centerlabrarymaterials`;
CREATE TABLE `center_library_centerlabrarymaterials` (
  `id` int NOT NULL AUTO_INCREMENT,
  `put_num` int NOT NULL,
  `unit_price` double NOT NULL,
  `total_price` double NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `type_name_id` int NOT NULL,
  `ware_app_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `center_library_centerlab_ware_app_id_type_name_id_8e34d0e9_uniq` (`ware_app_id`,`type_name_id`),
  KEY `center_library_cente_type_name_id_65c570bc_fk_home_mate` (`type_name_id`),
  CONSTRAINT `center_library_cente_type_name_id_65c570bc_fk_home_mate` FOREIGN KEY (`type_name_id`) REFERENCES `home_materialstype` (`id`),
  CONSTRAINT `center_library_cente_ware_app_id_b0763954_fk_center_li` FOREIGN KEY (`ware_app_id`) REFERENCES `center_library_centerwarehousingapplication` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of center_library_centerlabrarymaterials
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for center_library_centerlabraryquantity
-- ----------------------------
DROP TABLE IF EXISTS `center_library_centerlabraryquantity`;
CREATE TABLE `center_library_centerlabraryquantity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `put_num` int NOT NULL,
  `push_num` int NOT NULL,
  `balance_num` int NOT NULL,
  `total_price` double NOT NULL,
  `out_price` double NOT NULL,
  `type_name_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type_name_id` (`type_name_id`),
  CONSTRAINT `center_library_cente_type_name_id_45f74ba3_fk_home_mate` FOREIGN KEY (`type_name_id`) REFERENCES `home_materialstype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of center_library_centerlabraryquantity
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for center_library_centerlibrary
-- ----------------------------
DROP TABLE IF EXISTS `center_library_centerlibrary`;
CREATE TABLE `center_library_centerlibrary` (
  `id` int NOT NULL AUTO_INCREMENT,
  `library_name` varchar(100) NOT NULL,
  `total_budget` double NOT NULL,
  `des` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `create_user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `library_name` (`library_name`),
  KEY `center_library_cente_create_user_id_44bd51b4_fk_auth_user` (`create_user_id`),
  CONSTRAINT `center_library_cente_create_user_id_44bd51b4_fk_auth_user` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of center_library_centerlibrary
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for center_library_centerlibraryfile
-- ----------------------------
DROP TABLE IF EXISTS `center_library_centerlibraryfile`;
CREATE TABLE `center_library_centerlibraryfile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `library_name_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `center_library_cente_library_name_id_314b15da_fk_center_li` (`library_name_id`),
  CONSTRAINT `center_library_cente_library_name_id_314b15da_fk_center_li` FOREIGN KEY (`library_name_id`) REFERENCES `center_library_centerlibrary` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of center_library_centerlibraryfile
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for center_library_centeroutboundorder
-- ----------------------------
DROP TABLE IF EXISTS `center_library_centeroutboundorder`;
CREATE TABLE `center_library_centeroutboundorder` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `total_price` double NOT NULL,
  `applicant` varchar(100) NOT NULL,
  `applicant_user` varchar(100) NOT NULL,
  `des` varchar(100) NOT NULL,
  `is_ex` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `app_code_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `applicant_user` (`applicant_user`),
  UNIQUE KEY `app_code_id` (`app_code_id`),
  CONSTRAINT `center_library_cente_app_code_id_de5cf767_fk_material_` FOREIGN KEY (`app_code_id`) REFERENCES `material_application_exwarehousingapplication` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of center_library_centeroutboundorder
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for center_library_centeroutboundorderdetail
-- ----------------------------
DROP TABLE IF EXISTS `center_library_centeroutboundorderdetail`;
CREATE TABLE `center_library_centeroutboundorderdetail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `number` int NOT NULL,
  `app_code_id` int NOT NULL,
  `assessment_detail_id` int NOT NULL,
  `total_price` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `assessment_detail_id` (`assessment_detail_id`),
  UNIQUE KEY `center_library_centerout_app_code_id_assessment_d_67d7081e_uniq` (`app_code_id`,`assessment_detail_id`),
  CONSTRAINT `center_library_cente_app_code_id_9a35628b_fk_center_li` FOREIGN KEY (`app_code_id`) REFERENCES `center_library_centeroutboundorder` (`id`),
  CONSTRAINT `center_library_cente_assessment_detail_id_b673fff3_fk_material_` FOREIGN KEY (`assessment_detail_id`) REFERENCES `material_application_centerassessmentdetail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of center_library_centeroutboundorderdetail
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for center_library_centeroutboundorderhistory
-- ----------------------------
DROP TABLE IF EXISTS `center_library_centeroutboundorderhistory`;
CREATE TABLE `center_library_centeroutboundorderhistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `application_user` varchar(20) NOT NULL,
  `action` varchar(20) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `application_id` int NOT NULL,
  `history_detail_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `history_detail_id` (`history_detail_id`),
  UNIQUE KEY `center_library_centerout_application_id_history_d_a2db8b07_uniq` (`application_id`,`history_detail_id`),
  CONSTRAINT `center_library_cente_application_id_b08d13c2_fk_center_li` FOREIGN KEY (`application_id`) REFERENCES `center_library_centeroutboundorder` (`id`),
  CONSTRAINT `center_library_cente_history_detail_id_ca4c442b_fk_material_` FOREIGN KEY (`history_detail_id`) REFERENCES `material_application_applicationhistory` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of center_library_centeroutboundorderhistory
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for center_library_centerwarehousingapplication
-- ----------------------------
DROP TABLE IF EXISTS `center_library_centerwarehousingapplication`;
CREATE TABLE `center_library_centerwarehousingapplication` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_code` varchar(15) NOT NULL,
  `total_price` double NOT NULL,
  `des` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `create_u_id` int NOT NULL,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_code` (`app_code`),
  KEY `center_library_cente_create_u_id_63bcf811_fk_auth_user` (`create_u_id`),
  CONSTRAINT `center_library_cente_create_u_id_63bcf811_fk_auth_user` FOREIGN KEY (`create_u_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of center_library_centerwarehousingapplication
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for center_library_centerwarehousingfile
-- ----------------------------
DROP TABLE IF EXISTS `center_library_centerwarehousingfile`;
CREATE TABLE `center_library_centerwarehousingfile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `library_name_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `center_library_cente_library_name_id_b2665684_fk_center_li` (`library_name_id`),
  CONSTRAINT `center_library_cente_library_name_id_b2665684_fk_center_li` FOREIGN KEY (`library_name_id`) REFERENCES `center_library_centerwarehousingapplication` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of center_library_centerwarehousingfile
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
BEGIN;
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (1, '2022-08-27 18:00:29.982938', '2', '局长', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (2, '2022-08-27 18:01:48.509806', '3', '仓库管理员', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (3, '2022-08-27 18:03:10.569448', '4', '供应商', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (4, '2022-08-27 18:05:19.321990', '4', '供应商', 2, '[]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (5, '2022-08-27 18:05:35.395814', '2', 'ybkb', 2, '[{\"changed\": {\"fields\": [\"Groups\", \"Last login\"]}}]', 3, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (6, '2022-08-27 18:06:32.888437', '2', 'ybkb', 2, '[]', 3, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (7, '2022-08-27 18:09:48.329137', '1', '供应商1', 2, '[{\"changed\": {\"fields\": [\"\\u516c\\u53f8\\u540d\\u79f0\", \"\\u4f9b\\u5e94\\u5546\\u63cf\\u8ff0\"]}}, {\"added\": {\"name\": \"(\\u4f9b\\u5e94\\u5546\\u9644\\u4ef6)\", \"object\": \"SupplierFile object (1)\"}}]', 9, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (8, '2022-08-27 18:12:03.781731', '4', '供应商', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (9, '2022-08-27 18:13:09.359797', '4', '供应商', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (10, '2022-08-27 18:27:22.909578', '4', '测试项目1', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"(\\u91c7\\u8d2d\\u8ba1\\u5212\\u3001\\u653f\\u5e9c\\u91c7\\u8d2d\\u6279\\u590d\\u3001\\u6295\\u6807\\u624b\\u7eed)\", \"object\": \"LocalWarehousingFile object (1)\"}}]', 6, 2);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (11, '2022-08-27 18:34:34.022117', '4', '测试项目1', 2, '[]', 6, 2);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (12, '2022-08-27 18:43:01.940113', '4', '供应商', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (13, '2022-08-27 19:04:17.233891', '4', '测试项目1', 2, '[{\"changed\": {\"fields\": [\"\\u5ba1\\u6838\\u901a\\u8fc7\"]}}]', 6, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (14, '2022-08-27 19:23:00.610084', '3', 'ybkb1', 2, '[{\"changed\": {\"fields\": [\"Groups\", \"Last login\"]}}]', 3, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (15, '2022-08-27 19:23:09.568075', '4', 'ybkb2', 2, '[{\"changed\": {\"fields\": [\"Groups\", \"Last login\"]}}]', 3, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (16, '2022-08-27 19:25:23.385704', '3', '1', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"\\u9886\\u7528\\u8be6\\u60c5\", \"object\": \"\\u76d2\\u88c5\\u5e26\\u6ee4\\u82af\\u5438\\u5634_10\"}}]', 24, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (17, '2022-08-27 19:30:45.868709', '3', '2', 2, '[{\"changed\": {\"fields\": [\"\\u7533\\u8bf7\\u4e3b\\u9898\"]}}]', 24, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (18, '2022-08-27 19:31:13.225364', '3', '2', 2, '[{\"added\": {\"name\": \"\\u9886\\u7528\\u8be6\\u60c5\", \"object\": \"\\u6838\\u9178\\u6e05\\u9664\\u5242_20\"}}]', 24, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (19, '2022-08-27 19:32:04.226148', '3', '2', 2, '[]', 24, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (20, '2022-08-27 19:32:14.370433', '3', '2', 2, '[]', 24, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (21, '2022-08-27 19:36:53.036778', '3', '2', 2, '[]', 24, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (22, '2022-08-27 19:37:28.344729', '3', '2', 2, '[]', 24, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (23, '2022-08-27 19:40:58.915668', '1', '分管领导', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (24, '2022-08-27 19:41:06.441095', '2', '局长', 2, '[]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (25, '2022-08-27 19:42:10.112604', '1', '分管领导', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (26, '2022-08-27 19:42:52.682543', '2', '局长', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (27, '2022-08-27 19:43:36.326724', '3', '2', 2, '[]', 24, 3);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (28, '2022-08-27 19:43:44.511665', '3', '2', 2, '[{\"changed\": {\"name\": \"\\u9886\\u7528\\u8be6\\u60c5\", \"object\": \"\\u76d2\\u88c5\\u5e26\\u6ee4\\u82af\\u5438\\u5634_12\", \"fields\": [\"\\u9886\\u7528\\u6570\\u91cf\"]}}]', 24, 3);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (29, '2022-08-27 19:45:10.985569', '3', '2', 2, '[{\"changed\": {\"name\": \"\\u9886\\u7528\\u8be6\\u60c5\", \"object\": \"\\u76d2\\u88c5\\u5e26\\u6ee4\\u82af\\u5438\\u5634_16\", \"fields\": [\"\\u9886\\u7528\\u6570\\u91cf\"]}}]', 24, 3);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (30, '2022-08-27 19:46:22.633273', '3', '2', 2, '[]', 24, 3);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (31, '2022-08-27 19:47:33.383963', '3', '2', 2, '[{\"changed\": {\"name\": \"\\u9886\\u7528\\u8be6\\u60c5\", \"object\": \"\\u76d2\\u88c5\\u5e26\\u6ee4\\u82af\\u5438\\u5634_20\", \"fields\": [\"\\u9886\\u7528\\u6570\\u91cf\"]}}]', 24, 3);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (32, '2022-08-27 19:50:51.591262', '3', '2', 2, '[]', 24, 3);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (33, '2022-08-27 19:51:35.408642', '3', '2', 2, '[{\"changed\": {\"name\": \"\\u9886\\u7528\\u8be6\\u60c5\", \"object\": \"\\u76d2\\u88c5\\u5e26\\u6ee4\\u82af\\u5438\\u5634_23\", \"fields\": [\"\\u9886\\u7528\\u6570\\u91cf\"]}}]', 24, 3);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (34, '2022-08-27 20:02:19.553434', '3', '2', 2, '[]', 24, 3);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (35, '2022-08-27 20:04:25.078691', '3', '2', 2, '[{\"changed\": {\"name\": \"\\u9886\\u7528\\u8be6\\u60c5\", \"object\": \"\\u76d2\\u88c5\\u5e26\\u6ee4\\u82af\\u5438\\u5634_40\", \"fields\": [\"\\u9886\\u7528\\u6570\\u91cf\"]}}]', 24, 3);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (36, '2022-08-27 20:10:04.916890', '2', '局长', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (37, '2022-08-27 20:13:59.056103', '3', '2', 2, '[{\"changed\": {\"name\": \"\\u9886\\u7528\\u8be6\\u60c5\", \"object\": \"\\u76d2\\u88c5\\u5e26\\u6ee4\\u82af\\u5438\\u5634_10\", \"fields\": [\"\\u9886\\u7528\\u6570\\u91cf\"]}}]', 24, 4);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (38, '2022-08-27 20:19:12.999060', '5', '主管科室', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (39, '2022-08-27 20:19:51.280005', '3', '2', 2, '[{\"changed\": {\"name\": \"\\u9886\\u7528\\u8be6\\u60c5\", \"object\": \"\\u76d2\\u88c5\\u5e26\\u6ee4\\u82af\\u5438\\u5634_3\", \"fields\": [\"\\u9886\\u7528\\u6570\\u91cf\"]}}]', 24, 4);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (40, '2022-08-27 20:26:04.240224', '3', '2', 2, '[]', 24, 4);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (41, '2022-08-27 20:27:56.800769', '5', 'ybkb3', 2, '[{\"changed\": {\"fields\": [\"Groups\", \"Last login\"]}}]', 3, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (42, '2022-08-27 20:28:32.849802', '5', 'ybkb3', 2, '[]', 3, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (43, '2022-08-27 20:29:10.527042', '3', '2', 2, '[]', 24, 4);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (44, '2022-08-27 20:57:17.947100', '3', '2', 2, '[{\"added\": {\"name\": \"\\u5730\\u65b9\\u5e93\\u7814\\u5224\", \"object\": \"1\"}}]', 24, 5);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (45, '2022-08-28 09:55:12.110695', '6', 'ybkb4', 2, '[{\"changed\": {\"fields\": [\"Groups\", \"Last login\"]}}]', 3, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (46, '2022-08-28 09:56:07.454425', '3', '仓库管理员', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 2, 1);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (47, '2022-08-28 11:09:12.716441', '3', '2', 2, '[]', 24, 5);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (48, '2022-08-28 11:22:28.343712', '3', '2', 2, '[]', 24, 5);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (49, '2022-08-28 11:26:23.710691', '3', '2', 2, '[]', 24, 5);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (50, '2022-08-28 11:31:29.546352', '3', '2', 2, '[{\"added\": {\"name\": \"\\u5730\\u65b9\\u5e93\\u7814\\u5224\", \"object\": \"2\"}}, {\"changed\": {\"name\": \"\\u5730\\u65b9\\u5e93\\u7814\\u5224\", \"object\": \"1\", \"fields\": [\"\\u7269\\u8d44\\u7c7b\\u578b\"]}}]', 24, 5);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (51, '2022-08-28 11:32:09.229534', '3', '2', 2, '[]', 24, 5);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (52, '2022-08-28 18:14:39.989211', '1', '20220827001', 2, '[{\"changed\": {\"fields\": [\"\\u662f\\u5426\\u51fa\\u5e93\"]}}]', 7, 5);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (53, '2022-08-28 18:16:31.159757', '1', '20220827001', 2, '[{\"changed\": {\"fields\": [\"\\u662f\\u5426\\u51fa\\u5e93\"]}}]', 7, 5);
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES (54, '2022-08-28 18:21:23.000551', '1', '20220827001', 2, '[{\"changed\": {\"fields\": [\"\\u662f\\u5426\\u51fa\\u5e93\"]}}]', 7, 5);
COMMIT;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (31, 'admin', 'logentry');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (2, 'auth', 'group');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (1, 'auth', 'permission');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (3, 'auth', 'user');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (13, 'center_library', 'centerlabrarymaterials');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (14, 'center_library', 'centerlabraryquantity');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (15, 'center_library', 'centerlibrary');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (16, 'center_library', 'centerlibraryfile');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (17, 'center_library', 'centeroutboundorder');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (18, 'center_library', 'centeroutboundorderdetail');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (21, 'center_library', 'centeroutboundorderhistory');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (19, 'center_library', 'centerwarehousingapplication');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (20, 'center_library', 'centerwarehousingfile');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (22, 'home', 'codenumber');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (23, 'home', 'materialstype');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (5, 'local_library', 'locallabrarymaterials');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (6, 'local_library', 'locallibrary');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (7, 'local_library', 'localoutboundorder');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (8, 'local_library', 'localoutboundorderdetail');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (12, 'local_library', 'localoutboundorderhistory');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (11, 'local_library', 'localwarehousingfile');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (10, 'local_library', 'supplierfile');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (9, 'local_library', 'suppliermessage');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (30, 'material_application', 'accounts');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (29, 'material_application', 'applicationdetail');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (28, 'material_application', 'applicationhistory');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (27, 'material_application', 'centerassessmentdetail');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (26, 'material_application', 'exapplicationfile');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (24, 'material_application', 'exwarehousingapplication');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (25, 'material_application', 'localassessmentdetail');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (32, 'sessions', 'session');
COMMIT;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (1, 'home', '0001_initial', '2022-08-27 17:42:38.624865');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (2, 'contenttypes', '0001_initial', '2022-08-27 17:42:39.954471');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (3, 'auth', '0001_initial', '2022-08-27 17:42:40.125683');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (4, 'material_application', '0001_initial', '2022-08-27 17:42:40.127750');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (5, 'local_library', '0001_initial', '2022-08-27 17:42:40.129561');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (6, 'local_library', '0002_initial', '2022-08-27 17:42:40.253217');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (7, 'center_library', '0001_initial', '2022-08-27 17:42:40.255245');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (8, 'center_library', '0002_initial', '2022-08-27 17:42:40.370479');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (9, 'material_application', '0002_initial', '2022-08-27 17:42:40.629625');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (10, 'admin', '0001_initial', '2022-08-27 17:46:33.585536');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (11, 'admin', '0002_logentry_remove_auto_add', '2022-08-27 17:46:33.595671');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (12, 'admin', '0003_logentry_add_action_flag_choices', '2022-08-27 17:46:33.605499');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (13, 'contenttypes', '0002_remove_content_type_name', '2022-08-27 17:46:33.663118');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (14, 'auth', '0002_alter_permission_name_max_length', '2022-08-27 17:46:33.695062');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (15, 'auth', '0003_alter_user_email_max_length', '2022-08-27 17:46:33.729243');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (16, 'auth', '0004_alter_user_username_opts', '2022-08-27 17:46:33.739245');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (17, 'auth', '0005_alter_user_last_login_null', '2022-08-27 17:46:33.771033');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (18, 'auth', '0006_require_contenttypes_0002', '2022-08-27 17:46:33.773466');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (19, 'auth', '0007_alter_validators_add_error_messages', '2022-08-27 17:46:33.783454');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (20, 'auth', '0008_alter_user_username_max_length', '2022-08-27 17:46:33.851006');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (21, 'auth', '0009_alter_user_last_name_max_length', '2022-08-27 17:46:33.884422');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (22, 'auth', '0010_alter_group_name_max_length', '2022-08-27 17:46:33.914644');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (23, 'auth', '0011_update_proxy_permissions', '2022-08-27 17:46:33.936574');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (24, 'auth', '0012_alter_user_first_name_max_length', '2022-08-27 17:46:33.968665');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (25, 'center_library', '0003_initial', '2022-08-27 17:46:34.323394');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (26, 'local_library', '0003_initial', '2022-08-27 17:46:34.737584');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (27, 'sessions', '0001_initial', '2022-08-27 17:46:34.753204');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (28, 'local_library', '0004_alter_localoutboundorder_options_and_more', '2022-08-27 19:03:07.070690');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (29, 'material_application', '0003_alter_accounts_app_code_alter_accounts_number_and_more', '2022-08-27 19:03:07.111649');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (30, 'material_application', '0004_alter_accounts_entry_name_alter_accounts_type_name', '2022-08-27 19:04:10.196504');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (31, 'material_application', '0005_alter_accounts_unique_together_and_more', '2022-08-27 19:10:01.115809');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (32, 'center_library', '0004_centeroutboundorderdetail_total_price_and_more', '2022-08-28 11:55:34.205208');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (33, 'local_library', '0005_localoutboundorderdetail_total_price_and_more', '2022-08-28 11:55:34.246909');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (34, 'material_application', '0006_alter_applicationhistory_options_and_more', '2022-08-28 11:55:34.287394');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (35, 'local_library', '0006_alter_localoutboundorder_total_price_and_more', '2022-08-28 17:00:56.918909');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (36, 'material_application', '0007_localassessmentdetail_total_price_and_more', '2022-08-28 17:16:04.608811');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (37, 'local_library', '0007_remove_localoutboundorderdetail_library_name_and_more', '2022-08-28 17:16:04.688802');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (38, 'local_library', '0008_localoutboundorderdetail_number', '2022-08-28 17:36:33.709618');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (39, 'center_library', '0005_remove_centeroutboundorderdetail_library_name_and_more', '2022-08-28 22:00:56.711160');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (40, 'material_application', '0008_alter_applicationhistory_add_time', '2022-08-28 22:49:48.779686');
COMMIT;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of django_session
-- ----------------------------
BEGIN;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('rhxuq374i7gcfc5jqfbdact1bydelij8', '.eJzFV0tzmzAQ_isZzokDCCGUY-899lRnPHqsbFoeLoJpMxn_9yJwUkeVY2Hj5KSRdtnHt5-W1XOwYl27WXUamlUug4cgCm4PzzgTP6EyAvmDVet6IeqqbXK-MCqLvVQvvtYSii973TcGNkxvjNmMI8hwGikqUEixiDMuiIgQJ1SFTBGCSIqk4MAlUA4s61XDSCVxpFSMuDFaQtXp3tb352VQsRKWwcPNMlguuwRi2S-YxmAWoGgZ3PaivA92VFKsuVHsTuSNKGAUliZkbcQ-9volUuxghzD2cNI1xSi7F1C1PRxFzhvWPO23ddfyuqtk3Uho7sdPmJTfxq-qrijMCW-ASdF0JfcO9_3Idrc310l592jEkEsjjcIw9vZEBk8piYVRURCZXZiqyzF-2dnontLvNffffB7-Z6JilwE5HOIoxXPT-TdrYFN3Oq_WbLstcsHavK68kT_y-ccWYjIuNtiJwyiJU2pKhyk9sM1xNgO92bD71bGqzdv_af6RTeTcNG0IsX0QuQpFUDg449Qv4BNN_8ILUdSCFa-1GXbvdJ53tP3pPhmBa9CdXI3uLoxGspesJ37OCn022-eAbi62Z3OR-xh0ujPdFJoStGZrOM1H-4MPpuRkGxag1M_oXJOdg6fzzHVXAnO28S4KbeRTVwQHF6O_NJyZIYYkYXppuz4MnmBklowrMql2L51kdThwwB__QWaagQkX6UzUnC3-PKTsaruGeYyUoVcmY59ynsCdCdFfmvaCrj4jaN6J2TAh-8A1vGScJcMiTIg4ycyAn6IsG8b9xHHRtfGpNzkU8o4V7cn7QXA8GIvRsTqb57ldF_NuvzcCF9f_Cf15PEOirl-vZ3J2KbDLFojkSBTGiL4T9doJ07p_vm-P4jRKPx0or-RsmFL7wPWmoVFiHgxEpTBnX387VREqBieC8En9ZVOX8NpkdPu0dU49Di3_gp2b_8lJ0j9nu0yZfUB2j8HuL4P6Qio:1oSK0v:PKaI_GBcqlqcFsQEdIf8uQhN_XR-UN5TwX-PPrMiYr0', '2022-09-11 23:15:53.481517');
COMMIT;

-- ----------------------------
-- Table structure for home_codenumber
-- ----------------------------
DROP TABLE IF EXISTS `home_codenumber`;
CREATE TABLE `home_codenumber` (
  `id` int NOT NULL AUTO_INCREMENT,
  `db_name` varchar(100) NOT NULL,
  `date_str` varchar(100) NOT NULL,
  `number` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of home_codenumber
-- ----------------------------
BEGIN;
INSERT INTO `home_codenumber` (`id`, `db_name`, `date_str`, `number`) VALUES (4, 'LocalWarehousingApplication', '20220827', 2);
INSERT INTO `home_codenumber` (`id`, `db_name`, `date_str`, `number`) VALUES (7, 'ExWarehousingApplication', '20220827', 1);
COMMIT;

-- ----------------------------
-- Table structure for home_materialstype
-- ----------------------------
DROP TABLE IF EXISTS `home_materialstype`;
CREATE TABLE `home_materialstype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `materials_name` varchar(100) NOT NULL,
  `specifications` varchar(100) NOT NULL,
  `unit` varchar(100) NOT NULL,
  `warning_quantity` double NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_materialstype_materials_name_specifica_6f6a4959_uniq` (`materials_name`,`specifications`,`unit`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of home_materialstype
-- ----------------------------
BEGIN;
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (1, '盒装带滤芯吸嘴', '10ul（加长），96个/盒', '盒', 10, '2022-08-27 17:43:55.914836', '2022-08-27', '2022-08-27 17:43:55.914898');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (2, '盒装带滤芯吸嘴', '1250ul，96个/盒', '盒', 10, '2022-08-27 17:43:55.916872', '2022-08-27', '2022-08-27 17:43:55.916907');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (3, '核酸清除剂', '≥500 mL/瓶', '瓶', 10, '2022-08-27 17:43:55.918665', '2022-08-27', '2022-08-27 17:43:55.918698');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (4, '新型冠状病毒抗原检测试剂', '1人份/袋。样本类型：鼻拭子', '袋', 10, '2022-08-27 17:43:55.920303', '2022-08-27', '2022-08-27 17:43:55.920330');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (5, '新型冠状病毒抗原检测试剂', '40人份/盒。样本类型：鼻拭子', '盒', 10, '2022-08-27 17:43:55.921807', '2022-08-27', '2022-08-27 17:43:55.921834');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (6, '样本释放剂', '1人份。样本类型：拭子类样本（咽/鼻/眼结膜）', '份', 10, '2022-08-27 17:43:55.923295', '2022-08-27', '2022-08-27 17:43:55.923335');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (7, '盒装带滤芯吸嘴', '10ul，96个/盒', '盒', 10, '2022-08-27 17:43:55.924776', '2022-08-27', '2022-08-27 17:43:55.924801');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (8, '盒装带滤芯吸嘴', '200ul，96个/盒', '盒', 10, '2022-08-27 17:43:55.926229', '2022-08-27', '2022-08-27 17:43:55.926254');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (9, '盒装带滤芯吸嘴', '100ul，96个/盒', '盒', 10, '2022-08-27 17:43:55.927710', '2022-08-27', '2022-08-27 17:43:55.927735');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (10, '8连管（含盖）', '125排/盒', '盒', 10, '2022-08-27 17:43:55.929156', '2022-08-27', '2022-08-27 17:43:55.929180');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (11, '微量离心管（EP管）', '1.5ml', '盒', 10, '2022-08-27 17:43:55.930596', '2022-08-27', '2022-08-27 17:43:55.930620');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (12, '微量离心管（EP管）', '2.0ml', '盒', 10, '2022-08-27 17:43:55.932103', '2022-08-27', '2022-08-27 17:43:55.932127');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (13, '核酸提取试剂', '8人份/盒', '盒', 10, '2022-08-27 17:43:55.933963', '2022-08-27', '2022-08-27 17:43:55.933997');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (14, '核酸提取试剂', '24人份/盒', '盒', 10, '2022-08-27 17:43:55.935691', '2022-08-27', '2022-08-27 17:43:55.935720');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (15, '核酸提取试剂', '48人份/盒', '盒', 10, '2022-08-27 17:43:55.937261', '2022-08-27', '2022-08-27 17:43:55.937288');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (16, '核酸提取试剂', '96人份/盒', '盒', 10, '2022-08-27 17:43:55.938828', '2022-08-27', '2022-08-27 17:43:55.938855');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (17, '核酸提取试剂', '48人份/盒、96人份/盒。', '人份', 10, '2022-08-27 17:43:55.940349', '2022-08-27', '2022-08-27 17:43:55.940374');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (18, '核酸提取试剂', '48人份/盒、96人份/盒。处理样本体积：50-200ul', '人份', 10, '2022-08-27 17:43:55.941861', '2022-08-27', '2022-08-27 17:43:55.941887');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (19, '新型冠状病毒2019-nCoV核酸检测试剂盒', '50人份/盒、200人份/盒。', '人份', 10, '2022-08-27 17:43:55.943377', '2022-08-27', '2022-08-27 17:43:55.943403');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (20, '新型冠状病毒2019-nCoV核酸检测试剂盒', '100人份/盒', '人份', 10, '2022-08-27 17:43:55.944873', '2022-08-27', '2022-08-27 17:43:55.944899');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (21, '新型冠状病毒2019-nCoV核酸检测试剂盒', '50 人份/盒、96人份/盒', '人份', 10, '2022-08-27 17:43:55.946311', '2022-08-27', '2022-08-27 17:43:55.946337');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (22, '新型冠状病毒2019-nCoV核酸检测试剂盒', '48人份/盒、96人份/盒', '人份', 10, '2022-08-27 17:43:55.947780', '2022-08-27', '2022-08-27 17:43:55.947807');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (23, '新型冠状病毒2019-nCoV核酸检测试剂盒', '试剂盒内所提供试剂量≥48次检测需求。最低检出限：不高于200 copies /mL', '人份', 10, '2022-08-27 17:43:55.949356', '2022-08-27', '2022-08-27 17:43:55.949425');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (24, '新型冠病毒核酸检测质控品', '0.5ml/支', '盒', 10, '2022-08-27 17:43:55.951694', '2022-08-27', '2022-08-27 17:43:55.951726');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (25, '新型冠病毒核酸检测质控品', '装量不得小于1ml/支', '盒', 10, '2022-08-27 17:43:55.953369', '2022-08-27', '2022-08-27 17:43:55.953396');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (26, '新型冠状病毒(2019-nCoV)IgM/IgG抗体检测试剂盒', '测定速度：10分钟。样本量：20µL', '人份', 10, '2022-08-27 17:43:55.954881', '2022-08-27', '2022-08-27 17:43:55.954923');
INSERT INTO `home_materialstype` (`id`, `materials_name`, `specifications`, `unit`, `warning_quantity`, `add_time`, `add_date`, `modify_time`) VALUES (27, '新型冠状病毒(2019-nCoV)IgM/IgG抗体检测试剂盒', '检测速度：≤15 分钟。样本量：检测 IgM、IgG 所需总样本量≤20 微升', '人份', 10, '2022-08-27 17:43:55.956445', '2022-08-27', '2022-08-27 17:43:55.956470');
COMMIT;

-- ----------------------------
-- Table structure for local_library_locallabrarymaterials
-- ----------------------------
DROP TABLE IF EXISTS `local_library_locallabrarymaterials`;
CREATE TABLE `local_library_locallabrarymaterials` (
  `id` int NOT NULL AUTO_INCREMENT,
  `push_num` int NOT NULL,
  `unit_price` double NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `library_name_id` int NOT NULL,
  `type_name_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `local_library_locallabra_library_name_id_type_nam_4fc6cbca_uniq` (`library_name_id`,`type_name_id`),
  KEY `local_library_locall_type_name_id_0ae855a7_fk_home_mate` (`type_name_id`),
  CONSTRAINT `local_library_locall_library_name_id_fbba985e_fk_local_lib` FOREIGN KEY (`library_name_id`) REFERENCES `local_library_locallibrary` (`id`),
  CONSTRAINT `local_library_locall_type_name_id_0ae855a7_fk_home_mate` FOREIGN KEY (`type_name_id`) REFERENCES `home_materialstype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of local_library_locallabrarymaterials
-- ----------------------------
BEGIN;
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (2, 0, 10, '2022-08-27 19:04:17.177747', '2022-08-27', '2022-08-27 19:04:17.177823', 4, 1);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (3, 20, 20, '2022-08-27 19:04:17.180049', '2022-08-27', '2022-08-28 18:21:22.987651', 4, 2);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (4, 40, 12, '2022-08-27 19:04:17.182512', '2022-08-27', '2022-08-28 18:21:22.997604', 4, 3);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (5, 0, 12, '2022-08-27 19:04:17.184807', '2022-08-27', '2022-08-27 19:04:17.184861', 4, 4);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (6, 0, 15, '2022-08-27 19:04:17.187238', '2022-08-27', '2022-08-27 19:04:17.187293', 4, 5);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (7, 0, 14, '2022-08-27 19:04:17.189378', '2022-08-27', '2022-08-27 19:04:17.189430', 4, 6);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (8, 0, 13, '2022-08-27 19:04:17.191349', '2022-08-27', '2022-08-27 19:04:17.191400', 4, 7);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (9, 0, 17, '2022-08-27 19:04:17.193416', '2022-08-27', '2022-08-27 19:04:17.193467', 4, 8);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (10, 0, 19, '2022-08-27 19:04:17.195960', '2022-08-27', '2022-08-27 19:04:17.196051', 4, 9);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (11, 0, 20, '2022-08-27 19:04:17.198434', '2022-08-27', '2022-08-27 19:04:17.198499', 4, 10);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (12, 0, 21, '2022-08-27 19:04:17.201085', '2022-08-27', '2022-08-27 19:04:17.201154', 4, 11);
INSERT INTO `local_library_locallabrarymaterials` (`id`, `push_num`, `unit_price`, `add_time`, `add_date`, `modify_time`, `library_name_id`, `type_name_id`) VALUES (13, 0, 23, '2022-08-27 19:04:17.204139', '2022-08-27', '2022-08-27 19:04:17.204233', 4, 12);
COMMIT;

-- ----------------------------
-- Table structure for local_library_locallibrary
-- ----------------------------
DROP TABLE IF EXISTS `local_library_locallibrary`;
CREATE TABLE `local_library_locallibrary` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_code` varchar(100) NOT NULL,
  `entry_name` varchar(100) NOT NULL,
  `budget` double NOT NULL,
  `less_budget` double NOT NULL,
  `des` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `file` varchar(100) NOT NULL,
  `is_approve` tinyint(1) NOT NULL,
  `create_user_id` int NOT NULL,
  `supplier_name_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_code` (`app_code`),
  UNIQUE KEY `entry_name` (`entry_name`),
  KEY `local_library_locall_create_user_id_97b28b3d_fk_auth_user` (`create_user_id`),
  KEY `local_library_locall_supplier_name_id_6fae86af_fk_local_lib` (`supplier_name_id`),
  CONSTRAINT `local_library_locall_create_user_id_97b28b3d_fk_auth_user` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `local_library_locall_supplier_name_id_6fae86af_fk_local_lib` FOREIGN KEY (`supplier_name_id`) REFERENCES `local_library_suppliermessage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of local_library_locallibrary
-- ----------------------------
BEGIN;
INSERT INTO `local_library_locallibrary` (`id`, `app_code`, `entry_name`, `budget`, `less_budget`, `des`, `add_time`, `add_date`, `modify_time`, `file`, `is_approve`, `create_user_id`, `supplier_name_id`) VALUES (4, '20220827002', '测试项目1', 500, 499.992, '100', '2022-08-27 18:27:22.845523', '2022-08-27', '2022-08-28 18:21:22.999613', 'upload/local_library/2022/8/27/测试物料明细文件_rlK0T9K.xlsx', 1, 2, 1);
COMMIT;

-- ----------------------------
-- Table structure for local_library_localoutboundorder
-- ----------------------------
DROP TABLE IF EXISTS `local_library_localoutboundorder`;
CREATE TABLE `local_library_localoutboundorder` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `applicant` varchar(100) NOT NULL,
  `applicant_user` varchar(100) NOT NULL,
  `des` varchar(100) NOT NULL,
  `total_price` double NOT NULL,
  `is_ex` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `app_code_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `applicant_user` (`applicant_user`),
  UNIQUE KEY `app_code_id` (`app_code_id`),
  UNIQUE KEY `local_library_localoutbo_app_code_id_user_id_b4e989f0_uniq` (`app_code_id`,`user_id`),
  KEY `local_library_localo_user_id_1d4fd30d_fk_auth_user` (`user_id`),
  CONSTRAINT `local_library_localo_app_code_id_34ac709f_fk_material_` FOREIGN KEY (`app_code_id`) REFERENCES `material_application_exwarehousingapplication` (`id`),
  CONSTRAINT `local_library_localo_user_id_1d4fd30d_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of local_library_localoutboundorder
-- ----------------------------
BEGIN;
INSERT INTO `local_library_localoutboundorder` (`id`, `title`, `applicant`, `applicant_user`, `des`, `total_price`, `is_ex`, `add_time`, `add_date`, `app_code_id`, `user_id`) VALUES (1, '2', '申请单位1', '申请人', '', 80, 1, '2022-08-27 19:25:00.000000', '2022-08-27', 3, 2);
COMMIT;

-- ----------------------------
-- Table structure for local_library_localoutboundorderdetail
-- ----------------------------
DROP TABLE IF EXISTS `local_library_localoutboundorderdetail`;
CREATE TABLE `local_library_localoutboundorderdetail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_code_id` int NOT NULL,
  `assessment_detail_id` int NOT NULL,
  `total_price` double NOT NULL,
  `number` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `assessment_detail_id` (`assessment_detail_id`),
  UNIQUE KEY `local_library_localoutbo_app_code_id_assessment_d_72fb67a5_uniq` (`app_code_id`,`assessment_detail_id`),
  CONSTRAINT `local_library_localo_app_code_id_86ff16eb_fk_local_lib` FOREIGN KEY (`app_code_id`) REFERENCES `local_library_localoutboundorder` (`id`),
  CONSTRAINT `local_library_localo_assessment_detail_id_6119b528_fk_material_` FOREIGN KEY (`assessment_detail_id`) REFERENCES `material_application_localassessmentdetail` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of local_library_localoutboundorderdetail
-- ----------------------------
BEGIN;
INSERT INTO `local_library_localoutboundorderdetail` (`id`, `app_code_id`, `assessment_detail_id`, `total_price`, `number`) VALUES (1, 1, 1, 30, 10);
INSERT INTO `local_library_localoutboundorderdetail` (`id`, `app_code_id`, `assessment_detail_id`, `total_price`, `number`) VALUES (2, 1, 2, 50, 20);
COMMIT;

-- ----------------------------
-- Table structure for local_library_localoutboundorderhistory
-- ----------------------------
DROP TABLE IF EXISTS `local_library_localoutboundorderhistory`;
CREATE TABLE `local_library_localoutboundorderhistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `application_user` varchar(20) NOT NULL,
  `action` varchar(20) NOT NULL,
  `add_time` date NOT NULL,
  `application_id` int NOT NULL,
  `history_detail_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `history_detail_id` (`history_detail_id`),
  UNIQUE KEY `local_library_localoutbo_application_id_history_d_c83965c5_uniq` (`application_id`,`history_detail_id`),
  CONSTRAINT `local_library_localo_application_id_f096b815_fk_local_lib` FOREIGN KEY (`application_id`) REFERENCES `local_library_localoutboundorder` (`id`),
  CONSTRAINT `local_library_localo_history_detail_id_41a754e5_fk_material_` FOREIGN KEY (`history_detail_id`) REFERENCES `material_application_applicationhistory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of local_library_localoutboundorderhistory
-- ----------------------------
BEGIN;
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (1, '', '研判完成', '2022-08-28', 1, 31);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (2, '', '', '2022-08-28', 1, 30);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (3, '', '', '2022-08-28', 1, 28);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (4, '', '', '2022-08-28', 1, 25);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (5, '', '', '2022-08-28', 1, 15);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (6, '', '发起审批', '2022-08-27', 1, 11);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (7, '', '通过', '2022-08-27', 1, 10);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (8, '', '发起审批', '2022-08-27', 1, 9);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (9, '', '发起审批', '2022-08-27', 1, 8);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (10, '', '发起审批', '2022-08-27', 1, 7);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (11, '', '通过', '2022-08-27', 1, 6);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (12, '', '发起审批', '2022-08-27', 1, 5);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (13, '', '发起审批', '2022-08-27', 1, 4);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (14, '', '发起审批', '2022-08-27', 1, 3);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (15, '', '发起审批', '2022-08-27', 1, 2);
INSERT INTO `local_library_localoutboundorderhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`, `history_detail_id`) VALUES (16, '', '发起审批', '2022-08-27', 1, 1);
COMMIT;

-- ----------------------------
-- Table structure for local_library_localwarehousingfile
-- ----------------------------
DROP TABLE IF EXISTS `local_library_localwarehousingfile`;
CREATE TABLE `local_library_localwarehousingfile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `library_name_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `local_library_localw_library_name_id_7344daf9_fk_local_lib` (`library_name_id`),
  CONSTRAINT `local_library_localw_library_name_id_7344daf9_fk_local_lib` FOREIGN KEY (`library_name_id`) REFERENCES `local_library_locallibrary` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of local_library_localwarehousingfile
-- ----------------------------
BEGIN;
INSERT INTO `local_library_localwarehousingfile` (`id`, `file`, `add_time`, `library_name_id`) VALUES (1, 'upload/local_library/2022/8/27/测试物料明细文件_6AN7byY.xlsx', '2022-08-27 18:27:22.907908', 4);
COMMIT;

-- ----------------------------
-- Table structure for local_library_supplierfile
-- ----------------------------
DROP TABLE IF EXISTS `local_library_supplierfile`;
CREATE TABLE `local_library_supplierfile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `library_name_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `local_library_suppli_library_name_id_5eaeeb6f_fk_local_lib` (`library_name_id`),
  CONSTRAINT `local_library_suppli_library_name_id_5eaeeb6f_fk_local_lib` FOREIGN KEY (`library_name_id`) REFERENCES `local_library_suppliermessage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of local_library_supplierfile
-- ----------------------------
BEGIN;
INSERT INTO `local_library_supplierfile` (`id`, `file`, `add_time`, `library_name_id`) VALUES (1, 'upload/local_library/2022/8/27/尚硅谷大数据项目之电商数仓4可视化报表.doc', '2022-08-27 18:09:48.328495', 1);
COMMIT;

-- ----------------------------
-- Table structure for local_library_suppliermessage
-- ----------------------------
DROP TABLE IF EXISTS `local_library_suppliermessage`;
CREATE TABLE `local_library_suppliermessage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company_name` varchar(100) NOT NULL,
  `supplier_des` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `local_library_suppliermessage_user_id_ae8b6a2c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of local_library_suppliermessage
-- ----------------------------
BEGIN;
INSERT INTO `local_library_suppliermessage` (`id`, `company_name`, `supplier_des`, `add_time`, `modify_time`, `add_date`, `user_id`) VALUES (1, '供应商1', '这是一个供应商1', '2022-08-27 18:05:35.400029', '2022-08-27 18:09:48.326294', '2022-08-27', 2);
COMMIT;

-- ----------------------------
-- Table structure for material_application_accounts
-- ----------------------------
DROP TABLE IF EXISTS `material_application_accounts`;
CREATE TABLE `material_application_accounts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_code` varchar(100) NOT NULL,
  `db_type` varchar(10) NOT NULL,
  `entry_name` varchar(100) NOT NULL,
  `type_name` varchar(100) NOT NULL,
  `action` varchar(10) NOT NULL,
  `number` int NOT NULL,
  `price` double NOT NULL,
  `unit_price` double NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `specifications` varchar(100) NOT NULL,
  `unit` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `material_application_acc_app_code_entry_name_type_e12c48a0_uniq` (`app_code`,`entry_name`,`type_name`,`specifications`,`unit`,`db_type`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of material_application_accounts
-- ----------------------------
BEGIN;
INSERT INTO `material_application_accounts` (`id`, `app_code`, `db_type`, `entry_name`, `type_name`, `action`, `number`, `price`, `unit_price`, `add_time`, `add_date`, `specifications`, `unit`) VALUES (5, '20220827002', '1', '测试项目1', '微量离心管（EP管）', '1', 0, 0, 21, '2022-08-27 19:04:17.208068', '2022-08-27', '', '');
INSERT INTO `material_application_accounts` (`id`, `app_code`, `db_type`, `entry_name`, `type_name`, `action`, `number`, `price`, `unit_price`, `add_time`, `add_date`, `specifications`, `unit`) VALUES (6, '20220827002', '1', '测试项目1', '8连管（含盖）', '1', 0, 0, 20, '2022-08-27 19:04:17.212407', '2022-08-27', '', '');
INSERT INTO `material_application_accounts` (`id`, `app_code`, `db_type`, `entry_name`, `type_name`, `action`, `number`, `price`, `unit_price`, `add_time`, `add_date`, `specifications`, `unit`) VALUES (7, '20220827002', '1', '测试项目1', '盒装带滤芯吸嘴', '1', 0, 0, 10, '2022-08-27 19:04:17.214830', '2022-08-27', '', '');
INSERT INTO `material_application_accounts` (`id`, `app_code`, `db_type`, `entry_name`, `type_name`, `action`, `number`, `price`, `unit_price`, `add_time`, `add_date`, `specifications`, `unit`) VALUES (8, '20220827002', '1', '测试项目1', '样本释放剂', '1', 0, 0, 14, '2022-08-27 19:04:17.221650', '2022-08-27', '', '');
INSERT INTO `material_application_accounts` (`id`, `app_code`, `db_type`, `entry_name`, `type_name`, `action`, `number`, `price`, `unit_price`, `add_time`, `add_date`, `specifications`, `unit`) VALUES (9, '20220827002', '1', '测试项目1', '新型冠状病毒抗原检测试剂', '1', 0, 0, 12, '2022-08-27 19:04:17.223862', '2022-08-27', '', '');
INSERT INTO `material_application_accounts` (`id`, `app_code`, `db_type`, `entry_name`, `type_name`, `action`, `number`, `price`, `unit_price`, `add_time`, `add_date`, `specifications`, `unit`) VALUES (10, '20220827002', '1', '测试项目1', '核酸清除剂', '1', 0, 0, 12, '2022-08-27 19:04:17.228160', '2022-08-27', '', '');
INSERT INTO `material_application_accounts` (`id`, `app_code`, `db_type`, `entry_name`, `type_name`, `action`, `number`, `price`, `unit_price`, `add_time`, `add_date`, `specifications`, `unit`) VALUES (15, '20220827001', '1', '', '盒装带滤芯吸嘴', '2', 10, 30, 20, '2022-08-28 18:14:39.976009', '2022-08-28', '', '');
INSERT INTO `material_application_accounts` (`id`, `app_code`, `db_type`, `entry_name`, `type_name`, `action`, `number`, `price`, `unit_price`, `add_time`, `add_date`, `specifications`, `unit`) VALUES (16, '20220827001', '1', '', '核酸清除剂', '2', 20, 50, 12, '2022-08-28 18:14:39.984769', '2022-08-28', '', '');
INSERT INTO `material_application_accounts` (`id`, `app_code`, `db_type`, `entry_name`, `type_name`, `action`, `number`, `price`, `unit_price`, `add_time`, `add_date`, `specifications`, `unit`) VALUES (18, '20220827001', '1', '', '盒装带滤芯吸嘴', '2', 10, 30, 20, '2022-08-28 18:21:22.986087', '2022-08-28', '1250ul，96个/盒', '盒');
INSERT INTO `material_application_accounts` (`id`, `app_code`, `db_type`, `entry_name`, `type_name`, `action`, `number`, `price`, `unit_price`, `add_time`, `add_date`, `specifications`, `unit`) VALUES (19, '20220827001', '1', '', '核酸清除剂', '2', 20, 50, 12, '2022-08-28 18:21:22.996158', '2022-08-28', '≥500 mL/瓶', '瓶');
COMMIT;

-- ----------------------------
-- Table structure for material_application_applicationdetail
-- ----------------------------
DROP TABLE IF EXISTS `material_application_applicationdetail`;
CREATE TABLE `material_application_applicationdetail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `number` int NOT NULL,
  `application_id` int NOT NULL,
  `type_name_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `material_application_application_id_046e806f_fk_material_` (`application_id`),
  KEY `material_application_type_name_id_12038058_fk_home_mate` (`type_name_id`),
  CONSTRAINT `material_application_application_id_046e806f_fk_material_` FOREIGN KEY (`application_id`) REFERENCES `material_application_exwarehousingapplication` (`id`),
  CONSTRAINT `material_application_type_name_id_12038058_fk_home_mate` FOREIGN KEY (`type_name_id`) REFERENCES `home_materialstype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of material_application_applicationdetail
-- ----------------------------
BEGIN;
INSERT INTO `material_application_applicationdetail` (`id`, `number`, `application_id`, `type_name_id`) VALUES (1, 3, 3, 2);
INSERT INTO `material_application_applicationdetail` (`id`, `number`, `application_id`, `type_name_id`) VALUES (2, 20, 3, 3);
COMMIT;

-- ----------------------------
-- Table structure for material_application_applicationhistory
-- ----------------------------
DROP TABLE IF EXISTS `material_application_applicationhistory`;
CREATE TABLE `material_application_applicationhistory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `application_user` varchar(20) NOT NULL,
  `action` varchar(20) NOT NULL,
  `add_time` date NOT NULL,
  `application_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `material_application_application_id_b651c639_fk_material_` (`application_id`),
  CONSTRAINT `material_application_application_id_b651c639_fk_material_` FOREIGN KEY (`application_id`) REFERENCES `material_application_exwarehousingapplication` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of material_application_applicationhistory
-- ----------------------------
BEGIN;
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (1, 'admin', '发起审批', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (2, 'admin', '发起审批', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (3, 'admin', '发起审批', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (4, 'admin', '发起审批', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (5, 'admin', '发起审批', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (6, 'ybkb2', '通过', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (7, 'ybkb2', '发起审批', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (8, 'ybkb2', '发起审批', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (9, 'ybkb2', '发起审批', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (10, 'ybkb3', '通过', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (11, 'ybkb3', '发起审批', '2022-08-27', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (15, 'ybkb3', '', '2022-08-28', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (25, 'ybkb3', '', '2022-08-28', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (28, 'ybkb3', '', '2022-08-28', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (30, 'ybkb3', '', '2022-08-28', 3);
INSERT INTO `material_application_applicationhistory` (`id`, `application_user`, `action`, `add_time`, `application_id`) VALUES (31, 'ybkb4', '研判完成', '2022-08-28', 3);
COMMIT;

-- ----------------------------
-- Table structure for material_application_centerassessmentdetail
-- ----------------------------
DROP TABLE IF EXISTS `material_application_centerassessmentdetail`;
CREATE TABLE `material_application_centerassessmentdetail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `number` int NOT NULL,
  `is_ex` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `application_id` int NOT NULL,
  `library_name_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `material_application_application_id_c38fe88f_fk_material_` (`application_id`),
  KEY `material_application_library_name_id_d4f35c67_fk_center_li` (`library_name_id`),
  CONSTRAINT `material_application_application_id_c38fe88f_fk_material_` FOREIGN KEY (`application_id`) REFERENCES `material_application_exwarehousingapplication` (`id`),
  CONSTRAINT `material_application_library_name_id_d4f35c67_fk_center_li` FOREIGN KEY (`library_name_id`) REFERENCES `center_library_centerlabraryquantity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of material_application_centerassessmentdetail
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for material_application_exapplicationfile
-- ----------------------------
DROP TABLE IF EXISTS `material_application_exapplicationfile`;
CREATE TABLE `material_application_exapplicationfile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `library_name_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `material_application_library_name_id_5c4d2f66_fk_material_` (`library_name_id`),
  CONSTRAINT `material_application_library_name_id_5c4d2f66_fk_material_` FOREIGN KEY (`library_name_id`) REFERENCES `material_application_exwarehousingapplication` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of material_application_exapplicationfile
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for material_application_exwarehousingapplication
-- ----------------------------
DROP TABLE IF EXISTS `material_application_exwarehousingapplication`;
CREATE TABLE `material_application_exwarehousingapplication` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_code` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `applicant` varchar(100) NOT NULL,
  `applicant_user` varchar(100) NOT NULL,
  `des` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `add_date` date NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `status` varchar(5) NOT NULL,
  `next_node` varchar(100) NOT NULL,
  `create_user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_code` (`app_code`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `applicant_user` (`applicant_user`),
  KEY `material_application_create_user_id_0a49daf9_fk_auth_user` (`create_user_id`),
  CONSTRAINT `material_application_create_user_id_0a49daf9_fk_auth_user` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of material_application_exwarehousingapplication
-- ----------------------------
BEGIN;
INSERT INTO `material_application_exwarehousingapplication` (`id`, `app_code`, `title`, `applicant`, `applicant_user`, `des`, `add_time`, `add_date`, `modify_time`, `status`, `next_node`, `create_user_id`) VALUES (3, '20220827001', '2', '申请单位1', '申请人', '', '2022-08-27 19:25:00.000000', '2022-08-27', '2022-08-28 11:32:09.228670', '4', '6', 1);
COMMIT;

-- ----------------------------
-- Table structure for material_application_localassessmentdetail
-- ----------------------------
DROP TABLE IF EXISTS `material_application_localassessmentdetail`;
CREATE TABLE `material_application_localassessmentdetail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `number` int NOT NULL,
  `is_ex` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `application_id` int NOT NULL,
  `library_name_id` int NOT NULL,
  `total_price` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `material_application_application_id_1436add9_fk_material_` (`application_id`),
  KEY `material_application_library_name_id_bf277ba0_fk_local_lib` (`library_name_id`),
  CONSTRAINT `material_application_application_id_1436add9_fk_material_` FOREIGN KEY (`application_id`) REFERENCES `material_application_exwarehousingapplication` (`id`),
  CONSTRAINT `material_application_library_name_id_bf277ba0_fk_local_lib` FOREIGN KEY (`library_name_id`) REFERENCES `local_library_locallabrarymaterials` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of material_application_localassessmentdetail
-- ----------------------------
BEGIN;
INSERT INTO `material_application_localassessmentdetail` (`id`, `number`, `is_ex`, `add_time`, `application_id`, `library_name_id`, `total_price`) VALUES (1, 3, 0, '2022-08-27 20:57:17.938096', 3, 3, 0);
INSERT INTO `material_application_localassessmentdetail` (`id`, `number`, `is_ex`, `add_time`, `application_id`, `library_name_id`, `total_price`) VALUES (2, 20, 0, '2022-08-28 11:31:29.533092', 3, 4, 0);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
