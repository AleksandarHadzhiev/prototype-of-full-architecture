CREATE TABLE IF NOT EXISTS todos 
                (id SERIAL, 
                title VARCHAR(255) NOT NULL,
                content TEXT NOT NULL, 
                date_created VARCHAR(25) NOT NULL,
                date_completed VARCHAR(25),
                date_to_complete VARCHAR(25),
                status VARCHAR(15) DEFAULT 'pending');