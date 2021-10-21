create table wm_payment_type
(
    code        varchar(10) not null primary key,
    description varchar(50) not null,
    enabled     tinyint(1)  not null
);
commit;

call sp_register_completed_migration('baseline', '17_wm_payment_type.sql');
