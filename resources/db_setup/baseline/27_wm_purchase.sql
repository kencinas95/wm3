create table wm_purchase
(
    id              int auto_increment primary key,
    final_price     double      not null,
    creation_date   date        not null,
    payment_date    date        not null,
    bundle_group_id char(32)    not null,
    payment_id      varchar(10) not null,
    user_id         int         not null,
    constraint wm_purchase_bundle_group_id_e6405f81_fk_wm_bundle_group_id
        foreign key (bundle_group_id) references wm_bundle_group (id),
    constraint wm_purchase_payment_id_5eef6cbf_fk_wm_payment_type_code
        foreign key (payment_id) references wm_payment_type (code),
    constraint wm_purchase_user_id_ecca3930_fk_wm_user_uid
        foreign key (user_id) references wm_user (uid)
);
commit;

call sp_register_completed_migration('baseline', '27_wm_purchase.sql');
