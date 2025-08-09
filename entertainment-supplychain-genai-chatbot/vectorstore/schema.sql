CREATE TABLE vector_store (
    id SERIAL PRIMARY KEY,
    document_title VARCHAR(255) NOT NULL,
    s3_path VARCHAR(255) NOT NULL,
    embedding FLOAT8[] NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_embedding ON vector_store USING ivfflat (embedding);