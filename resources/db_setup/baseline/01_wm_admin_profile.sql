create table wm_admin_profile
(
    code         varchar(32) not null primary key,
    description  varchar(64) not null,
    is_superuser tinyint(1)  not null,
    constraint description unique (description)
);
commit;

call sp_register_completed_migration('baseline', '01_wm_admin_profile.sql');
