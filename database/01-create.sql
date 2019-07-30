-- Create database
CREATE DATABASE hmbot;
GRANT CONNECT ON DATABASE hmbot TO hmbot;

-- Connect to the hmbot database
-- \c hmbot;

-- Table 01. Languages
CREATE TABLE hm_lang (
    id serial PRIMARY KEY,
    code char(2) NOT NULL,
    name varchar(32) NOT NULL,
    active boolean NOT NULL DEFAULT true
);

-- Table 02. Messages
CREATE TABLE hm_message (
    id serial PRIMARY KEY,
    code varchar(32) NOT NULL,
    lang_id integer NOT NULL REFERENCES hm_lang,
    message varchar(128) NOT NULL,
    active boolean NOT NULL DEFAULT true
);

-- Table 03. Guilds (Discord servers)
CREATE TABLE hm_guild (
    id bigint PRIMARY KEY,
    lang_id integer NOT NULL REFERENCES hm_lang, 
    active boolean NOT NULL DEFAULT true
);

-- Table 04. React functionality
CREATE TABLE hm_react (
    id serial PRIMARY KEY,
    guild_id bigint NOT NULL,
    user_id integer NOT NULL,
    emote_id integer NOT NULL,
    active boolean NOT NULL DEFAULT true
);

-- Grant permissions to the bot
GRANT USAGE ON SCHEMA public TO hmbot;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO hmbot;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO hmbot;
