create table django_content_type
(
    id        int auto_increment primary key,
    app_label varchar(100) not null,
    model     varchar(100) not null,
    constraint django_content_type_app_label_model_unique unique (app_label, model)
);
commit;

create table django_session
(
    session_key  varchar(40) not null primary key,
    session_data longtext    not null,
    expire_date  datetime(6) not null
);
commit;

create index django_session_expire_date on django_session (expire_date);
commit;

call sp_register_completed_migration('baseline', '00_django_tables.sql');
