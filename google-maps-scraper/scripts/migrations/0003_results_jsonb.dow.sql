BEGIN;
    ALTER TABLE results 
        ADD COLUMN title TEXT NOT NULL,
        ADD COLUMN category TEXT NOT NULL,
        ADD COLUMN address TEXT NOT NULL,
        ADD COLUMN openhours TEXT NOT NULL,
        ADD COLUMN website TEXT NOT NULL,
        ADD COLUMN phone TEXT NOT NULL,
        ADD COLUMN pluscode TEXT  NOT NULL,
        ADD COLUMN review_count INT NOT NULL,
        ADD COLUMN rating NUMERIC NOT NULL,
        ADD COLUMN latitude DOUBLE PRECISION NOT NULL DEFAULT 0,
        ADD COLUMN longitude DOUBLE PRECISION NOT NULL DEFAULT 0;
COMMIT;
