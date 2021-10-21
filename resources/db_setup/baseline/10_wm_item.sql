create table wm_item
(
    id            int auto_increment primary key,
    name          varchar(100)   not null,
    description   varchar(1000)  not null,
    price         decimal(10, 2) not null,
    highlighted   tinyint(1)     not null,
    views         int unsigned   not null,
    sales         int unsigned   not null,
    creation_date date           not null,
    category_id   varchar(25)    not null,
    origin_id     int            not null,
    constraint wm_item_category_id_67507b32_fk_wm_item_category_code
        foreign key (category_id) references wm_item_category (code),
    constraint wm_item_origin_id_e957ae8c_fk_wm_item_origin_id
        foreign key (origin_id) references wm_item_origin (id)
);
commit;

call sp_register_completed_migration('baseline', '10_wm_item.sql');
