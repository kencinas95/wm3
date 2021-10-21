insert into wm_user_contact_status(code, description) values ('PENDING', 'Pendiente');
insert into wm_user_contact_status(code, description) values ('TRUSTED', 'Confiable');
insert into wm_user_contact_status(code, description) values ('UNREACHABLE', 'Inalcanzable');
insert into wm_user_contact_status(code, description) values ('DEPRECATED', 'Obsoleto');
insert into wm_user_contact_status(code, description) values ('UNKNOWN', 'Desconocido');
commit;

call sp_register_completed_migration('v001', '02_wm_user_contact_status.sql');
