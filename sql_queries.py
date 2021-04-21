# DROP TABLES IF EXISTS
query_drop_musicsession = "DROP TABLE IF EXISTS music_session"

query_drop_usersession = "DROP TABLE IF EXISTS user_session"

query_drop_songsuser = "DROP TABLE IF EXISTS songs_user"

drop_queries = [
    query_drop_musicsession,
    query_drop_usersession,
    query_drop_songsuser,
]


# CREATE TABLES
query_create_musicsession = "CREATE TABLE IF NOT EXISTS music_session \
                    (session_id int, item_in_session int, artist text, \
                    song_title text, song_length int, \
                    PRIMARY KEY(session_id, item_in_session))"

query_create_usersession = "CREATE TABLE IF NOT EXISTS user_session \
                    (user_id int, session_id int, artist text, song_title text, \
                    item_in_session int, user_first_name text, user_last_name text, \
                    PRIMARY KEY(user_id, session_id, item_in_session))"

query_create_songsuser = "CREATE TABLE IF NOT EXISTS songs_user \
                    (song_title text, user_id int, user_first_name text, user_last_name text, \
                    PRIMARY KEY(song_title, user_id))"

create_queries = [
    query_create_musicsession,
    query_create_usersession,
    query_create_songsuser,
]


# INSERT INTO TABLES
query_insert_musicsession = "INSERT INTO music_session \
                            (session_id, item_in_session, artist, song_title, song_length) \
                            VALUES (%s, %s, %s, %s, %s)"

query_insert_usersession = "INSERT INTO user_session \
                            (user_id, session_id, artist, song_title, \
                            item_in_session, user_first_name, user_last_name) \
                            VALUES (%s, %s, %s, %s, %s, %s, %s)"

query_insert_songsuser = "INSERT INTO songs_user \
                            (song_title, user_id, user_first_name, user_last_name) \
                            VALUES (%s, %s, %s, %s)"

insert_queries = [
    query_insert_musicsession,
    query_insert_usersession,
    query_insert_songsuser,
]


# SELECT FROM TABLES
query_select_musicsession = "SELECT artist, song_title, song_length \
                            FROM music_session \
                            WHERE session_id=338 AND item_in_session=4"

query_select_usersession = "SELECT artist, song_title, user_first_name, user_last_name \
                            FROM user_session \
                            WHERE user_id=10 AND session_id=182"

query_select_songuser = "SELECT user_first_name, user_last_name FROM songs_user \
                        WHERE song_title='All Hands Against His Own'"

select_queries = [
    query_select_musicsession,
    query_select_usersession,
    query_select_songuser,
]

