insert into wm_payment_type(code, description, enabled) values ('CASH', 'Efectivo', 1);
insert into wm_payment_type(code, description, enabled) values ('TRANS', 'Transferencia Bancaria', 1);
insert into wm_payment_type(code, description, enabled) values ('PF', 'PagoFacil', 1);
insert into wm_payment_type(code, description, enabled) values ('RP', 'RapiPago', 1);
insert into wm_payment_type(code, description, enabled) values ('DEBIT', 'Tarjeta (debito)', 0);
insert into wm_payment_type(code, description, enabled) values ('CREDIT', 'Tarjeta (credito)', 0);
insert into wm_payment_type(code, description, enabled) values ('MP', 'MercadoPago', 1);
insert into wm_payment_type(code, description, enabled) values ('PP', 'PayPal', 0);
commit;