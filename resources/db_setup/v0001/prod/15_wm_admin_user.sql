-- test
-- uLWwFpLWZuVTQIVdRseTskcCS6tUU1oE
INSERT INTO wm_admin_user(username, password, profile_id, pepper, name, surname, email, phone, env)
VALUES ('kevin.encinas',
        '0e418b989218dbd5528f68c0ae5631c45c2ef81a65d4c4bca648092ec0ee69d0eac50ba20622a0690226ae514dee300f5b7da4af81a3e64c91831892705b989e',
        'SU',
        'e998ca26f392dabfbf59632164be3b1784ee52c797d95ab600fabe913d750bc6',
        'Kevin Nahuel',
        'Encinas Vargas',
        'encinaskevin096@gmail.com',
        1138672849,
        'dev');
COMMIT;

call sp_register_completed_migration('v001', 'prod/15_wm_admin_user.sql');
