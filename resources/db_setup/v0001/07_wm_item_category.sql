insert into wm_item_category(code, description) values ('TOY::FLUFFY', 'Peluche');
commit;

call sp_register_completed_migration('v001', '07_wm_item_category.sql');
