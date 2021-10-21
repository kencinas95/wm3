create table wm_item_stock
(
    id            int auto_increment primary key,
    stock         int unsigned not null,
    update_date   date         not null,
    last_buy_date datetime(6)  not null,
    item_id       int          not null,
    constraint wm_item_stock_item_id_e5b6d380_fk_wm_item_id
        foreign key (item_id) references wm_item (id)
);
commit;

call sp_register_completed_migration('baseline', '13_wm_item_stock.sql');
