-- Drop all django tables from database
drop table if exists django_content_type;
drop table if exists django_session;
drop table if exists django_migrations;


-- Drop all wm tables from database
set FOREIGN_KEY_CHECKS = 0;
drop table if exists wm_admin_permission;
drop table if exists wm_admin_profile;
drop table if exists wm_admin_session;
drop table if exists wm_admin_user;
drop table if exists wm_bundle;
drop table if exists wm_bundle_group;
drop table if exists wm_comment;
drop table if exists wm_comment_complain;
drop table if exists wm_comment_complain_status;
drop table if exists wm_item;
drop table if exists wm_item_category;
drop table if exists wm_item_image;
drop table if exists wm_item_origin;
drop table if exists wm_item_origin_category;
drop table if exists wm_item_stock;
drop table if exists wm_offer;
drop table if exists wm_offer_status;
drop table if exists wm_offer_type;
drop table if exists wm_payment_type;
drop table if exists wm_purchase;
drop table if exists wm_purchase_status;
drop table if exists wm_user;
drop table if exists wm_user_activation;
drop table if exists wm_user_contact;
drop table if exists wm_user_contact_status;
drop table if exists wm_user_contact_type;
drop table if exists wm_user_gender;
drop table if exists wm_user_payments;
drop table if exists wm_user_session;
drop table if exists wm_user_status;
drop table if exists wm_user_tier;
commit;
set FOREIGN_KEY_CHECKS = 1;

-- Drop all infra tables from database
drop table if exists infra_versions;
drop table if exists infra_properties;
drop table if exists infra_migrations;
drop table if exists infra_sp;
commit;

-- Drop all procedures from database
drop procedure if exists sp_upgrade_version;
drop procedure if exists sp_register_procedure;
drop procedure if exists sp_register_completed_migration;

-- Delete all logs
SET GLOBAL general_log = 'OFF';
RENAME TABLE mysql.general_log TO mysql.general_log_temp;
DELETE FROM mysql.`general_log_temp`;
RENAME TABLE mysql.general_log_temp TO mysql.general_log;
SET GLOBAL general_log = 'ON';

commit;
