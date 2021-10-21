insert into wm_user_contact_type(code, description) values ('WEB::EMAIL', 'Web::Email');
insert into wm_user_contact_type(code, description) values ('WEB::FB', 'Web::Facebook');
insert into wm_user_contact_type(code, description) values ('WEB::IG', 'Web::Instagram');
insert into wm_user_contact_type(code, description) values ('WEB::TW', 'Web::Twitter');
insert into wm_user_contact_type(code, description) values ('PH::LC', 'Tel::Fijo');
insert into wm_user_contact_type(code, description) values ('PH::CP', 'Tel::Celular');
insert into wm_user_contact_type(code, description) values ('PH::WA', 'Tel::WhatsApp');
insert into wm_user_contact_type(code, description) values ('::TELEGRAM', 'Otro::Telegram');
commit;

call sp_register_completed_migration('v001', '05_wm_user_contact_type.sql');
