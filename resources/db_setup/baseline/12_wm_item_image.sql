create table wm_item_image
(
    id        int auto_increment primary key,
    thumbnail tinyint(1)   not null,
    path      varchar(100) not null,
    mime_type varchar(50)  not null,
    item_id   int          not null,
    constraint wm_item_image_item_id_a1e8a415_fk_wm_item_id
        foreign key (item_id) references wm_item (id)
);
commit;

call sp_register_completed_migration('baseline', '12_wm_item_image.sql');
