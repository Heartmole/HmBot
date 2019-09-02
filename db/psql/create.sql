-- Create database
CREATE DATABASE hmbot;
GRANT CONNECT ON DATABASE hmbot TO hmbot;

-- Connect to the hmbot database
-- \c hmbot;

-- Table 01. Guilds (Discord servers)
CREATE TABLE hm_guild (
    guild_id bigint PRIMARY KEY,
    lang varchar(5) DEFAULT NULL,
    active boolean NOT NULL DEFAULT true
);

-- Table 02. Reaction functionality
CREATE TABLE hm_react (
    react_id bigserial NOT NULL,
    guild_id bigint NOT NULL REFERENCES hm_guild,
    user_id bigint NOT NULL,
    emote_id bigint DEFAULT NULL,
    emote varchar(5) DEFAULT NULL,
    owner_id bigint NOT NULL,
    active boolean NOT NULL DEFAULT true
);

-- Grant permissions to the bot
GRANT USAGE ON SCHEMA public TO hmbot;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO hmbot;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO hmbot;
