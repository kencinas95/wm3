create table wm_user_tier
(
    code             varchar(15) not null primary key,
    base_points      int         not null,
    next_tier_points int         not null
);
commit;

call sp_register_completed_migration('baseline', '23_wm_user_tier.sql');
