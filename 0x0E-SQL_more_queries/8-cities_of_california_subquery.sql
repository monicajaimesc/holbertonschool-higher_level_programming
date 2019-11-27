-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, name FROM cities
    WHERE state_id IN (SELECT id
    FROM states
    -- state has one record where..
    WHERE name = 'california') ORDER BY id;
