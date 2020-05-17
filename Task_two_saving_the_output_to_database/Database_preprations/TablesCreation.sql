-- =============================================
-- Author:      Mohamed Yahia
-- Create date: May,2020
-- Description: This script for creation of tables that will store the historical data fetched from coinAPI.io
-- =============================================



--Creation of table : cryptocurrencies.
-- Table: public.cryptocurrencies
--Drop table if exist.
DROP TABLE public.cryptocurrencies CASCADE ;

CREATE TABLE public.cryptocurrencies
(
    currency character varying(500) COLLATE pg_catalog."default",
    currency_code character varying(500) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cryptocurrencies_pkey PRIMARY KEY (currency_code)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.cryptocurrencies
    OWNER to postgres;




-- Creation of table: public.ohlcv_historical_data;

--Drop table if exist.
DROP TABLE public.ohlcv_historical_data;

CREATE TABLE public.ohlcv_historical_data
(
    time_period_start timestamp with time zone,
    time_period_end timestamp with time zone,
    time_open timestamp with time zone,
    time_close timestamp with time zone,
    price_open double precision,
    price_high double precision,
    price_low double precision,
    price_close double precision,
    volume_traded double precision,
    trades_count bigint,
    currency_code text COLLATE pg_catalog."default",
    CONSTRAINT ohlcv_historical_data_currency_code_fkey FOREIGN KEY (currency_code)
        REFERENCES public.cryptocurrencies (currency_code) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE SET NULL
        NOT VALID
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.ohlcv_historical_data
    OWNER to postgres;