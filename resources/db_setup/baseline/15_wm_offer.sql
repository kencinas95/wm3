create table wm_offer
(
    id            int auto_increment primary key,
    title         varchar(250)  not null,
    description   varchar(500)  not null,
    settings      varchar(1000) not null,
    creation_date datetime(6)   not null,
    start_date    datetime(6)   not null,
    end_date      datetime(6)   not null,
    status_id     varchar(15)   not null,
    constraint wm_offer_status_id_c2caefa6_fk_wm_offer_status_code
        foreign key (status_id) references wm_offer_status (code)
);
commit;

call sp_register_completed_migration('baseline', '15_wm_offer.sql');
