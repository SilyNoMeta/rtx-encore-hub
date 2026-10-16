<img src="../assets/logo.png" alt="Logo RTX Encore Hub" width="80" height="80">

# Utiliser RTX Encore Hub

[English](USER-GUIDE.md) · [简体中文](USER-GUIDE.zh-CN.md) · [Retour au projet](../README.fr.md)

RTX Encore Hub installe [RTX Encore](https://github.com/SilyNoMeta/rtx-encore) dans vos jeux, tient à jour le mod et les DLL NVIDIA, vérifie qu'un jeu démarre bien avec, et sait toujours revenir en arrière. L'interface suit la langue de Windows : français, anglais ou chinois simplifié ; les autres langues utilisent l'anglais. Ce guide reprend les libellés français de l'application.

## Installer le Hub

Téléchargez `RTX-Encore-Hub-Setup-<version>.exe` depuis la page des publications et lancez-le. Il s'installe pour votre compte seulement, **sans droits d'administrateur**, dans `%LOCALAPPDATA%\Programs\RTX Encore Hub`. Rien d'autre n'est à installer avant.

L'installateur n'est pas signé : Windows peut afficher un avertissement SmartScreen au premier lancement. Chaque publication donne le SHA-256 de son installateur ; comparez-le si vous voulez être sûr du fichier.

Le Hub cherche ses propres mises à jour à son démarrage, puis une fois par jour. **Mises à jour** montre la nouvelle version et ses notes ; **Mettre à jour et relancer** télécharge l'installateur, vérifie son empreinte, l'exécute et relance le Hub. Vous pouvez remettre à plus tard, ou ignorer une version. Une mise à jour attend la fin d'une installation en cours dans un jeu. Vos réglages et vos sauvegardes ne sont jamais touchés par une mise à jour ni par une désinstallation.

**Version portable.** `RTX-Encore-Hub-Portable-<version>.zip` n'installe rien : décompressez-la dans un dossier où vous pouvez écrire (pas sous Program Files) et lancez `rtx-encore-hub.exe`. Le fichier `portable.txt` à côté fait garder au Hub tout ce qu'il écrit dans le dossier `data` voisin, sauvegardes comprises : gardez ce dossier. La version portable ne se met pas à jour elle-même : **Télécharger la version portable**, dans **Mises à jour**, ouvre la page de la publication ; fermez le Hub, puis remplacez `rtx-encore-hub.exe` et `encorehub-elevated.exe` par ceux de la nouvelle archive.

## Retrouver vos jeux

**Bibliothèque** réunit les jeux de Steam, Epic et GOG installés sur la machine. Pour les autres :

- **Paramètres → Dossiers de jeux → Ajouter un dossier…** : chaque sous-dossier qui contient un exécutable reconnu devient un jeu ;
- **Ajouter un jeu** : désignez directement l'exécutable d'un jeu.

Le mod va à côté du programme qui dessine le jeu : derrière un lanceur (The Witcher 3 de GOG démarre `REDprelauncher.exe`), le Hub prend le jeu que le lanceur démarre ; derrière RTX Remix, le mod va à côté de `NvRemixBridge.exe`, dans le dossier `.trex` du jeu.

Une tuile dit l'état du jeu par un pictogramme et un mot : non installé, installé, à mettre à jour, modifié par le jeu, en échec. La recherche (`Ctrl+F`) ignore les accents et la ponctuation ; un filtre limite la liste à une API graphique ; `F5` relit les dossiers. Le volet rappelle votre machine : carte, mémoire, pilote, écran.

## Lire la fiche d'un jeu

Choisissez une tuile.

- **Ce qui est possible ici** dit, pour la génération d'images, DLSS Super Resolution, Smooth Motion et Neural Rendering, si la fonction est possible sur votre carte et votre pilote, et sinon pourquoi. C'est déduit des fichiers et du pilote : ce n'est pas une preuve en jeu.
- **DLL NVIDIA** compare, DLL par DLL, la version du jeu, la meilleure copie déjà sur la machine et ce que le Hub propose. Une DLL absente de la machine est téléchargée : DLSS, Ray Reconstruction et la génération d'images depuis le dépôt officiel de NVIDIA sur GitHub, la DLL de Neural Rendering depuis le compartiment du projet. **Une DLL n'est acceptée qu'avec une signature NVIDIA valide** ; celle de Neural Rendering doit en plus être exactement le build que le mod attend.
- **La version la plus récente, d'office** : pour une DLL que le jeu a déjà, le Hub prend la version la plus récente que le RTX Encore du jeu admet, comme le font les mises à jour de NVIDIA elles-mêmes. La version qu'il proposait jusque-là reste au choix sous la même ligne (« Prendre … en … plutôt que la version proposée »), et chaque case reste la vôtre. Une DLL plus récente dans le jeu n'est jamais ramenée en arrière. Le lot DLSS 310.9.16 de la bêta de l'application NVIDIA est préparé ainsi : il est pris d'office avec RTX Encore 1.0.0-rc.1 ou plus récent ; avec une bêta du mod, c'est la 310.9.1. La génération d'images 310.9.16 est la seule à accepter le preset C, la composition Lite : plus rapide, avec des compromis d'image, sans protection anti-déchirure ni recomposition d'interface.
- **Plugins Streamline** : pour un jeu qui utilise Streamline, le Hub remplace ses plugins par ceux de la version la plus récente que le RTX Encore du jeu admet (« Passer les plugins Streamline en … », coché d'office). Ils se prennent tous ensemble, jamais un par un. L'interposer du jeu (`sl.interposer.dll`) n'est jamais remplacé, comme dans les mises à jour de NVIDIA elles-mêmes ; la fiche dit sa version et vous prévient quand elle diffère de celle des plugins pris. La 2.14.1 vient du SDK de production de NVIDIA ; la 2.14.16, de la bêta de l'application NVIDIA, est prise avec RTX Encore 1.0.0-rc.1 ou plus récent.
- **Choisir une fois pour tous les jeux** : dans **Paramètres → Par défaut à l'installation**, vous dites ce que le Hub prend d'office : la version des plugins Streamline, celle de DLSS, de Ray Reconstruction et de la génération d'images (« la plus récente que le mod admet », « ne pas remplacer », ou une version), et vos presets DLSS. Chaque fiche part de ces choix et vous laisse les changer pour ce jeu. Un preset choisi ainsi n'est écrit que dans un jeu qui n'a pas déjà le sien, et seulement si ses DLL le prennent ; la fiche le dit par la case « Écrire vos presets par défaut ».
- **Ce que vous décochez dans un jeu y reste laissé de côté** : une DLL NVIDIA, les plugins Streamline ou vos presets par défaut décochés sur la fiche d'un jeu sont retenus pour ce jeu. La fiche le rappelle, « Tout mettre à jour » n'y touche pas, et recocher la case le reprend.
- **Modèle DLSS Super Resolution** : le Hub peut écrire le modèle choisi dans le profil de pilote du jeu, comme les outils de NVIDIA. Tant que son effet n'a pas été constaté en jeu sur votre pilote, la fiche dit « non confirmé en jeu ».
- **Réglages de départ** : une proposition pour votre carte. Le multiplicateur de génération d'images est, par défaut, celui que le jeu décide ; ×2, ×3 et ×4 sont au choix.
- **Nom du proxy** : le nom sous lequel le jeu charge le mod (`version.dll`, `dxgi.dll`, `winmm.dll`, `dinput8.dll`). Pour chacun, la fiche dit si le jeu le chargera et pourquoi : ce que son exécutable importe, un correctif de compatibilité que Windows applique au jeu, un autre outil déjà présent, ce qui s'est passé au dernier lancement, et ce que disent les profils de la communauté. Le nom recommandé en découle ; vous pouvez passer à un autre en une opération, annulable comme les autres. Dans un jeu doté d'un chargeur ASI, le mod peut aussi être un plugin, `rtx-encore.asi`. Un outil déjà présent sous un nom n'est jamais écrasé. Un mode de compatibilité que Windows applique au jeu se retire depuis sa fiche, pour votre compte et, après la demande des droits d'administrateur par Windows, pour tous les comptes ; le Hub note ce qu'il a retiré, et **Remettre** le rétablit tel qu'il était.

**Anti-triche.** Quand le Hub reconnaît un anti-triche (EasyAntiCheat, BattlEye…), la tuile et la fiche le nomment. Votre compte peut être banni, ou le mod peut ne pas se charger : rien n'est écrit dans ce jeu avant que vous ayez accepté ce risque dans la fenêtre de validation. La détection repose sur des fichiers connus et peut manquer une protection.

## Installer ou mettre à jour

Le bouton principal de la fiche ouvre un assistant en trois étapes.

1. **Inspection** : ce que le jeu contient, ce que votre machine permet.
2. **Ce qui va être écrit** : la liste exacte, avec ce qui est là maintenant et ce qui y sera. Rien n'est encore écrit. Chaque fichier remplacé est sauvegardé d'abord, hors du dossier du jeu.
3. **Vérification au lancement**, si vous laissez la case cochée.

Une installation est tout ou rien : si une écriture échoue, tout est remis en place. Si le Hub est arrêté en plein milieu (coupure, plantage), il annule l'installation interrompue à son prochain démarrage, avant toute autre chose, et vous le dit.

Si le dossier du jeu refuse l'écriture à votre compte, Windows demande les droits d'administrateur **pour cette opération seulement**. Ce n'est pas le Hub qui les reçoit, mais un petit programme qui n'applique que le plan que vous venez d'accepter et revérifie chaque fichier.

**Tout mettre à jour**, dans la bibliothèque, met à jour le mod dans tous les jeux qui en portent une copie plus ancienne. Avec la case « Mettre aussi à jour les DLL NVIDIA et les plugins Streamline », cochée d'office, chaque jeu reçoit en même temps ce que sa fiche prend d'office : les versions choisies dans **Paramètres → Par défaut à l'installation**, et vos presets par défaut là où le jeu n'a pas les siens. Un jeu dont un fichier NVIDIA ne peut pas venir a quand même son mod mis à jour, et l'écran le nomme. Chaque jeu a sa propre transaction, et « Restaurer le jeu » sur sa fiche remet tout comme avant ; les jeux avec anti-triche sont laissés de côté.

## Vérifier qu'un jeu démarre bien

**Lancer le jeu**, en haut de la fiche d'un jeu, le démarre comme son lanceur le ferait, sans rien observer.

**Santé → Lancer et vérifier** démarre le jeu et l'observe pendant sa première minute : le processus tient-il, le mod s'est-il chargé, que dit son journal. Le résultat tient en une phrase, « Tout va bien », ou la cause en clair, puis en constats : carte et architecture reconnues, pilote reconnu ou non, modules acceptés, Neural Rendering prêt ou non. Quand le jeu a pris un autre fichier sous le nom du mod, ou ne l'a jamais demandé, la page le dit et propose le nom vers lequel passer ; elle prévient aussi quand l'ancien mod dlssg_for_sm86 est encore chargé dans le jeu.

Si le jeu s'arrête dans la première minute ou si le mod ne se charge pas, la page propose de **restaurer** l'état d'avant en un clic. Après deux échecs de suite sur la même installation, c'est le bouton principal. **Préparer un diagnostic** fait une archive de fichiers texte, sans votre nom d'utilisateur ni celui de la machine, à relire puis à joindre vous-même à un ticket : le Hub n'envoie rien.

Cette vérification dit qu'un jeu démarre et que le mod s'y charge. Elle ne juge ni l'image ni les performances.

## Revenir en arrière

**Sauvegardes de ce jeu**, sur la page Santé, liste chaque opération du Hub, datée. Vous pouvez revenir à l'état d'avant une opération, ou d'avant toute intervention du Hub (**Restaurer le jeu**).

Un fichier que le jeu, son lanceur ou un autre outil a changé depuis n'est jamais écrasé : il est laissé tel quel et signalé. Le fichier de réglages `rtx-encore.jsonc` est le vôtre : s'il a changé depuis, le Hub vous demande avant de le remettre.

Une copie du mod posée à la main est reconnue, mais le Hub n'a de sauvegarde d'origine que pour ce qu'il a lui-même écrit.

## Quand le jeu se met à jour

Si une mise à jour ou une réparation du jeu a remplacé des fichiers de l'installation, la fiche le dit : **Le jeu a modifié l'installation**.

- **Réappliquer** réécrit le mod s'il manque, et les DLL NVIDIA dont le Hub a encore une meilleure copie. Une DLL que le jeu a apportée plus récente est gardée.
- **Oublier** garde les fichiers du jeu tels quels et cesse de les suivre.

## Régler le mod

**Tous les réglages de ce jeu** édite `rtx-encore.jsonc` par un formulaire qui reprend les sections du fichier. Chaque réglage porte son explication, sa valeur par défaut et, s'il y a lieu, « redémarrage nécessaire ». Un réglage sans effet sur votre carte est grisé, avec la raison. Les presets DLSS suivent les DLL du jeu : le formulaire ne propose que ceux que la DLL installée prend, et dit pourquoi les autres manquent ; le preset C de génération d'images, par exemple, n'existe que dans DLSS-G 310.9.16. Les commentaires et les clés que le Hub ne connaît pas sont gardés tels quels.

Un jeu qui se ferme au lancement avec le menu du mod (Star Wars Outlaws) peut s'en passer : activez `disableInGameMenu` dans Compatibilité, et changez les réglages ici. Quand un jeu se ferme dans sa première minute avec le mod chargé, **Lancer et vérifier** propose **Relancer sans le menu en jeu**, qui le fait pour vous.

Rien n'est écrit avant que vous ayez vu les changements. Le dernier changement s'annule d'un bouton. **Profils de ce jeu** enregistre les réglages en vigueur sous un nom, et y revient en un clic.

## Profils de la communauté

La communauté est ouverte depuis la 1.0.0-rc.2. Elle est expérimentale et peu testée, et elle commence vide : les premiers profils seront les vôtres.

- Les profils d'un jeu sont classés **du plus proche de votre machine au plus lointain**, avec la raison : même carte, même définition, pilote plus ancien… Par défaut, seuls les profils faits sur une carte de votre famille sont montrés.
- La page montre d'abord une douzaine de profils ; **Afficher plus de profils** en ajoute. Des **filtres** resserrent la liste : mes profils, même carte, même définition, confirmés par d'autres, officiels, avec mesure, Neural Rendering, Smooth Motion, FG à multiplicateur fixe ou dynamique. Seuls ceux qui départagent les profils sont proposés.
- **Importer** montre d'abord ce qui changerait, section par section. Les raccourcis clavier ne sont pris que si vous le demandez ; les diagnostics, jamais. Vos réglages d'avant sont gardés sous le nom « Avant import », et un bouton remet le fichier exactement comme il était.
- **J'aime**, **Ça marche chez moi** et **Signaler** tiennent en un clic et se retirent.
- **Publier mon profil** : la machine et les versions sont remplies par le Hub ; vous ajoutez le mode DLSS, le niveau de ray tracing, une note. **Tout ce qui part est affiché avant l'envoi, tel qu'il part.** Ni chemin de fichier, ni nom d'utilisateur, ni nom de machine : une note qui en contient est refusée.

Il n'y a pas de compte. Une clé est créée sur votre machine et y reste ; vous choisissez un pseudo.

## Mettre à jour le mod

**Paramètres → D'où vient RTX Encore** : les publications publiques du dépôt RTX Encore, vérifiées par leur SHA-256, ou un dossier local contenant un build du mod. Dans **Mises à jour**, le **canal du mod** se choisit comme celui du Hub : **Stable** ne propose que les versions finales, **Candidat** suit aussi les préversions. Tant que vous n'avez rien choisi, un Hub qui est lui-même une préversion suit le canal candidat, pour lui comme pour le mod. La page dit quelle version du mod chaque jeu porte, et montre les notes de chaque publication.

## Données, réseau et vie privée

Le Hub garde ses réglages, ses téléchargements, ses jaquettes et les sauvegardes de chaque jeu dans `%LOCALAPPDATA%\EncoreHub` (dans `data` à côté de la version portable). Ce dossier est votre retour arrière : ne le supprimez pas tant que des jeux portent une installation du Hub.

Le Hub contacte, sans compte et sans rien envoyer de vous :

- GitHub, pour les publications du mod, celles du Hub, et les DLL de NVIDIA ;
- `encore-dl.nometa.fr`, pour la DLL de Neural Rendering, une version au choix quand vous la prenez, la liste des sources, et les profils de la communauté quand vous ouvrez sa page ;
- `encore-community.nometa.fr`, seulement quand vous publiez, retirez, aimez, confirmez ou signalez un profil : ce que vous avez relu, signé par la clé de votre machine. Pour couper la communauté, mettez `"Community": "off"` dans `%LOCALAPPDATA%\EncoreHub\settings.json` ;
- Steam et Wikipédia, pour les jaquettes qui manquent : le titre du jeu leur est envoyé. **Paramètres → Jaquettes** coupe cette recherche.

Il n'y a aucune télémétrie.

## Clavier et lecteur d'écran

Tout se fait au clavier. `Ctrl+F` va à la recherche, `F5` relit les dossiers, `Alt+Gauche` revient en arrière. Chaque état se dit par un mot, pas seulement par une couleur.

## Un problème ?

Ouvrez un [ticket](https://github.com/SilyNoMeta/rtx-encore-hub/issues/new/choose) avec la version du Hub, le jeu, le lanceur, la carte, le pilote et les étapes qui reproduisent le problème. Joignez le diagnostic préparé par la page Santé après l'avoir relu.
