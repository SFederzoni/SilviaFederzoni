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
   Auteur : ChatGPT x Silvia Federzoni
   ========================================================== */

async function loadHALPublications() {
  const halId = "silvia-federzoni"; // Identifiant HAL (adapter si besoin)
  const url = `https://api.archives-ouvertes.fr/search/?q=authIdHal_s:${halId}&fl=title_s,authFullName_s,producedDateY_i,docType_s,label_bibtex,linkExtUrl_s&rows=50&sort=producedDateY_i desc`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    const container = document.getElementById('hal-publications');

    container.innerHTML = ''; // On vide le contenu initial

    if (!data.response || data.response.numFound === 0) {
      container.innerHTML = "<p>Aucune publication trouvée sur HAL.</p>";
      return;
    }

    // Construction des blocs de publications
    data.response.docs.forEach(pub => {
      const title = pub.title_s || "Titre non disponible";
      const authors = pub.authFullName_s ? pub.authFullName_s.join(', ') : "Auteurs inconnus";
      const year = pub.producedDateY_i || "";
      const type = pub.docType_s || "";
      const link = pub.linkExtUrl_s ? pub.linkExtUrl_s[0] : null;

      const div = document.createElement('div');
      div.classList.add('publication');
      div.style.marginBottom = '1.2rem';
      div.style.padding = '0.5rem 0';
      div.style.borderBottom = '1px solid #ddd';

      div.innerHTML = `
        <strong>${title}</strong><br>
        <em>${authors}</em> — ${type} (${year})<br>
        ${link ? `<a href="${link}" target="_blank">↗ Voir sur HAL</a>` : ""}
      `;

      container.appendChild(div);
    });

  } catch (error) {
    document.getElementById('hal-publications').innerHTML =
      "<p>❌ Erreur lors du chargement des publications HAL.</p>";
    console.error("Erreur HAL API :", error);
  }
}

// Exécuter le script quand la page est chargée
document.addEventListener('DOMContentLoaded', loadHALPublications);
</script>


