---
layout: default
title: "Publications"
permalink: /publications/
---

# Publications

<!-- Stats globales -->
<div id="global-stats" style="text-align: center; margin: 2rem 0; padding: 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; color: white; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
  <div style="font-size: 1.1rem; margin-bottom: 0.5rem; opacity: 0.9;">📊 Statistiques de mes publications</div>
  <div style="display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap; font-size: 1.8rem; font-weight: bold;">
    <div>
      <span id="total-pubs">0</span>
      <div style="font-size: 0.9rem; font-weight: normal; opacity: 0.9;">publications</div>
    </div>
  </div>
</div>

<!-- Barre de recherche + Lien CV HAL -->
<div style="display: flex; justify-content: space-between; align-items: center; gap: 1rem; margin-bottom: 2rem; flex-wrap: wrap;">
  
  <!-- Lien CV HAL (gauche) -->
  <div style="display: flex; flex-direction: column; align-items: flex-start; gap: 0.5rem;">
    <p style="margin: 0; font-size: 0.9rem; color: #666;">La liste est synchronisée automatiquement avec mon profil HAL</p>
    <a href="https://cv.hal.science/federzoni-silvia?langChosen=fr" target="_blank" style="display: flex; align-items: center; gap: 0.5rem; text-decoration: none;">
      <img src="https://hal.science/assets/img/hal-logo-header.png" alt="HAL" style="height: 45px;">
      <span style="color: #1b365d; font-weight: bold;">Mon CV HAL</span>
    </a>
  </div>

  <!-- Barre de recherche (droite) -->
  <div style="flex: 1; min-width: 300px; max-width: 500px;">
    <input 
      type="text" 
      id="searchBox" 
      placeholder="🔍 Rechercher (titre, auteur, année, venue)..."
      style="width: 100%; padding: 12px 20px; font-size: 16px; border: 2px solid #ddd; border-radius: 25px; outline: none; transition: border 0.3s;"
      onfocus="this.style.borderColor='#667eea'"
      onblur="this.style.borderColor='#ddd'"
    >
    <div style="text-align: right; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">
      <span id="resultCount">0</span> résultat(s)
    </div>
  </div>
</div>

<!-- Publications -->
<div id="hal-publications">
  <p style="text-align: center; color: #999; padding: 2rem;"><em>⏳ Chargement des publications depuis HAL...</em></p>
</div>

<script>
/* ==========================================================
   Script : Publications HAL avec recherche et Google Analytics
   ========================================================== */

// Fonction pour tracker les clics avec Google Analytics
function trackPublicationClick(action, publicationTitle, halId) {
  if (typeof gtag !== 'undefined') {
    gtag('event', action, {
      'event_category': 'Publications',
      'event_label': publicationTitle,
      'hal_id': halId
    });
  }
}

async function loadHALPublications() {
  const halId = "federzoni-silvia";
  const url = `https://api.archives-ouvertes.fr/search/?q=authIdHal_s:${halId}&fl=title_s,authFullName_s,producedDateY_i,docType_s,journalTitle_s,bookTitle_s,conferenceTitle_s,linkExtUrl_s,abstract_s,halId_s,uri_s&pageSize=100&sort=producedDateY_i desc`;
  
  // Dictionnaire pour nommer les types de documents proprement
  const typeLabels = {
    ART: "Articles de revue",
    COMM: "Communications",
    COUV: "Chapitres d'ouvrages",
    THESE: "Thèses",
    DOUV: "Directions d'ouvrages",
    OTHER: "Autres publications",
    UNDEFINED: "Documents de travail", 
    POSTER: "Posters" 
  };
  
  try {
    const response = await fetch(url);
    const data = await response.json();
    const container = document.getElementById('hal-publications');
    container.innerHTML = '';
    
    if (!data.response || data.response.numFound === 0) {
      container.innerHTML = "<p style='text-align: center; color: #999;'>Aucune publication trouvée sur HAL.</p>";
      return;
    }
    
    // Mettre à jour les stats globales
    const totalPubs = data.response.numFound;
    document.getElementById('total-pubs').textContent = totalPubs;
    document.getElementById('resultCount').textContent = totalPubs;
    
    // Groupement par type
    const grouped = {};
    data.response.docs.forEach(pub => {
      const type = pub.docType_s || "OTHER";
      if (!grouped[type]) grouped[type] = [];
      grouped[type].push(pub);
    });
    
    // Construction HTML pour chaque groupe
    for (const [type, pubs] of Object.entries(grouped)) {
      const section = document.createElement('section');
      section.innerHTML = `<h2>${typeLabels[type] || type}</h2>`;
      section.style.marginBottom = "2rem";
      
      pubs.forEach(pub => {
        const title = pub.title_s || "Titre inconnu";
        const authors = pub.authFullName_s ? pub.authFullName_s.join(', ') : "Auteurs non renseignés";
        const year = pub.producedDateY_i || "";
        const venue = pub.journalTitle_s || pub.bookTitle_s || pub.conferenceTitle_s || "";
        
        // Construction des liens HAL et PDF
        const docHalId = pub.halId_s || pub.uri_s;
        const halLink = docHalId ? `https://hal.science/${docHalId}` : null;
        const pdfLink = docHalId ? `https://hal.science/${docHalId}/document` : null;
        
        // Créer le div de publication
        const div = document.createElement('div');
        div.classList.add('publication');
        div.setAttribute('data-search-text', 
          `${title.toLowerCase()} ${authors.toLowerCase()} ${year} ${venue.toLowerCase()}`
        );
        
        // Structure HTML avec stats à droite
        div.innerHTML = `
          <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem;">
            <div style="flex: 1;">
              ${authors} (${year}). <em>${title}</em>.
              ${venue ? `<span style="color:#444;">${venue}</span>.` : ""}
              <br>
              ${halLink ? `<a href="${halLink}" target="_blank" style="color:#007acc; margin-right: 15px;" onclick="trackPublicationClick('view_hal', '${title.replace(/'/g, "\\'")}', '${docHalId}')">voir sur HAL &gt;&gt;</a>` : ""}
              ${pdfLink ? `<a href="${pdfLink}" target="_blank" style="color:#d9534f;" onclick="trackPublicationClick('download_pdf', '${title.replace(/'/g, "\\'")}', '${docHalId}')">télécharger pdf</a>` : ""}
            </div>
          </div>
        `;
        
        section.appendChild(div);
      });
      
      container.appendChild(section);
    }
    
    // Initialiser la recherche
    setupSearch();
    
  } catch (error) {
    document.getElementById('hal-publications').innerHTML =
      "<p style='text-align: center; color: #dc3545;'>❌ Erreur lors du chargement des publications HAL.</p>";
    console.error("Erreur HAL API :", error);
  }
}

// Fonction de recherche
function setupSearch() {
  const searchBox = document.getElementById('searchBox');
  const publications = document.querySelectorAll('.publication');
  
  searchBox.addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase().trim();
    let visibleCount = 0;
    
    publications.forEach(pub => {
      const searchText = pub.getAttribute('data-search-text');
      
      if (searchText.includes(searchTerm)) {
        pub.style.display = 'block';
        visibleCount++;
      } else {
        pub.style.display = 'none';
      }
    });
    
    // Mettre à jour le compteur de résultats
    document.getElementById('resultCount').textContent = visibleCount;
    
    // Gérer l'affichage des sections vides
    document.querySelectorAll('section').forEach(section => {
      const visiblePubs = Array.from(section.querySelectorAll('.publication')).filter(
        pub => pub.style.display !== 'none'
      );
      section.style.display = visiblePubs.length > 0 ? 'block' : 'none';
    });
    
    // Track la recherche dans Google Analytics
    if (searchTerm && typeof gtag !== 'undefined') {
      gtag('event', 'search', {
        'event_category': 'Publications',
        'search_term': searchTerm,
        'results_count': visibleCount
      });
    }
  });
}

document.addEventListener('DOMContentLoaded', loadHALPublications);
</script>

<style>
h2 {
  position: relative;
  display: block; 
  padding-bottom: 0.3rem;
  color: #1b365d;
  margin-top: 2rem;
  width: 100%;
}

/* Ligne dégradée en bas du h2 */
h2::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 4px;
  width: 100%;
  background: linear-gradient(
    to right,
    #1b365d,
    #123977,
    #193b8f,
    #3238a5,
    #5230b7,
    #7c26b2,
    #9d18ab,
    #b800a2,
    #cc0089,
    #d80070,
    #dd175a,
    #dc3545
  );
  border-radius: 2px;
}

.publication {
  line-height: 1.6;
  font-size: 1rem;
  padding: 1rem;
  margin-bottom: 1rem;
  background: #fafafa;
  border-radius: 8px;
  transition: all 0.3s ease;
  border-left: 3px solid transparent;
}

.publication:hover {
  background: #f0f0f0;
  border-left-color: #667eea;
  transform: translateX(5px);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.publication em {
  font-style: italic;
}

.publication a {
  text-decoration: none;
  font-weight: 500;
  transition: opacity 0.2s;
}

.publication a:hover {
  opacity: 0.7;
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 768px) {
  #global-stats > div:last-child {
    font-size: 1.4rem;
  }
  
  .publication {
    padding: 0.8rem;
  }
}
</style>
