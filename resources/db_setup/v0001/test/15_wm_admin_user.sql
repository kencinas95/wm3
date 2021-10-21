-- prod
-- 2K5ZAphhurkAF7bdV02SEIyaNdnNIEol
INSERT INTO wm_admin_user(username, password, profile_id, pepper, name, surname, email, phone, env)
VALUES ('kevin.encinas',
        '8ab1969ebd2d782dd68c9353714f9cab0f60bfaa3dd6ca94737a9076dbef447eaeaee465c267dabbef39a29ccf8a0d6024593df019bcd5643d4ef952e025685d',
        'SU',
        '929417478b50f0eb428ee5bebc06302f5e022747e831a8f0c1ecbf1448fc31e4',
        'Kevin Nahuel',
        'Encinas Vargas',
        'encinaskevin096@gmail.com',
        1138672849,
        'dev');
COMMIT;

call sp_register_completed_migration('v001', 'test/15_wm_admin_user.sql');
