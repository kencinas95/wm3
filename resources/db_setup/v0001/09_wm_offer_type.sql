insert into wm_offer_type(code, description) values ('DISCOUNT', 'Descuento');
insert into wm_offer_type(code, description) values ('BONUS', 'Bonus');
insert into wm_offer_type(code, description) values ('GIFT', 'Regalo');
commit;

call sp_register_completed_migration('v001', '09_wm_offer_type.sql');
