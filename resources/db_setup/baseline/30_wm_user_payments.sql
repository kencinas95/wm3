create table wm_user_payments
(
    id             int auto_increment primary key,
    user_id        int         not null,
    paymenttype_id varchar(10) not null,
    constraint wm_user_payments_user_id_paymenttype_id_eedfe9f2_uniq
        unique (user_id, paymenttype_id),
    constraint wm_user_payments_paymenttype_id_d634c841_fk_wm_payment_type_code
        foreign key (paymenttype_id) references wm_payment_type (code),
    constraint wm_user_payments_user_id_76025a0a_fk_wm_user_uid
        foreign key (user_id) references wm_user (uid)
);
commit;

call sp_register_completed_migration('baseline', '30_wm_user_payments.sql');
