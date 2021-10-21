create table wm_comment
(
    comment_id int auto_increment primary key,
    message    varchar(250) not null,
    liked      tinyint(1)   null,
    created_at datetime(6)  not null,
    item_id    int          not null,
    user_id    int          not null,
    constraint wm_comment_item_id_d516f403_fk_wm_item_id
        foreign key (item_id) references wm_item (id),
    constraint wm_comment_user_id_e5f09d38_fk_wm_user_uid
        foreign key (user_id) references wm_user (uid)
);
commit;

call sp_register_completed_migration('baseline', '25_wm_comment.sql');
