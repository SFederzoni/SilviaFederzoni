---
layout: default
title: "Publications"
permalink: /publications/
--- 

# Publications 


<!-- ==============================
     Section : entête de la page
     ============================== -->
<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;">
  <!-- Logo HAL -->
 <a href="https://cv.hal.science/federzoni-silvia?langChosen=fr" target="_blank">
   <img src="https://hal.science/assets/img/hal-logo-header.png" alt="HAL" style="height: 30px;">
</a>
  <div>
    <p style="margin: 0;">Synchronisé automatiquement avec mon profil HAL</p>
    <p><a href="[https://hal.archives-ouvertes.fr/silvia-federzoni](https://cv.hal.science/federzoni-silvia?langChosen=fr"
          target="_blank"
          style="color: #3366cc; text-decoration: none; font-weight: bold;">
          → Voir mon profil HAL complet
       </a></p>
  </div>
</div>

<!-- ==============================
     Section : liste des publications
     ============================== -->
<ul style="list-style-type: none; padding: 0;">
{% for pub in site.data.publications %}
  <li style="margin-bottom: 1.5rem; padding: 1rem; border-left: 4px solid #ff6600; background: #f9f9f9; border-radius: 8px;">
    <strong>{{ pub.authors }}</strong> ({{ pub.year }}).<br>
    <em>{{ pub.title }}</em>.<br>
    {% if pub.source %}<span style="color: #555;">{{ pub.source }}</span>.<br>{% endif %}
    <a href="{{ pub.link }}" target="_blank" style="color: #0066cc;">🔗 Lire sur HAL</a>
  </li>
{% endfor %}
</ul>


<script>
/* ==========================================================
   Script pour récupérer automatiquement les publications HAL
   ========================================================== */

async function loadHALPublications() {
  const halId = "silvia-federzoni"; // ton identifiant HAL
  const url = `https://api.archives-ouvertes.fr/search/?q=authIdHal_s:${halId}&fl=title_s,authFullName_s,producedDateY_i,docType_s,journalTitle_s,bookTitle_s,conferenceTitle_s,label_bibtex,linkExtUrl_s,abstract_s&rows=100&sort=producedDateY_i desc`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    const container = document.getElementById('hal-publications');
    container.innerHTML = '';

    if (!data.response || data.response.numFound === 0) {
      container.innerHTML = "<p>Aucune publication trouvée sur HAL.</p>";
      return;
    }

    // Création d'une section par type de document
    const grouped = {};

    data.response.docs.forEach(pub => {
      const type = pub.docType_s || "Autre";
      if (!grouped[type]) grouped[type] = [];
      grouped[type].push(pub);
    });

    // Construction HTML pour chaque groupe
    for (const [type, pubs] of Object.entries(grouped)) {
      const section = document.createElement('section');
      section.innerHTML = `<h2>${type.charAt(0).toUpperCase() + type.slice(1)}</h2>`;
      section.style.marginBottom = "2rem";

      pubs.forEach(pub => {
        const title = pub.title_s || "Titre inconnu";
        const authors = pub.authFullName_s ? pub.authFullName_s.join(', ') : "Auteurs non renseignés";
        const year = pub.producedDateY_i || "";
        const link = pub.linkExtUrl_s ? pub.linkExtUrl_s[0] : null;
        const abstract = pub.abstract_s ? pub.abstract_s[0] : null;
        const venue = pub.journalTitle_s || pub.bookTitle_s || pub.conferenceTitle_s || "";

        const div = document.createElement('div');
        div.classList.add('publication');
        div.style.marginBottom = '1.2rem';
        div.style.padding = '0.5rem 0';
        div.style.borderBottom = '1px solid #ddd';

        div.innerHTML = `
          <strong>${title}</strong><br>
          <em>${authors}</em> — ${year} ${venue ? `— <span style="color:#444;">${venue}</span>` : ""}<br>
          ${abstract ? `<details><summary>Résumé</summary><p>${abstract}</p></details>` : ""}
          ${link ? `<a href="${link}" target="_blank" style="color:#007acc;">↗ Voir sur HAL</a>` : ""}
        `;
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


