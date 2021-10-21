insert into wm_offer_status(code, description) values ('DISABLED', 'Desactivada');
insert into wm_offer_status(code, description) values ('CANCELLED', 'Cancelada');
insert into wm_offer_status(code, description) values ('RUNNING', 'Corriendo');
insert into wm_offer_status(code, description) values ('STOPPED', 'Frenada');
commit ;

call sp_register_completed_migration('v001', '12_wm_offer_status.sql');
