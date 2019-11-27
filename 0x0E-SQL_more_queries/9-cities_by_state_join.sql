-- lists all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities WHERE states.id = cities.states_id;
