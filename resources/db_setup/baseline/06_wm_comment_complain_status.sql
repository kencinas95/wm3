create table wm_comment_complain_status
(
    code        varchar(15) not null primary key,
    description varchar(50) not null
);
commit;

call sp_register_completed_migration('baseline', '06_wm_comment_complain_status.sql');
