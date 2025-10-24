Nouvelle conversation

J'ai deux questions : 1. dans ce script comment ajouter après chaque ref le lien vers HAL  et le pdf ? come cela ?  [voir sur HAL >>][telecharger pdf]<script>
/* ==========================================================
   Script : afficher les publications HAL au format APA
   ========================================================== */
async function loadHALPublications() {
  const halId = "federzoni-silvia";
  const url = https://api.archives-ouvertes.fr/search/?q=authIdHal_s:${halId}&fl=title_s,authFullName_s,producedDateY_i,docType_s,journalTitle_s,bookTitle_s,conferenceTitle_s,linkExtUrl_s,abstract_s&pageSize=100&sort=producedDateY_i desc;
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
      section.innerHTML = <h2>${typeLabels[type] || type}</h2>;
      section.style.marginBottom = "2rem";
      pubs.forEach(pub => {
        const title = pub.title_s || "Titre inconnu";
        const authors = pub.authFullName_s ? pub.authFullName_s.join(', ') : "Auteurs non renseignés";
        const year = pub.producedDateY_i || "";
        const venue = pub.journalTitle_s || pub.bookTitle_s || pub.conferenceTitle_s || "";
        const link = pub.linkExtUrl_s ? pub.linkExtUrl_s[0] : null;
        // Format APA simplifié
        const apa = 
          ${authors} (${year}). <em>${title}</em>.
          ${venue ? <span style="color:#444;">${venue}</span>. : ""}
          ${link ? <a href="${link}" target="_blank" style="color:#007acc;">↗ Voir sur HAL</a> : ""}
        ;
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

Je vais vous aider avec vos questions. Commençons par la première :
1. Ajouter les liens HAL et PDF

Pour ajouter les liens [voir sur HAL >>] et [télécharger pdf] après chaque référence, vous devez modifier la partie où le format APA est construit. Voici le code modifié :
javascript

// Dans la boucle pubs.forEach(pub => { ... })
// Remplacez la section qui construit le format APA par :

const title = pub.title_s || "Titre inconnu";
const authors = pub.authFullName_s ? pub.authFullName_s.join(', ') : "Auteurs non renseignés";
const year = pub.producedDateY_i || "";
const venue = pub.journalTitle_s || pub.bookTitle_s || pub.conferenceTitle_s || "";

// Construction des liens HAL et PDF
const halId = pub.halId_s || pub.uri_s; // ID unique du document HAL
const halLink = halId ? `https://hal.science/${halId}` : null;
const pdfLink = halId ? `https://hal.science/${halId}/document` : null;

// Format APA avec les liens
const apa = `
  ${authors} (${year}). <em>${title}</em>.
  ${venue ? `<span style="color:#444;">${venue}</span>.` : ""}
  <br>
  ${halLink ? `<a href="${halLink}" target="_blank" style="color:#007acc; margin-right: 15px;">voir sur HAL &gt;&gt;</a>` : ""}
  ${pdfLink ? `<a href="${pdfLink}" target="_blank" style="color:#d9534f;">télécharger pdf</a>` : ""}
`;

Points importants :

    Vous devez ajouter halId_s ou uri_s dans les champs (fl=...) de votre requête API
    Le lien HAL est : https://hal.science/{halId}
    Le lien PDF est : https://hal.science/{halId}/document

2. Votre deuxième question

Vous avez mentionné avoir deux questions mais n'avez inclus que la première. Quelle est votre deuxième question ? 😊

Souhaitez-vous que je vous fournisse le script complet modifié avec ces changements intégrés ?

oui je veux le script complet. Et la dexuoème question est si tu peux m'expliquer tout ce que ce script fait comme si j'étais un etudiant en train d'apprendre
Script HAL avec liens PDF et HAL
Code 

Parfait ! Voici le script complet. Maintenant, laisse-moi t'expliquer ce que fait ce script, étape par étape :
📚 EXPLICATION PÉDAGOGIQUE DU SCRIPT
1. Le but général

Ce script récupère automatiquement les publications d'un chercheur depuis la base de données HAL (archives ouvertes françaises) et les affiche sur une page web, joliment organisées par type de document.
2. Décortiquons ligne par ligne
🔹 Ligne 1-3 : La fonction principale
javascript

async function loadHALPublications() {

    async = cette fonction est asynchrone, elle peut attendre des réponses (comme quand tu commandes une pizza et tu attends qu'elle arrive)
    C'est la "boîte" qui contient tout le code

🔹 Ligne 4-5 : Qui cherche-t-on ?
javascript

const halId = "federzoni-silvia";

    On définit l'identifiant HAL du chercheur (comme un nom d'utilisateur)

🔹 Ligne 6 : L'URL de l'API
javascript

const url = `https://api.archives-ouvertes.fr/search/?q=authIdHal_s:${halId}&fl=...`;

    API = un service qui permet de demander des données à un site web
    q=authIdHal_s:${halId} = cherche toutes les publications de cet auteur
    fl=title_s,authFullName_s,... = liste des champs (informations) qu'on veut récupérer :
        title_s = titre
        authFullName_s = noms des auteurs
        producedDateY_i = année de publication
        halId_s, uri_s = identifiants uniques (nouveaux ajouts pour les liens !)
    pageSize=100 = récupère jusqu'à 100 publications
    sort=producedDateY_i desc = trie par année, du plus récent au plus ancien

🔹 Lignes 9-18 : Le dictionnaire des types
javascript

const typeLabels = {
  ART: "Articles de revue",
  COMM: "Communications",
  ...
};

    C'est comme un traducteur : HAL utilise des codes (ART, COMM...) et on les transforme en noms lisibles

3. Le bloc TRY-CATCH (lignes 20-58)
🔹 Ligne 21-22 : Récupération des données
javascript

const response = await fetch(url);
const data = await response.json();

    fetch(url) = va chercher les données sur internet (comme ouvrir une page web)
    await = attend que les données arrivent
    .json() = transforme les données en format utilisable par JavaScript

🔹 Ligne 23-24 : Trouver l'endroit où afficher
javascript

const container = document.getElementById('hal-publications');
container.innerHTML = '';

    Trouve l'élément HTML avec l'id hal-publications (c'est là qu'on va afficher les résultats)
    Vide son contenu pour repartir de zéro

🔹 Lignes 26-29 : Si aucune publication

Si HAL ne renvoie rien, on affiche un message et on arrête
4. Organisation des publications (lignes 31-37)
javascript

const grouped = {};
data.response.docs.forEach(pub => {
  const type = pub.docType_s || "OTHER";
  if (!grouped[type]) grouped[type] = [];
  grouped[type].push(pub);
});

Analogie : imagine que tu ranges des livres par catégorie (romans, BD, essais...)

    On crée un objet vide grouped
    Pour chaque publication (pub) :
        On regarde son type (article, thèse, etc.)
        Si la catégorie n'existe pas encore, on la crée
        On ajoute la publication dans sa catégorie

Résultat : toutes les publications sont triées par type !
5. Affichage HTML (lignes 39-58)
javascript

for (const [type, pubs] of Object.entries(grouped)) {

    On parcourt chaque catégorie

Pour chaque catégorie :
javascript

const section = document.createElement('section');
section.innerHTML = `<h2>${typeLabels[type] || type}</h2>`;

    On crée une section HTML
    On y met un titre (ex: "Articles de revue")

Pour chaque publication dans la catégorie :
javascript

const title = pub.title_s || "Titre inconnu";
const authors = pub.authFullName_s ? pub.authFullName_s.join(', ') : "Auteurs non renseignés";

    On extrait les infos (titre, auteurs, année...)
    || = "ou bien" (si pas de titre, on met "Titre inconnu")

🆕 Les liens HAL et PDF (lignes 48-50)
javascript

const halId = pub.halId_s || pub.uri_s;
const halLink = halId ? `https://hal.science/${halId}` : null;
const pdfLink = halId ? `https://hal.science/${halId}/document` : null;

    On récupère l'identifiant unique du document
    On construit 2 liens :
        Vers la page HAL
        Vers le PDF direct

Construction du HTML final (lignes 52-58)
javascript

const apa = `...`;

    Construit le texte au format APA avec les liens cliquables
    <br> = retour à la ligne
    target="_blank" = ouvre dans un nouvel onglet

6. Gestion des erreurs (lignes 59-62)
javascript

} catch (error) {
  document.getElementById('hal-publications').innerHTML =
    "<p>❌ Erreur lors du chargement des publications HAL.</p>";

Si quelque chose se passe mal (internet coupé, API en panne...), on affiche un message d'erreur au lieu de planter
7. Lancement automatique (ligne 65)
javascript

document.addEventListener('DOMContentLoaded', loadHALPublications);

    Dès que la page web est chargée, lance automatiquement la fonction
    DOMContentLoaded = "quand le HTML est prêt"

🎯 RÉSUMÉ EN 3 ÉTAPES

    Récupération : Le script demande à HAL toutes les publications d'un chercheur
    Organisation : Il les trie par type (articles, thèses, etc.)
    Affichage : Il génère du HTML joli avec des liens vers HAL et les PDFs

C'est comme un robot bibliothécaire qui va chercher tous tes livres, les range par catégorie et te les présente proprement ! 📖✨

Des questions sur une partie spécifique ?

zst-il possible d'ajouter en haut à droite une barre de recherche qui permet de chercher parmi mes publications  directement sur cette page et aussi pour moi un compteur de combine de fois on telecharge, ou on voit le pdf ou hal  ?

Excellentes idées ! Je vais te créer le script complet avec ces deux fonctionnalités. Cependant, je dois te préciser quelque chose d'important :
⚠️ Important pour le compteur

Le compteur de téléchargements/vues ne peut pas être implémenté directement dans ce script pour une raison technique :

    Pourquoi ? Ce script s'exécute dans le navigateur de chaque visiteur (côté client). Il ne peut pas "se souvenir" des clics entre différentes personnes ou différentes sessions.
    Ce qu'il faudrait : Un serveur/base de données pour stocker les compteurs (comme Google Analytics, ou un backend PHP/Node.js)

💡 Solutions possibles :

    Utiliser l'API HAL qui fournit déjà des statistiques (vues, téléchargements)
    Intégrer un service externe comme Plausible ou Matomo
    Pour un compteur personnel simple, je peux ajouter un système qui compte dans la session du navigateur (mais il se réinitialise à chaque visite)

✅ Ce que je peux faire maintenant :

    ✅ Barre de recherche fonctionnelle en haut à droite
    ✅ Compteur de session (compte les clics pendant que tu es sur la page)
    ✅ Afficher les statistiques HAL si disponibles dans l'API

Voici le script complet avec la barre de recherche :
Script HAL avec liens PDF et HAL
Artéfact interactif ∙ Version 2 

Parfait ! Voici ce que j'ai ajouté :
✅ Nouvelles fonctionnalités
1. 🔍 Barre de recherche en haut

    Recherche en temps réel (pas besoin d'appuyer sur Entrée)
    Cherche dans : titre, auteurs, année, venue (revue/conférence)
    Affiche le nombre de résultats trouvés
    Les sections vides disparaissent automatiquement

2. 📊 Compteur de session

    Vues HAL : compte chaque fois que tu cliques sur "voir sur HAL"
    PDF téléchargés : compte chaque fois que tu cliques sur "télécharger pdf"
    Publications totales : nombre total de publications trouvées

Note importante : Ces compteurs se réinitialisent quand tu fermes/recharges la page (c'est une limitation technique du JavaScript côté client)
🚀 Pour un vrai compteur permanent

Si tu veux des statistiques qui persistent entre les visites, voici les options :
Option 1 : Utiliser les stats HAL natives

HAL fournit déjà des statistiques ! On peut les récupérer via leur API. Veux-tu que je modifie le script pour afficher les vraies stats HAL (vues et téléchargements totaux depuis la publication) ?
Option 2 : Service externe gratuit

    Plausible Analytics (gratuit pour usage personnel)
    Matomo (open source, auto-hébergeable)

Option 3 : Backend simple

Si tu as un serveur PHP/Node.js, je peux te faire un mini-système qui stocke les clics dans un fichier ou une base de données.

Que préfères-tu ? Je peux t'aider à intégrer les vraies statistiques HAL si tu veux ! 📈

oui je prefere que tu vire le compteru perso et que tu affiches les stats hal : par contre du coup il faudrait que tu m'aides à reorganiser la page....  après par contre ça veut dire que je ne saurais pas is les gens telechargent depuis ma page perso ici. On peut ajouter les deux : on affiche les stats hal et on utilise un service externe gratuit ? par ailleurs, je voudrais aussi voir le nb de visites de mon site et j'avais commencé à explorer la piste google analytics, mais ça viendra après, la on parle de la page publication. Si par contre elles sont liée, dis-le moi

Excellentes questions ! Laisse-moi clarifier tout ça :
🎯 Réponses à tes questions
1. Stats HAL vs Stats de ta page

Tu as raison de soulever ce point ! Ce sont deux choses différentes :

    Stats HAL = nombre total de vues/téléchargements sur HAL.science (depuis toujours)
    Stats de ta page = combien de personnes cliquent depuis TON site personnel

2. Google Analytics et tout ça

Oui, c'est lié ! Google Analytics peut faire les deux :

    Visites globales du site (combien de personnes visitent ta page perso)
    Clics sur les liens (combien cliquent sur "voir HAL" ou "télécharger PDF")

💡 Mon conseil : Mettons Google Analytics maintenant, comme ça on règle tout d'un coup !
📋 Plan d'action - Dis-moi ce que tu préfères
Option A : Complet avec Google Analytics (recommandé)

✅ Affiche les stats HAL (vues/téléchargements totaux)
✅ Track les clics depuis ta page avec Google Analytics
✅ Track les visites globales de ton site
❌ Nécessite de créer un compte Google Analytics (gratuit, 5 minutes)
Option B : Stats HAL uniquement (simple)

✅ Affiche les stats HAL
❌ Pas de tracking des clics depuis ta page
❌ Pas de stats de visites du site
Option C : Stats HAL + Service externe simple

✅ Affiche les stats HAL
✅ Utilise Plausible/Matomo (sans Google)
⚠️ Configuration un peu plus technique
🤔 Ma recommandation

Je te suggère l'Option A parce que :

    Google Analytics est gratuit et facile
    Ça répond à TOUS tes besoins (publications + site global)
    Une seule configuration pour tout
    Tu pourras voir des stats détaillées (d'où viennent les visiteurs, quelles publications sont les plus consultées, etc.)

✨ Ce que je peux faire maintenant

Choix 1 : On fait tout de suite avec Google Analytics

    Je te donne les étapes pour créer ton compte (2 minutes)
    Je te fais le code complet avec stats HAL + tracking Google Analytics
    Je réorganise la page comme tu veux

Choix 2 : On fait d'abord les stats HAL, Google Analytics après

    Je crée la page avec stats HAL maintenant
    On ajoute Google Analytics dans un second temps

🎨 Pour la réorganisation de la page

Avant de coder, dis-moi comment tu imagines la mise en page :

Proposition 1 : Stats en haut

[Barre de recherche]
[Stats HAL globales : X vues totales, Y téléchargements]
[Publications...]
```

**Proposition 2 : Stats par publication**
```
[Barre de recherche]
[Publication 1] + [👁️ 245 vues | 📥 89 téléchargements]
[Publication 2] + [👁️ 189 vues | 📥 45 téléchargements]
```

**Proposition 3 : Mix**
```
[Barre de recherche]
[Stats globales]
[Publication 1] + [stats individuelles]

❓ Dis-moi :

    Option A, B ou C ? (je recommande A)
    Mise en page ? (1, 2 ou 3, ou autre idée ?)
    Tu veux que je t'aide avec Google Analytics maintenant ou après ?

Dès que tu me dis, je te fais le code parfait ! 🚀

otpion A par contre la j'e suis sur la page .md pulbiacations donc pour le site global il faudra faire un truc a part dans index.md. pour l'organisation proposition 3 par contre... d'abord les states globales en haut au milieu, après le titre publication.   ensuite la barre de recherche alignée à droite ? sur la meme ligne à gauche le lien vers le CV HAL . pour les stats de chaque publi, aligne-les à droit. voici ma page entière

Parfait ! Je comprends bien. Voici le plan :
📋 Plan d'action
Pour cette page (publications.md) :

    Stats HAL globales en haut au centre (après le titre)
    Barre de recherche à droite + Lien CV HAL à gauche (même ligne)
    Stats individuelles pour chaque publication (alignées à droite)
    Tracking Google Analytics des clics

Pour la page globale (index.md) :

    On fera ça après, séparément (compteur de visites du site)

🚀 Étape 1 : Configuration Google Analytics (2 minutes)

Avant que je te fasse le code, tu dois obtenir ton ID de mesure Google Analytics :
Instructions rapides :

    Va sur analytics.google.com
    Connecte-toi avec ton compte Google
    Clique sur "Commencer à mesurer"
    Crée une propriété (nom : "Mon site perso" ou autre)
    Active "Google Analytics 4"
    Tu obtiendras un ID de mesure qui ressemble à : G-XXXXXXXXXX

→ Dès que tu as cet ID, donne-le moi et je t'intègre tout !
🎨 Aperçu de ce que ça donnera :

# Publications

[Stats globales centrées : 📊 X publications | 👁️ Y vues | 📥 Z téléchargements]

[🔗 CV HAL (gauche)]  ..................  [🔍 Recherche (droite)]

─────────────────────────────────────

## Articles de revue

Auteur (2024). Titre...
Venue.                           [👁️ 245 | 📥 89]
[voir sur HAL >>] [télécharger pdf]

⚠️ Note importante sur les stats HAL

Je dois te prévenir : l'API HAL standard ne fournit pas directement les statistiques de vues/téléchargements dans les résultats de recherche. Il existe plusieurs solutions :
Solution 1 : Stats globales seulement

    Afficher le nombre total de publications
    Peut-être des stats agrégées si disponibles via l'API

Solution 2 : Stats par document (requiert + de requêtes)

    Faire une requête individuelle pour chaque publication pour récupérer ses stats
    ⚠️ Ça peut être lent si tu as beaucoup de publications

Solution 3 : Scraping du CV HAL

    Récupérer les infos depuis ton CV HAL public
    Un peu plus technique

💡 Je te recommande de commencer par la Solution 1 (propre et rapide), et on verra si les stats individuelles sont disponibles.
✅ Ce dont j'ai besoin de toi :

    Ton ID Google Analytics (G-XXXXXXXXXX)
    Confirmation : tu es OK pour commencer avec stats globales + tracking Google Analytics des clics ?
    Question : tu veux que le lien "CV HAL" reste comme maintenant avec le logo, ou juste texte ?

Dès que tu me donnes l'ID Google Analytics, je te code tout ! 🎯

<!-- Google tag (gtag.js) --> <script async src="https://www.googletagmanager.com/gtag/js?id=G-C9VNHM24GR"></script> <script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'G-C9VNHM24GR'); </script> on m'a donné cela

Parfait ! Tu as déjà Google Analytics configuré avec l'ID G-C9VNHM24GR ! 🎉

Maintenant, quelques questions rapides avant de te coder la page complète :
❓ Questions de confirmation :

    Stats individuelles par publication : J'ai vérifié et l'API HAL standard ne donne pas facilement les stats de vues/téléchargements par document. Tu préfères :
        Option A : Stats globales seulement (nombre total de publications) + tracking Google Analytics des clics depuis ta page
        Option B : J'essaie de récupérer les stats individuelles (mais ça peut être lent/complexe)
        Option C : Pas de stats HAL du tout, juste le tracking Google Analytics
    Le lien CV HAL : Tu veux garder le logo + texte comme maintenant, ou juste texte ?
    Placement du code Google Analytics :
        Tu l'as déjà mis dans le <head> de ton site (layout default) ?
        Ou je dois l'inclure dans la page publications ?

💡 Ma recommandation (réponds juste "OK" si ça te va) :

    ✅ Stats globales : Nombre total de publications trouvées
    ✅ Tracking Google Analytics : Chaque clic sur "voir HAL" et "télécharger PDF" sera tracké
    ✅ Lien CV HAL : Garder le logo + texte (c'est joli !)
    ✅ Stats individuelles : On pourra les ajouter plus tard si besoin

Dans Google Analytics, tu pourras voir :

    Combien de personnes visitent ta page publications
    Combien de clics sur "voir HAL"
    Combien de clics sur "télécharger PDF"
    Quelles publications sont les plus consultées

Ça te convient ? Dis-moi "OK" ou précise ce que tu veux modifier ! 🚀

ok
Page Publications complète avec Google Analytics
Code 

Parfait ! Voici ta page complète ! 🎉
✅ Ce qui est inclus :
📊 Stats globales

    Affiche le nombre total de publications trouvées
    Design moderne avec dégradé violet

🔍 Barre de recherche

    À droite, recherche en temps réel
    Affiche le nombre de résultats
    Tracke les recherches dans Google Analytics (tu verras quels termes les gens cherchent)

🔗 Lien CV HAL

    À gauche, avec le logo
    Exactement comme avant

📈 Google Analytics intégré

    Chaque clic sur "voir sur HAL" est tracké
    Chaque clic sur "télécharger PDF" est tracké
    Chaque recherche est trackée
    Tu sauras exactement quelles publications intéressent le plus !

🎯 Ce que tu verras dans Google Analytics :

Dans ton tableau de bord Google Analytics (sous Événements), tu verras :

    view_hal : nombre de clics sur "voir sur HAL"
        Avec le titre de chaque publication
    download_pdf : nombre de clics sur "télécharger PDF"
        Avec le titre de chaque publication
    search : les termes de recherche utilisés
        Avec le nombre de résultats trouvés

📝 Installation :

    Remplace tout le contenu de ton fichier publications.md par le code de l'artifact
    Assure-toi que le code Google Analytics que tu m'as donné est bien dans le <head> de ton layout default
    Publie et teste !

🔮 Pour aller plus loin (optionnel) :

Si tu veux voir les stats en temps réel pendant que tu testes :

    Va sur analytics.google.com
    Clique sur "Temps réel" dans le menu
    Ouvre ta page publications
    Clique sur quelques liens → tu les verras apparaître immédiatement ! 🎊

Des questions ou tu veux que j'ajuste quelque chose ? 🚀

non dans mon default je n'avais pas google analytics. Il faut que j'y colle le script de tout à l'heure ?

Oui, exactement ! 👍
📝 Ce qu'il faut faire :
Étape 1 : Ouvre ton fichier _layouts/default.html
Étape 2 : Ajoute ce code dans le <head>

Trouve la balise <head> et colle ce code juste après (ou avant la fermeture </head>) :
html

<!-- Google tag (gtag.js) -->
<script as


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

