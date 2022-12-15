DROP TABLE IF EXISTS feedbacks;
DROP TABLE IF EXISTS events;

CREATE TABLE IF NOT EXISTS public.events
(
    id serial NOT NULL CONSTRAINT events_pk PRIMARY KEY,
    title varchar(256),
    "description" varchar(256),
    "location" varchar(256),
    likes integer DEFAULT 0,
    "image" varchar(256),
    event_datetime timestamp without time zone
);

CREATE UNIQUE INDEX IF NOT EXISTS events_idx ON events(id);

ALTER TABLE IF EXISTS public.events
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.feedbacks
(
    id serial NOT NULL CONSTRAINT feedbacks_pk PRIMARY KEY,
    event_id integer NOT NULL,
    content varchar(256),
    created_at timestamp without time zone,
    FOREIGN KEY (event_id) REFERENCES public.events (id)
);

CREATE UNIQUE INDEX IF NOT EXISTS feedbacks_idx ON feedbacks(id);

ALTER TABLE IF EXISTS public.feedbacks
    OWNER to postgres;

ALTER TABLE public.feedbacks
    ADD CONSTRAINT tbl_feedbacks_pk FOREIGN KEY (event_id) REFERENCES tbl_events (id);
