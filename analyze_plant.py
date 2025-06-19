import openai
import base64
import os

# === Konfiguration ===
OPENAI_API_KEY = "dein-openai-api-key"
BILD_DATEIPFAD = "plant.jpg"  # oder ein Snapshot deiner Kamera

# === OpenAI Setup ===
openai.api_key = OPENAI_API_KEY

# === Bild einlesen und Base64 enkodieren ===
def bilde_base64(pfad):
    with open(pfad, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# === Bildanalyse mit GPT Vision ===
def pflanzenanalyse(image_path):
    image_base64 = bilde_base64(image_path)

    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text":
                     "Analysiere dieses Pflanzenbild. Sieht die Pflanze gesund aus? Braucht sie Wasser, Dünger oder Pflege? Gib eine klare Empfehlung."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
                ]
            }
        ],
        max_tokens=500
    )

    return response['choices'][0]['message']['content']

# === Hauptfunktion ===
if __name__ == "__main__":
    if not os.path.exists(BILD_DATEIPFAD):
        print("❌ Bilddatei nicht gefunden.")
    else:
        print("📷 Pflanze wird analysiert …")
        ergebnis = pflanzenanalyse(BILD_DATEIPFAD)
        print("\n🪴 Ergebnis der Analyse:\n")
        print(ergebnis)
