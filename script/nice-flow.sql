CREATE TABLE `easy_project`
(
    `id`           int     NOT NULL AUTO_INCREMENT,
    `project_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目名称',
    `project_code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目编码',
    `is_delete`    tinyint NOT NULL DEFAULT '0' COMMENT '是否删除: 0=否, 1=是',
    `create_time`  datetime(0) NOT NULL COMMENT '创建时间',
    `update_time`  datetime(0) NOT NULL COMMENT '更新时间',
    `delete_time`  datetime(0)  COMMENT '删除时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COMMENT '项目表' COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

CREATE TABLE `easy_flow`
(
    `id`               int     NOT NULL AUTO_INCREMENT,
    `project_id`       int     NOT NULL COMMENT '项目id',
    `flow_name`        varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'flow名称',
    `flow_code`        varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'flow编码',
    `flow_content`     varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'flow内容',
    `flow_param`       varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'flow参数',
    `flow_description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'flow描述',
    `flow_alarm_email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'flow告警邮箱',
    `flow_cron`        varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'flow定时表达式',
    `is_delete`        tinyint NOT NULL DEFAULT '0' COMMENT '是否删除: 0=否, 1=是',
    `create_time`      datetime(0) NOT NULL COMMENT '创建时间',
    `update_time`      datetime(0) NOT NULL COMMENT '更新时间',
    `delete_time`      datetime(0)  COMMENT '删除时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COMMENT 'flow表' COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;


CREATE TABLE `easy_flow_version`
(
    `id`           int          NOT NULL AUTO_INCREMENT,
    `flow_id`      int          NOT NULL COMMENT '任务，主键ID',
    `flow_content` varchar(255) NOT NULL COMMENT '源代码',
    `flow_remark`  varchar(128) COMMENT '备注',
    `is_delete`    tinyint      NOT NULL DEFAULT '0' COMMENT '是否删除: 0=否, 1=是',
    `create_time`  datetime(0) NOT NULL COMMENT '创建时间',
    `update_time`  datetime(0) NOT NULL COMMENT '更新时间',
    `delete_time`  datetime(0)  COMMENT '删除时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COMMENT 'flow版本记录表' COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;


CREATE TABLE `easy_plugin`
(
    `id`             int     NOT NULL AUTO_INCREMENT,
    `plugin_name`    varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '插件名称',
    `plugin_icon`    varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '插件图标',
    `plugin_type`    varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '插件类型，用于插件分类',
    `plugin_id`      varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '插件唯一标识',
    `plugin_version` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '插件版本',
    `plugin_status`  tinyint NOT NULL COMMENT '插件状态: 0=禁用, 1=启用',
    `plugin_source`  tinyint NOT NULL COMMENT '插件来源: 0=系统自带, 1=第三方',
    `is_delete`      tinyint NOT NULL DEFAULT '0' COMMENT '是否删除: 0=否, 1=是',
    `create_time`    datetime(0) NOT NULL COMMENT '创建时间',
    `update_time`    datetime(0) NOT NULL COMMENT '更新时间',
    `delete_time`    datetime(0)  COMMENT '删除时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COMMENT '插件表' COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

CREATE TABLE `easy_flow_instance`
(
    `id`           int     NOT NULL AUTO_INCREMENT,
    `flow_id`      varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目名称',
    `project_code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目编码',
    `is_delete`    tinyint NOT NULL DEFAULT '0' COMMENT '是否删除: 0=否, 1=是',
    `create_time`  datetime(0) NOT NULL COMMENT '创建时间',
    `update_time`  datetime(0) NOT NULL COMMENT '更新时间',
    `delete_time`  datetime(0)  COMMENT '删除时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COMMENT 'flow执行实例表' COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;
