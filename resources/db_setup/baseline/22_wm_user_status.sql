create table wm_user_status
(
    code        varchar(15) not null primary key,
    description varchar(50) not null,
    constraint description
        unique (description)
);
commit;

call sp_register_completed_migration('baseline', '22_wm_user_status.sql');
