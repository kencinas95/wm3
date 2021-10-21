insert into wm_purchase_status(code, description) values ('PAID', 'Pagado');
insert into wm_purchase_status(code, description) values ('IN_PROGRESS', 'En progreso');
insert into wm_purchase_status(code, description) values ('CUSTOMER_CANCELLED', 'Cancelado por el cliente');
insert into wm_purchase_status(code, description) values ('PRODUCER_CANCELLED', 'Cancelado por el productor');
insert into wm_purchase_status(code, description) values ('READY', 'Listo para el retiro');
insert into wm_purchase_status(code, description) values ('DELIVERED', 'Entregado');
commit;

call sp_register_completed_migration('v001', '11_wm_purchase_status.sql');
