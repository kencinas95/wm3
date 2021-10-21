create table wm_purchase_status
(
    code        varchar(25) not null primary key,
    description varchar(50) not null
);
commit;

call sp_register_completed_migration('baseline', '18_wm_purchase_status.sql');
