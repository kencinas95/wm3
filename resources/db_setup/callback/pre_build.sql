-- Log actions (For DEV profile)
-- SET GLOBAL log_output = 'TABLE';
-- SET GLOBAL general_log = 'ON';

-- Drop procedures
drop procedure if exists sp_upgrade_version;
drop procedure if exists sp_register_procedure;
drop procedure if exists sp_register_completed_migration;

-- Drop tables
drop table if exists infra_sp;

-- Create tables
create table if not exists infra_versions
(
    version     varchar(32) not null primary key,
    updated_at  datetime    not null,
    is_active  tinyint(1)   not null,
    constraint version
        UNIQUE (version)
);
create table if not exists infra_properties
(
    `key`           varchar(128) not null primary key,
    `value`         varchar(256) not null,
    description     longtext,
    env             varchar(16)  not null
);
create table if not exists infra_migrations
(
    id          int auto_increment primary key,
    version     varchar(32) not null,
    script      varchar(256) not null,
    inserted_at datetime not null,
    constraint version_script unique (version, script)
);
create table if not exists infra_sp(
    name        varchar(128) not null primary key,
    package     varchar(128) not null,
    user        varchar(128) not null
);
commit;

-- Create procedures
delimiter $$
create procedure sp_register_completed_migration
(
    in p_version varchar(32),
    in p_sql_script varchar(256)
)
begin
    insert into infra_migrations(version, script, inserted_at)
    values (p_version, p_sql_script, now());
    commit;
end$$

create procedure sp_upgrade_version(in p_version varchar(32))
begin
    update infra_versions set is_active = 0 where is_active = 1;
    insert into infra_versions (version, updated_at, is_active) values (p_version, now(), 1);
    commit;
end$$

create procedure sp_register_procedure(
    in p_sp_name varchar(128),
    in p_package varchar(128)
)
begin
    insert into infra_sp (name, package, user)
    values (p_sp_name, p_package, current_user());
    commit;
end$$

delimiter ;

-- Register all procedures for user "wishmakers"
call sp_register_procedure('sp_register_completed_migration', 'infra');
call sp_register_procedure('sp_register_procedure', 'infra');
call sp_register_procedure('sp_upgrade_version', 'infra');
