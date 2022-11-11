DROP TABLE IF EXISTS tbl_feedbacks;
DROP TABLE IF EXISTS tbl_events;

CREATE TABLE IF NOT EXISTS public.tbl_events
(
    id serial NOT NULL CONSTRAINT events_pk PRIMARY KEY,
    title varchar(256),
    "description" varchar(256),
    "location" varchar(256),
    likes integer DEFAULT 0,
    "image" varchar(256),
    event_date timestamp without time zone
);

CREATE UNIQUE INDEX IF NOT EXISTS tbl_events_idx ON tbl_events(id);

ALTER TABLE IF EXISTS public.tbl_events
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.tbl_feedbacks
(
    id serial NOT NULL CONSTRAINT feedbacks_pk PRIMARY KEY,
    event_id integer NOT NULL,
    content varchar(256),
    created_at timestamp without time zone,
    FOREIGN KEY (event_id) REFERENCES public.tbl_events (id)
);

CREATE UNIQUE INDEX IF NOT EXISTS tbl_feedbacks_idx ON tbl_feedbacks(id);

ALTER TABLE IF EXISTS public.tbl_feedbacks
    OWNER to postgres;
