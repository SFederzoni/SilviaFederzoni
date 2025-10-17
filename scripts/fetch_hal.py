import requests
import yaml

# === CONFIGURATION ===
# Remplace par ton identifiant HAL exact (visible sur tes dépôts HAL)
HAL_ID = "silvia-federzoni"

# === RÉCUPÉRATION DES PUBLICATIONS VIA L'API HAL ===
url = f"https://api.archives-ouvertes.fr/search/?q=authIdHal_s:{HAL_ID}&fl=title_s,authFullName_s,producedDateY_i,linkExtUrl_s,docType_s,journalTitle_s,conferenceTitle_s&rows=1000"
response = requests.get(url)
data = response.json()

# === CONVERSION DES DONNÉES EN FORMAT YAML SIMPLE ===
publications = []
for d in data.get("response", {}).get("docs", []):
    pub = {
        "title": d.get("title_s", [""])[0],
        "authors": ", ".join(d.get("authFullName_s", [])),
        "year": d.get("producedDateY_i", ""),
        "link": d.get("linkExtUrl_s", [""])[0],
    }

    # Ajout de la source (journal ou conférence)
    if "journalTitle_s" in d:
        pub["source"] = d["journalTitle_s"][0]
    elif "conferenceTitle_s" in d:
        pub["source"] = d["conferenceTitle_s"][0]

    publications.append(pub)

# === ÉCRITURE DU FICHIER YAML ===
with open("_data/publications.yml", "w", encoding="utf-8") as f:
    yaml.dump(publications, f, allow_unicode=True, sort_keys=False)

print(f"{len(publications)} publications HAL enregistrées ✅")
