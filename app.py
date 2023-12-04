from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de monstros (pode ser substituída por um banco de dados)
monstersdungeon = [
 {"id": 1, "Monster": "Devil Troop of Desire", "Área": "D1R1", "Level": 46, "HP": 9.100, "EXP": 3.500},
 {"id": 2, "Monster": "Doggebi of Monster Face", "Área": "D1R1", "Room": "1", "Level": 46, "HP": 9.100, "EXP": 3.500},
 {"id": 3, "Monster": "Doggebi with a Gong", "Área": "D1R5", "Room": "5", "Level": 46, "HP": 9.100, "EXP": 3.500},
 {"id": 4, "Monster": "Drunken Doggebi", "Área": "D1R1", "Room": "1", "Level": 47, "HP": 9.500, "EXP": 4.000},
 {"id": 5, "Monster": "Devil Troop of Pain", "Área": "D1R5", "Room": "5", "Level": 47, "HP": 9.500, "EXP": 4.000},
 {"id": 6, "Monster": "Doggebi with a Mask of Black Crow", "Área": "D1R5", "Room": "5", "Level": 48, "HP": 9.800, "EXP": 4.700},
 {"id": 7, "Monster": "Devil Troop of Jealousy", "Área": "D1R3", "Room": "3", "Level": 48, "HP": 9.800, "EXP": 4.700},
 {"id": 8, "Monster": "Devil Troop of Hatred", "Área": "D1R5", "Room": "5", "Level": 48, "HP": 9.800, "EXP": 4.700},
 {"id": 9, "Monster": "Giant Doggebi", "Área": "D1R9", "Room": "9", "Level": 49, "HP": 10.000, "EXP": 5.400},
 {"id": 10, "Monster": "Devil Troop of Madness", "Área": "D1R9", "Room": "9", "Level": 49, "HP": 10.000, "EXP": 5.400},
 {"id": 11, "Monster": "Guardian of Doggebi", "Área": "D1R9", "Room": "9", "Level": 50, "HP": 11.000, "EXP": 6.300},
 {"id": 12, "Monster": "Devil Troop of Anger", "Área": "D1R9", "Room": "9", "Level": 50, "HP": 11.000, "EXP": 6.300},
 {"id": 13, "Monster": "Minister of the Royal Tomb", "Área": "D2H1R1", "Hall": "1", "Room": "1", "Level": 61, "HP": 16.000, "EXP": 34.000},
 {"id": 14, "Monster": "The Royal Tomb Keeper", "Área": "D2H1R1", "Hall": "1", "Room": "1", "Level": 62, "HP": 17.000, "EXP": 39.000},
 {"id": 15, "Monster": "The Royal Tomb Keeper", "Área": "D2H1R1", "Hall": "1", "Room": "ALL", "Level": 63, "HP": 18.000, "EXP": 46.000},
 {"id": 16, "Monster": "The Royal Tomb Keeper", "Área": "D2H1R1", "Hall": "1", "Room": "ALL", "Level": 64, "HP": 18.000, "EXP": 54.000},
 {"id": 17, "Monster": "The Royal Tomb Keeper", "Área": "D2H1R1", "Hall": "1", "Room": "ALL", "Level": 65, "HP": 19.000, "EXP": 64.000},
 {"id": 18, "Monster": "Warrior of Shadow Troop", "Área": "D2H2R9", "Hall": "2", "Room": "9", "Level": 66, "HP": 20.000, "EXP": 75.000},
 {"id": 19, "Monster": "Hook of Shadow Troop", "Área": "D2H2R4", "Hall": "2", "Room": "4", "Level": 67, "HP": 21.000, "EXP": 89.000},
 {"id": 20, "Monster": "Watcher of Shadow Troop", "Área": "D2H2R3", "Hall": "2", "Room": "3", "Level": 68, "HP": 22.000, "EXP": 110.000},
 {"id": 21, "Monster": "Chief Warrior of Shadow Troop", "Área": "D2H2R1", "Hall": "3", "Room": "1", "Level": 69, "HP": 23.000, "EXP": 130.000},
 {"id": 22, "Monster": "Spear Hand of Shadow Troop", "Área": "D2H3R2", "Hall": "3", "Room": "2", "Level": 70, "HP": 24.000, "EXP": 150.000},
 {"id": 23, "Monster": "1st Commander of The Royal Tomb", "Área": "D2H3R4", "Hall": "3", "Room": "4", "Level": 70, "HP": 440.000, "EXP": 150.000},
 {"id": 24, "Monster": "2nd Commander of The Royal Tomb", "Área": "D2H3R4", "Hall": "3", "Room": "4", "Level": 70, "HP": 440.000, "EXP": 150.000},
 {"id": 25, "Monster": "3rd Commander of The Royal Tomb", "Área": "D2H3R4", "Hall": "3", "Room": "4", "Level": 70, "HP": 440.000, "EXP": 150.000},
 {"id": 26, "Monster": "Chief Escort of The Royal Tomb", "Área": "D2H3R4", "Hall": "3", "Room": "4", "Level": 70, "HP": 440.000, "EXP": 150.000},
 {"id": 27, "Monster": "Chief Guard of The Royal Tomb", "Área": "D2H3R4", "Hall": "3", "Room": "4", "Level": 70, "HP": 440.000, "EXP": 150.000},
 {"id": 28, "Monster": "Imperial Commander of The Royal Tomb", "Área": "D2H3R4", "Hall": "3", "Room": "4", "Level": 70, "HP": 440.000, "EXP": 150.000},
 {"id": 29, "Monster": "Lord of Shadow Troop", "Área": "D2H3R4", "Hall": "3", "Room": "4", "Level": 70, "HP": 440.000, "EXP": 150.000}, 
 {"id": 30, "Monster": "High Class Doggebi of Monster Face", "Área": "D3F1", "Floor": "1", "Level": 51, "HP": 11.000, "EXP": 7.300},
 {"id": 31, "Monster": "High Class Doggebi with a Gong", "Área": "D3F1", "Floor": "1", "Level": 51, "HP": 11.000, "EXP": 7.300},
 {"id": 32, "Monster": "High Class Drunken Doggebi", "Área": "D3F1", "Floor": "1", "Level": 51, "HP": 11.000, "EXP": 7.300},
 {"id": 33, "Monster": "High Class Doggebi with a Mask of Black Crow", "Área": "D3F1", "Floor": "1", "Level": 52, "HP": 11.000, "EXP": 8.400},
 {"id": 34, "Monster": "High Class Drunken Doggebi", "Área": "D3F1", "Floor": "1", "Level": 53, "HP": 12.000, "EXP": 9.800},
 {"id": 35, "Monster": "Chief of Demon Crack Troop", "Área": "D3F2", "Floor": "2", "Level": 54, "HP": 12.000, "EXP": 11.000},
 {"id": 36, "Monster": "Demon Crack Soldier", "Área": "D3F2", "Floor": "2", "Level": 54, "HP": 12.000, "EXP": 11.000},
 {"id": 37, "Monster": "Monster of Demon Crack Troop", "Área": "D3F2", "Floor": "2", "Level": 54, "HP": 12.000, "EXP": 11.000},
 {"id": 38, "Monster": "White Beast of Demon Crack Troop", "Área": "D3F3", "Floor": "3", "Level": 57, "HP": 14.000, "EXP": 18.000},
 {"id": 39, "Monster": "Blue Beast of Demon Crack Troop", "Área": "D3F3", "Floor": "3", "Level": 57, "HP": 14.000, "EXP": 18.000},
 {"id": 40, "Monster": "Punitive Force of Demon Crack Troop", "Área": "D3F3", "Floor": "3", "Level": 58, "HP": 14.000, "EXP": 21.000},
 {"id": 41, "Monster": "Hermit of White Beard", "Área": "D3F4", "Floor": "4", "Level": 71, "HP": 26.000, "EXP": 180.000},
 {"id": 42, "Monster": "Hermit of Long Beard", "Área": "D3F4", "Floor": "4", "Level": 72, "HP": 27.000, "EXP": 210.000},
 {"id": 43, "Monster": "Hermit of Red Face", "Área": "D3F4", "Floor": "4", "Level": 73, "HP": 28.000, "EXP": 250.000},
 {"id": 44, "Monster": "Hermit of White Beard", "Área": "D3F5", "Floor": "5", "Level": 74, "HP": 30.000, "EXP": 300.000},
 {"id": 45, "Monster": "Hermit of Mask", "Área": "D3F5", "Floor": "5", "Level": 75, "HP": 31.000, "EXP": 360.000},
 {"id": 46, "Monster": "Tough Hermit", "Área": "D3F5", "Floor": "5", "Level": 76, "HP": 33.000, "EXP": 430.000},
 {"id": 47, "Monster": "Hermit of Mask", "Área": "D3F6", "Floor": "6", "Level": 77, "HP": 35.000, "EXP": 510.000},
 {"id": 48, "Monster": "Hermit of Red Face", "Área": "D3F6", "Floor": "6", "Level": 77, "HP": 35.000, "EXP": 510.000},
 {"id": 49, "Monster": "Hermit of Anger", "Área": "D3F6", "Floor": "6", "Level": 78, "HP": 36.000, "EXP": 610.000},
 {"id": 50, "Monster": "Tough Hermit", "Área": "D3F6", "Floor": "6", "Level": 78, "HP": 36.000, "EXP": 610.000},
 {"id": 51, "Monster": "Hermit of Anger", "Área": "D3F7", "Floor": "7", "Level": 79, "HP": 38.000, "EXP": 730.000},
 {"id": 52, "Monster": "High Class Giant Doggebi", "Área": "D3F7", "Floor": "7", "Level": 79, "HP": 38.000, "EXP": 730.000},
 {"id": 53, "Monster": "High Class Doggebi with a Mask of Black Panther", "Área": "D3F8", "Floor": "8", "Level": 79, "HP": 38.000, "EXP": 730.000},
 {"id": 54, "Monster": "Tough Hermit", "Área": "D3F8", "Floor": "8", "Level": 79, "HP": 38.000, "EXP": 730.000},
 {"id": 55, "Monster": "High Class Guardian of Doggebi", "Área": "D3F8", "Floor": "8", "Level": 80, "HP": 40.000, "EXP": 880.000},
 {"id": 56, "Monster": "Hermit of Anger", "Área": "D3F9", "Floor": "9D3F9", "Level": 76, "HP": 33.000, "EXP": 430.000},
 {"id": 57, "Monster": "Demon Worker", "Área": "D4F1", "Floor": "1", "Level": 50, "HP": 11.000, "EXP": 6.300},
 {"id": 58, "Monster": "Demon Guard", "Área": "D4F2", "Floor": "2", "Level": 65, "HP": 19.000, "EXP": 64.000},
 {"id": 59, "Monster": "Larva", "Área": "D4F4", "Floor": "4", "Level": 70, "HP": 24.000, "EXP": 150.000},
 {"id": 60, "Monster": "Demon Patrol", "Área": "D4F3", "Floor": "3", "Level": 70, "HP": 24.000, "EXP": 150.000},
 {"id": 61, "Monster": "Black Armored Insect", "Área": "D4F4", "Floor": "4", "Level": 70, "HP": 24.000, "EXP": 150.000},
 {"id": 62, "Monster": "Demon Warrior", "Área": "D4F4", "Floor": "4", "Level": 73, "HP": 28.000, "EXP": 250.000},
 {"id": 63, "Monster": "Demon Infantry", "Área": "D4F5", "Floor": "5", "Level": 75, "HP": 31.000, "EXP": 360.000},
 {"id": 64, "Monster": "Crazy Demon Warrior", "Área": "D4F5", "Floor": "5", "Level": 78, "HP": 36.000, "EXP": 610.000},
 {"id": 65, "Monster": "Banshee", "Área": "D5F1", "Floor": "1", "Level": 81, "HP": 43.000, "EXP": 1.100.000},
 {"id": 66, "Monster": "Skeleton", "Área": "D5F1", "Floor": "1", "Level": 81, "HP": 43.000, "EXP": 1.100.000},
 {"id": 67, "Monster": "Skeleton Archer", "Área": "D5F1", "Floor": "1", "Level": 81, "HP": 43.000, "EXP": 1.100.000},
 {"id": 68, "Monster": "Banshee", "Área": "D5F2", "Floor": "2", "Level": 82, "HP": 45.000, "EXP": 1.300.000},
 {"id": 69, "Monster": "Skeleton", "Área": "D5F2", "Floor": "2", "Level": 82, "HP": 45.000, "EXP": 1.300.000},
 {"id": 70, "Monster": "Skeleton Archer", "Área": "D5F2", "Floor": "2", "Level": 82, "HP": 45.000, "EXP": 1.300.000},
 {"id": 71, "Monster": "Elite Skeleton", "Área": "D5F2", "Floor": "2", "Level": 82, "HP": 45.000, "EXP": 1.300.000},
 {"id": 72, "Monster": "Banshee", "Área": "D5F3", "Floor": "3", "Level": 83, "HP": 48.000, "EXP": 1.500.000},
 {"id": 73, "Monster": "Skeleton", "Área": "D5F3", "Floor": "3", "Level": 83, "HP": 48.000, "EXP": 1.500.000},
 {"id": 74, "Monster": "Skeleton Archer", "Área": "D5F3", "Floor": "3", "Level": 83, "HP": 48.000, "EXP": 1.500.000},
 {"id": 75, "Monster": "Elite Skeleton", "Área": "D5F3", "Floor": "3", "Level": 83, "HP": 48.000, "EXP": 1.500.000},
 {"id": 76, "Monster": "Banshee", "Área": "D5F3", "Floor": "3", "Level": 84, "HP": 51.000, "EXP": 1.700.000},
 {"id": 77, "Monster": "Skeleton Warrior", "Área": "D5F3", "Floor": "3", "Level": 84, "HP": 51.000, "EXP": 1.700.000},
 {"id": 78, "Monster": "Skeleton Archer", "Área": "D5F3", "Floor": "3", "Level": 84, "HP": 51.000, "EXP": 1.700.000},
 {"id": 79, "Monster": "Elite Skeleton", "Área": "D5F2", "Floor": "2", "Level": 84, "HP": 51.000, "EXP": 1.700.000},
 {"id": 80, "Monster": "Elite Skeleton", "Área": "D5F4", "Floor": "4", "Level": 84, "HP": 51.000, "EXP": 1.700.000},
 {"id": 81, "Monster": "Wraith", "Área": "D5F4", "Floor": "4", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 82, "Monster": "Skeleton Warrior", "Área": "D5F4", "Floor": "4", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 83, "Monster": "Skeleton Archer", "Área": "D5F4", "Floor": "4", "Level": 83, "HP": 48.000, "EXP": 1.500.000},
 {"id": 84, "Monster": "Banshee", "Área": "D5F4", "Floor": "4", "Level": 84, "HP": 51.000, "EXP": 1.700.000},
 {"id": 85, "Monster": "Banshee", "Área": "D5F4", "Floor": "4", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 86, "Monster": "Skeleton Warrior", "Área": "D5F5", "Floor": "5", "Level": 86, "HP": 57.000, "EXP": 2.200.000},
 {"id": 87, "Monster": "Banshee", "Área": "D5F5", "Floor": "5", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 88, "Monster": "Skeleton Archer", "Área": "D5F5", "Floor": "5", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 89, "Monster": "Elite Skeleton", "Área": "D5F5", "Floor": "5", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 90, "Monster": "Wraith", "Área": "D5F5", "Floor": "5", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 91, "Monster": "Skeleton Warrior", "Área": "D5F6", "Floor": "6", "Level": 86, "HP": 57.000, "EXP": 2.200.000},
 {"id": 92, "Monster": "Banshee", "Área": "D5F6", "Floor": "6", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 93, "Monster": "Skeleton Archer", "Área": "D5F6", "Floor": "6", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 94, "Monster": "Elite Skeleton", "Área": "D5F6", "Floor": "6", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 95, "Monster": "Wraith", "Área": "D5F6", "Floor": "6", "Level": 85, "HP": 54.000, "EXP": 1.900.000},
 {"id": 96, "Monster": "High Class Fire element", "Área": "D5F7", "Floor": "7", "Level": 92, "HP": 82.000, "EXP": 4.800.000},
 {"id": 97, "Monster": "High Class Water element", "Área": "D5F7", "Floor": "7", "Level": 92, "HP": 82.000, "EXP": 4.800.000},
 {"id": 98, "Monster": "High Class Earth element", "Área": "D5F7", "Floor": "7", "Level": 92, "HP": 82.000, "EXP": 4.800.000},
 {"id": 99, "Monster": "High Class Wood element", "Área": "D5F7", "Floor": "7", "Level": 92, "HP": 82.000, "EXP": 4.800.000},
 {"id": 100, "Monster": "High Class Iron element", "Área": "D5F7", "Floor": "7", "Level": 92, "HP": 82.000, "EXP": 4.800.000},
 {"id": 101, "Monster": "Wraith", "Área": "D5F7", "Floor": "7", "Level": 86, "HP": 57.000, "EXP": 2.200.000},
 {"id": 102, "Monster": "High Class Security guard of the priest", "Área": "D5F7", "Floor": "7", "Level": 94, "HP": 92.000, "EXP": 6.200.000},
 {"id": 103, "Monster": "High Class Wood element", "Área": "D5F8", "Floor": "8", "Level": 93, "HP": 87.000, "EXP": 5.400.000},
 {"id": 104, "Monster": "High Class Iron element", "Área": "D5F8", "Floor": "8", "Level": 93, "HP": 87.000, "EXP": 5.400.000},
 {"id": 105, "Monster": "Security guard of the priest", "Área": "D5F8", "Floor": "8", "Level": 93, "HP": 87.000, "EXP": 5.400.000},
 {"id": 106, "Monster": "High Class Fire element", "Área": "D5F8", "Floor": "8", "Level": 93, "HP": 87.000, "EXP": 5.400.000},
 {"id": 107, "Monster": "High Class Earth element", "Área": "D5F8", "Floor": "8", "Level": 93, "HP": 87.000, "EXP": 5.400.000},
 {"id": 108, "Monster": "High Class Water element", "Área": "D5F8", "Floor": "8", "Level": 93, "HP": 87.000, "EXP": 5.400.000},
 {"id": 109, "Monster": "High Class Security guard of the priest", "Área": "D5F8", "Floor": "8", "Level": 94, "HP": 92.000, "EXP": 6.200.000},
 {"id": 110, "Monster": "Wraith", "Área": "D5F8", "Floor": "8", "Level": 86, "HP": 57.000, "EXP": 2.200.000},
 {"id": 111, "Monster": "High Class Iron element", "Área": "D5F9", "Floor": "9", "Level": 94, "HP": 92.000, "EXP": 6.200.000},
 {"id": 112, "Monster": "High Class Wood element", "Área": "D5F9", "Floor": "9", "Level": 94, "HP": 92.000, "EXP": 6.200.000},
 {"id": 113, "Monster": "High Class Water element", "Área": "D5F9", "Floor": "9", "Level": 94, "HP": 92.000, "EXP": 6.200.000},
 {"id": 114, "Monster": "High Class Earth element", "Área": "D5F9", "Floor": "9", "Level": 94, "HP": 92.000, "EXP": 6.200.000},
 {"id": 115, "Monster": "High Class Fire element", "Área": "D5F9", "Floor": "9", "Level": 94, "HP": 92.000, "EXP": 6.200.000},
 {"id": 116, "Monster": "High Class Security guard of the priest", "Área": "D5F9", "Floor": "9", "Level": 95, "HP": 98.000, "EXP": 7.100.000},
 {"id": 117, "Monster": "Wraith", "Área": "D5F9", "Floor": "9", "Level": 87, "HP": 61.000, "EXP": 2.500.000},
 {"id": 118, "Monster": "Dungeon Warrior", "Área": "D6F1", "Floor": "1", "Level": 117, "HP": 440.000, "EXP": 350.000.000},
 {"id": 119, "Monster": "Dungeon Scout Soldier", "Área": "D6F1", "Floor": "1", "Level": 119, "HP": 490.000, "EXP": 440.000.000},
 {"id": 120, "Monster": "Dungeon Shield Soldier", "Área": "D6F1", "Level": 118, "HP": 460.000, "EXP": 390.000.000},
 {"id": 121, "Monster": "Dungeon Warrior", "Área": "D6F2", "Floor": "2", "Level": 120, "HP": 520.000, "EXP": 490.000.000},
 {"id": 122, "Monster": "Dungeon Scout Soldier", "Área": "D6F2", "Floor": "2", "Level": 120, "HP": 520.000, "EXP": 490.000.000},
 {"id": 123, "Monster": "Elite Dungeon Warrior", "Área": "D6F2", "Floor": "2", "Level": 122, "HP": 580.000, "EXP": 620.000.000},
 {"id": 124, "Monster": "Elite Dungeon Scout Soldier", "Área": "D6F2", "Floor": "2", "Level": 122, "HP": 580.000, "EXP": 620.000.000},
 {"id": 125, "Monster": "Elite Dungeon Shield Soldier", "Área": "D6F2", "Floor": "2", "Level": 122, "HP": 580.000, "EXP": 620.000.000},
 {"id": 126, "Monster": "Dungeon Guard", "Área": "D6F2", "Floor": "2", "Level": 121, "HP": 550.000, "EXP": 550.000.000},
 {"id": 127, "Monster": "Elite Dungeon Guard", "Área": "D6F2", "Floor": "2", "Level": 122, "HP": 580.000, "EXP": 620.000.000},
 {"id": 128, "Monster": "Dungeon Shock Trooper", "Área": "D6F2", "Floor": "2", "Level": 121, "HP": 550.000, "EXP": 550.000.000},
 {"id": 129, "Monster": "Elite Dungeon Shock Trooper", "Área": "D6F2", "Floor": "2", "Level": 122, "HP": 580.000, "EXP": 620.000.000},
 {"id": 130, "Monster": "Dungeon Ax Soldier", "Área": "D6F2", "Floor": "2", "Level": 121, "HP": 550.000, "EXP": 550.000.000},
 {"id": 131, "Monster": "Elite Dungeon Ax Soldier", "Área": "D6F2", "Floor": "2", "Level": 122, "HP": 580.000, "EXP": 620.000.000},
 {"id": 132, "Monster": "Ruins Destroyer (Water)", "Área": "D6F2.5", "Floor": "2.5", "Level": 123, "HP": 620.000, "EXP": 690.000.000},
 {"id": 133, "Monster": "Dungeon Magician", "Área": "D6F2.5", "Floor": "2.5", "Level": 124, "HP": 650.000, "EXP": 780.000.000},
 {"id": 134, "Monster": "Ohgeuma (Wind)", "Área": "D6F2.5", "Floor": "2.5", "Level": 124, "HP": 650.000, "EXP": 780.000.000},
 {"id": 135, "Monster": "[Elite] Dungeon Knight", "Área": "D6F2.5", "Floor": "2.5", "Level": 126, "HP": 730.000, "EXP": 970.000.000},
 {"id": 136, "Monster": "Lord Bisaim (Water)", "Área": "D6F2.5", "Floor": "2.5", "Level": 124, "HP": 650.000, "EXP": 780.000.000},
 {"id": 137, "Monster": "Death Lich (Earth)", "Área": "D6F2.5", "Floor": "2.5", "Level": 124, "HP": 650.000, "EXP": 780.000.000},
 {"id": 138, "Monster": "Death Knight (Earth)", "Área": "D6F2.5", "Floor": "2.5", "Level": 125, "HP": 690.000, "EXP": 870.000.000},
 {"id": 139, "Monster": "Shadow Murder (Wind)", "Área": "D6F2.5", "Floor": "2.5", "Level": 123, "HP": 620.000, "EXP": 690.000.000},
 {"id": 140, "Monster": "Elite Death Knight (Earth)", "Área": "D6F3", "Floor": "3", "Level": 129, "HP": 870.000, "EXP": 1.400.000.000},
 {"id": 141, "Monster": "Elite Ohgeuma (Wind)", "Área": "D6F3", "Floor": "3", "Level": 128, "HP": 820.000, "EXP": 1.200.000.000},
 {"id": 142, "Monster": "Elite Lord Bisaim (Water)", "Área": "D6F3", "Floor": "3", "Level": 128, "HP": 820.000, "EXP": 1.200.000.000},
 {"id": 143, "Monster": "Elite Death Lich (Earth)", "Área": "D6F3", "Floor": "3", "Level": 128, "HP": 820.000, "EXP": 1.200.000.000},
 {"id": 144, "Monster": "Elite Shadow Murder (Wind)", "Área": "D6F3", "Floor": "3", "Level": 127, "HP": 780.000, "EXP": 1.100.000.000},
 {"id": 145, "Monster": "Elite Ruins Destroyer (Water)", "Área": "D6F3", "Floor": "3", "Level": 127, "HP": 780.000, "EXP": 1.100.000.000},
 {"id": 146, "Monster": "Elite Death Harvester (Earth)", "Área": "D6F3", "Floor": "3", "Level": 127, "HP": 780.000, "EXP": 1.100.000.000},
 {"id": 147, "Monster": "[Elite] Dungeon Knight", "Área": "D6F3", "Floor": "3", "Level": 130, "HP": 920.000, "EXP": 1.500.000.000}
]

monstersworld = [
    {"id": 1, "name": "Monstro1",               "level": 5,     "area": "Floresta",     "hp": 100,      "xp": 50},
    {"id": 2, "name": "Monstro2",               "level": 8,     "area": "Montanha",     "hp": 150,      "xp": 80},
    {"id": 1, "name": "Devil Troop of Desire",  "level": 46,    "area": "D1R1",         "hp": 9.100,    "xp": 3.500}
    # Adicione mais monstros conforme necessário
]

# Rota para obter todos os monstros
@app.route('/monsters', methods=['GET'])
def get_monsters():
    return jsonify({'monsters': monsters})

# Rota para obter informações sobre um monstro específico
@app.route('/monsters/<int:monster_id>', methods=['GET'])
def get_monster(monster_id):
    monster = next((m for m in monsters if m['id'] == monster_id), None)
    if monster:
        return jsonify({'monster': monster})
    return jsonify({'message': 'Monstro não encontrado'}), 404

# Rota para adicionar um novo monstro
@app.route('/monsters', methods=['POST'])
def add_monster():
    new_monster = request.get_json()
    new_monster['id'] = len(monsters) + 1
    monsters.append(new_monster)
    return jsonify({'message': 'Monstro adicionado com sucesso'}), 201

# Rota para atualizar informações de um monstro
@app.route('/monsters/<int:monster_id>', methods=['PUT'])
def update_monster(monster_id):
    monster = next((m for m in monsters if m['id'] == monster_id), None)
    if monster:
        updated_monster = request.get_json()
        monster.update(updated_monster)
        return jsonify({'message': 'Monstro atualizado com sucesso'})
    return jsonify({'message': 'Monstro não encontrado'}), 404

# Rota para excluir um monstro
@app.route('/monsters/<int:monster_id>', methods=['DELETE'])
def delete_monster(monster_id):
    global monsters
    monsters = [m for m in monsters if m['id'] != monster_id]
    return jsonify({'message': 'Monstro excluído com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
