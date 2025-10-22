---
layout: default
title: "Publications"
permalink: /publications/
---

# Publications
<p>Synchronisé automatiquement avec mon profil HAL</p>

<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;">
  <a href="https://cv.hal.science/federzoni-silvia?langChosen=fr" target="_blank">
    <img src="https://hal.science/assets/img/hal-logo-header.png" alt="HAL" style="height: 45px;">
  </a>
  <div>
    <p style="margin: 0;"> <a href="https://cv.hal.science/federzoni-silvia?langChosen=fr" target="_blank" style="color: #3366cc; text-decoration: none; font-weight: bold;">
         Mon CV HAL</p>
    <p>

  </a>
      </a>
    </p>
  </div>
</div>

<div id="hal-publications">
  <p><em>Chargement des publications depuis HAL...</em></p>
</div>

<script>
/* ==========================================================
   Script : afficher les publications HAL au format APA
   ========================================================== */

async function loadHALPublications() {
  const halId = "federzoni-silvia";
  const url = `https://api.archives-ouvertes.fr/search/?q=authIdHal_s:${halId}&fl=title_s,authFullName_s,producedDateY_i,docType_s,journalTitle_s,bookTitle_s,conferenceTitle_s,linkExtUrl_s,abstract_s&pageSize=100&sort=producedDateY_i desc`;

  // Dictionnaire pour nommer les types de documents proprement
  const typeLabels = {
    ART: "Articles de revue",
    COMM: "Communications",
    COUV: "Chapitres d’ouvrages",
    THESE: "Thèses",
    DOUV: "Directions d’ouvrages",
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
      container.innerHTML = "<p>Aucune publication trouvée sur HAL.</p>";
      return;
    }

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
        const link = pub.linkExtUrl_s ? pub.linkExtUrl_s[0] : null;

        // Format APA simplifié
        const apa = `
          ${authors} (${year}). <em>${title}</em>.
          ${venue ? `<span style="color:#444;">${venue}</span>.` : ""}
          ${link ? `<a href="${link}" target="_blank" style="color:#007acc;">↗ Voir sur HAL</a>` : ""}
        `;

        const div = document.createElement('div');
        div.classList.add('publication');
        div.style.marginBottom = '1rem';
        div.innerHTML = apa;
        section.appendChild(div);
      });

      container.appendChild(section);
    }

  } catch (error) {
    document.getElementById('hal-publications').innerHTML =
      "<p>❌ Erreur lors du chargement des publications HAL.</p>";
    console.error("Erreur HAL API :", error);
  }
}

document.addEventListener('DOMContentLoaded', loadHALPublications);
</script>

<style>
h2 {
  position: relative; /* nécessaire pour positionner le ::after */
  display: flexible; 
  padding-bottom: 0.3rem;
  color: #1b365d;
  margin-top: 2rem;
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
  line-height: 1.5;
  font-size: 1rem;
  padding: 0.4rem 0;
}
.publication em {
  font-style: italic;
}
</style>
