---
layout: default
title: "Publications"
permalink: /publications/
--- 

# Publications 
<a href="https://cv.hal.science/federzoni-silvia?langChosen=fr" target="_blank">
   <img src="https://hal.science/assets/img/hal-logo-header.png" alt="HAL" style="height: 30px;">
</a>

<!-- ==============================
     Section : entête de la page
     ============================== -->
<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;">
  <!-- Logo HAL -->
  <img src="https://www.ccsd.cnrs.fr/wp-content/uploads/2019/07/logo_HAL.png"
       alt="Logo HAL"
       style="height: 60px;">
  <div>
    <h1 style="margin: 0;">📚 Publications sur HAL</h1>
    <p style="margin: 0;">Synchronisé automatiquement avec mon profil HAL</p>
    <p><a href="https://hal.archives-ouvertes.fr/silvia-federzoni"
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


