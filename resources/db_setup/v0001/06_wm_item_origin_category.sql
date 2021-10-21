insert into wm_item_origin_category(code, description) values ('AN', 'Anime');
insert into wm_item_origin_category(code, description) values ('VG', 'Video Game');
insert into wm_item_origin_category(code, description) values ('US_SERIES', 'US Series');
insert into wm_item_origin_category(code, description) values ('JP_SERIES', 'JP Series');
insert into wm_item_origin_category(code, description) values ('KR_SERIES', 'KR Series');
insert into wm_item_origin_category(code, description) values ('US_COMIC', 'US Comics');
insert into wm_item_origin_category(code, description) values ('EU_COMIC', 'EU Comics');
insert into wm_item_origin_category(code, description) values ('JP_COMIC', 'Manga');
insert into wm_item_origin_category(code, description) values ('KR_COMIC', 'Manhwa');
insert into wm_item_origin_category(code, description) values ('ZN_COMIC', 'Manhua');
insert into wm_item_origin_category(code, description) values ('CARTOON', 'Cartoons');
insert into wm_item_origin_category(code, description) values ('MV', 'Peliculas');
insert into wm_item_origin_category(code, description) values ('WEB', 'Web/Meme');
insert into wm_item_origin_category(code, description) values ('OTHER', 'Otros');
commit;

call sp_register_completed_migration('v001', '06_wm_item_origin_category.sql');
