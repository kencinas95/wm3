create table wm_offer_type
(
    code        varchar(15) not null primary key,
    description varchar(25) not null
);
commit;

call sp_register_completed_migration('baseline', '16_wm_offer_type.sql');
