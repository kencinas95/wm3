create table wm_bundle
(
    id              int auto_increment primary key,
    bundle_group_id char(32) not null,
    item_id         int      not null,
    constraint wm_bundle_bundle_group_id_d4f7ff07_fk_wm_bundle_group_id
        foreign key (bundle_group_id) references wm_bundle_group (id),
    constraint wm_bundle_item_id_211cbd61_fk_wm_item_id
        foreign key (item_id) references wm_item (id)
);
commit;

call sp_register_completed_migration('baseline', '11_wm_bundle.sql');
