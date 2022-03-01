CREATE USER martin;
CREATE DABASE annotation_platform;
ALTER ROLE martin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE annotation_platform TO martin;
ALTER DATABASE annotation_platform OWNER TO martin;
