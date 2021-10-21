insert into wm_comment_complain_status(code, description) values ('SENT', 'Enviado');
insert into wm_comment_complain_status(code, description) values ('READ', 'Leido');
insert into wm_comment_complain_status(code, description) values ('ON_PROGRESS', 'En progreso');
insert into wm_comment_complain_status(code, description) values ('CLOSED', 'Cerrado');
commit;

call sp_register_completed_migration('v001', '08_wm_comment_complain_status.sql');
