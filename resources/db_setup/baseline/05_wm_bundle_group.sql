create table wm_bundle_group
(
    id            char(32)    not null primary key,
    creation_date datetime(6) not null
);
commit;

call sp_register_completed_migration('baseline', '05_wm_bundle_group.sql');
