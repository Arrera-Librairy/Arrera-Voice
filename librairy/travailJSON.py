import json


class jsonWork:
    def __init__(self, file):
        self.fichier = file

    def getContenuJSON(self):
        """
        Retourne un dictionnaire un json
        :return : contenu du fichier json complet
        """
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            dict = json.load(openfile)
        return dict

    def lectureJSON(self, flag):
        """
        Lire un flag du fichier json
        :param flag: Flag qui contient la valeur que vous voulez lire
        :return: Contenu du flag
        """
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            dict = json.load(openfile)[flag]
        return str(dict)

    def lectureJSONMultiFlag(self, flag1, flag2):
        """
         Lire un flag qui se trouve un un dictionnaire stoker dans le JSON
        :param flag1: Flag ou se trouve le dictionnaire secondaie
        :param flag2: Flag ou se trouve la valeur
        :return: Valeur contenu du flag
        """
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            dict = json.load(openfile)[flag1][flag2]
        return str(dict)

    def lectureJSONList(self, flag):
        """
         Lire un flag qui contient une liste
        :param flag: Flag ou se trouve la liste que vous voulez lire
        :return: retourne La liste
        """
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            liste = json.load(openfile)[flag]
        return list(liste)

    def lectureJSONDict(self, flag):
        """
        Lire un flag qui contient un dictionnaire
        :param flag: Flag ou se trouve le dictionnaire que vous voulez lire
        :return: Retourne le dictionnaire
        """
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            dictionnaire = json.load(openfile)[flag]
        return dict(dictionnaire)

    def EcritureJSON(self, flag, valeur):  # Permet d'ecrire une nouvelle valeur a flag definie
        """
        Ecrire une valeur dans un flag choisi
        :param flag: Flag ou vous voulez ecrire votre valeur
        :param valeur: Valeur que vous voulez ecrire
        """
        openfile = open(self.fichier, 'r', encoding='utf-8')
        dict = json.load(openfile)
        openfile.close()
        writeFile = open(self.fichier, 'w', encoding='utf-8')
        dict[flag] = valeur
        json.dump(dict, writeFile, indent=2)

    def EcritureJSONList(self, flag, valeur: list):
        """
        Ecrire une liste dans le flag choisie
        :param flag: Flag ou vous voulez ecrire votre liste
        :param valeur: liste que vous voulez ecrire
        """
        # Chargez le fichier JSON
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            data = json.load(openfile)
        # Vérifiez si le champ (flag) existe et est une liste
        if flag in data and isinstance(data[flag], list):
            # Ajoutez la nouvelle valeur à la liste
            data[flag].append(valeur)
            # Écrivez le fichier JSON mis à jour
            with open(self.fichier, 'w', encoding='utf-8') as writeFile:
                json.dump(data, writeFile, indent=2)

    def EcritureJSONDictionnaire(self, flag, cle, valeur):
        """
        Ecrire un dictionnaire dans le flag choisie
        :param flag: Flag ou vous voulez ecrire votre dictionnaire
        :param cle: Cles de votre dictionnaire
        :param valeur: Valeur que vous voulez erire dans dictionnaire a cette cles
        """
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)

        if flag in data and isinstance(data[flag], dict):
            data[flag][cle] = valeur  # Met à jour le dictionnaire
            with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                json.dump(data, fichier_modifie, indent=2)

    def supprJSONDict(self, flag, cle):
        """
         Supprimer un cles choisi dans dictionnaire stoker dans un JSON
        :param flag: Flag ou se trouve le dictionnaire
        :param cle: Cle du dictionnaire que vous voulez supprimer
        """
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)

        if flag in data and isinstance(data[flag], dict):
            if cle in data[flag]:
                del data[flag][cle]  # Supprime la clé spécifiée du dictionnaire
                with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                    json.dump(data, fichier_modifie, indent=2)

    def suppressionJson(self, flag: str):
        """
        Supprimer la valeur du flag selectionner
        :param flag: Flag ou vous voulez supprimer la valeur
        """
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)
        if flag in data:
            data[flag] = ""  # Supprime le champ spécifié
            with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                json.dump(data, fichier_modifie, indent=2)

    def suppressionJsonList(self, flag, valeur):
        """
        Supprimer un valeur dans un liste stoker dans un JSON
        :param flag: Flag ou se touve la liste
        :param valeur: valeur de la liste que vous voulez supprimer
        """
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)
        if flag in data and isinstance(data[flag], list):
            liste = data[flag]

            if valeur in liste:
                liste.remove(valeur)  # Supprime la valeur spécifiée de la liste
                with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                    json.dump(data, fichier_modifie, indent=2)

    def compteurFlagJSON(self):
        """
        Retourne le nombre de flag que contient le JSON
        :return: retourne le nombre de flag présent de le fichier json
        """
        openfile = open(self.fichier, 'r', encoding='utf-8')
        dict = json.load(openfile)
        openfile.close()
        return len(dict)

    def supprDictReorg(self, flag):
        """
        Supprimer un flag du fichier JSON tout en reoganisant le fichier
        :param flag: Flag que vous voulez supprimer
        """
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            dict = json.load(openfile)
            del dict[flag]
            newDict = {}
            newKey = 0
            for cle in sorted(dict.keys(), key=lambda x: int(x)):
                newDict[str(newKey)] = dict[cle]
                newKey += 1
            writeFile = open(self.fichier, 'w', encoding='utf-8')
            json.dump(newDict, writeFile, indent=2)
            writeFile.close()

    def creerFlagDictionnaire(self, flag):
        """
        Creation d'un dictionnaire dans sun flag choisi du fichier json
        :param flag: Flag que vous voulez crée
        :return:
        """
        # Lecture du fichier JSON
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)

        # Vérification et création du flag
        if flag not in data or not isinstance(data[flag], dict):
            data[flag] = {}
            # Écriture des modifications dans le fichier JSON
            with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                json.dump(data, fichier_modifie, indent=2)

    def ajouterFlagDict(self, flag, cle, valeur):
        """
        Ajouter une cles dans un flag qui contien un dictionnaire
        :param flag: Flag du nouveau dictionnaire
        :param cle: cle de valeur contenu dans ce nouveau dictionnaire
        :param valeur: Valeur de cette cle
        """
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)

        # Vérification que le flag existe et est un dictionnaire
        if flag in data and isinstance(data[flag], dict):
            data[flag][cle] = valeur  # Ajout de la nouvelle clé-valeur

            # Écriture des modifications dans le fichier JSON
            with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                json.dump(data, fichier_modifie, indent=2)

    def supprDictByFlag(self, flag, name):
        """
         Supprimer un valeur avec sa cles dans un dictionnaire stoker dans le JSON juste avec la valeur
        :param flag: Flag du dictionnaire
        :param name: Valeur de la cles que vous voulez supprimer
        """
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)

        for key, value in data.items():
            if value.get(flag) == name:
                self.supprDictReorg(key)

    def writeDictOnJson(self, dict: dict):
        """
        ECrire un dictionnaire python dans le fichier json
        :param dict: Dictionnaire que vous voulez ecrire dans votre fichier json
        """
        with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
            json.dump(dict, fichier_modifie, indent=2)