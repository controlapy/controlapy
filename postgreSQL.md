sudo -u postgres psql
CREATE DATABASE controlapy;
CREATE USER contralor WITH PASSWORD 'password';
ALTER ROLE contradolor SET client_encoding TO 'utf8';
ALTER ROLE contradolor SET default_transaction_isolation TO 'read committed';
ALTER ROLE contradolor SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE controlapy TO contradolor;