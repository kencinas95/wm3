create table wm_user_session
(
    sid     varchar(256) not null primary key,
    expires datetime(6)  not null,
    user_id int          not null,
    constraint wm_user_session_user_id_e5b444eb_fk_wm_user_uid
        foreign key (user_id) references wm_user (uid)
);
commit;

call sp_register_completed_migration('baseline', '31_wm_user_session.sql');
