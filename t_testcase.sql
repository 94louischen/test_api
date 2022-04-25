/*
 Navicat Premium Data Transfer

 Source Server         : 基础测试环境
 Source Server Type    : MySQL
 Source Server Version : 50733
 Source Host           : 10.210.10.168:3306
 Source Schema         : infra_test

 Target Server Type    : MySQL
 Target Server Version : 50733
 File Encoding         : 65001

 Date: 25/04/2022 16:40:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_testcase
-- ----------------------------
DROP TABLE IF EXISTS `t_testcase`;
CREATE TABLE `t_testcase`  (
  `id` int(4) NOT NULL AUTO_INCREMENT COMMENT '表id',
  `case_id` int(3) NULL DEFAULT NULL COMMENT '测试编号',
  `module_name` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '模块名称',
  `title` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '测试标题',
  `url` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '请求url',
  `headers` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '请求头',
  `params` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '请求参数',
  `method` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '请求方法',
  `expected` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '预期值',
  `actual` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '实际值',
  `result` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '接口执行结果',
  `check_sql` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '检查sql',
  `extraction` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '参数提取',
  `enable` int(1) NOT NULL DEFAULT 1 COMMENT '用例状态，默认1（1：启用，0：禁用）',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `auther` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用例编写者',
  `data_type` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '入参关键字， params(一般在url?参数名=参数值), data(一般用于form表单类型参数)， json(一般用于json类型请求参数)',
  `pro_runing` int(1) NOT NULL DEFAULT 0 COMMENT '是否线上运行，默认0（1：运行，0：不运行）',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3259 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '基础自动化测试用例表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
