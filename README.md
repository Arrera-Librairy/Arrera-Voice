# Arrera Voice

La bibliothèque Arrera Voice est une librairie qui permet de faire de la synthèse vocale en français. Elle est basée sur le moteur de synthèse vocale de Google et permet également de réaliser de la reconnaissance vocale, toujours en utilisant le moteur de Google. Elle propose aussi un système de détection de mots-clés (trigger word).

## Installation

Telechargez le fichier `arrera_voice.py` et placez-le dans le même dossier que votre script python. Et importer le dans votre code

```python
from arrera_voice import*
```

Oublier pas de le telecharger les modules necessaires en utilisant la commande suivante:

```bash
pip install -r requirements.txt
```
Ecrire le fichier le json de configuration `config.json` dans le meme dossier que votre script python. Le fichier doit contenir les informations suivantes:

```json
{
  "soundMicro": "1",
  "fileMicro": "conf/bootMicro.mp3",
  "listWord": ["six","copilote","assistant"]
}
```
### Explication des paramètres du fichier de configuration

- `"soundMicro"` : permet de définir si le son du micro doit être activé ou non. Si la valeur est égale à "1", le son du micro est activé, sinon il est désactivé.
- `"fileMicro"` : permet de définir le fichier audio qui sera joué lorsque le micro est activé.(Le fichier doit être au format mp3)
- `"listWord"` : permet de définir la liste des mots-clés qui seront utilisés pour la détection de mots-clés.(Maximun 3 mots-clés)

## Utilisation

### Synthèse vocale

Pour faire de la synthèse vocale, il suffit d'appeler la fonction `say()` en passant en paramètre le texte à synthétiser.

```python
from arrera_voice import*

av = ArreraVoice()
av.say("Bonjour, comment ça va?")
```

### Lecture d'un fichier audio

Pour lire un fichier audio, il suffit d'appeler la fonction `playFile()` en passant en paramètre le chemin du fichier audio.

```python
from arrera_voice import*
av = ArreraVoice()
av.playFile("audio.mp3")
```

### Reconnaissance vocale

Pour faire de la reconnaissance vocale, il suffit d'appeler la fonction `listen()` et la methode `getTextMicro()`.

```python
from arrera_voice import*
av = ArreraVoice()
sortieMicro = av.listen()

if sortieMicro == 0:
    print("Vous avez dit: " + av.getTextMicro())
```

### Détection de mots-clés

Pour faire de la détection de mots-clés, il suffit d'appeler la fonction `triggerWord()`.

```python
from arrera_voice import*
av = ArreraVoice()
sortie = av.triggerWord()
```

La méthode `triggerWord()` retourne `1` si un mot-clé est détecté, sinon elle retourne `-3` s'il y a un problème avec les mots-clés paramétrés.