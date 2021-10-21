insert into wm_user_status(code, description) values ('PENDING', 'Pendiente');
insert into wm_user_status(code, description) values ('ACTIVE', 'Activo');
insert into wm_user_status(code, description) values ('UNKNOWN', 'Desconocido');
insert into wm_user_status(code, description) values ('BANNED', 'Baneado');
insert into wm_user_status(code, description) values ('DELETED', 'Eliminado');
commit;

call sp_register_completed_migration('v001', '04_wm_user_status.sql');