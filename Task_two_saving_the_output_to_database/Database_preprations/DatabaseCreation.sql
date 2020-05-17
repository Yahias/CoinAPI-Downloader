-- =============================================
-- Author:      Mohamed Yahia
-- Create date: May,2020
-- Description: This script for creating the database for the historical data fetched from coinAPI.io
-- =============================================


-- Database name: coin_api
--Drop the database if exists.
DROP DATABASE coin_api;

CREATE DATABASE coin_api
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
