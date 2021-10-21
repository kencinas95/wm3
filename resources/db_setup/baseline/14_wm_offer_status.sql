create table wm_offer_status
(
    code        varchar(15) not null primary key,
    description varchar(25) not null
);
commit;

call sp_register_completed_migration('baseline', '14_wm_offer_status.sql');
