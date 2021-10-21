create table wm_comment_complain
(
    id         int auto_increment primary key,
    code       varchar(128) not null,
    message    varchar(500) not null,
    created_at datetime(6)  not null,
    replied_at datetime(6)  not null,
    status_id  varchar(15)  not null,
    user_id    int          not null,
    constraint wm_comment_complain_status_id_8ad292bb_fk_wm_commen
        foreign key (status_id) references wm_comment_complain_status (code),
    constraint wm_comment_complain_user_id_2c3f2115_fk_wm_user_uid
        foreign key (user_id) references wm_user (uid)
);
commit;

call sp_register_completed_migration('baseline', '26_wm_comment_compain.sql');
