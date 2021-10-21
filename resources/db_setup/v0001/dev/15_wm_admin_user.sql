-- dev
-- n6RrVZoy65Uhz2luk7MPbIZGUzBfhEK2
insert into wm_admin_user(username, password, profile_id, pepper, name, surname, email, phone) values ('kevin.encinas', 'aa0a6eed7d8ec8d476c4eb4290385a69a2ec33eed50464ab151025f463b87d4e56de7366c5dd48e039ca3081914133fc0f102df73de2e54fac2a80be7b9926dd', 'SU', '8b47e98c4e74b5eedbabc148435f88171be95e815b3278e088ad82dedfaabab1', 'Kevin Nahuel', 'Encinas Vargas', 'encinaskevin096@gmail.com', 1138672849);
commit;

call sp_register_completed_migration('v001', 'dev/15_wm_admin_user.sql');
