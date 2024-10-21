# ===================== Capstone Project Naufal Mirza Maulana =====================
# Game Store Platform

# ===================== Import tabulate untuk menggunakan tabel =====================
import tabulate

# Welcome Menu
print("===========================================================")
print("                WELCOME TO NISHI GAME STORE                   ")
print("          Your most trusted store for gaming needs         ")
print("===========================================================\n")

# ===================== Data Game dan Data User =====================
# Data User dan Saldo
users  = {'Admin': 'Admin123', 'Nishi': 'Nishi12'} # --> Username dan Password
user_balances = {'Admin': 1000000, 'Nishi': 2500000} # --> Saldo dari Users

# Save riawayat transaksi dari users
transaction_history = {} # --> Dictionary kosong untuk menyimpan data dari transaksi

# Data Game
games_list = [
    {'Name': 'Assassins Creed Mirage', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Mixed', 'Price': 619000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Need for Speed Heat', 'Genre': 'Racing', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 759000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Hogwarts Legacy', 'Genre': 'Open World', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 799000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Mortal Kombat 1', 'Genre': 'Fighting', 'Rating': 'PEGI 18', 'Review': 'Mixed', 'Price': 790000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Elden Ring', 'Genre': 'RPG', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 599000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'EA Sports FC 25', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mixed', 'Price': 799000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'F1 24', 'Genre': 'Racing', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 759000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Red Dead Redemption II', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 879000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Cyberpunk 2077', 'Genre': 'RPG', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 699999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Assassins Creed Origins', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 619000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Sekiro : Shadows Die Twice', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 891000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Black Myth : Wukong', 'Genre': 'Action', 'Rating': 'PEGI 16', 'Review': 'Overwhelmingly Positive', 'Price': 699999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'God Of War', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 729000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'God Of War Ragnarok', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Mostly Positive', 'Price': 879000, 'Status': 'Sale', 'Refunded': False},
    {'Name': "Marvel's Spider-Man Remastered", 'Genre': 'Action', 'Rating': 'PEGI 16', 'Review': 'Overwhelmingly Positive', 'Price': 879000, 'Status': 'Sale', 'Refunded': False},
    {'Name': "Marvel's Spider-Man : Miles Morales", 'Genre': 'Action', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 729000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'STAR WARS Jedi: Survivor', 'Genre': 'Action', 'Rating': 'PEGI 12', 'Review': 'Mostly Positive', 'Price': 759000, 'Status': 'Sale', 'Refunded': False},
    {'Name': "Ghost of Tsushima Director's Cut", 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 879000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Dying Light 2: Reloaded Edition', 'Genre': 'RPG', 'Rating': 'PEGI 18', 'Review': 'Mostly Positive', 'Price': 849000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'The Last of Us Part I', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 879000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'NBA 2K24', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Negative', 'Price': 891000, 'Status': 'Sale', 'Refunded': False},
    {'Name': "Baldur's Gate 3", 'Genre': 'RPG', 'Rating': 'PEGI 18', 'Review': 'Overwhelmingly Positive', 'Price': 699999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Far Cry 6', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Mixed', 'Price': 619000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Resident Evil 4', 'Genre': 'Horror', 'Rating': 'PEGI 18', 'Review': 'Overwhelmingly Positive', 'Price': 595999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Shadow of The Tomb Raider: Definitive Edition', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 976000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Gran Turismo 7', 'Genre': 'Racing', 'Rating': 'PEGI 3', 'Review': 'Very Positive', 'Price': 759000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Dead Space Remake', 'Genre': 'Horror', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 749000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Ghostwire: Tokyo', 'Genre': 'Action', 'Rating': 'PEGI 16', 'Review': 'Mostly Positive', 'Price': 669000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Forza Horizon 5', 'Genre': 'Racing', 'Rating': 'PEGI 3', 'Review': 'Overwhelmingly Positive', 'Price': 699999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Deathloop', 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 649000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Returnal', 'Genre': 'Action', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 699999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Call of Duty: Modern Warfare II', 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Mixed', 'Price': 849000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Diablo IV', 'Genre': 'RPG', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 799000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Gotham Knights', 'Genre': 'Action', 'Rating': 'PEGI 16', 'Review': 'Mixed', 'Price': 699000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Forspoken', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Mostly Negative', 'Price': 799000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Final Fantasy XVI', 'Genre': 'RPG', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 899000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Stray', 'Genre': 'Adventure', 'Rating': 'PEGI 12', 'Review': 'Overwhelmingly Positive', 'Price': 459000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Kena: Bridge of Spirits', 'Genre': 'Adventure', 'Rating': 'PEGI 12', 'Review': 'Very Positive', 'Price': 499000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Hades', 'Genre': 'Roguelike', 'Rating': 'PEGI 12', 'Review': 'Overwhelmingly Positive', 'Price': 299000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'It Takes Two', 'Genre': 'Co-op', 'Rating': 'PEGI 12', 'Review': 'Overwhelmingly Positive', 'Price': 349000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Valheim', 'Genre': 'Survival', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 199000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Sifu', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Riders Republic', 'Genre': 'Sports', 'Rating': 'PEGI 12', 'Review': 'Mostly Positive', 'Price': 599000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Hitman 3', 'Genre': 'Stealth', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 649000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Doom Eternal', 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Overwhelmingly Positive', 'Price': 499000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Assassins Creed Valhalla', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 699000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Assassins Creed Odyssey', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 619000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Assassins Creed Black Flag', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Assassins Creed Syndicate', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Mostly Positive', 'Price': 319000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Far Cry 5', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Mostly Positive', 'Price': 529000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Far Cry Primal', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Mostly Positive', 'Price': 489000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Far Cry 4', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 299000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Far Cry 3', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 249000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Resident Evil Village', 'Genre': 'Horror', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 699000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Resident Evil 3 Remake', 'Genre': 'Horror', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 619000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Resident Evil 2 Remake', 'Genre': 'Horror', 'Rating': 'PEGI 18', 'Review': 'Overwhelmingly Positive', 'Price': 499000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Far Cry New Dawn', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Mostly Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Assassins Creed Unity', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Mixed', 'Price': 299000, 'Status': 'Sale', 'Refunded': False},
    {'Name': "Tom Clancy's The Division 2", 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Mostly Positive', 'Price': 349000, 'Status': 'Sale', 'Refunded': False},
    {'Name': "Tom Clancy's Ghost Recon Breakpoint", 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Mixed', 'Price': 599000, 'Status': 'Sale', 'Refunded': False},
    {'Name': "Tom Clancy's Rainbow Six Siege", 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Assassins Creed Rogue', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Mostly Positive', 'Price': 219000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Resident Evil 7 Biohazard', 'Genre': 'Horror', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 599000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Far Cry 2', 'Genre': 'Action', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 199000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Metal Gear Solid V: The Phantom Pain', 'Genre': 'Stealth', 'Rating': 'PEGI 18', 'Review': 'Overwhelmingly Positive', 'Price': 329000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'The Witcher 3: Wild Hunt', 'Genre': 'RPG', 'Rating': 'PEGI 18', 'Review': 'Overwhelmingly Positive', 'Price': 299000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'The Witcher 2: Assassins of Kings', 'Genre': 'RPG', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 179000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Cyberpunk 2077: Phantom Liberty', 'Genre': 'RPG', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 299000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Star Wars Jedi: Fallen Order', 'Genre': 'Action', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 449000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Horizon Forbidden West', 'Genre': 'Action', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 799000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Horizon Zero Dawn', 'Genre': 'Action', 'Rating': 'PEGI 16', 'Review': 'Overwhelmingly Positive', 'Price': 499000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'The Elder Scrolls V: Skyrim', 'Genre': 'RPG', 'Rating': 'PEGI 18', 'Review': 'Overwhelmingly Positive', 'Price': 299000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Death Stranding', 'Genre': 'Adventure', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 649000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'No Man\'s Sky', 'Genre': 'Survival', 'Rating': 'PEGI 7', 'Review': 'Mostly Positive', 'Price': 499000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Control', 'Genre': 'Action', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 499000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Dishonored 2', 'Genre': 'Stealth', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Dishonored: Death of the Outsider', 'Genre': 'Stealth', 'Rating': 'PEGI 18', 'Review': 'Mostly Positive', 'Price': 299000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Need for Speed Payback', 'Genre': 'Racing', 'Rating': 'PEGI 12', 'Review': 'Mostly Positive', 'Price': 499000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Need for Speed Rivals', 'Genre': 'Racing', 'Rating': 'PEGI 12', 'Review': 'Very Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Need for Speed Most Wanted', 'Genre': 'Racing', 'Rating': 'PEGI 12', 'Review': 'Very Positive', 'Price': 299000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Forza Motorsport 7', 'Genre': 'Racing', 'Rating': 'PEGI 3', 'Review': 'Overwhelmingly Positive', 'Price': 699999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Forza Horizon 4', 'Genre': 'Racing', 'Rating': 'PEGI 3', 'Review': 'Very Positive', 'Price': 699999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'NBA 2K23', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 849000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'NBA 2K22', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 799000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'PES 2021', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 599000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'PES 2020', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 549000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'FIFA 22', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 649000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'FIFA 21', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 599000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'FIFA 20', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 499000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Forza Horizon 3', 'Genre': 'Racing', 'Rating': 'PEGI 3', 'Review': 'Very Positive', 'Price': 699999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Need for Speed Underground 2', 'Genre': 'Racing', 'Rating': 'PEGI 12', 'Review': 'Overwhelmingly Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'NBA Live 19', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 499000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'PES 2019', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'FIFA 19', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Need for Speed Hot Pursuit', 'Genre': 'Racing', 'Rating': 'PEGI 12', 'Review': 'Very Positive', 'Price': 349000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Forza Motorsport 6', 'Genre': 'Racing', 'Rating': 'PEGI 3', 'Review': 'Very Positive', 'Price': 599999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'PES 2018', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 349000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'FIFA 18', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 349000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Need for Speed Carbon', 'Genre': 'Racing', 'Rating': 'PEGI 12', 'Review': 'Very Positive', 'Price': 299000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Forza Horizon 2', 'Genre': 'Racing', 'Rating': 'PEGI 3', 'Review': 'Very Positive', 'Price': 599999, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'NBA Live 18', 'Genre': 'Sports', 'Rating': 'PEGI 3', 'Review': 'Mostly Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Need for Speed The Run', 'Genre': 'Racing', 'Rating': 'PEGI 12', 'Review': 'Mostly Positive', 'Price': 399000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Call of Duty: Black Ops Cold War', 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Mostly Positive', 'Price': 799000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Call of Duty: Black Ops III', 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 649000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Call of Duty: Ghosts', 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Mixed', 'Price': 599000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Battlefield V', 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 649000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Battlefield 1', 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Very Positive', 'Price': 599000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Battlefield 2042', 'Genre': 'Shooter', 'Rating': 'PEGI 18', 'Review': 'Mixed', 'Price': 799000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Halo Infinite', 'Genre': 'Shooter', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 649000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Halo: The Master Chief Collection', 'Genre': 'Shooter', 'Rating': 'PEGI 16', 'Review': 'Overwhelmingly Positive', 'Price': 599000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Halo 5: Guardians', 'Genre': 'Shooter', 'Rating': 'PEGI 16', 'Review': 'Mostly Positive', 'Price': 549000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Tomb Raider: Anniversary', 'Genre': 'Adventure', 'Rating': 'PEGI 16', 'Review': 'Very Positive', 'Price': 299000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Tomb Raider: Legend', 'Genre': 'Adventure', 'Rating': 'PEGI 16', 'Review': 'Mostly Positive', 'Price': 249000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Tomb Raider: Underworld', 'Genre': 'Adventure', 'Rating': 'PEGI 16', 'Review': 'Mostly Positive', 'Price': 349000, 'Status': 'Sale', 'Refunded': False},
    {'Name': 'Tomb Raider: The Last Revelation', 'Genre': 'Adventure', 'Rating': 'PEGI 16', 'Review': 'Mostly Positive', 'Price': 199000, 'Status': 'Sale', 'Refunded': False}


]

# ======================================================================================

# Save Game ke library users
user_libraries = {} # --> Dictionary kosong untuk menyimpan game ke dalam library


# ======================================================================================
# ===================== Fungsi print =====================
# Welcome Menu dalam Fungsi
def print_welcome():
    print("===========================================================")
    print("                WELCOME TO NISHI GAME STORE                   ")
    print("          Your most trusted store for gaming needs         ")
    print("===========================================================\n")

# Print daftar game
def print_games():
    if len(games_list) !=0:
        print("\n=================== GAME STORE ====================")
        table_data = [[i + 1, game['Name'], game['Genre'], game['Rating'], game['Review'], game['Price'], game['Status']]
                    for i, game in enumerate(games_list)]
        headers = ["ID", "Name", "Genre", "Rating", "Review", "Price", "Status"]
        table = tabulate.tabulate(table_data, headers, tablefmt = "fancy_grid")
        print(table)

# Print daftar Users
def print_users():
    print("\n=================== LIST OF USERS ====================")
    table_data = [[i + 1, user, user_balances[user]] for i, user in enumerate(users)]
    headers = ["ID", "Username", "Balance"]
    table = tabulate.tabulate(table_data, headers, tablefmt="fancy_grid")
    print(table)

# ======================================================================================
# ===================== Fungsi print =====================

# ================================================
# |                 Admin Login                  |
# ================================================
def login_admin():
    print("\nAdmin Login")
    username = "Admin"
    password = input("Enter Admin Password: ")

    if users[username] == password:
        print("\nAdmin logged in successfully")
        print("Welcome, Admin! You have access to all game management features.\n")
        return username
    else:
        print("\n Wrong password for admin.")
        return None
    
# ================================================
# |                 User Login                   |
# ================================================
def login_user():
    print("\nUser Login")
    username = input("Enter your username: ")

    if username not in users:
        print("\nUsername not found. Please try again or create a new account.")
        return None
    
    attempts = 3
    while attempts > 0:
        password = input("Enter your password: ")
        if users[username] == password:
            print(f"\nWelcome, {username}! You have successfully logged in.\n")
            return username
        else:
            attempts -= 1
            print(f"Wrong password. Attempts remaining: {attempts}.")

        if attempts == 0:
            reset_choice = input("Do you want to change your password? (yes/no): ")
            if reset_choice.lower() == 'yes' or 'y':
                new_password = input("Enter your new password: ")
                users[username] = new_password
                print("password updated successfully. You can now login with your new password.")
            else:
                print("You've exceeded the maximum number of attempts.")
        return None

# ================================================
# |               Buat Akun Baru                 |
# ================================================
def create_account():
    print("\nCreate a New User Account")
    username = input("Enter new username: ")

    if username in users:
        print("\nUsername already exists. please try another one.")
        return
    
    password = input("Enter a password: ")
    users[username] = password
    user_balances[username] = 0
    print(f"\nAccount created successfully for {username}. Enjoy shopping!")

# ======================================================================================

# ===================== Fitur Admin =====================

# ========= Delete and View Users =========

# ================================================
# |              Fungsi View Users               |
# ================================================
def view_users():
    print_users()

# ================================================
# |          Fungsi Riwayat Transaksi            |
# ================================================
def view_transaction_history():
    """Admin dapat melihat riwayat transaksi semua pengguna"""
    print("\n=================== TRANSACTION HISTORY ====================\n")
    if not transaction_history:
        print("No transactions found.\n")
        print("===========================================================\n\n")
    else:
        for user, transactions in transaction_history.items():
            print(f"\nUser: {user}")
            for transaction in transactions:
                print(f"- {transaction}\n")

# ========= Users Delete =========

# ================================================
# |            Fungsi Delete Users               |
# ================================================
def delete_users():
    print("\n==================== DELETE USER ====================")
    print_users()
    username = input("Enter the username to delete: ")

    if username == 'Admin':
        print("You cannot delete the Admin account.")
        return
    
    if username in users:
        confirmation = input(f"Are you sure you want to delete the user '{username}'? This action cannot be undone. (yes/no):  ")
        if confirmation.lower() == 'yes' or 'y':
            del users[username]
            del user_balances[username]

            if username in user_libraries:
                del user_libraries[username]
            
            if username in transaction_history:
                del transaction_history[username]
            print(f"User '{username}' has been deleted successfully.")
            print_users() # --> konfimasi list sudah di update
        else:
            print("User deletion cancelled.")
    else:
        print("User not found. Please enter a valid username.")


# ================================================
# |               Fungsi Add Game                |
# ================================================
def add_game():
    while True:
        print("\n Add Game Menu:")
        print("1. Add a new game to the store")
        print("2. Back to Admin Menu")
        choice = input("Select your choice: ")

        if choice == "1":
            print("\n Add a New Game to the Store")
            name = input("Enter the game name: ")

            if any(game['Name'].lower() == name.lower() for game in games_list):
                print("Game is already in the store.")
                continue

            genre = input("Enter the game genre: ")
            rating = input("Enter the game rating (e.g., PEGI 18): ")
            review = input("Enter the game review: ")

            try:
                price =  int(input("Enter the game price: "))
                new_game = {'Name': name, 'Genre': genre, 'Rating': rating, 'Review': review, 'Price': price, 'Status': 'Sale', 'Refunded': False}

                # Menampilkan game baru dalam tabel untuk mengkonfimasi
                print("\nGame to be added: ")
                print(tabulate.tabulate([[new_game['Name'], new_game['Genre'], new_game['Rating'], new_game['Review'], new_game['Price']]],
                                        headers=["Name", "Genre", "Rating", "Review", "Price"], tablefmt="fancy_grid"))

                confirmation = input(f"Are you sure you want to add the game '{name}' to the store? (yes/no): ")
                if confirmation.lower() == 'yes'or 'y':
                    games_list.append(new_game)
                    print(f"\nGame '{name}' has been added successfully to the store.\n")
                    print_games()  # --> konfimasi list sudah di update
                else:
                    print("Add game cancelled.")
            except ValueError:
                print("Invalid price input.")
        elif choice == "2":
            break
        else:
            print("Invalid choice, please select a valid option.")

# ================================================
# |              Fungsi Edit Game                |
# ================================================
def edit_game():
    while True:
        print("\nEdit Game Menu:")
        print("1. Choose a game to edit")
        print("2. Back to Admin Menu")
        choice = input("Select your choice: ")

        if choice == "1":
            print_games()
            if len(games_list) != 0:
                try:
                    game_index = int(input("Enter the game ID to edit: ")) - 1
                    if 0 <= game_index < len(games_list):
                        game = games_list[game_index]
                        
                        # Menampilkan game yang dipilih menggunakan tabel
                        print("\nSelected Game:")
                        print(tabulate.tabulate([[game['Name'], game['Genre'], game['Rating'], game['Review'], game['Price']]],
                                                headers=["Name", "Genre", "Rating", "Review", "Price"], tablefmt="fancy_grid"))

                        print("\nWhich field would you like to edit?")
                        print("1. Name")
                        print("2. Genre")
                        print("3. Rating")
                        print("4. Review")
                        print("5. Price")

                        field_choice = input("Select the field to edit (1-5): ")

                        if field_choice == "1":
                            new_name = input(f"Enter new name for '{game['Name']}': ")
                            confirmation = input(f"Are you sure you want to change the name to '{new_name}'? (yes/no): ")
                            if confirmation.lower() == 'yes'or 'y':
                                game['Name'] = new_name
                                print(f"Game name updated successfully to '{new_name}'.")
                            else:
                                print("Edit name cancelled.")

                        elif field_choice == "2":
                            new_genre = input(f"Enter new genre for '{game['Name']}': ")
                            confirmation = input(f"Are you sure you want to change the genre to '{new_genre}'? (yes/no): ")
                            if confirmation.lower() == 'yes'or 'y':
                                game['Genre'] = new_genre
                                print(f"Game genre updated successfully to '{new_genre}'.")
                            else:
                                print("Edit genre cancelled.")

                        elif field_choice == "3":
                            new_rating = input(f"Enter new rating for '{game['Name']}': ")
                            confirmation = input(f"Are you sure you want to change the rating to '{new_rating}'? (yes/no): ")
                            if confirmation.lower() == 'yes'or 'y':
                                game['Rating'] = new_rating
                                print(f"Game rating updated successfully to '{new_rating}'.")
                            else:
                                print("Edit rating cancelled.")

                        elif field_choice == "4":
                            new_review = input(f"Enter new review for '{game['Name']}': ")
                            confirmation = input(f"Are you sure you want to change the review to '{new_review}'? (yes/no): ")
                            if confirmation.lower() == 'yes'or 'y':
                                game['Review'] = new_review
                                print(f"Game review updated successfully to '{new_review}'.")
                            else:
                                print("Edit review cancelled.")

                        elif field_choice == "5":
                            try:
                                new_price = int(input(f"Enter new price for '{game['Name']}': "))
                                confirmation = input(f"Are you sure you want to change the price to {new_price}? (yes/no): ")
                                if confirmation.lower() == 'yes'or 'y':
                                    game['Price'] = new_price
                                    print(f"Game price updated successfully to {new_price}.")
                                else:
                                    print("Edit price cancelled.")
                            except ValueError:
                                print("Invalid price input.")
                        else:
                            print("Invalid field selection. Please select a number between 1 and 5.")
                        print_games()  # --> konfimasi list sudah di update
                    else:
                        print("Invalid game ID.")
                except ValueError:
                    print("Invalid input.")
        elif choice == "2":
            break
        else:
            print("Invalid choice, please select a valid option.")

# ================================================
# |             Fungsi Delete Game               |
# ================================================
def delete_game():
    while True:
        print("\nDelete Game Menu:")
        print("1. Choose a game to delete")
        print("2. Delete all games")
        print("3. Back to Admin Menu")
        choice = input("Select your choice: ")

        if choice == "1":
            print_games()
            if len(games_list) != 0:
                try:
                    game_index = int(input("Enter the game ID to delete: ")) - 1
                    if 0 <= game_index < len(games_list):
                        game = games_list[game_index]
                        
                        # Menampilkan game yang dipilih menggunakan tabel
                        print("\nSelected Game:")
                        print(tabulate.tabulate([[game['Name'], game['Genre'], game['Rating'], game['Review'], game['Price']]],
                                                headers=["Name", "Genre", "Rating", "Review", "Price"], tablefmt="fancy_grid"))
                        
                        confirmation = input(f"Are you sure you want to delete the game '{game['Name']}'? (yes/no): ")
                        if confirmation.lower() == 'yes' or 'y':
                            games_list.pop(game_index)
                            print(f"\nGame '{game['Name']}' has been deleted successfully.")
                            print_games()  # --> konfimasi list sudah di update
                        else:
                            print("Game deletion cancelled.")
                    else:
                        print("Invalid game ID.")
                except ValueError:
                    print("Invalid input.")
        elif choice == "2":
            if len(games_list) == 0:
                print("\nThere are no games to delete.")
            else:
                print("\nAll Games:")
                print_games()
                confirmation = input("Are you sure you want to delete ALL games? (yes/no): ")
                if confirmation.lower() == 'yes' or 'y':
                    games_list.clear()
                    print("\nAll games have been deleted successfully.")
                else:
                    print("Delete all games cancelled.")
        elif choice == "3":
            break
        else:
            print("Invalid choice, please select a valid option.")
            
# ======================================================================================

# ===================== Fitur Users =====================

# ================================================
# |               Fungsi Buy Game                |
# ================================================
def buy_game(username):
    while True:
        print("\nBuy Games Menu:")
        print("1. View All Games")
        print("2. Filter Games")
        print("3. Back to User Menu")

        buy_choice = input("Select your choice: ")

        if len(games_list) != 0:
            if buy_choice == "1":
                print_games()
                try:
                    game_id = int(input("Enter the game ID you want to buy: ")) - 1
                    if 0 <= game_id < len(games_list):
                        selected_game = games_list[game_id]
                        game_price = selected_game['Price']
                        
                        if username in user_libraries and selected_game['Name'] in user_libraries[username]:
                            print("You already own this game.")
                            continue

                        if selected_game['Status'] != 'Sale':
                            print("This game is not for sale.")
                            continue

                        if user_balances[username] < game_price:
                            print(f"Insufficient balance. Your balance is {user_balances[username]}, but the game costs {game_price}.")
                            continue

                        confirmation = input(f"Are you sure you want to buy '{selected_game['Name']}' for {game_price}? (yes/no): ")
                        if confirmation.lower() == 'yes' or 'y':
                            user_balances[username] -= game_price
                            print(f"You purchased '{selected_game['Name']}' for {game_price}.")
                            user_libraries.setdefault(username, []).append(selected_game['Name'])
                            selected_game['Status'] = 'Owned'
                            transaction_history.setdefault(username, []).append(f"Bought {selected_game['Name']} for {game_price}")
                            print(f"Game '{selected_game['Name']}' has been added to your library.")
                        else:
                            print("Purchase cancelled.")
                    else:
                        print("Invalid game ID.")
                except ValueError:
                    print("Invalid input. Please enter a valid number for the game ID.")
                    
            elif buy_choice == "2":
                filtered_games = filter_games()
                if not filtered_games:
                    continue
                try:
                    game_id = int(input("Enter the game ID you want to buy from filtered list: ")) - 1
                    if 0 <= game_id < len(filtered_games):
                        selected_game = filtered_games[game_id]
                        game_price = selected_game['Price']
                        
                        if username in user_libraries and selected_game['Name'] in user_libraries[username]:
                            print("You already own this game.")
                            continue

                        if selected_game['Status'] != 'Sale':
                            print("This game is not for sale.")
                            continue

                        if user_balances[username] < game_price:
                            print(f"Insufficient balance. Your balance is {user_balances[username]}, but the game costs {game_price}.")
                            continue

                        confirmation = input(f"Are you sure you want to buy '{selected_game['Name']}' for {game_price}? (yes/no): ")
                        if confirmation.lower() == 'yes' or 'y':
                            user_balances[username] -= game_price
                            print(f"You purchased '{selected_game['Name']}' for {game_price}.")
                            user_libraries.setdefault(username, []).append(selected_game['Name'])
                            selected_game['Status'] = 'Owned'
                            transaction_history.setdefault(username, []).append(f"Bought {selected_game['Name']} for {game_price}")
                            print(f"Game '{selected_game['Name']}' has been added to your library.")
                        else:
                            print("Purchase cancelled.")
                    else:
                        print("Invalid game ID.")
                except ValueError:
                    print("Invalid input. Please enter a valid number for the game ID.")
            
            elif buy_choice == "3":
                break
            else:
                print("Invalid choice. Please select a valid option.")
        else:
            print("There is no data game")

# ================================================
#    Fungsi filter game(genre, rating, review)
# ================================================
def filter_games():
    print("\nFilter Games:")
    print("1. By Genre")
    print("2. By Rating")
    print("3. By Review")
  
    
    filter_choice = input("Select filter option: ")
    filtered_list = []
    
    if filter_choice == "1":
        genre = input("Enter the genre you want to filter: ")
        filtered_list = [game for game in games_list if game['Genre'].lower() == genre.lower()]
    elif filter_choice == "2":
        rating = input("Enter the rating you want to filter (e.g., PEGI 18): ")
        filtered_list = [game for game in games_list if game['Rating'].lower() == rating.lower()]
    elif filter_choice == "3":
        review = input("Enter the review you want to filter (e.g., Very Positive): ")
        filtered_list = [game for game in games_list if game['Review'].lower() == review.lower()]
    else:
        print("Invalid filter option.")
        return filtered_list

    if filtered_list:
        print("\nFiltered Games:")
        table_data = [[i + 1, game['Name'], game['Genre'], game['Rating'], game['Review'], game['Price'], game['Status']]
                      for i, game in enumerate(filtered_list)]
        headers = ["ID", "Name", "Genre", "Rating", "Review", "Price", "Status"]
        table = tabulate.tabulate(table_data, headers, tablefmt="fancy_grid")
        print(table)
        return filtered_list
    else:
        print("No games found matching your filter criteria.")
        return filtered_list

# ================================================
# |            Fungsi Mencari game               |
# ================================================
def search_game(username):
    search_term = input("Enter the game name to search: ").lower()
    filtered_games = [game for game in games_list if search_term in game['Name'].lower()]

    if filtered_games:
        print("\nSearch Results:")
        table_data = [[i + 1, game['Name'], game['Genre'], game['Rating'], game['Review'], game['Price'], game['Status']]
                      for i, game in enumerate(filtered_games)]
        headers = ["ID", "Name", "Genre", "Rating", "Review", "Price", "Status"]
        table = tabulate.tabulate(table_data, headers, tablefmt="fancy_grid")
        print(table)
        
        while True:
            try:
                choice = input("\nDo you want to buy a game from the list? (yes/no): ").lower()
                if choice == 'yes' or 'y':
                    game_id = int(input("Enter the ID of the game you want to buy: ")) - 1
                    if 0 <= game_id < len(filtered_games):
                        selected_game = filtered_games[game_id]
                        game_price = selected_game['Price']

                        # Mengecek apakah game sudah dimiliki atau belum
                        if username in user_libraries and selected_game['Name'] in user_libraries[username]:
                            print("You already own this game.")
                            continue

                        # Mengecek status sale pada game
                        if selected_game['Status'] != 'Sale':
                            print("This game is not for sale.")
                            continue

                        # Mengecek saldo user cukup atau tidak
                        if user_balances[username] < game_price:
                            print(f"Insufficient balance. Your balance is {user_balances[username]}, but the game costs {game_price}.")
                            continue

                        # Confirm pembelian
                        confirm = input(f"Are you sure you want to buy '{selected_game['Name']}' for {game_price}? (yes/no): ").lower()
                        if confirm == 'yes' or 'y':
                            user_balances[username] -= game_price
                            user_libraries.setdefault(username, []).append(selected_game['Name'])
                            selected_game['Status'] = 'Owned'
                            transaction_history.setdefault(username, []).append(f"Bought {selected_game['Name']} for {game_price}")
                            print(f"Game '{selected_game['Name']}' has been added to your library.")
                            break 
                        else:
                            print("Purchase cancelled.")
                            break 
                    else:
                        print("Invalid game ID. Please try again.")
                elif choice == 'no' or 'n':
                    break  
                else:
                    print("Please enter 'yes' or 'no'.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    else:
        print(f"No games found containing '{search_term}' in the name.")

# ================================================
# |             Fungsi view library              |
# ================================================
def view_library(username):
    print(f"\nLibrary for {username}")
    
    if not user_libraries.get(username):
        print("Your library is empty.")
        return

    table_data = []
    for game_name in user_libraries[username]:
        game_details = next((game for game in games_list if game['Name'] == game_name), None)
        if game_details:
            table_data.append([game_details['Name'], game_details['Genre'], game_details['Rating'], game_details['Review'], game_details['Price'], "Owned"])
    
    headers = ["Name", "Genre", "Rating", "Review", "Price", "Status"]
    table = tabulate.tabulate(table_data, headers, tablefmt="fancy_grid")
    print(table)

# ================================================
# |             Fungsi Refund Game               |
# ================================================
def refund_game(username):
    print("\nRefund a Game")
    
    if username not in user_libraries or not user_libraries[username]:
        print("No games in your library.")
        return

    print(f"\nYour library:")
    for i, game_name in enumerate(user_libraries[username], 1):
        print(f"{i}. {game_name}")
    
    try:
        game_id = int(input("Enter the game ID to refund: ")) - 1
        if game_id < 0 or game_id >= len(user_libraries[username]):
            print("Invalid game ID.")
            return
    except ValueError:
        print("Invalid input.")
        return

    game_name = user_libraries[username][game_id]
    game = next((g for g in games_list if g['Name'] == game_name), None)
    if not game:
        print("Game not found.")
        return

    game_price = game['Price']
    confirmation = input(f"Are you sure you want to refund '{game_name}' for {game_price}? (yes/no): ")
    if confirmation.lower() == 'yes' or 'y':
        transaction_history[username].remove(f"Bought {game_name} for {game_price}")
        user_balances[username] += game_price
        user_libraries[username].remove(game_name)
        game['Status'] = 'Sale'
        game['Refunded'] = True
        transaction_history.setdefault('refunds', []).append({'username': username, 'game': game_name, 'price': game_price, 'status': 'refunded'})
        print(f"Refunded {game_name} for {game_price}.")
    else:
        print("Refund cancelled.")

# ================================================
# |             Fungsi add saldo                 |
# ================================================
def add_balance(username):
    print("\nAdd Balance to Your Account")
    try:
        amount = int(input("Enter the amount to add: "))
        if amount > 0:
            user_balances[username] += amount
            print(f"Balance updated! Current balance: {user_balances[username]}")
        else:
            print("Please enter a positive amount.")
    except ValueError:
        print("Invalid input.")

# Fungsi show balance
def show_balance(username):
    print(f"\nYour balance: {user_balances[username]} credits.")

# ================================================
# |                  Main Menu                   |
# ================================================
# Fungsi utama aplikasi
def main():
    while True:
        print("1. Login as Admin")
        print("2. Login as User")
        print("3. Create a new account")
        print("4. Exit")

        choice = input("Select your choice: ")

        if choice == "1":
            admin_username = login_admin()
            if admin_username:
                while True:
                    print("===========================================================")
                    print("|                      ADMIN MENU                         |")
                    print("===========================================================\n")
                    print("1. Add Game")
                    print("2. Edit Game")
                    print("3. View Users")
                    print("4. Delete User")
                    print("5. Delete Game")
                    print("6. View User Transactions")
                    print("7. Log Out\n")
                    print("===========================================================\n")
                    admin_choice = input("Select your choice: ")

                    if admin_choice == "1":
                        add_game()
                    elif admin_choice == "2":
                        edit_game()
                    elif admin_choice == "3":
                        view_users()
                    elif admin_choice == "4":
                        delete_users()
                    elif admin_choice == "5":
                        delete_game()
                    elif admin_choice == "6":
                        view_transaction_history()
                    elif admin_choice == "7":
                        print("Logging out...\n")
                        print_welcome()
                        break
                    else:
                        print("Invalid choice.")

        elif choice == "2":
            user_username = login_user()
            if user_username:
                while True:
                    print("===========================================================")
                    print("|                       USER MENU                         |")
                    print("===========================================================\n")
                    print("1. Buy Games")
                    print("2. Search Game")
                    print("3. View Library")
                    print("4. Add Balance")
                    print("5. Show Balance")
                    print("6. Refund Game") 
                    print("7. Log Out\n")
                    print("===========================================================\n")

                    user_choice = input("Select your choice: ")

                    if user_choice == "1":
                        buy_game(user_username)
                    elif user_choice == "2":
                        search_game(user_username) 
                    elif user_choice == "3":
                        view_library(user_username)
                    elif user_choice == "4":
                        add_balance(user_username)
                    elif user_choice == "5":
                        show_balance(user_username)
                    elif user_choice == "6":
                        refund_game(user_username)
                    elif user_choice == "7":
                        print("Logging out...\n")
                        print_welcome()
                        break
                    else:
                        print("Invalid choice.")

        elif choice == "3":
            create_account()

        elif choice == "4":
            print("\n\n===========================================================")
            print("|        THANK YOU FOR VISITING NISHI GAME STORE!         |")
            print("===========================================================")
            break

        else:
            print("Invalid choice.")

main()