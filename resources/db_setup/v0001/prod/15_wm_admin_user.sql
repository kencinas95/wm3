-- prod
-- HsQnMEIOHCtGCJXz29OlPBHGOt9LOzwV
insert into wm_admin_user(username, password, profile_id, pepper, name, surname, email, phone, env) values ('kevin.encinas', 'd1c78d00337848434e2d3739a7bc4508c2f754a4f10fa92ecfcf2bc0c8b29564fa67cc41b1d6a4176ddd81d2e39ae690ef828c3405793363d00ab2a8ea6f179c', 'SU', 'dac7788d748c097ef1a8f1921b45f4da1c367c2ab86b74a07e34b6bfc70e7ccd', 'Kevin Nahuel', 'Encinas Vargas', 'encinaskevin096@gmail.com', 1138672849, 'prod');
commit;

call sp_register_completed_migration('v001', 'prod/15_wm_admin_user.sql');
