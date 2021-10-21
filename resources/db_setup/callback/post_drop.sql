drop procedure if exists sp_check_post_drop;

delimiter $$
create procedure sp_check_post_drop()
begin
    declare has_tables int;
    declare message varchar(256);
    declare t_tables varchar(256);

    select table_name
    from INFORMATION_SCHEMA.TABLES
    where
        table_name like 'wm_%'
        or table_name like 'infra_%'
        or table_name like 'django_%';
end$$
delimiter ;;

call sp_check_post_drop();
drop procedure sp_check_post_drop;
