create table wm_item_category
(
    code        varchar(25) not null primary key,
    description varchar(50) not null,
    constraint description
        unique (description)
);
commit;

call sp_register_completed_migration('baseline', '07_wm_item_category.sql');
