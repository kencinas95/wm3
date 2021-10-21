create table wm_admin_session
(
    sid     varchar(128) not null primary key,
    since   datetime(6)  not null,
    user_id varchar(128) not null,
    constraint user_id
        unique (user_id),
    constraint wm_admin_session_user_id_ff021daa_fk_wm_admin_user_username
        foreign key (user_id) references wm_admin_user (username)
);
commit;

call sp_register_completed_migration('baseline', '04_wm_admin_session.sql');
