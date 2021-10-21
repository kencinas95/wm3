create table wm_user
(
    uid         int auto_increment primary key,
    name        varchar(100) not null,
    surname     varchar(100) not null,
    username    varchar(250) not null,
    password    varchar(128) not null,
    pepper      varchar(128) not null,
    birth_date  date         not null,
    created_at  datetime(6)  not null,
    last_login  datetime(6)  not null,
    news_feed   tinyint(1)   not null,
    tier_points int          not null,
    gender_id   varchar(3)   not null,
    status_id   varchar(15)  not null,
    tier_id     varchar(15)  not null,
    constraint username
        unique (username),
    constraint wm_user_gender_id_815e5a22_fk_wm_user_gender_code
        foreign key (gender_id) references wm_user_gender (code),
    constraint wm_user_status_id_f193b8b7_fk_wm_user_status_code
        foreign key (status_id) references wm_user_status (code),
    constraint wm_user_tier_id_97ad259c_fk_wm_user_tier_code
        foreign key (tier_id) references wm_user_tier (code)
);
commit;

call sp_register_completed_migration('baseline', '24_wm_user.sql');
