-- test
-- EPDXYlYKwdIQXWGiT56xedTgHWHhwssY
insert into wm_admin_user(username, password, profile_id, pepper, name, surname, email, phone) values ('kevin.encinas', 'e3cc256db0b59d7055cb239468b3a2a56e34e8b996026330c563fee444929f9d13b2c2e9d068c74658a0be7369fa273a75108f096d72a9e7dfce2fe8fe24d7e2', 'SU', 'bcd0e1628fce692bff6fd8130ea2eb66d09026e7322616df48b50fc8ed8bc7b9', 'Kevin Nahuel', 'Encinas Vargas', 'encinaskevin096@gmail.com', 1138672849);
commit;

call sp_register_completed_migration('v001', 'prod/15_wm_admin_user.sql');
