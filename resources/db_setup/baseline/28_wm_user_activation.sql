create table wm_user_activation
(
    code         varchar(128) not null primary key,
    created_at   datetime(6)  not null,
    activated_at datetime(6)  not null,
    user_id      int          not null,
    constraint wm_user_activation_user_id_7e40b9d3_fk_wm_user_uid
        foreign key (user_id) references wm_user (uid)
);
commit;

call sp_register_completed_migration('baseline', '28_wm_user_activation.sql');
