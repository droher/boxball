-- Built (then modified) using https://pgtune.leopard.in.ua/ with these settings:
-- DB Version: 11
-- OS Type: linux
-- DB Type: dw
-- Total Memory (RAM): 2 GB
-- CPUs num: 1
-- Connections num: 20
-- Data Storage: ssd
-- Substitute your own as you see fit
-- Note that work memory is extremely high relative to the other settings; this is because
-- few simultaneous connections are expected.
ALTER SYSTEM SET
 maintenance_work_mem = '512MB';
ALTER SYSTEM SET
 max_wal_size = '8GB';
ALTER SYSTEM SET
 checkpoint_timeout = '500';
ALTER SYSTEM SET
 work_mem = '512MB';