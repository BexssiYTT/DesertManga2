document.addEventListener('DOMContentLoaded', () => {
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
                    <button onclick="openMangaReader(${index}, ${cIdx})" class="action-btn" style="background:#1e293b; color:#00f3ff; border:1px solid rgba(0,243,255,0.3); padding:8px 12px; font-size:13px; text-align:left;">📖 ${ch.title} (${ch.pages.length} stron)</button>
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

    // Modal edycji mangi dla admina
    window.openEditMangaModal = function(index) {
        let customMangas = JSON.parse(localStorage.getItem('created_mangas_db') || '[]');
        let manga = customMangas[index];

        let editBox = document.createElement('div');
        editBox.className = 'modal-overlay';
        editBox.innerHTML = `
            <div class="modal-box" style="width: 450px; max-height: 85vh; overflow-y: auto;">
                <span class="close-modal" id="close-edit-manga">&times;</span>
                <h3 style="color: #c084fc; margin-top:0;">Edytuj Mangę</h3>
                <form id="edit-manga-form" style="display:flex; flex-direction:column; gap:10px;">
                    <label style="font-size:12px; color:#94a3b8;">Tytuł:</label>
                    <input type="text" id="edit-m-title" value="${manga.title}" required style="padding:8px; background:#05070b; border:1px solid #00f3ff; color:#fff; border-radius:4px;">
                    <label style="font-size:12px; color:#94a3b8;">Opis:</label>
                    <textarea id="edit-m-desc" rows="3" style="padding:8px; background:#05070b; border:1px solid #00f3ff; color:#fff; border-radius:4px; resize:none;">${manga.desc || ''}</textarea>
                    <label style="font-size:12px; color:#94a3b8;">Cena (PLN):</label>
                    <input type="number" id="edit-m-price" value="${manga.price || ''}" style="padding:8px; background:#05070b; border:1px solid #00f3ff; color:#fff; border-radius:4px;">
                    <button type="submit" class="action-btn" style="background:#10b981; color:#fff; margin-top:10px;">Zapisz Zmiany</button>
                    <button type="button" onclick="deleteManga(${index})" class="action-btn" style="background:#ef4444; color:#fff;">Usuń Mangę</button>
                </form>
            </div>
        `;
        document.body.appendChild(editBox);
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
