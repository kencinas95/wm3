create table wm_user_contact_type
(
    code        varchar(15) not null primary key,
    description varchar(50) not null
);
commit;

call sp_register_completed_migration('baseline', '20_wm_user_contact_type.sql');
