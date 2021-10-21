create table wm_item_origin_category
(
    code        varchar(10) not null primary key,
    description varchar(25) not null
);
commit;

call sp_register_completed_migration('baseline', '08_wm_item_origin_category.sql');
