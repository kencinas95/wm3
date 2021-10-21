create table wm_user_contact
(
    id        int auto_increment primary key,
    value     varchar(250) not null,
    is_main   tinyint(1)   not null,
    status_id varchar(15)  not null,
    t_id      varchar(15)  not null,
    user_id   int          not null,
    constraint wm_user_contact_status_id_1cb436c0_fk_wm_user_c
        foreign key (status_id) references wm_user_contact_status (code),
    constraint wm_user_contact_t_id_b530dff6_fk_wm_user_contact_type_code
        foreign key (t_id) references wm_user_contact_type (code),
    constraint wm_user_contact_user_id_9b8f4038_fk_wm_user_uid
        foreign key (user_id) references wm_user (uid)
);
commit;

call sp_register_completed_migration('baseline', '29_wm_user_contact.sql');
