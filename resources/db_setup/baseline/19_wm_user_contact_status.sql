create table wm_user_contact_status
(
    code        varchar(15) not null primary key,
    description varchar(15) not null
);
commit;

call sp_register_completed_migration('baseline', '19_wm_user_contact_status.sql');
