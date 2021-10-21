create table wm_user_gender
(
    code        varchar(3)  not null primary key,
    description varchar(25) not null,
    constraint description
        unique (description)
);
commit;

call sp_register_completed_migration('baseline', '21_wm_user_gender.sql');
