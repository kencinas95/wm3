insert into wm_user_tier(code, base_points, next_tier_points) values ('BRONZE', 0, 1000);
insert into wm_user_tier(code, base_points, next_tier_points) values ('SILVER', 10000, 5000);
insert into wm_user_tier(code, base_points, next_tier_points) values ('GOLD', 50000, 100000);
insert into wm_user_tier(code, base_points, next_tier_points) values ('PLATINUM', 100000, 500000);
insert into wm_user_tier(code, base_points, next_tier_points) values ('DIAMOND', 500000, 1000000);
insert into wm_user_tier(code, base_points, next_tier_points) values ('BLACK', 1000000, 1000000000);
commit;