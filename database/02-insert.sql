-- Table 01. Languages
INSERT INTO hm_lang (code, name) VALUES ('en', 'English');
INSERT INTO hm_lang (code, name) VALUES ('es', 'Español');

-- Table 02. Messages (English)
INSERT INTO hm_message (lang_id, code, message) VALUES (1, 'ping_first', 'The bot is alive :)');
INSERT INTO hm_message (lang_id, code, message) VALUES (1, 'ping_second', 'It took {seconds} seconds to send this message.');
INSERT INTO hm_message (lang_id, code, message) VALUES (1, 'lang_usage', E'Usage: `{command} <language>`\nUse `{command} list` to see the supported languages.');
INSERT INTO hm_message (lang_id, code, message) VALUES (1, 'lang_list', E'**List of supported languages**\n{languages}');
INSERT INTO hm_message (lang_id, code, message) VALUES (1, 'lang_selected', 'English selected as the bot language.');
INSERT INTO hm_message (lang_id, code, message) VALUES (1, 'lang_unknown', E'Language {lang} not found.\nUse `{command} list` to see the supported languages.');
INSERT INTO hm_message (lang_id, code, message) VALUES (1, 'flag_usage', E'Usage: `{command} <flag name>`\nUse `{command} list` to see the existing flag filters.');
INSERT INTO hm_message (lang_id, code, message) VALUES (1, 'flag_list', E'**List of flag filters**\n{flags}');
INSERT INTO hm_message (lang_id, code, message) VALUES (1, 'react_usage', 'Usage: `{command} :emote: @user`');
-- Table 02. Messages (Español)
INSERT INTO hm_message (lang_id, code, message) VALUES (2, 'ping_first', 'El bot está vivo :)');
INSERT INTO hm_message (lang_id, code, message) VALUES (2, 'ping_second', 'Tomó {seconds} segundos para enviar este mensaje.');
INSERT INTO hm_message (lang_id, code, message) VALUES (2, 'lang_usage', E'Modo de uso: `{command} <idioma>`\nUse `{command} list` para ver los idiomas soportados.');
INSERT INTO hm_message (lang_id, code, message) VALUES (2, 'lang_list', E'**Lista de idiomas soportados**\n{languages}');
INSERT INTO hm_message (lang_id, code, message) VALUES (2, 'lang_selected', 'Se seleccionó el español como el idioma para el bot.');
INSERT INTO hm_message (lang_id, code, message) VALUES (2, 'lang_unknown', E'No se encontró el idioma {lang}.\nUse `{command} list` para ver los idiomas soportados.');
INSERT INTO hm_message (lang_id, code, message) VALUES (2, 'flag_usage', E'Modo de uso: `{command} <bandera>`\nUse `{command} list` para ver las filtros de banderas existentes.');
INSERT INTO hm_message (lang_id, code, message) VALUES (2, 'flag_list', E'**Lista de filtros de banderas**\n{flags}');
INSERT INTO hm_message (lang_id, code, message) VALUES (2, 'react_usage', 'Modo de uso: `{command} <emote> <@usuario>`');
