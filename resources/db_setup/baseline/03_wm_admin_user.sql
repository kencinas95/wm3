create table wm_admin_user
(
    username   varchar(128)    not null primary key,
    password   varchar(128)    not null,
    pepper     varchar(64)     not null,
    name       varchar(128)    not null,
    surname    varchar(128)    not null,
    email      varchar(254)    not null,
    phone      bigint unsigned not null,
    env        varchar(10)     not null,
    profile_id varchar(32)     not null,
    constraint wm_admin_user_profile_id_c8282593_fk_wm_admin_profile_code
        foreign key (profile_id) references wm_admin_profile (code)
);
commit;

call sp_register_completed_migration('baseline', '03_wm_admin_user.sql');
