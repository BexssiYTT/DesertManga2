import os

path = os.path.expanduser('~/storage/shared/manga_strona')
os.makedirs(path, exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1200">
    <title>Desert Studio - DesertAnime & Manga</title>
    <link rel="stylesheet" href="style.css">
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
    <script type="text/javascript">
        (function(){
            emailjs.init("JcnP4qYjFD_dvpPbZ");
        })();
    </script>
</head>
<body>
    <aside class="sidebar">
        <div class="sidebar-top-icon">👤</div>
        <div class="sidebar-icon active" data-tab="home">🏠</div>
        <div class="sidebar-icon" data-tab="anime">🎬</div>
        <div class="sidebar-icon" data-tab="create-manga">➕</div>
        <div class="sidebar-icon" data-tab="favorites">⭐</div>
        <div class="sidebar-icon" data-tab="profile">⚙️</div>
    </aside>

    <div class="main-container">
        <header class="top-header">
            <div class="search-box">
                <input type="text" id="global-search-input" placeholder="Szukaj mangi lub anime...">
            </div>
            <div class="hamburger-menu" id="menu-toggle">≡</div>
        </header>

        <div class="dropdown-menu" id="dropdown-menu">
            <button id="login-menu-btn" class="menu-item-btn">Zaloguj</button>
            <button id="register-menu-btn" class="menu-item-btn">Rejestracja</button>
            <button id="settings-menu-btn" class="menu-item-btn" style="border-top: 1px solid rgba(0,243,255,0.2);">⚙️ Ustawienia</button>
        </div>

        <nav class="nav-bar">
            <div class="nav-links">
                <span class="tab-link active" data-tab="home">Home (Mangi)</span>
                <span class="tab-link" data-tab="anime">Anime 🎬</span>
                <span class="tab-link" data-tab="favorites">Ulubione</span>
                <span class="tab-link" data-tab="history">Historia</span>
                <span class="tab-link" data-tab="profile">Profil</span>
                <span class="tab-link" data-tab="create-manga">Stwórz Mangę / Anime</span>
                <span class="tab-link" data-tab="admin-panel" id="admin-nav-tab" style="display: none; color: #c084fc;">Admin Panel</span>
            </div>
        </nav>

        <div id="modal-overlay" class="modal-overlay" style="display: none;">
            <div class="modal-box">
                <span class="close-modal" id="close-modal-btn">&times;</span>
                <h3 id="modal-title">Zaloguj się</h3>
                <form id="auth-form">
                    <input type="text" id="username" placeholder="Login lub E-mail" required>
                    <input type="password" id="password" placeholder="Hasło" required>
                    <button type="submit" class="action-btn">Zatwierdź</button>
                </form>
            </div>
        </div>

        <div id="email-modal-overlay" class="modal-overlay" style="display: none;">
            <div class="modal-box">
                <span class="close-modal" id="close-email-modal">&times;</span>
                <h3>Weryfikacja E-mail</h3>
                <p style="font-size: 13px; color: #94a3b8; margin-bottom: 15px;">Wprowadź kod wysłany na Twój e-mail:</p>
                <form id="email-verify-form">
                    <input type="text" id="verification-code-input" placeholder="Wpisz kod" maxlength="4" required style="text-align: center; font-size: 20px; letter-spacing: 5px;">
                    <button type="submit" class="action-btn">Potwierdź kod</button>
                </form>
            </div>
        </div>

        <div id="settings-modal-overlay" class="modal-overlay" style="display: none;">
            <div class="modal-box" style="width: 420px;">
                <span class="close-modal" id="close-settings-modal">&times;</span>
                <h3>Ustawienia aplikacji</h3>
                <div style="margin-top: 20px; display: flex; flex-direction: column; gap: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span>Tryb Ciemny (Dark Mode)</span>
                        <label class="switch">
                            <input type="checkbox" id="dark-mode-toggle" checked>
                            <span class="slider round"></span>
                        </label>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span>Powiadomienia dźwiękowe</span>
                        <label class="switch">
                            <input type="checkbox" id="sound-toggle" checked>
                            <span class="slider round"></span>
                        </label>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 5px;">
                        <span style="font-size: 14px;">Rozmiar czcionki interfejsu</span>
                        <select id="font-size-select" style="padding: 8px; background: #05070b; color: #fff; border: 1px solid rgba(0,243,255,0.3); border-radius: 6px;">
                            <option value="small">Mała</option>
                            <option value="medium" selected>Średnia (Domyślna)</option>
                            <option value="large">Duża</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>

        <div id="payment-modal-overlay" class="modal-overlay" style="display: none;">
            <div class="modal-box" style="width: 400px;">
                <span class="close-modal" id="close-payment-modal">&times;</span>
                <h3>Wybierz metodę płatności</h3>
                <p id="payment-item-title" style="color: #00f3ff; font-weight: bold; margin-bottom: 15px;"></p>
                <div style="display: flex; flex-direction: column; gap: 10px;">
                    <button class="action-btn pay-method-btn" data-method="BLIK">📱 Płatność BLIK</button>
                    <button class="action-btn pay-method-btn" data-method="Karta">💳 Karta Płatnicza</button>
                    <button class="action-btn pay-method-btn" data-method="Przelew">🏦 Szybki Przelew</button>
                </div>
            </div>
        </div>

        <main class="content-body">
            <div id="section-home" class="tab-content active-section">
                <a href="https://discord.gg/HXRUPVTA8c" target="_blank" class="main-banner">
                    <div class="banner-content">
                        <h1>Desert Studio 💬</h1>
                        <p>Odkrywaj mangi, anime i dołącz do społeczności Desert na Discordzie!</p>
                    </div>
                    <div class="banner-discord-btn">Dołącz na Discord 🚀</div>
                </a>

                <h2>Polecane / Mangi</h2>
                <div class="manga-grid" id="grid-home">
                    <p style="color: #94a3b8; font-size: 14px;">Brak mang. Dodaj pierwszą w zakładce "Stwórz Mangę / Anime".</p>
                </div>
            </div>

            <div id="section-anime" class="tab-content" style="display: none;">
                <h2>🎬 Katalog Anime</h2>
                <div class="manga-grid" id="grid-anime">
                    <p style="color: #94a3b8; font-size: 14px;">Brak dodanych anime.</p>
                </div>
            </div>

            <div id="section-favorites" class="tab-content" style="display: none;">
                <h2>Twoje Ulubione (Mangi i Anime)</h2>
                <div class="manga-grid" id="grid-favorites">
                    <p style="color: #94a3b8; font-size: 14px;">Brak elementów w ulubionych.</p>
                </div>
            </div>

            <div id="section-history" class="tab-content" style="display: none;">
                <h2>Historia Przeglądania</h2>
                <div class="manga-grid" id="grid-history">
                    <p style="color: #94a3b8; font-size: 14px;">Twoja historia czytania jest pusta.</p>
                </div>
            </div>

            <div id="section-profile" class="tab-content" style="display: none;">
                <h2>Profil Użytkownika</h2>
                <div class="admin-card" style="background: var(--card-bg); border: 1px solid rgba(0, 243, 255, 0.3); padding: 25px; border-radius: 10px; max-width: 500px; margin-top: 20px; display: flex; flex-direction: column; gap: 15px;">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div id="profile-pfp" style="width: 80px; height: 80px; border-radius: 50%; background: #030508; border: 2px solid #00f3ff; background-size: cover; background-position: center;"></div>
                        <div>
                            <p style="font-size: 18px; color: var(--text-color); margin: 0;"><b id="profile-username" style="color: #00f3ff;">Niezalogowany</b></p>
                            <p style="font-size: 13px; color: #94a3b8; margin: 5px 0 0 0;">Rola: <span id="profile-role" style="color: #c084fc;">Gość</span></p>
                        </div>
                    </div>
                    <hr style="border-color: rgba(0,243,255,0.2); width: 100%;">
                    <div id="logged-profile-settings" style="display: none; flex-direction: column; gap: 12px;">
                        <label style="font-size: 14px; color: #94a3b8;">Zmień Nazwę Użytkownika (Login):</label>
                        <div style="display: flex; gap: 10px;">
                            <input type="text" id="new-username-input" placeholder="Nowa nazwa..." style="flex: 1; padding: 10px; background: #05070b; border: 1px solid rgba(0,243,255,0.3); color: #fff; border-radius: 6px;">
                            <button class="action-btn" id="save-username-btn" style="padding: 8px 15px;">Zmień Nick</button>
                        </div>

                        <label style="font-size: 14px; color: #94a3b8; margin-top: 5px;">Zmień Link do Awataru (PFP URL):</label>
                        <input type="text" id="pfp-url-input" placeholder="https://imgur.com/..." style="padding: 10px; background: #05070b; border: 1px solid rgba(0,243,255,0.3); color: #fff; border-radius: 6px;">
                        <button class="action-btn" id="save-pfp-btn" style="padding: 8px;">Zapisz Awatar</button>
                    </div>
                    <button class="action-btn" id="profile-logout-btn" style="margin-top: 10px; display: none; background: #ef4444; color: white;">Wyloguj się</button>
                </div>
            </div>

            <div id="section-create-manga" class="tab-content" style="display: none;">
                <h2>Stwórz Mangę lub Anime</h2>
                <div style="display: flex; gap: 15px; margin-top: 15px;">
                    <button id="btn-mode-manga" class="action-btn" style="flex: 1; background: #00f3ff;">Dodaj Mangę</button>
                    <button id="btn-mode-anime" class="action-btn" style="flex: 1; background: #1e293b; color: #00f3ff; border: 1px solid #00f3ff;">Dodaj Anime</button>
                </div>

                <!-- FORMULARZ MANGI -->
                <div id="form-container-manga" class="admin-card" style="background: var(--card-bg); border: 1px solid rgba(0, 243, 255, 0.3); padding: 25px; border-radius: 10px; max-width: 700px; margin-top: 20px;">
                    <form id="create-manga-form" style="display: flex; flex-direction: column; gap: 15px;">
                        <input type="text" id="cm-title" placeholder="Nazwa mangi..." required style="padding: 12px; background: #05070b; border: 1px solid rgba(0,243,255,0.3); color: #fff; border-radius: 6px;">
                        <textarea id="cm-desc" placeholder="Opis fabuły mangi..." rows="3" required style="padding: 12px; background: #05070b; border: 1px solid rgba(0,243,255,0.3); color: #fff; border-radius: 6px; resize: none;"></textarea>
                        
                        <div style="display: flex; gap: 10px;">
                            <input type="text" id="cm-genre" placeholder="Gatunki (np. Action, Fantasy)..." required style="flex: 2; padding: 12px; background: #05070b; border: 1px solid rgba(0,243,255,0.3); color: #fff; border-radius: 6px;">
                            <select id="cm-status" style="flex: 1; padding: 12px; background: #05070b; color: #fff; border: 1px solid rgba(0,243,255,0.3); border-radius: 6px;">
                                <option value="Trwa">Trwa</option>
                                <option value="Zakończona">Zakończona</option>
                            </select>
                        </div>

                        <label style="font-size: 14px; color: #94a3b8;">Prześlij okładkę (PNG / JPG):</label>
                        <input type="file" id="cm-file" accept="image/png, image/jpeg" style="padding: 10px; background: #05070b; border: 1px solid rgba(0,243,255,0.3); color: #fff; border-radius: 6px;">
                        <input type="number" id="cm-price" placeholder="Cena w PLN (np. 15) - zostaw puste dla darmowej..." style="padding: 12px; background: #05070b; border: 1px solid rgba(0,243,255,0.3); color: #fff; border-radius: 6px;">

                        <hr style="border-color: rgba(0,243,255,0.2);">
                        <h4 style="color: #00f3ff; margin: 0;">Zarządzanie Rozdziałami i Stronami</h4>
                        <div id="manga-chapters-builder-list" style="display: flex; flex-direction: column; gap: 12px;"></div>
                        <button type="button" id="add-manga-chapter-btn" class="action-btn" style="background: #1e293b; color: #00f3ff; border: 1px solid #00f3ff; padding: 8px 12px; font-size: 13px;">+ Dodaj Rozdział</button>

                        <button type="submit" class="action-btn" style="margin-top: 10px;">Opublikuj Mangę</button>
                    </form>
                </div>

                <!-- FORMULARZ ANIME -->
                <div id="form-container-anime" class="admin-card" style="background: var(--card-bg); border: 1px solid rgba(168, 85, 247, 0.4); padding: 25px; border-radius: 10px; max-width: 700px; margin-top: 20px; display: none;">
                    <form id="create-anime-form" style="display: flex; flex-direction: column; gap: 15px;">
                        <input type="text" id="ca-title" placeholder="Tytuł anime..." required style="padding: 12px; background: #05070b; border: 1px solid rgba(168,85,247,0.3); color: #fff; border-radius: 6px;">
                        <textarea id="ca-desc" placeholder="Opis fabuły..." rows="3" required style="padding: 12px; background: #05070b; border: 1px solid rgba(168,85,247,0.3); color: #fff; border-radius: 6px; resize: none;"></textarea>
                        
                        <div style="display: flex; gap: 10px;">
                            <input type="text" id="ca-genre" placeholder="Gatunki (np. Akcja, Shounen)..." required style="flex: 2; padding: 12px; background: #05070b; border: 1px solid rgba(168,85,247,0.3); color: #fff; border-radius: 6px;">
                            <select id="ca-usk" style="flex: 1; padding: 12px; background: #05070b; color: #fff; border: 1px solid rgba(168,85,247,0.3); border-radius: 6px;">
                                <option value="USK 6">USK 6</option>
                                <option value="USK 12">USK 12</option>
                                <option value="USK 16" selected>USK 16</option>
                                <option value="USK 18">USK 18</option>
                            </select>
                        </div>

                        <label style="font-size: 14px; color: #94a3b8;">Plakat / Plakat okładkowy:</label>
                        <input type="file" id="ca-file" accept="image/png, image/jpeg" style="padding: 10px; background: #05070b; border: 1px solid rgba(168,85,247,0.3); color: #fff; border-radius: 6px;">
                        
                        <input type="number" id="ca-price" placeholder="Cena za całość/dostęp PLN (zostaw puste dla free)..." style="padding: 12px; background: #05070b; border: 1px solid rgba(168,85,247,0.3); color: #fff; border-radius: 6px;">

                        <hr style="border-color: rgba(168,85,247,0.2);">
                        <h4 style="color: #c084fc; margin: 0;">Zarządzanie Sezonami i Odcinkami</h4>
                        <div id="seasons-builder-list" style="display: flex; flex-direction: column; gap: 12px;"></div>
                        <button type="button" id="add-season-btn" class="action-btn" style="background: #1e293b; color: #c084fc; border: 1px solid #c084fc;">+ Dodaj Sezon</button>

                        <button type="submit" class="action-btn" style="background: linear-gradient(135deg, #a855f7, #6366f1); margin-top: 10px;">Opublikuj Anime</button>
                    </form>
                </div>
            </div>

            <div id="section-admin-panel" class="tab-content" style="display: none;">
                <h2>⚡ Panel Administratora & Skarbonka</h2>
                <div class="admin-grid" style="display: grid; grid-template-columns: 1fr; gap: 20px; margin-top: 20px; max-width: 600px;">
                    <div class="admin-card" style="background: var(--card-bg); border: 1px solid rgba(0, 243, 255, 0.5); padding: 20px; border-radius: 8px;">
                        <h4 style="color: #00f3ff; margin-top: 0;">💰 Skarbonka (Pula ze sprzedaży)</h4>
                        <p style="font-size: 20px; font-weight: bold; color: #10b981;">Stan konta: <span id="admin-piggy-bank">0.00</span> PLN</p>
                        <form id="payout-form" style="display: flex; flex-direction: column; gap: 12px; margin-top: 15px;">
                            <input type="number" id="payout-amount" placeholder="Kwota do wypłaty (PLN)..." required style="padding: 10px; background: #05070b; border: 1px solid rgba(0,243,255,0.3); color: #fff; border-radius: 6px;">
                            <select id="payout-method" style="padding: 10px; background: #05070b; color: #fff; border: 1px solid rgba(0,243,255,0.3); border-radius: 6px;">
                                <option value="Przelew Bankowy">Przelew Bankowy</option>
                                <option value="PayPal">PayPal</option>
                                <option value="BLIK na telefon">BLIK na telefon</option>
                            </select>
                            <button type="submit" class="action-btn" style="background: #10b981; color: #fff;">Wypłać środki</button>
                        </form>
                    </div>

                    <div class="admin-card" style="background: var(--card-bg); border: 1px solid rgba(168, 85, 247, 0.4); padding: 20px; border-radius: 8px;">
                        <h4 style="color: #c084fc; margin-top: 0;">Nadaj Uprawnienia Admina</h4>
                        <form id="add-user-admin-form" style="display: flex; flex-direction: column; gap: 12px; margin-top: 10px;">
                            <input type="text" id="admin-target-user" placeholder="Wpisz nazwę użytkownika..." required style="padding: 10px; background: #05070b; border: 1px solid rgba(168,85,247,0.3); color: #fff; border-radius: 6px;">
                            <button type="submit" class="action-btn">Nadaj uprawnienia admina</button>
                        </form>
                    </div>
                </div>
            </div>
        </main>
    </div>

    <!-- CZYTNIK MANGI (PEŁNY EKRAN / OVERLAY) -->
    <div id="manga-reader-modal" class="modal-overlay" style="display: none; justify-content: flex-start; align-items: stretch; flex-direction: column; background: #030508;">
        <div style="background: #0b0f19; padding: 12px 25px; border-bottom: 1px solid rgba(0,243,255,0.3); display: flex; justify-content: space-between; align-items: center;">
            <span id="reader-chapter-title" style="color: #00f3ff; font-weight: bold; font-size: 16px;">Tytuł Rozdziału</span>
            <div style="display: flex; gap: 15px; align-items: center;">
                <button id="reader-prev-ch" class="action-btn" style="padding: 6px 12px; font-size: 12px;">⏮ Poprz. Rozdział</button>
                <button id="reader-next-ch" class="action-btn" style="padding: 6px 12px; font-size: 12px;">Nast. Rozdział ⏭</button>
                <span id="close-manga-reader" style="cursor:pointer; font-size: 24px; color: #ef4444; margin-left: 15px;">&times;</span>
            </div>
        </div>
        <div id="reader-pages-container" style="flex: 1; overflow-y: auto; display: flex; flex-direction: column; align-items: center; padding: 20px; gap: 15px; background: #05070b;">
            <!-- Tutaj ładują się strony obrazkowe mangi -->
        </div>
    </div>

    <!-- DOLNY ODTWARZACZ ANIME -->
    <div id="video-player-bar" class="video-player-bar" style="display: none;">
        <div class="video-container-box">
            <div class="video-header-info">
                <span id="player-anime-title" style="color: #00f3ff; font-weight: bold;">Tytuł - Odcinek</span>
                <span id="close-player-btn" style="cursor:pointer; font-size: 20px; color: #ef4444;">&times;</span>
            </div>
            <video id="active-video-element" controls controlsList="nodownload" style="width: 100%; height: 260px; background: #000; border-radius: 6px; outline: none;"></video>
            <div class="video-controls-row" style="display: flex; justify-content: center; gap: 15px; margin-top: 8px;">
                <button id="player-prev-btn" class="action-btn" style="padding: 6px 15px; font-size: 13px;">⏮ Poprzedni</button>
                <button id="player-next-btn" class="action-btn" style="padding: 6px 15px; font-size: 13px;">Następny ⏭</button>
            </div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
"""

css_content = """:root {
    --bg-color: #07090e;
    --sidebar-bg: #0b0f19;
    --header-bg: #0b0f19;
    --card-bg: #0b0f19;
    --text-color: #f1f5f9;
}

body.light-mode {
    --bg-color: #f8fafc;
    --sidebar-bg: #e2e8f0;
    --header-bg: #ffffff;
    --card-bg: #ffffff;
    --text-color: #0f172a;
}

body.font-small { font-size: 13px; }
body.font-medium { font-size: 15px; }
body.font-large { font-size: 18px; }

body {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: var(--bg-color);
    color: var(--text-color);
    display: flex;
    flex-direction: row;
    min-width: 1200px;
    width: 1200px;
    height: 100vh;
    overflow: hidden;
    transition: background 0.3s, color 0.3s;
}

.sidebar {
    width: 65px;
    background: var(--sidebar-bg);
    border-right: 1px solid rgba(0, 243, 255, 0.15);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 20px;
    gap: 25px;
    flex-shrink: 0;
    z-index: 10;
}
.sidebar-top-icon { font-size: 24px; color: #a855f7; text-shadow: 0 0 10px rgba(168, 85, 247, 0.5); }
.sidebar-icon { font-size: 24px; cursor: pointer; padding: 10px; border-radius: 10px; color: #94a3b8; transition: all 0.3s ease; }
.sidebar-icon:hover { color: #00f3ff; text-shadow: 0 0 10px #00f3ff; }
.sidebar-icon.active { background: rgba(0, 243, 255, 0.1); color: #00f3ff; box-shadow: inset 0 0 10px rgba(0, 243, 255, 0.3); }

.main-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    background: var(--bg-color);
    position: relative;
    width: calc(1200px - 65px);
    padding-bottom: 320px;
}

.top-header {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 15px 25px;
    background: var(--header-bg);
    border-bottom: 1px solid rgba(0, 243, 255, 0.2);
    position: relative;
    z-index: 5;
}
.search-box input {
    width: 100%;
    max-width: 450px;
    padding: 10px 20px;
    border-radius: 25px;
    border: 1px solid rgba(0, 243, 255, 0.3);
    background: var(--card-bg);
    color: var(--text-color);
    outline: none;
    text-align: center;
    font-size: 15px;
}
.hamburger-menu {
    position: absolute;
    right: 25px;
    font-size: 28px;
    cursor: pointer;
    font-weight: bold;
    color: #00f3ff;
}

.dropdown-menu {
    display: none;
    position: absolute;
    top: 65px;
    right: 20px;
    background: var(--card-bg);
    border: 1px solid rgba(0, 243, 255, 0.3);
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
    flex-direction: column;
    z-index: 100;
    width: 160px;
}
.menu-item-btn {
    background: none;
    border: none;
    padding: 14px;
    text-align: left;
    width: 100%;
    cursor: pointer;
    font-size: 15px;
    color: var(--text-color);
    font-weight: bold;
}
.menu-item-btn:hover { background: rgba(0, 243, 255, 0.15); color: #00f3ff; }

.nav-bar {
    display: flex;
    align-items: center;
    padding: 12px 25px;
    background: var(--header-bg);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}
.nav-links {
    display: flex;
    gap: 20px;
    font-weight: bold;
    font-size: 15px;
    flex-wrap: wrap;
}
.nav-links span { cursor: pointer; color: #94a3b8; transition: all 0.3s; }
.nav-links span:hover { color: #00f3ff; }
.nav-links span.active { color: #00f3ff; border-bottom: 2px solid #00f3ff; padding-bottom: 4px; }

.main-banner {
    width: 100%;
    height: 180px;
    background: linear-gradient(135deg, rgba(88,101,242,0.2), rgba(0,243,255,0.15)), #0b0f19;
    border: 1px solid rgba(88, 101, 242, 0.5);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 35px;
    box-shadow: 0 0 20px rgba(88, 101, 242, 0.2);
    margin-bottom: 25px;
    box-sizing: border-box;
    text-decoration: none;
    transition: all 0.3s ease;
}
.main-banner:hover {
    border-color: #5865F2;
    box-shadow: 0 0 30px rgba(88, 101, 242, 0.4);
    transform: translateY(-2px);
}
.banner-content h1 {
    font-size: 28px;
    color: #5865F2;
    margin: 0 0 8px 0;
    text-shadow: 0 0 10px rgba(88, 101, 242, 0.5);
}
.banner-content p {
    font-size: 14px;
    color: #94a3b8;
    margin: 0;
}
.banner-discord-btn {
    background: #5865F2;
    color: #ffffff;
    padding: 12px 22px;
    border-radius: 8px;
    font-weight: bold;
    font-size: 15px;
    box-shadow: 0 0 15px rgba(88, 101, 242, 0.5);
    white-space: nowrap;
    transition: background 0.3s;
}
.main-banner:hover .banner-discord-btn {
    background: #4752c4;
}

.modal-overlay {
    position: fixed;
    top: 0; left: 0;
    width: 1200px; height: 100vh;
    background: rgba(3, 5, 8, 0.85);
    backdrop-filter: blur(5px);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}
.modal-box {
    background: var(--card-bg);
    color: var(--text-color);
    padding: 30px;
    border-radius: 12px;
    width: 380px;
    position: relative;
    box-shadow: 0 0 35px rgba(0, 243, 255, 0.25);
    border: 1px solid rgba(0, 243, 255, 0.4);
}
.close-modal {
    position: absolute;
    top: 12px; right: 18px;
    font-size: 24px;
    cursor: pointer;
    color: #00f3ff;
}
.modal-box form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-top: 15px;
}
.modal-box input {
    padding: 12px;
    border: 1px solid rgba(0, 243, 255, 0.3);
    background: #05070b;
    color: #fff;
    border-radius: 6px;
    font-size: 15px;
    outline: none;
}
.action-btn {
    background: linear-gradient(135deg, #00f3ff, #0077ff);
    color: #000;
    border: none;
    padding: 12px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: bold;
    font-size: 15px;
    box-shadow: 0 0 15px rgba(0, 243, 255, 0.4);
    transition: all 0.3s;
}
.action-btn:hover { box-shadow: 0 0 25px rgba(0, 243, 255, 0.8); transform: translateY(-2px); }

.switch { position: relative; display: inline-block; width: 50px; height: 24px; }
.switch input { opacity: 0; width: 0; height: 0; }
.slider { position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; transition: .4s; border-radius: 24px; }
.slider:before { position: absolute; content: ""; height: 16px; width: 16px; left: 4px; bottom: 4px; background-color: white; transition: .4s; border-radius: 50%; }
input:checked + .slider { background-color: #00f3ff; }
input:checked + .slider:before { transform: translateX(26px); }

.content-body { padding: 25px; flex: 1; }
.content-body h2 { margin-top: 0; font-size: 22px; border-bottom: 2px solid rgba(0, 243, 255, 0.2); padding-bottom: 8px; color: var(--text-color); }
.manga-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 20px; padding-top: 15px; }
.manga-card { display: flex; flex-direction: column; align-items: center; background: var(--card-bg); border-radius: 10px; overflow: hidden; border: 1px solid rgba(0, 243, 255, 0.15); box-shadow: 0 4px 15px rgba(0,0,0,0.5); transition: all 0.3s ease; cursor: pointer; }
.manga-card:hover { transform: translateY(-6px); border-color: #00f3ff; }
.manga-cover { width: 100%; height: 180px; background: #030508; position: relative; background-size: cover; background-position: center; }
.manga-label { background: var(--card-bg); color: var(--text-color); width: 100%; text-align: center; font-size: 14px; padding: 10px 0; font-weight: bold; }
.manga-price { font-size: 12px; color: #00f3ff; padding-bottom: 6px; font-weight: bold; }
.manga-rating { font-size: 11px; color: #fbbf24; padding-bottom: 8px; }

.video-player-bar {
    position: fixed;
    bottom: 0;
    left: 65px;
    width: calc(1200px - 65px);
    background: rgba(7, 9, 14, 0.95);
    border-top: 2px solid #00f3ff;
    padding: 15px 25px;
    box-sizing: border-box;
    z-index: 500;
    box-shadow: 0 -10px 30px rgba(0,0,0,0.8);
}
.video-container-box {
    max-width: 600px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.video-header-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
"""

js_content = """document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const dropdownMenu = document.getElementById('dropdown-menu');
    const loginMenuBtn = document.getElementById('login-menu-btn');
    const registerMenuBtn = document.getElementById('register-menu-btn');
    const settingsMenuBtn = document.getElementById('settings-menu-btn');
    
    const modalOverlay = document.getElementById('modal-overlay');
    const closeModalBtn = document.getElementById('close-modal-btn');
    const modalTitle = document.getElementById('modal-title');
    const authForm = document.getElementById('auth-form');
    const adminNavTab = document.getElementById('admin-nav-tab');

    const emailModalOverlay = document.getElementById('email-modal-overlay');
    const closeEmailModal = document.getElementById('close-email-modal');
    const emailVerifyForm = document.getElementById('email-verify-form');

    const settingsModalOverlay = document.getElementById('settings-modal-overlay');
    const closeSettingsModal = document.getElementById('close-settings-modal');
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const soundToggle = document.getElementById('sound-toggle');
    const fontSizeSelect = document.getElementById('font-size-select');

    const paymentModalOverlay = document.getElementById('payment-modal-overlay');
    const closePaymentModal = document.getElementById('close-payment-modal');
    const paymentItemTitle = document.getElementById('payment-item-title');
    const payMethodBtns = document.querySelectorAll('.pay-method-btn');

    const tabLinks = document.querySelectorAll('.tab-link, .sidebar-icon[data-tab]');
    const tabContents = document.querySelectorAll('.tab-content');

    const createMangaForm = document.getElementById('create-manga-form');
    const createAnimeForm = document.getElementById('create-anime-form');
    const addUserAdminForm = document.getElementById('add-user-admin-form');
    const payoutForm = document.getElementById('payout-form');
    const adminPiggyBank = document.getElementById('admin-piggy-bank');

    const btnModeManga = document.getElementById('btn-mode-manga');
    const btnModeAnime = document.getElementById('btn-mode-anime');
    const formContainerManga = document.getElementById('form-container-manga');
    const formContainerAnime = document.getElementById('form-container-anime');
    const seasonsBuilderList = document.getElementById('seasons-builder-list');
    const addSeasonBtn = document.getElementById('add-season-btn');

    // Miejsca rozdziałów mangi w creatorze
    const mangaChaptersBuilderList = document.getElementById('manga-chapters-builder-list');
    const addMangaChapterBtn = document.getElementById('add-manga-chapter-btn');

    const profileUsername = document.getElementById('profile-username');
    const profileRole = document.getElementById('profile-role');
    const profileLogoutBtn = document.getElementById('profile-logout-btn');
    const profilePfp = document.getElementById('profile-pfp');
    const loggedProfileSettings = document.getElementById('logged-profile-settings');
    const pfpUrlInput = document.getElementById('pfp-url-input');
    const savePfpBtn = document.getElementById('save-pfp-btn');
    
    const newUsernameInput = document.getElementById('new-username-input');
    const saveUsernameBtn = document.getElementById('save-username-btn');
    const globalSearchInput = document.getElementById('global-search-input');

    // Player Elements
    const videoPlayerBar = document.getElementById('video-player-bar');
    const activeVideoElement = document.getElementById('active-video-element');
    const playerAnimeTitle = document.getElementById('player-anime-title');
    const closePlayerBtn = document.getElementById('close-player-btn');
    const playerPrevBtn = document.getElementById('player-prev-btn');
    const playerNextBtn = document.getElementById('player-next-btn');

    // Manga Reader Elements
    const mangaReaderModal = document.getElementById('manga-reader-modal');
    const readerChapterTitle = document.getElementById('reader-chapter-title');
    const readerPagesContainer = document.getElementById('reader-pages-container');
    const closeMangaReader = document.getElementById('close-manga-reader');
    const readerPrevCh = document.getElementById('reader-prev-ch');
    const readerNextCh = document.getElementById('reader-next-ch');

    let mode = 'login';
    let isLogged = localStorage.getItem('logged_user');
    let pendingUser = null;
    let pendingPass = null;
    let generatedEmailCode = "";
    let selectedItemForPayment = null;
    
    let currentPlayingList = [];
    let currentPlayingIndex = 0;

    let currentReadingMangaIndex = null;
    let currentReadingChapterIndex = 0;

    if (localStorage.getItem('dark_mode') === 'false') {
        document.body.classList.add('light-mode');
        darkModeToggle.checked = false;
    }
    if (localStorage.getItem('sound_enabled') === 'false') {
        soundToggle.checked = false;
    }
    const savedFontSize = localStorage.getItem('font_size') || 'medium';
    fontSizeSelect.value = savedFontSize;
    document.body.classList.add('font-' + savedFontSize);

    darkModeToggle.addEventListener('change', () => {
        if (darkModeToggle.checked) {
            document.body.classList.remove('light-mode');
            localStorage.setItem('dark_mode', 'true');
        } else {
            document.body.classList.add('light-mode');
            localStorage.setItem('dark_mode', 'false');
        }
    });

    soundToggle.addEventListener('change', () => {
        localStorage.setItem('sound_enabled', soundToggle.checked);
    });

    fontSizeSelect.addEventListener('change', () => {
        document.body.classList.remove('font-small', 'font-medium', 'font-large');
        document.body.classList.add('font-' + fontSizeSelect.value);
        localStorage.setItem('font_size', fontSizeSelect.value);
    });

    function isAdmin(username) {
        if (!username) return false;
        if (username === "admin") return true;
        return localStorage.getItem('admin_user_' + username) === 'true';
    }

    function refreshUI() {
        let piggyBalance = parseFloat(localStorage.getItem('admin_piggy_bank') || '0').toFixed(2);
        adminPiggyBank.textContent = piggyBalance;

        if (isLogged) {
            loginMenuBtn.textContent = "Wyloguj (" + isLogged + ")";
            registerMenuBtn.style.display = "none";
            profileUsername.textContent = isLogged;
            profileRole.textContent = isAdmin(isLogged) ? "Administrator" : "Użytkownik";
            profileLogoutBtn.style.display = "block";
            loggedProfileSettings.style.display = "flex";
            
            newUsernameInput.value = isLogged;

            let userPfp = localStorage.getItem('pfp_' + isLogged);
            if (userPfp) {
                profilePfp.style.backgroundImage = `url('${userPfp}')`;
                pfpUrlInput.value = userPfp;
            } else {
                profilePfp.style.backgroundImage = '';
                pfpUrlInput.value = '';
            }

            if (isAdmin(isLogged)) {
                adminNavTab.style.display = "inline";
            } else {
                adminNavTab.style.display = "none";
            }
        } else {
            loginMenuBtn.textContent = "Zaloguj";
            registerMenuBtn.style.display = "block";
            profileUsername.textContent = "Niezalogowany";
            profileRole.textContent = "Gość";
            profileLogoutBtn.style.display = "none";
            loggedProfileSettings.style.display = "none";
            profilePfp.style.backgroundImage = '';
            adminNavTab.style.display = "none";
        }
        loadMangas();
        loadAnime();
        loadFavorites();
        loadHistory();
    }

    // Przełączanie formularzy w "Stwórz Mangę / Anime"
    btnModeManga.addEventListener('click', () => {
        btnModeManga.style.background = '#00f3ff';
        btnModeManga.style.color = '#000';
        btnModeAnime.style.background = '#1e293b';
        btnModeAnime.style.color = '#00f3ff';
        formContainerManga.style.display = 'block';
        formContainerAnime.style.display = 'none';
    });

    btnModeAnime.addEventListener('click', () => {
        btnModeAnime.style.background = '#a855f7';
        btnModeAnime.style.color = '#fff';
        btnModeManga.style.background = '#1e293b';
        btnModeManga.style.color = '#00f3ff';
        formContainerAnime.style.display = 'block';
        formContainerManga.style.display = 'none';
    });

    // Kreator Rozdziałów i Stron Mangi
    let mangaChapterBuilderData = [];

    function renderMangaChaptersBuilder() {
        if (!mangaChaptersBuilderList) return;
        mangaChaptersBuilderList.innerHTML = '';
        mangaChapterBuilderData.forEach((ch, cIdx) => {
            let pagesHtml = '';
            ch.pages.forEach((pageUrl, pIdx) => {
                pagesHtml += `
                    <div style="display: flex; gap: 8px; margin-top: 5px; align-items: center;">
                        <span style="font-size: 12px; color: #94a3b8;">Strona ${pIdx + 1}</span>
                        <button type="button" onclick="removeMangaPage(${cIdx}, ${pIdx})" style="background:#ef4444; color:#fff; border:none; padding:4px 8px; border-radius:4px; cursor:pointer; font-size:11px;">Usuń strone</button>
                    </div>
                `;
            });

            let chapterBox = document.createElement('div');
            chapterBox.style.cssText = "background: #030508; padding: 15px; border-radius: 8px; border: 1px solid rgba(0,243,255,0.2);";
            chapterBox.innerHTML = `
                <div style="display: flex; gap: 10px; align-items: center;">
                    <input type="text" placeholder="Nazwa Rozdziału (np. Rozdział 1)" value="${ch.title}" oninput="updateMangaChapterTitle(${cIdx}, this.value)" style="flex:1; padding:8px; background:#05070b; border:1px solid rgba(0,243,255,0.3); color:#fff; border-radius:4px;">
                    <button type="button" onclick="removeMangaChapter(${cIdx})" style="background:#ef4444; color:#fff; border:none; padding:8px 12px; border-radius:4px; cursor:pointer;">Usuń Rozdział</button>
                </div>
                <div style="margin-top: 10px; padding-left: 10px; border-left: 2px solid #00f3ff;">
                    <p style="margin:0 0 5px 0; font-size:12px; color:#00f3ff;">Strony (Wybierz pliki PNG/JPG):</p>
                    <input type="file" accept="image/png, image/jpeg" multiple onchange="addMangaPages(${cIdx}, event)" style="font-size:11px; color:#94a3b8; margin-bottom: 5px;">
                    ${pagesHtml}
                </div>
            `;
            mangaChaptersBuilderList.appendChild(chapterBox);
        });
    }

    if (addMangaChapterBtn) {
        addMangaChapterBtn.addEventListener('click', () => {
            mangaChapterBuilderData.push({ title: `Rozdział ${mangaChapterBuilderData.length + 1}`, pages: [] });
            renderMangaChaptersBuilder();
        });
    }

    window.updateMangaChapterTitle = (cIdx, val) => { mangaChapterBuilderData[cIdx].title = val; }
    window.removeMangaChapter = (cIdx) => { mangaChapterBuilderData.splice(cIdx, 1); renderMangaChaptersBuilder(); }
    window.removeMangaPage = (cIdx, pIdx) => { mangaChapterBuilderData[cIdx].pages.splice(pIdx, 1); renderMangaChaptersBuilder(); }
    
    window.addMangaPages = (cIdx, event) => {
        const files = event.target.files;
        if (files) {
            Array.from(files).forEach(file => {
                const reader = new FileReader();
                reader.onload = function(e) {
                    mangaChapterBuilderData[cIdx].pages.push(e.target.result);
                    renderMangaChaptersBuilder();
                };
                reader.readAsDataURL(file);
            });
        }
    }

    // Kreator Sezonów i Odcinków dla Anime
    let seasonBuilderData = [];

    function renderSeasonsBuilder() {
        if (!seasonsBuilderList) return;
        seasonsBuilderList.innerHTML = '';
        seasonBuilderData.forEach((season, sIdx) => {
            let epsHtml = '';
            season.episodes.forEach((ep, eIdx) => {
                epsHtml += `
                    <div style="display: flex; gap: 8px; margin-top: 5px; align-items: center;">
                        <input type="text" placeholder="Nazwa odcinka..." value="${ep.title}" oninput="updateEpTitle(${sIdx}, ${eIdx}, this.value)" style="flex:2; padding:8px; background:#030508; border:1px solid rgba(168,85,247,0.3); color:#fff; border-radius:4px;">
                        <input type="file" accept="video/mp4,video/mkv,video/webm" onchange="updateEpFile(${sIdx}, ${eIdx}, event)" style="flex:2; font-size:11px; color:#94a3b8;">
                        <button type="button" onclick="removeEpisode(${sIdx}, ${eIdx})" style="background:#ef4444; color:#fff; border:none; padding:6px 10px; border-radius:4px; cursor:pointer;">&times;</button>
                    </div>
                `;
            });

            let seasonBox = document.createElement('div');
            seasonBox.style.cssText = "background: #030508; padding: 15px; border-radius: 8px; border: 1px solid rgba(168,85,247,0.2);";
            seasonBox.innerHTML = `
                <div style="display: flex; gap: 10px; align-items: center;">
                    <input type="text" placeholder="Nazwa Sezonu (np. Sezon 1)" value="${season.name}" oninput="updateSeasonName(${sIdx}, this.value)" style="flex:1; padding:8px; background:#05070b; border:1px solid rgba(168,85,247,0.3); color:#fff; border-radius:4px;">
                    <button type="button" onclick="removeSeason(${sIdx})" style="background:#ef4444; color:#fff; border:none; padding:8px 12px; border-radius:4px; cursor:pointer;">Usuń Sezon</button>
                </div>
                <div style="margin-top: 10px; padding-left: 10px; border-left: 2px solid #a855f7;">
                    <p style="margin:0 0 5px 0; font-size:12px; color:#c084fc;">Odcinki:</p>
                    ${epsHtml}
                    <button type="button" onclick="addEpisodeToSeason(${sIdx})" class="action-btn" style="background: #1e293b; color: #c084fc; border: 1px solid #c084fc; padding: 6px 12px; font-size: 12px; margin-top: 8px;">+ Dodaj Odcinek</button>
                </div>
            `;
            seasonsBuilderList.appendChild(seasonBox);
        });
    }

    if (addSeasonBtn) {
        addSeasonBtn.addEventListener('click', () => {
            seasonBuilderData.push({ name: `Sezon ${seasonBuilderData.length + 1}`, episodes: [] });
            renderSeasonsBuilder();
        });
    }

    window.updateSeasonName = (sIdx, val) => { seasonBuilderData[sIdx].name = val; }
    window.removeSeason = (sIdx) => { seasonBuilderData.splice(sIdx, 1); renderSeasonsBuilder(); }
    window.addEpisodeToSeason = (sIdx) => { seasonBuilderData[sIdx].episodes.push({ title: `Odcinek ${seasonBuilderData[sIdx].episodes.length + 1}`, videoUrl: '' }); renderSeasonsBuilder(); }
    window.updateEpTitle = (sIdx, eIdx, val) => { seasonBuilderData[sIdx].episodes[eIdx].title = val; }
    window.removeEpisode = (sIdx, eIdx) => { seasonBuilderData[sIdx].episodes.splice(eIdx, 1); renderSeasonsBuilder(); }
    
    window.updateEpFile = (sIdx, eIdx, event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                seasonBuilderData[sIdx].episodes[eIdx].videoUrl = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    }

    // Publikacja Mangę
    createMangaForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const title = document.getElementById('cm-title').value;
        const desc = document.getElementById('cm-desc').value;
        const genre = document.getElementById('cm-genre').value;
        const status = document.getElementById('cm-status').value;
        const fileInput = document.getElementById('cm-file');
        const price = document.getElementById('cm-price').value;

        if (fileInput.files && fileInput.files[0]) {
            const reader = new FileReader();
            reader.onload = function(event) {
                saveMangaData(title, desc, genre, status, event.target.result, price, mangaChapterBuilderData);
            };
            reader.readAsDataURL(fileInput.files[0]);
        } else {
            saveMangaData(title, desc, genre, status, '', price, mangaChapterBuilderData);
        }
    });

    function saveMangaData(title, desc, genre, status, img, price, chapters) {
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        customMangas.push({ title, desc, genre, status, img, price, chapters, comments: [], ratings: [] });
        localStorage.setItem('created_mangas_db', JSON.stringify(customMangas));
        alert("Manga opublikowana pomyślnie!");
        createMangaForm.reset();
        mangaChapterBuilderData = [];
        renderMangaChaptersBuilder();
        loadMangas();
    }

    // Publikacja Anime
    createAnimeForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const title = document.getElementById('ca-title').value;
        const desc = document.getElementById('ca-desc').value;
        const genre = document.getElementById('ca-genre').value;
        const usk = document.getElementById('ca-usk').value;
        const price = document.getElementById('ca-price').value;
        const fileInput = document.getElementById('ca-file');

        if (seasonBuilderData.length === 0) {
            alert("Dodaj przynajmniej jeden sezon i odcinek!");
            return;
        }

        if (fileInput.files && fileInput.files[0]) {
            const reader = new FileReader();
            reader.onload = function(event) {
                saveAnimeData(title, desc, genre, usk, price, event.target.result, seasonBuilderData);
            };
            reader.readAsDataURL(fileInput.files[0]);
        } else {
            saveAnimeData(title, desc, genre, usk, price, '', seasonBuilderData);
        }
    });

    function saveAnimeData(title, desc, genre, usk, price, img, seasons) {
        let animeList = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
        animeList.push({ title, desc, genre, usk, price, img, seasons, comments: [], ratings: [] });
        localStorage.setItem('created_anime_db', JSON.stringify(animeList));
        alert("Anime opublikowane pomyślnie!");
        createAnimeForm.reset();
        seasonBuilderData = [];
        renderSeasonsBuilder();
        loadAnime();
    }

    function loadMangas() {
        const customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        const gridHome = document.getElementById('grid-home');
        
        if (customMangas.length === 0) {
            gridHome.innerHTML = '<p style="color: #94a3b8; font-size: 14px;">Brak mang. Dodaj pierwszą w zakładce "Stwórz Mangę / Anime".</p>';
            return;
        }

        let html = '';
        customMangas.forEach((item, index) => {
            let bgStyle = item.img ? `style="background-image: url('${item.img}');"` : '';
            let priceText = item.price ? `<div class="manga-price">Cena: ${item.price} PLN</div>` : '';
            let avgRating = item.ratings && item.ratings.length > 0 ? (item.ratings.reduce((a,b)=>a+b,0)/item.ratings.length).toFixed(1) : 'Brak ocen';
            
            html += `
                <div class="manga-card" onclick="openMangaDetails(${index})">
                    <div class="manga-cover" ${bgStyle}></div>
                    <div class="manga-label">${item.title}</div>
                    ${priceText}
                    <div class="manga-rating">⭐ ${avgRating} | 📖 Manga</div>
                </div>
            `;
        });
        gridHome.innerHTML = html;
    }

    function loadAnime() {
        const customAnime = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
        const gridAnime = document.getElementById('grid-anime');
        
        if (customAnime.length === 0) {
            gridAnime.innerHTML = '<p style="color: #94a3b8; font-size: 14px;">Brak anime. Dodaj pierwsze w zakładce "Stwórz Mangę / Anime".</p>';
            return;
        }

        let html = '';
        customAnime.forEach((item, index) => {
            let bgStyle = item.img ? `style="background-image: url('${item.img}');"` : '';
            let priceText = item.price ? `<div class="manga-price">Cena: ${item.price} PLN</div>` : '';
            let avgRating = item.ratings && item.ratings.length > 0 ? (item.ratings.reduce((a,b)=>a+b,0)/item.ratings.length).toFixed(1) : 'Brak ocen';
            
            html += `
                <div class="manga-card" onclick="openAnimeDetails(${index})">
                    <div class="manga-cover" ${bgStyle}></div>
                    <div class="manga-label">${item.title}</div>
                    ${priceText}
                    <div class="manga-rating">⭐ ${avgRating} | 🎬 Anime</div>
                </div>
            `;
        });
        gridAnime.innerHTML = html;
    }

    // Szczegóły Mangi (Stylowe jak oglądajanime) oraz przycisk edycji dla admina
    window.openMangaDetails = function(index) {
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        let manga = customMangas[index];
        
        if (isLogged) {
            let history = JSON.parse(localStorage.getItem('history_' + isLogged) || '[]');
            if (!history.some(m => m.title === manga.title)) {
                history.unshift(manga);
                localStorage.setItem('history_' + isLogged, JSON.stringify(history));
                loadHistory();
            }
        }

        let isPaid = manga.price && parseFloat(manga.price) > 0;
        let purchasedList = JSON.parse(localStorage.getItem('purchased_' + (isLogged || 'guest')) || '[]');
        let hasAccess = !isPaid || purchasedList.includes(manga.title) || (isLogged && isAdmin(isLogged));

        let paymentBoxHtml = '';
        if (!hasAccess) {
            paymentBoxHtml = `<button onclick="initMangaPayment(${index})" class="action-btn" style="background:#10b981; color:#fff; width:100%; margin-bottom:15px;">Kup dostęp do Mangi za ${manga.price} PLN</button>`;
        }

        let adminEditBtn = '';
        if (isLogged && isAdmin(isLogged)) {
            adminEditBtn = `<button onclick="openEditMangaModal(${index})" class="action-btn" style="background: #c084fc; color: #000; width: 100%; margin-bottom: 10px;">⚙️ Edytuj Mangę (Admin)</button>`;
        }

        let chaptersHtml = '';
        if (manga.chapters && manga.chapters.length > 0) {
            manga.chapters.forEach((ch, cIdx) => {
                chaptersHtml += `
                    <button onclick="openMangaReader(${index}, ${cIdx})" class="action-btn" style="background:#1e293b; color:#00f3ff; border:1px solid rgba(0,243,255,0.3); padding:8px 12px; font-size:13px; text-align:left;">📖 ${ch.title} (${ch.pages ? ch.pages.length : 0} stron)</button>
                `;
            });
        } else {
            chaptersHtml = '<p style="color:#94a3b8; font-size:13px;">Brak rozdziałów.</p>';
        }

        let commentsHtml = '';
        if (manga.comments && manga.comments.length > 0) {
            manga.comments.forEach(c => {
                commentsHtml += `<div style="background:#05070b; padding:8px; margin:5px 0; border-radius:4px; font-size:13px;"><b>${c.user}:</b> ${c.text}</div>`;
            });
        } else {
            commentsHtml = '<p style="color:#94a3b8; font-size:13px;">Brak komentarzy.</p>';
        }

        let detailsBox = document.createElement('div');
        detailsBox.className = 'modal-overlay';
        detailsBox.innerHTML = `
            <div class="modal-box" style="width: 520px; max-height: 85vh; overflow-y: auto;">
                <span class="close-modal" id="close-manga-details">&times;</span>
                ${adminEditBtn}
                <h3 style="color: #00f3ff; margin-top:0;">${manga.title}</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 5px 0;"><b>Gatunek:</b> ${manga.genre || 'Brak'} | <b>Status:</b> <span style="color:#10b981;">${manga.status || 'Trwa'}</span></p>
                <p style="font-size: 14px; line-height: 1.4; color: var(--text-color);">${manga.desc || 'Brak opisu.'}</p>
                ${paymentBoxHtml}
                <div style="margin: 10px 0;">
                    <button onclick="toggleFavoriteManga(${index})" class="action-btn" style="background: #1e293b; color: #fbbf24; border:1px solid #fbbf24; width:100%;">⭐ Dodaj do Ulubionych</button>
                </div>
                <hr style="border-color: rgba(0,243,255,0.2);">
                <h4 style="color:#00f3ff; margin:10px 0;">Lista Rozdziałów:</h4>
                <div style="max-height: 200px; overflow-y: auto; background: #030508; padding: 10px; border-radius: 6px; display: flex; flex-direction: column; gap: 6px;">
                    ${chaptersHtml}
                </div>
                <hr style="border-color: rgba(0,243,255,0.2);">
                <h4>Oceny i Komentarze</h4>
                <div style="margin-bottom: 10px;">
                    Oceń (1-5): 
                    <button onclick="rateManga(${index}, 1)" class="action-btn" style="padding:4px 8px;">1</button>
                    <button onclick="rateManga(${index}, 2)" class="action-btn" style="padding:4px 8px;">2</button>
                    <button onclick="rateManga(${index}, 3)" class="action-btn" style="padding:4px 8px;">3</button>
                    <button onclick="rateManga(${index}, 4)" class="action-btn" style="padding:4px 8px;">4</button>
                    <button onclick="rateManga(${index}, 5)" class="action-btn" style="padding:4px 8px;">5</button>
                </div>
                <div style="max-height: 100px; overflow-y: auto; background: #030508; padding: 10px; border-radius: 6px;">
                    ${commentsHtml}
                </div>
                <form id="manga-comment-form" style="margin-top: 10px; display:flex; gap:5px;">
                    <input type="text" id="manga-comment-input" placeholder="Napisz komentarz..." required style="flex:1; padding:8px; background:#05070b; border:1px solid rgba(0,243,255,0.3); color:#fff; border-radius:4px;">
                    <button type="submit" class="action-btn" style="padding:8px 12px;">Wyślij</button>
                </form>
            </div>
        `;
        document.body.appendChild(detailsBox);

        document.getElementById('close-manga-details').addEventListener('click', () => { detailsBox.remove(); });

        document.getElementById('manga-comment-form').addEventListener('submit', (e) => {
            e.preventDefault();
            if (!isLogged) { alert("Musisz się zalogować!"); return; }
            const text = document.getElementById('manga-comment-input').value;
            if(!manga.comments) manga.comments = [];
            manga.comments.push({ user: isLogged, text: text });
            customMangas[index] = manga;
            localStorage.setItem('created_mangas_db', JSON.stringify(customMangas));
            detailsBox.remove();
            openMangaDetails(index);
        });
    }

    // Czytnik Stron Mangi
    window.openMangaReader = function(mangaIndex, chapterIndex) {
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        let manga = customMangas[mangaIndex];
        
        let isPaid = manga.price && parseFloat(manga.price) > 0;
        let purchasedList = JSON.parse(localStorage.getItem('purchased_' + (isLogged || 'guest')) || '[]');
        let hasAccess = !isPaid || purchasedList.includes(manga.title) || (isLogged && isAdmin(isLogged));

        if (!hasAccess) {
            alert("Musisz kupić dostęp do tej mangi!");
            return;
        }

        currentReadingMangaIndex = mangaIndex;
        currentReadingChapterIndex = chapterIndex;

        renderReaderContent();
        mangaReaderModal.style.display = 'flex';
    }

    function renderReaderContent() {
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        let manga = customMangas[currentReadingMangaIndex];
        let chapter = manga.chapters[currentReadingChapterIndex];

        readerChapterTitle.textContent = `${manga.title} - ${chapter.title}`;
        readerPagesContainer.innerHTML = '';

        if (!chapter.pages || chapter.pages.length === 0) {
            readerPagesContainer.innerHTML = '<p style="color: #94a3b8;">Brak stron w tym rozdziale.</p>';
            return;
        }

        chapter.pages.forEach((pageUrl, pIdx) => {
            let imgEl = document.createElement('img');
            imgEl.src = pageUrl;
            imgEl.style.cssText = "max-width: 800px; width: 100%; height: auto; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.8);";
            readerPagesContainer.appendChild(imgEl);
        });
    }

    closeMangaReader.addEventListener('click', () => {
        mangaReaderModal.style.display = 'none';
    });

    readerPrevCh.addEventListener('click', () => {
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        let manga = customMangas[currentReadingMangaIndex];
        if (currentReadingChapterIndex > 0) {
            currentReadingChapterIndex--;
            renderReaderContent();
            readerPagesContainer.scrollTop = 0;
        } else {
            alert("To pierwszy rozdział.");
        }
    });

    readerNextCh.addEventListener('click', () => {
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        let manga = customMangas[currentReadingMangaIndex];
        if (currentReadingChapterIndex < manga.chapters.length - 1) {
            currentReadingChapterIndex++;
            renderReaderContent();
            readerPagesContainer.scrollTop = 0;
        } else {
            alert("To ostatni rozdział.");
        }
    });

    window.toggleFavoriteManga = function(index) {
        if (!isLogged) { alert("Musisz się zalogować!"); return; }
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        let manga = customMangas[index];
        let favs = JSON.parse(localStorage.getItem('favorites_' + isLogged) || '[]');
        
        let existingIndex = favs.findIndex(m => m.title === manga.title);
        if (existingIndex > -1) { favs.splice(existingIndex, 1); alert("Usunięto z ulubionych."); }
        else { favs.push(manga); alert("Dodano do ulubionych!"); }
        localStorage.setItem('favorites_' + isLogged, JSON.stringify(favs));
        loadFavorites();
    }

    window.rateManga = function(index, stars) {
        if (!isLogged) { alert("Musisz się zalogować!"); return; }
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        let manga = customMangas[index];
        if(!manga.ratings) manga.ratings = [];
        manga.ratings.push(stars);
        customMangas[index] = manga;
        localStorage.setItem('created_mangas_db', JSON.stringify(customMangas));
        alert("Dziękujemy za ocenę!");
        loadMangas();
    }

    // Szczegóły Anime oraz Wybór Odcinków i Player (z opcją edycji dla admina)
    window.openAnimeDetails = function(index) {
        let customAnime = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
        let anime = customAnime[index];
        
        if (isLogged) {
            let history = JSON.parse(localStorage.getItem('history_' + isLogged) || '[]');
            if (!history.some(m => m.title === anime.title)) {
                history.unshift(anime);
                localStorage.setItem('history_' + isLogged, JSON.stringify(history));
                loadHistory();
            }
        }

        let isPaid = anime.price && parseFloat(anime.price) > 0;
        let purchasedList = JSON.parse(localStorage.getItem('purchased_' + (isLogged || 'guest')) || '[]');
        let hasAccess = !isPaid || purchasedList.includes(anime.title) || (isLogged && isAdmin(isLogged));

        let paymentBoxHtml = '';
        if (!hasAccess) {
            paymentBoxHtml = `<button onclick="initAnimePayment(${index})" class="action-btn" style="background:#10b981; color:#fff; width:100%; margin-bottom:15px;">Kup dostęp do Anime za ${anime.price} PLN</button>`;
        }

        let adminEditBtn = '';
        if (isLogged && isAdmin(isLogged)) {
            adminEditBtn = `<button onclick="openEditAnimeModal(${index})" class="action-btn" style="background: #c084fc; color: #000; width: 100%; margin-bottom: 10px;">⚙️ Edytuj Anime (Admin)</button>`;
        }

        let seasonsHtml = '';
        anime.seasons.forEach((season, sIdx) => {
            let epsListHtml = '';
            season.episodes.forEach((ep, eIdx) => {
                epsListHtml += `
                    <button onclick="playAnimeEpisode(${index}, ${sIdx}, ${eIdx})" class="action-btn" style="background:#1e293b; color:#00f3ff; border:1px solid rgba(0,243,255,0.3); padding:8px 12px; font-size:13px; text-align:left;">▶ ${ep.title}</button>
                `;
            });
            seasonsHtml += `
                <div style="margin-bottom: 12px;">
                    <b style="color:#c084fc; font-size:14px;">${season.name}</b>
                    <div style="display:flex; flex-direction:column; gap:6px; margin-top:6px;">
                        ${epsListHtml}
                    </div>
                </div>
            `;
        });

        let commentsHtml = '';
        if (anime.comments && anime.comments.length > 0) {
            anime.comments.forEach(c => {
                commentsHtml += `<div style="background:#05070b; padding:8px; margin:5px 0; border-radius:4px; font-size:13px;"><b>${c.user}:</b> ${c.text}</div>`;
            });
        } else {
            commentsHtml = '<p style="color:#94a3b8; font-size:13px;">Brak komentarzy.</p>';
        }

        let detailsBox = document.createElement('div');
        detailsBox.className = 'modal-overlay';
        detailsBox.innerHTML = `
            <div class="modal-box" style="width: 500px; max-height: 85vh; overflow-y: auto;">
                <span class="close-modal" id="close-anime-details">&times;</span>
                ${adminEditBtn}
                <h3 style="color: #00f3ff; margin-top:0;">${anime.title}</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 5px 0;"><b>Gatunek:</b> ${anime.genre} | <span style="color:#fbbf24; font-weight:bold;">${anime.usk}</span></p>
                <p style="font-size: 14px; line-height: 1.4; color: var(--text-color);">${anime.desc}</p>
                ${paymentBoxHtml}
                <div style="margin: 10px 0;">
                    <button onclick="toggleFavoriteAnime(${index})" class="action-btn" style="background: #1e293b; color: #fbbf24; border:1px solid #fbbf24; width:100%;">⭐ Ulubione</button>
                </div>
                <hr style="border-color: rgba(0,243,255,0.2);">
                <h4 style="color:#00f3ff; margin:10px 0;">Wybierz Odcinek:</h4>
                <div style="max-height: 200px; overflow-y: auto; background: #030508; padding: 10px; border-radius: 6px;">
                    ${seasonsHtml}
                </div>
                <hr style="border-color: rgba(0,243,255,0.2);">
                <h4>Oceny i Komentarze</h4>
                <div style="margin-bottom: 10px;">
                    Oceń (1-5): 
                    <button onclick="rateAnime(${index}, 1)" class="action-btn" style="padding:4px 8px;">1</button>
                    <button onclick="rateAnime(${index}, 2)" class="action-btn" style="padding:4px 8px;">2</button>
                    <button onclick="rateAnime(${index}, 3)" class="action-btn" style="padding:4px 8px;">3</button>
                    <button onclick="rateAnime(${index}, 4)" class="action-btn" style="padding:4px 8px;">4</button>
                    <button onclick="rateAnime(${index}, 5)" class="action-btn" style="padding:4px 8px;">5</button>
                </div>
                <div style="max-height: 100px; overflow-y: auto; background: #030508; padding: 10px; border-radius: 6px;">
                    ${commentsHtml}
                </div>
                <form id="anime-comment-form" style="margin-top: 10px; display:flex; gap:5px;">
                    <input type="text" id="anime-comment-input" placeholder="Napisz komentarz..." required style="flex:1; padding:8px; background:#05070b; border:1px solid rgba(0,243,255,0.3); color:#fff; border-radius:4px;">
                    <button type="submit" class="action-btn" style="padding:8px 12px;">Wyślij</button>
                </form>
            </div>
        `;
        document.body.appendChild(detailsBox);

        document.getElementById('close-anime-details').addEventListener('click', () => { detailsBox.remove(); });

        document.getElementById('anime-comment-form').addEventListener('submit', (e) => {
            e.preventDefault();
            if (!isLogged) { alert("Musisz się zalogować!"); return; }
            const text = document.getElementById('anime-comment-input').value;
            if(!anime.comments) anime.comments = [];
            anime.comments.push({ user: isLogged, text: text });
            customAnime[index] = anime;
            localStorage.setItem('created_anime_db', JSON.stringify(customAnime));
            detailsBox.remove();
            openAnimeDetails(index);
        });
    }

    // Modal edycji mangi dla admina z obsługą edycji rozdziałów i dodawania stron
    window.openEditMangaModal = function(index) {
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        let manga = customMangas[index];
        if (!manga.chapters) manga.chapters = [];

        function renderEditMangaChapters() {
            let listEl = document.getElementById('edit-manga-chapters-list');
            if (!listEl) return;
            listEl.innerHTML = '';
            
            manga.chapters.forEach((ch, cIdx) => {
                let pagesHtml = '';
                if (ch.pages) {
                    ch.pages.forEach((p, pIdx) => {
                        pagesHtml += `
                            <div style="display:flex; justify-between; align-items:center; gap:5px; margin-top:3px;">
                                <span style="font-size:11px; color:#94a3b8;">Strona ${pIdx + 1}</span>
                                <button type="button" onclick="editRemoveMangaPage(${index}, ${cIdx}, ${pIdx})" style="background:#ef4444; color:#fff; border:none; padding:2px 6px; border-radius:3px; cursor:pointer; font-size:10px;">Usuń</button>
                            </div>
                        `;
                    });
                }

                let chDiv = document.createElement('div');
                chDiv.style.cssText = "background:#030508; border:1px solid rgba(0,243,255,0.2); padding:10px; border-radius:6px; margin-bottom:8px;";
                chDiv.innerHTML = `
                    <div style="display:flex; gap:8px; align-items:center; margin-bottom:8px;">
                        <input type="text" value="${ch.title}" onchange="editUpdateChapterTitle(${index}, ${cIdx}, this.value)" style="flex:1; padding:6px; background:#05070b; border:1px solid rgba(0,243,255,0.3); color:#fff; border-radius:4px; font-size:12px;">
                        <button type="button" onclick="editRemoveMangaChapter(${index}, ${cIdx})" style="background:#ef4444; color:#fff; border:none; padding:6px 10px; border-radius:4px; cursor:pointer; font-size:11px;">Usuń Rozdział</button>
                    </div>
                    <div style="padding-left:10px; border-left:2px solid #00f3ff;">
                        <label style="font-size:11px; color:#00f3ff;">Dodaj strony do tego rozdziału:</label>
                        <input type="file" accept="image/png, image/jpeg" multiple onchange="editAddMangaPages(${index}, ${cIdx}, event)" style="font-size:11px; color:#94a3b8; display:block; margin-top:4px;">
                        ${pagesHtml}
                    </div>
                `;
                listEl.appendChild(chDiv);
            });
        }

        let editBox = document.createElement('div');
        editBox.className = 'modal-overlay';
        editBox.id = 'edit-manga-modal-box';
        editBox.innerHTML = `
            <div class="modal-box" style="width: 500px; max-height: 85vh; overflow-y: auto;">
                <span class="close-modal" id="close-edit-manga">&times;</span>
                <h3 style="color: #c084fc; margin-top:0;">Edytuj Mangę</h3>
                <form id="edit-manga-form" style="display:flex; flex-direction:column; gap:10px;">
                    <label style="font-size:12px; color:#94a3b8;">Tytuł:</label>
                    <input type="text" id="edit-m-title" value="${manga.title}" required style="padding:8px; background:#05070b; border:1px solid #00f3ff; color:#fff; border-radius:4px;">
                    <label style="font-size:12px; color:#94a3b8;">Opis:</label>
                    <textarea id="edit-m-desc" rows="3" style="padding:8px; background:#05070b; border:1px solid #00f3ff; color:#fff; border-radius:4px; resize:none;">${manga.desc || ''}</textarea>
                    <label style="font-size:12px; color:#94a3b8;">Cena (PLN):</label>
                    <input type="number" id="edit-m-price" value="${manga.price || ''}" style="padding:8px; background:#05070b; border:1px solid #00f3ff; color:#fff; border-radius:4px;">
                    
                    <hr style="border-color: rgba(0,243,255,0.2);">
                    <h4 style="color:#00f3ff; margin:0;">Zarządzanie Rozdziałami</h4>
                    <div id="edit-manga-chapters-list"></div>
                    <button type="button" onclick="editAddMangaChapter(${index})" class="action-btn" style="background:#1e293b; color:#00f3ff; border:1px solid #00f3ff; padding:6px 12px; font-size:12px;">+ Dodaj Nowy Rozdział</button>

                    <button type="submit" class="action-btn" style="background:#10b981; color:#fff; margin-top:10px;">Zapisz Zmiany</button>
                    <button type="button" onclick="deleteManga(${index})" class="action-btn" style="background:#ef4444; color:#fff;">Usuń Mangę</button>
                </form>
            </div>
        `;
        document.body.appendChild(editBox);
        renderEditMangaChapters();

        document.getElementById('close-edit-manga').addEventListener('click', () => { editBox.remove(); });

        document.getElementById('edit-manga-form').addEventListener('submit', (e) => {
            e.preventDefault();
            manga.title = document.getElementById('edit-m-title').value;
            manga.desc = document.getElementById('edit-m-desc').value;
            manga.price = document.getElementById('edit-m-price').value;
            customMangas[index] = manga;
            localStorage.setItem('created_mangas_db', JSON.stringify(customMangas));
            alert("Zaktualizowano mangę!");
            editBox.remove();
            refreshUI();
        });

        window.editUpdateChapterTitle = (mIdx, cIdx, val) => {
            let mangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
            mangas[mIdx].chapters[cIdx].title = val;
            localStorage.setItem('created_mangas_db', JSON.stringify(mangas));
        };

        window.editRemoveMangaChapter = (mIdx, cIdx) => {
            let mangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
            mangas[mIdx].chapters.splice(cIdx, 1);
            localStorage.setItem('created_mangas_db', JSON.stringify(mangas));
            document.getElementById('edit-manga-modal-box').remove();
            openEditMangaModal(mIdx);
        };

        window.editRemoveMangaPage = (mIdx, cIdx, pIdx) => {
            let mangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
            mangas[mIdx].chapters[cIdx].pages.splice(pIdx, 1);
            localStorage.setItem('created_mangas_db', JSON.stringify(mangas));
            document.getElementById('edit-manga-modal-box').remove();
            openEditMangaModal(mIdx);
        };

        window.editAddMangaChapter = (mIdx) => {
            let mangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
            if (!mangas[mIdx].chapters) mangas[mIdx].chapters = [];
            mangas[mIdx].chapters.push({ title: `Rozdział ${mangas[mIdx].chapters.length + 1}`, pages: [] });
            localStorage.setItem('created_mangas_db', JSON.stringify(mangas));
            document.getElementById('edit-manga-modal-box').remove();
            openEditMangaModal(mIdx);
        };

        window.editAddMangaPages = (mIdx, cIdx, event) => {
            const files = event.target.files;
            if (files && files.length > 0) {
                let mangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
                let loadedCount = 0;
                Array.from(files).forEach(file => {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        if (!mangas[mIdx].chapters[cIdx].pages) mangas[mIdx].chapters[cIdx].pages = [];
                        mangas[mIdx].chapters[cIdx].pages.push(e.target.result);
                        loadedCount++;
                        if (loadedCount === files.length) {
                            localStorage.setItem('created_mangas_db', JSON.stringify(mangas));
                            document.getElementById('edit-manga-modal-box').remove();
                            openEditMangaModal(mIdx);
                        }
                    };
                    reader.readAsDataURL(file);
                });
            }
        };
    }

    window.deleteManga = function(index) {
        if(confirm("Czy na pewno chcesz usunąć tę mangę?")) {
            let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
            customMangas.splice(index, 1);
            localStorage.setItem('created_mangas_db', JSON.stringify(customMangas));
            alert("Usunięto pomyślnie.");
            location.reload();
        }
    }

    // Modal edycji anime dla admina
    window.openEditAnimeModal = function(index) {
        let customAnime = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
        let anime = customAnime[index];

        let editBox = document.createElement('div');
        editBox.className = 'modal-overlay';
        editBox.innerHTML = `
            <div class="modal-box" style="width: 450px; max-height: 85vh; overflow-y: auto;">
                <span class="close-modal" id="close-edit-anime">&times;</span>
                <h3 style="color: #c084fc; margin-top:0;">Edytuj Anime</h3>
                <form id="edit-anime-form" style="display:flex; flex-direction:column; gap:10px;">
                    <label style="font-size:12px; color:#94a3b8;">Tytuł:</label>
                    <input type="text" id="edit-a-title" value="${anime.title}" required style="padding:8px; background:#05070b; border:1px solid #a855f7; color:#fff; border-radius:4px;">
                    <label style="font-size:12px; color:#94a3b8;">Opis:</label>
                    <textarea id="edit-a-desc" rows="3" style="padding:8px; background:#05070b; border:1px solid #a855f7; color:#fff; border-radius:4px; resize:none;">${anime.desc || ''}</textarea>
                    <label style="font-size:12px; color:#94a3b8;">Cena (PLN):</label>
                    <input type="number" id="edit-a-price" value="${anime.price || ''}" style="padding:8px; background:#05070b; border:1px solid #a855f7; color:#fff; border-radius:4px;">
                    <button type="submit" class="action-btn" style="background:#10b981; color:#fff; margin-top:10px;">Zapisz Zmiany</button>
                    <button type="button" onclick="deleteAnime(${index})" class="action-btn" style="background:#ef4444; color:#fff;">Usuń Anime</button>
                </form>
            </div>
        `;
        document.body.appendChild(editBox);
        document.getElementById('close-edit-anime').addEventListener('click', () => { editBox.remove(); });

        document.getElementById('edit-anime-form').addEventListener('submit', (e) => {
            e.preventDefault();
            anime.title = document.getElementById('edit-a-title').value;
            anime.desc = document.getElementById('edit-a-desc').value;
            anime.price = document.getElementById('edit-a-price').value;
            customAnime[index] = anime;
            localStorage.setItem('created_anime_db', JSON.stringify(customAnime));
            alert("Zaktualizowano anime!");
            editBox.remove();
            refreshUI();
        });
    }

    window.deleteAnime = function(index) {
        if(confirm("Czy na pewno chcesz usunąć to anime?")) {
            let customAnime = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
            customAnime.splice(index, 1);
            localStorage.setItem('created_anime_db', JSON.stringify(customAnime));
            alert("Usunięto pomyślnie.");
            location.reload();
        }
    }

    // Odtwarzanie Odcinka w Dolnym Playerze
    window.playAnimeEpisode = function(animeIndex, seasonIndex, epIndex) {
        let customAnime = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
        let anime = customAnime[animeIndex];
        
        let isPaid = anime.price && parseFloat(anime.price) > 0;
        let purchasedList = JSON.parse(localStorage.getItem('purchased_' + (isLogged || 'guest')) || '[]');
        let hasAccess = !isPaid || purchasedList.includes(anime.title) || (isLogged && isAdmin(isLogged));

        if (!hasAccess) {
            alert("Musisz kupić dostęp do tego anime, aby odtworzyć odcinek!");
            return;
        }

        let season = anime.seasons[seasonIndex];
        let ep = season.episodes[epIndex];

        if (!ep.videoUrl) {
            alert("Ten odcinek nie posiada pliku wideo!");
            return;
        }

        currentPlayingList = [];
        anime.seasons.forEach(s => {
            s.episodes.forEach(e => {
                currentPlayingList.push({ animeTitle: anime.title, seasonName: s.name, epTitle: e.title, url: e.videoUrl });
            });
        });

        currentPlayingIndex = currentPlayingList.findIndex(item => item.animeTitle === anime.title && item.seasonName === season.name && item.epTitle === ep.title);

        setupPlayerContent();
    }

    function setupPlayerContent() {
        if(currentPlayingList.length === 0) return;
        let currentItem = currentPlayingList[currentPlayingIndex];
        
        playerAnimeTitle.textContent = `${currentItem.animeTitle} (${currentItem.seasonName}) - ${currentItem.epTitle}`;
        activeVideoElement.src = currentItem.url;
        activeVideoElement.play();
        videoPlayerBar.style.display = 'block';
    }

    closePlayerBtn.addEventListener('click', () => {
        activeVideoElement.pause();
        activeVideoElement.src = '';
        videoPlayerBar.style.display = 'none';
    });

    playerPrevBtn.addEventListener('click', () => {
        if(currentPlayingIndex > 0) {
            currentPlayingIndex--;
            setupPlayerContent();
        } else {
            alert("To pierwszy odcinek.");
        }
    });

    playerNextBtn.addEventListener('click', () => {
        if(currentPlayingIndex < currentPlayingList.length - 1) {
            currentPlayingIndex++;
            setupPlayerContent();
        } else {
            alert("To ostatny odcinek.");
        }
    });

    window.initAnimePayment = function(index) {
        selectedItemForPayment = { type: 'anime', index: index };
        let customAnime = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
        let anime = customAnime[index];
        paymentItemTitle.textContent = anime.title + " - " + anime.price + " PLN";
        paymentModalOverlay.style.display = 'flex';
    }

    window.initMangaPayment = function(index) {
        selectedItemForPayment = { type: 'manga', index: index };
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        let manga = customMangas[index];
        paymentItemTitle.textContent = manga.title + " - " + manga.price + " PLN";
        paymentModalOverlay.style.display = 'flex';
    }

    payMethodBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            let method = btn.getAttribute('data-method');
            if (!selectedItemForPayment) return;

            let price = 0;
            let title = '';
            if (selectedItemForPayment.type === 'manga') {
                let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
                let manga = customMangas[selectedItemForPayment.index];
                price = parseFloat(manga.price);
                title = manga.title;
            } else {
                let customAnime = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
                let anime = customAnime[selectedItemForPayment.index];
                price = parseFloat(anime.price);
                title = anime.title;
            }

            let currentPiggy = parseFloat(localStorage.getItem('admin_piggy_bank') || '0');
            localStorage.setItem('admin_piggy_bank', currentPiggy + price);

            let userKey = isLogged || 'guest';
            let purchased = JSON.parse(localStorage.getItem('purchased_' + userKey) || '[]');
            purchased.push(title);
            localStorage.setItem('purchased_' + userKey, JSON.stringify(purchased));

            alert(`Płatność metodą (${method}) powiodła się!`);
            paymentModalOverlay.style.display = 'none';
            refreshUI();
            if (selectedItemForPayment.type === 'manga') openMangaDetails(selectedItemForPayment.index);
            else openAnimeDetails(selectedItemForPayment.index);
        });
    });

    window.toggleFavoriteAnime = function(index) {
        if (!isLogged) { alert("Musisz się zalogować!"); return; }
        let customAnime = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
        let anime = customAnime[index];
        let favs = JSON.parse(localStorage.getItem('favorites_' + isLogged) || '[]');
        
        let existingIndex = favs.findIndex(m => m.title === anime.title);
        if (existingIndex > -1) { favs.splice(existingIndex, 1); alert("Usunięto z ulubionych."); }
        else { favs.push(anime); alert("Dodano do ulubionych!"); }
        localStorage.setItem('favorites_' + isLogged, JSON.stringify(favs));
        loadFavorites();
    }

    window.rateAnime = function(index, stars) {
        if (!isLogged) { alert("Musisz się zalogować!"); return; }
        let customAnime = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
        let anime = customAnime[index];
        if(!anime.ratings) anime.ratings = [];
        anime.ratings.push(stars);
        customAnime[index] = anime;
        localStorage.setItem('created_anime_db', JSON.stringify(customAnime));
        alert("Dziękujemy za ocenę!");
        loadAnime();
    }

    function loadFavorites() {
        const gridFavs = document.getElementById('grid-favorites');
        if (!isLogged) { gridFavs.innerHTML = '<p style="color: #94a3b8; font-size: 14px;">Zaloguj się, aby zobaczyć ulubione.</p>'; return; }
        let favs = JSON.parse(localStorage.getItem('favorites_' + isLogged) || '[]');
        if (favs.length === 0) { gridFavs.innerHTML = '<p style="color: #94a3b8; font-size: 14px;">Brak elementów w ulubionych.</p>'; return; }
        let html = '';
        favs.forEach(item => {
            let bgStyle = item.img ? `style="background-image: url('${item.img}');"` : '';
            html += `<div class="manga-card"><div class="manga-cover" ${bgStyle}></div><div class="manga-label">${item.title}</div></div>`;
        });
        gridFavs.innerHTML = html;
    }

    function loadHistory() {
        const gridHist = document.getElementById('grid-history');
        if (!isLogged) { gridHist.innerHTML = '<p style="color: #94a3b8; font-size: 14px;">Zaloguj się, aby zobaczyć historię.</p>'; return; }
        let hist = JSON.parse(localStorage.getItem('history_' + isLogged) || '[]');
        if (hist.length === 0) { gridHist.innerHTML = '<p style="color: #94a3b8; font-size: 14px;">Brak historii.</p>'; return; }
        let html = '';
        hist.forEach(item => {
            let bgStyle = item.img ? `style="background-image: url('${item.img}');"` : '';
            html += `<div class="manga-card"><div class="manga-cover" ${bgStyle}></div><div class="manga-label">${item.title}</div></div>`;
        });
        gridHist.innerHTML = html;
    }

    // Globalna wyszukiwarka
    globalSearchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        const gridHome = document.getElementById('grid-home');
        let mangaHtml = '';
        let filteredMangas = customMangas.filter(m => m.title.toLowerCase().includes(query));
        filteredMangas.forEach((item, index) => {
            let bgStyle = item.img ? `style="background-image: url('${item.img}');"` : '';
            mangaHtml += `<div class="manga-card" onclick="openMangaDetails(${index})"><div class="manga-cover" ${bgStyle}></div><div class="manga-label">${item.title}</div></div>`;
        });
        gridHome.innerHTML = mangaHtml || '<p style="color: #94a3b8; font-size: 14px;">Brak wyników mang.</p>';

        const customAnime = JSON.parse(localStorage.getItem('created_anime_db') || '[]');
        const gridAnime = document.getElementById('grid-anime');
        let animeHtml = '';
        let filteredAnime = customAnime.filter(a => a.title.toLowerCase().includes(query) || a.genre.toLowerCase().includes(query));
        filteredAnime.forEach((item, index) => {
            let bgStyle = item.img ? `style="background-image: url('${item.img}');"` : '';
            animeHtml += `<div class="manga-card" onclick="openAnimeDetails(${index})"><div class="manga-cover" ${bgStyle}></div><div class="manga-label">${item.title}</div></div>`;
        });
        gridAnime.innerHTML = animeHtml || '<p style="color: #94a3b8; font-size: 14px;">Brak wyników anime.</p>';
    });

    tabLinks.forEach(link => {
        link.addEventListener('click', () => {
            const target = link.getAttribute('data-tab');
            if(!target) return;
            tabLinks.forEach(l => l.classList.remove('active'));
            document.querySelectorAll(`[data-tab="${target}"]`).forEach(el => el.classList.add('active'));
            tabContents.forEach(content => {
                content.style.display = (content.id === 'section-' + target) ? 'block' : 'none';
            });
        });
    });

    menuToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        dropdownMenu.style.display = dropdownMenu.style.display === 'flex' ? 'none' : 'flex';
    });

    document.addEventListener('click', () => { dropdownMenu.style.display = 'none'; });

    loginMenuBtn.addEventListener('click', () => {
        if (isLogged) {
            localStorage.removeItem('logged_user');
            isLogged = null;
            alert("Wylogowano.");
            refreshUI();
            return;
        }
        modalTitle.textContent = "Zaloguj się";
        mode = 'login';
        modalOverlay.style.display = 'flex';
    });

    profileLogoutBtn.addEventListener('click', () => {
        localStorage.removeItem('logged_user');
        isLogged = null;
        alert("Wylogowano.");
        refreshUI();
    });

    registerMenuBtn.addEventListener('click', () => {
        modalTitle.textContent = "Zarejestruj konto";
        mode = 'register';
        modalOverlay.style.display = 'flex';
    });

    settingsMenuBtn.addEventListener('click', () => {
        settingsModalOverlay.style.display = 'flex';
    });

    closeModalBtn.addEventListener('click', () => { modalOverlay.style.display = 'none'; });
    closeEmailModal.addEventListener('click', () => { emailModalOverlay.style.display = 'none'; });
    closeSettingsModal.addEventListener('click', () => { settingsModalOverlay.style.display = 'none'; });
    closePaymentModal.addEventListener('click', () => { paymentModalOverlay.style.display = 'none'; });

    authForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const user = document.getElementById('username').value;
        const pass = document.getElementById('password').value;

        if (mode === 'register') {
            pendingUser = user;
            pendingPass = pass;
            generatedEmailCode = Math.floor(1000 + Math.random() * 9000).toString();
            
            emailjs.send("service_q9rd7dm", "template_qf8a01k", { email: user, passcode: generatedEmailCode }).then(() => {
                alert("Kod weryfikacyjny wysłany na e-mail!");
                modalOverlay.style.display = 'none';
                emailModalOverlay.style.display = 'flex';
            }, (error) => { alert("Błąd e-mail: " + JSON.stringify(error)); });
        } else {
            const savedPass = localStorage.getItem('db_user_' + user);
            if ((user === "admin" && pass === "tajnehaslo") || (savedPass && savedPass === pass)) {
                localStorage.setItem('logged_user', user);
                isLogged = user;
                alert("Zalogowano pomyślnie!");
                modalOverlay.style.display = 'none';
                refreshUI();
            } else { alert("Błędny login lub hasło!"); }
        }
        authForm.reset();
    });

    emailVerifyForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const enteredCode = document.getElementById('verification-code-input').value;
        if (enteredCode === generatedEmailCode) {
            localStorage.setItem('db_user_' + pendingUser, pendingPass);
            localStorage.setItem('logged_user', pendingUser);
            isLogged = pendingUser;
            alert("E-mail zweryfikowany!");
            emailModalOverlay.style.display = 'none';
            refreshUI();
        } else { alert("Błędny kod!"); }
        emailVerifyForm.reset();
    });

    addUserAdminForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const targetUser = document.getElementById('admin-target-user').value;
        localStorage.setItem('admin_user_' + targetUser, 'true');
        alert("Nadano uprawnienia admina dla: " + targetUser);
        addUserAdminForm.reset();
    });

    payoutForm.addEventListener('submit', (e) => {
        e.preventDefault();
        if (!isLogged || !isAdmin(isLogged)) {
            alert("Brak uprawnień!");
            return;
        }
        let amountToPayout = parseFloat(document.getElementById('payout-amount').value);
        let method = document.getElementById('payout-method').value;
        let currentPiggy = parseFloat(localStorage.getItem('admin_piggy_bank') || '0');

        if (amountToPayout > currentPiggy) {
            alert("Nie masz tylu środków w skarbonce!");
            return;
        }

        localStorage.setItem('admin_piggy_bank', currentPiggy - amountToPayout);
        alert(`Zlecono wypłatę kwoty ${amountToPayout} PLN za pomocą: ${method}. Środki wkrótce dotrą.`);
        payoutForm.reset();
        refreshUI();
    });

    refreshUI();
});
"""

with open(os.path.join(path, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(os.path.join(path, 'style.css'), 'w', encoding='utf-8') as f:
    f.write(css_content)

with open(os.path.join(path, 'script.js'), 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Zaktualizowano generator pomyślnie!")
