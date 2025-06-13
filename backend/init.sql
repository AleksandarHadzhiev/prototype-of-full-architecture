 CREATE TABLE IF NOT EXISTS todos 
                (id SERIAL, 
                title VARCHAR(255) NOT NULL,
                content VARCHAR() NOT NULL, 
                date_created VARCHAR(25) NOT NULL,
                date_completed VARCHAR(25) DEFAULT NULL,
                date_to_complete VARCHAR(25) DEFAULT NULL,
                status VARCHAR() DEFAULT 'pending');

