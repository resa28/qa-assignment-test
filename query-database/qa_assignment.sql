/*
 Navicat Premium Data Transfer

 Source Server         : localmysql8
 Source Server Type    : MySQL
 Source Server Version : 80036 (8.0.36)
 Source Host           : localhost:13306
 Source Schema         : qa_assignment

 Target Server Type    : MySQL
 Target Server Version : 80036 (8.0.36)
 File Encoding         : 65001

 Date: 04/01/2026 17:01:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for lps
-- ----------------------------
DROP TABLE IF EXISTS `lps`;
CREATE TABLE `lps`  (
  `lp_id` int NOT NULL,
  `lp_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`lp_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lps
-- ----------------------------
INSERT INTO `lps` VALUES (1, 'BCA');
INSERT INTO `lps` VALUES (2, 'BNI');
INSERT INTO `lps` VALUES (3, 'Mandiri');
INSERT INTO `lps` VALUES (4, 'Jago');

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `order_id` int NOT NULL,
  `lp_id` int NOT NULL,
  `symbol_id` int NOT NULL,
  `direction` enum('BUY','SELL') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `volume` bigint NOT NULL,
  PRIMARY KEY (`order_id`) USING BTREE,
  INDEX `idx_orders_symbol`(`symbol_id` ASC) USING BTREE,
  INDEX `idx_orders_lp`(`lp_id` ASC) USING BTREE,
  CONSTRAINT `fk_orders_lp` FOREIGN KEY (`lp_id`) REFERENCES `lps` (`lp_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_orders_symbol` FOREIGN KEY (`symbol_id`) REFERENCES `symbols` (`symbol_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES (1, 1, 1, 'SELL', 500000);
INSERT INTO `orders` VALUES (2, 2, 1, 'SELL', 500000);
INSERT INTO `orders` VALUES (3, 3, 1, 'BUY', 500000);
INSERT INTO `orders` VALUES (4, 2, 2, 'BUY', 500000);
INSERT INTO `orders` VALUES (5, 1, 2, 'BUY', 250000);
INSERT INTO `orders` VALUES (6, 3, 2, 'SELL', 500000);
INSERT INTO `orders` VALUES (7, 1, 3, 'BUY', 250000);
INSERT INTO `orders` VALUES (8, 3, 3, 'BUY', 500000);

-- ----------------------------
-- Table structure for symbols
-- ----------------------------
DROP TABLE IF EXISTS `symbols`;
CREATE TABLE `symbols`  (
  `symbol_id` int NOT NULL,
  `symbol_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `core_symbol` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`symbol_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of symbols
-- ----------------------------
INSERT INTO `symbols` VALUES (1, 'EURUSD', 'EUR/USD');
INSERT INTO `symbols` VALUES (2, 'GBPUSD', 'GBP/USD');
INSERT INTO `symbols` VALUES (3, 'OIL', 'OILCash');
INSERT INTO `symbols` VALUES (4, 'XAUUSD', 'XAU/USD');

SET FOREIGN_KEY_CHECKS = 1;
