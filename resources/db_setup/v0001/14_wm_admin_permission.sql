INSERT INTO wm_admin_permission (code, profile_id, `table`, allow_select, allow_insert, allow_update, allow_delete)
VALUES (1, 'SU', '*', 1, 1, 1, 1);
COMMIT;

call sp_register_completed_migration('v001', '14_wm_admin_permission.sql');
