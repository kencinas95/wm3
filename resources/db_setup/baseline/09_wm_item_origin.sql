create table wm_item_origin
(
    id          int auto_increment primary key,
    name        varchar(150) not null,
    category_id varchar(10)  not null,
    constraint name
        unique (name),
    constraint wm_item_origin_category_id_603cf773_fk_wm_item_o
        foreign key (category_id) references wm_item_origin_category (code)
);
commit;

call sp_register_completed_migration('baseline', '09_wm_item_origin.sql');
