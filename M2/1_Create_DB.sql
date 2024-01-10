/*crea bbdd*/
CREATE DATABASE IF NOT EXISTS zelda;

/*utilitza bbdd zelda*/
USE zelda;

/*elimina taules si eren creades*/
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS game_food;
DROP TABLE IF EXISTS game_weapons;
DROP TABLE IF EXISTS game_enemies;
DROP TABLE IF EXISTS game_sanctuaries_opened;
DROP TABLE IF EXISTS game_chests_opened;

/*Crea taules*/
CREATE TABLE IF NOT EXISTS game (
	game_id INT,
    user_name VARCHAR(50),
    date_started DATE,
    hearts_remaining INT,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region VARCHAR(20),
	created_at TIMESTAMP,
    modified_at TIMESTAMP
);
    
CREATE TABLE IF NOT EXISTS game_food (
	game_id INT,
	food_name VARCHAR(15),
    quantity_remaining INT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_weapons (
	game_id INT,
    weapon_name VARCHAR(15),
    equiped BOOLEAN,
    lives_remaining INT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP
);
    
CREATE TABLE IF NOT EXISTS game_enemies (
	game_id INT,
    region VARCHAR(20),
    num INT,
    xpos INT,
    ypos INT,
    lifes_remaining INT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_sanctuaries_opened (
	game_id INT,
    region VARCHAR(20),
    num INT,
    xpos INT,
    ypos INT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_chests_opened (
	game_id INT,
    region VARCHAR(20),
    num INT,
    xpos INT,
    ypos INT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP
);







