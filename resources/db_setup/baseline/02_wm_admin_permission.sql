create table wm_admin_permission
(
    code         int auto_increment primary key,
    `table`      varchar(128) not null,
    allow_select tinyint(1)   not null,
    allow_insert tinyint(1)   not null,
    allow_update tinyint(1)   not null,
    allow_delete tinyint(1)   not null,
    profile_id   varchar(32)  not null,
    constraint wm_admin_permission_profile_id_0cea396d_fk_wm_admin_profile_code
        foreign key (profile_id) references wm_admin_profile (code)
);
commit;

call sp_register_completed_migration('baseline', '02_wm_admin_permission.sql');
