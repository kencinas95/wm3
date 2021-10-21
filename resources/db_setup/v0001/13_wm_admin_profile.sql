INSERT INTO wm_admin_profile (code, description, is_superuser) VALUES ('SU', 'Superuser', 1);
COMMIT;

call sp_register_completed_migration('v001', '13_wm_admin_profile.sql');
