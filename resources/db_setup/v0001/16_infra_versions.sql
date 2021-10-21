call sp_upgrade_version('v0001');
call sp_register_completed_migration('v001', '16_infra_versions.sql');