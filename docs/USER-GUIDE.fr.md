<img src="../assets/logo.png" alt="Logo RTX Encore Hub" width="80" height="80">

# Utiliser RTX Encore Hub

[English](USER-GUIDE.md) · [简体中文](USER-GUIDE.zh-CN.md) · [Retour au projet](../README.fr.md)

RTX Encore Hub installe [RTX Encore](https://github.com/SilyNoMeta/rtx-encore) dans vos jeux, tient à jour le mod et les DLL NVIDIA, vérifie qu'un jeu démarre bien avec, et sait toujours revenir en arrière. L'interface suit la langue de Windows : français, anglais ou chinois simplifié ; les autres langues utilisent l'anglais. Ce guide reprend les libellés français de l'application.

## Utiliser la 1.2.2

**XeSS / XeFG : TRÈS EXPÉRIMENTAL.** Cette intégration a été particulièrement pénible à mettre au point :) Attendez-vous à des bugs, crashs, artefacts et différences entre jeux et API graphiques. N’hésitez pas à remonter les problèmes : dans RTX Encore Hub, ouvrez la page **Santé** du jeu, choisissez **Préparer un diagnostic**, relisez l’archive pour retirer les informations personnelles, puis joignez-la à une [issue RTX Encore](https://github.com/SilyNoMeta/rtx-encore/issues/new/choose). Indiquez les moteurs choisis, l’API graphique et le multiplicateur demandé. Le Hub ne téléverse pas l’archive à votre place.

La version stable 1.2.2 est disponible sur le canal Stable. Le canal Candidat inclut aussi les préversions.

Les réglages Intel, d’entrée commune et de NR par passe demandent le mod 1.2.0-beta.1 ou ultérieur. Le mod 1.2.2 n’utilise plus la politique des fournisseurs NVIDIA : le Hub la masque ; les anciens mods conservent leurs contrôles compatibles. XeFG reste expérimental et dépend du mod, de l’API graphique, du jeu et du runtime. Un multiplicateur demandé ne prouve pas les images affichées.

### Moteurs Intel et dépendances

Avec RTX Encore 1.2, choisissez la reconstruction XeSS ou la génération d’images XeFG là où le mod les prend en charge. Le Hub installe et vérifie les fichiers Intel et leur licence avec le mod ; ils sont sauvegardés et restaurés dans la même opération. Leur présence ne prouve pas qu’un moteur est actif.

### Neural Rendering, passe par passe

Pour chacune des quatre passes possibles, réglez l’intensité, le ton local, la structure locale, la structure de peau et le masque de personnage, ou suivez le réglage global. Une intensité à zéro laisse la passe tourner et ne supprime pas son coût.

Depuis RTX Encore 1.2.0-beta.1, NR peut aussi fonctionner après Ray Reconstruction dans les jeux Direct3D 12 compatibles qui fournissent une profondeur linéaire. Direct3D 11 et Vulkan ne prennent toujours pas en charge ce cas. Un essai local dans 007 First Light en path tracing confirme que NR fonctionne ; la qualité d’image et le coût n’ont pas été mesurés. Le crash intermittent au démarrage reste non résolu.

### Entrée HDR et exposition

Les réglages communs `srHdr` et `srAutoExposure` suivent le moteur de reconstruction choisi. Ils suivent le jeu par défaut et demandent un redémarrage. L’entrée HDR n’active pas le HDR de l’écran et ne convertit pas une image SDR en HDR.

Laissez les deux réglages sur `game` si le format d’entrée du jeu est inconnu. Une entrée HDR incorrecte peut dégrader l’image. L’exposition automatique peut aider le ghosting lié à l’exposition, sans être une correction générale ; certains modèles DLSS l’imposent. Celle de XeSS a un coût GPU et est déconseillée en LDR. XeSS Vulkan avec entrée LDR et exposition manuelle reste non pris en charge. Ray Reconstruction et la génération d’images restent inchangés.

La politique des fournisseurs reste locale et ne concerne que les anciens mods qui l’utilisent. RTX Encore 1.2.2 ignore une ancienne entrée `providerPatchPolicy`. La compatibilité NVIDIA ne demande plus de liste de versions prédéfinie ; les contrôles Intel restent inchangés. Ces contrôles de politique ne sont pas partagés dans les profils communautaires.

Avec XeFG, changer la limite FPS demande un redémarrage du jeu. L’espacement variable des images aux multiplicateurs XeFG élevés est expérimental. Une limite FPS ne prouve pas la cadence des images source.

[Notes de version](notes/1.2.2.fr.md) · [Notes de la 1.2.0-beta.1](notes/1.2.0-beta.1.fr.md)

## Installer le Hub

Téléchargez `RTX-Encore-Hub-Setup-<version>.exe` depuis la page des publications et lancez-le. Il s'installe pour votre compte seulement, **sans droits d'administrateur**, dans `%LOCALAPPDATA%\Programs\RTX Encore Hub`. Rien d'autre n'est à installer avant.

L'installateur n'est pas signé : Windows peut afficher un avertissement SmartScreen au premier lancement. Chaque publication donne le SHA-256 de son installateur ; comparez-le si vous voulez être sûr du fichier.

Le Hub cherche ses propres mises à jour à son démarrage, puis une fois par jour. **Mises à jour** montre la nouvelle version et ses notes ; **Mettre à jour et relancer** télécharge l'installateur, vérifie son empreinte, l'exécute et relance le Hub. Vous pouvez remettre à plus tard, ou ignorer une version. Une mise à jour attend la fin d'une installation en cours dans un jeu. La mise à jour ou désinstallation du programme installé conserve vos réglages et données de restauration.

**Version portable.** `RTX-Encore-Hub-Portable-<version>.zip` n'installe rien : décompressez-la dans un dossier où vous pouvez écrire (pas sous Program Files) et lancez `rtx-encore-hub.exe`. Le fichier `portable.txt` à côté fait garder au Hub son état dans le dossier `data` voisin : gardez ce dossier. Les sauvegardes des originaux et de l’historique sont partagées dans ce dossier de données : gardez-le lors d’un déplacement ou d’une mise à jour du Hub portable. La version portable ne se met pas à jour elle-même : **Télécharger la version portable**, dans **Mises à jour**, ouvre la page de la publication ; fermez le Hub, puis remplacez `rtx-encore-hub.exe` et `encorehub-elevated.exe` par ceux de la nouvelle archive.

## Retrouver vos jeux

**Bibliothèque** réunit les jeux de Steam, Epic et GOG installés sur la machine. Pour les autres :

- **Paramètres → Dossiers de jeux → Ajouter un dossier…** : chaque sous-dossier qui contient un exécutable reconnu devient un jeu ;
- **Ajouter un jeu** : désignez directement l'exécutable d'un jeu.

Le mod va à côté du programme qui dessine le jeu : derrière un lanceur (The Witcher 3 de GOG démarre `REDprelauncher.exe`), le Hub prend le jeu que le lanceur démarre ; derrière RTX Remix, le mod va à côté de `NvRemixBridge.exe`, dans le dossier `.trex` du jeu.

Une tuile dit l'état du jeu par un pictogramme et un mot : non installé, installé, à mettre à jour, modifié par le jeu, en échec. La recherche (`Ctrl+F`) ignore les accents et la ponctuation ; un filtre limite la liste à une API graphique ; `F5` relit les dossiers. Le volet rappelle votre machine : carte, mémoire, pilote, écran.

Lorsque la fiche hésite sur l’exécutable du jeu, relisez les programmes proposés et choisissez le jeu lui-même. Vous pouvez ensuite rendre le choix automatique. La recherche globale de la barre de titre retrouve également les jeux de votre bibliothèque.

## Lire la fiche d'un jeu

Choisissez une tuile.

- **Ce qui est possible ici** dit, pour la génération d'images, DLSS Super Resolution, Smooth Motion et Neural Rendering, si la fonction est possible sur votre carte et votre pilote, et sinon pourquoi. C'est déduit des fichiers et du pilote : ce n'est pas une preuve en jeu.
- **DLL NVIDIA** compare, DLL par DLL, la version du jeu, la meilleure copie déjà sur la machine et ce que le Hub propose. Une DLL absente de la machine est téléchargée : DLSS, Ray Reconstruction et la génération d'images depuis le dépôt officiel de NVIDIA sur GitHub, la DLL de Neural Rendering depuis le compartiment du projet. **Une DLL n'est acceptée qu'avec une signature NVIDIA valide** ; celle de Neural Rendering doit en plus être exactement le build que le mod attend.
- **Téléchargements NVIDIA actuels** : le catalogue intégré propose DLSS SR, RR, FG et NR 310.9.16, ainsi que les plugins Streamline 2.14.16. Lorsqu’un fichier demande un mod plus récent, le Hub l’explique au lieu de proposer un ancien téléchargement. Une DLL plus récente déjà dans le jeu est conservée. Le preset FG C demande une 310.9.16 compatible ; la composition Lite a des compromis d’image et n’utilise ni les réglages de protection normaux ni la recomposition d’interface.
- **Plugins Streamline** : ils sont pris ensemble, en un lot cohérent. Le `sl.interposer.dll` du jeu est conservé. La fiche affiche sa version séparément de celle des plugins et explique la différence.
- **Choisir une fois pour tous les jeux** : dans **Paramètres → Par défaut à l'installation**, vous dites ce que le Hub prend d'office : la version des plugins Streamline, celle de DLSS, de Ray Reconstruction et de la génération d'images (« la plus récente que le mod admet », « ne pas remplacer », ou une version), et vos presets DLSS. Chaque fiche part de ces choix et vous laisse les changer pour ce jeu. Un preset choisi ainsi n'est écrit que dans un jeu qui n'a pas déjà le sien, et seulement si ses DLL le prennent ; la fiche le dit par la case « Écrire vos presets par défaut ».
- **Ce que vous décochez dans un jeu y reste laissé de côté** : une DLL NVIDIA, les plugins Streamline ou vos presets par défaut décochés sur la fiche d'un jeu sont retenus pour ce jeu. La fiche le rappelle, « Tout mettre à jour » n'y touche pas, et recocher la case le reprend.
- **Modèle DLSS Super Resolution** : le Hub écrit le modèle choisi dans le `rtx-encore.jsonc` du jeu (`dlssSrPreset`), et RTX Encore l'applique au démarrage du jeu. Le Hub ne modifie jamais le profil de pilote NVIDIA du jeu ; quand ce profil impose un modèle de son côté (posé avec l'application NVIDIA, par exemple), la fiche le dit, car il peut l'emporter avec un mod plus ancien que 1.1.0.

- **Réglages de départ** : une proposition pour votre carte. Le multiplicateur de génération d'images est, par défaut, celui que le jeu décide ; ×2, ×3 et ×4 sont au choix.
- **Nom du proxy** : le nom sous lequel le jeu charge le mod (`version.dll`, `dxgi.dll`, `winmm.dll`, `dinput8.dll`). Pour chacun, la fiche dit si le jeu le chargera et pourquoi : ce que son exécutable importe, un correctif de compatibilité que Windows applique au jeu, un autre outil déjà présent, ce qui s'est passé au dernier lancement, et ce que disent les profils de la communauté. Le nom recommandé en découle ; vous pouvez passer à un autre en une opération, annulable comme les autres. Dans un jeu doté d'un chargeur ASI, le mod peut aussi être un plugin, `rtx-encore.asi`. Un outil déjà présent sous un nom n'est jamais écrasé. Un mode de compatibilité que Windows applique au jeu se retire depuis sa fiche, pour votre compte et, après la demande des droits d'administrateur par Windows, pour tous les comptes ; le Hub note ce qu'il a retiré, et **Remettre** le rétablit tel qu'il était.

**Anti-triche.** Quand le Hub reconnaît un anti-triche (EasyAntiCheat, BattlEye…), la tuile et la fiche le nomment. Votre compte peut être banni, ou le mod peut ne pas se charger : rien n'est écrit dans ce jeu avant que vous ayez accepté ce risque dans la fenêtre de validation. La détection repose sur des fichiers connus et peut manquer une protection.

## Installer ou mettre à jour

Le bouton principal de la fiche ouvre un assistant en trois étapes.

1. **Inspection** : ce que le jeu contient, ce que votre machine permet.
2. **Ce qui va être écrit** : la liste exacte, avec ce qui est là maintenant et ce qui y sera. Rien n'est encore écrit. Chaque fichier d’origine est conservé d’abord dans les données du Hub.
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

La fiche du jeu mémorise vos derniers choix de preset, multiplicateur et options sur cet appareil. Ils restent des propositions jusqu’à leur application ; leur disponibilité est vérifiée selon les composants actuels du jeu. Retour et Appliquer restent accessibles pendant le défilement de la fiche et de tous les réglages.

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

Les originaux et l’historique des opérations utilisent des ZIP partagés vérifiés dans les données du Hub. Seuls des octets identiques avec le même SHA-256 complet partagent une copie ; deux fichiers de même version mais de contenus différents restent distincts. Une copie n’est collectée que si aucun jeu, opération conservée ou retour après interruption n’en a besoin. La limite des huit opérations d’historique ne change pas ; le stockage des runtimes téléchargés reste séparé.

Au premier démarrage après une mise à jour depuis les 1.0.x, 1.1.x ou 1.2.x, le Hub optimise automatiquement les sauvegardes, y compris celles des jeux absents de la bibliothèque. Les originaux et l’historique restent restaurables, sans modifier les réglages. Les copies vérifiées des anciens dossiers du Hub et des dossiers `rtx-encore-backups` des jeux ne sont retirées qu’après validation de la conversion. Les fichiers inconnus ou altérés sont conservés. Vous pouvez arrêter entre deux jeux ; une interruption, un jeu indisponible ou un fichier verrouillé sera réessayé au prochain démarrage. Pour un nettoyage bloqué par les droits, utilisez **Réessayer avec les droits administrateur** dans la bibliothèque ; Windows demande votre accord avant le helper limité à ce jeu.

Gardez le dossier complet `%LOCALAPPDATA%\EncoreHub`, ou `data` à côté du Hub portable, tant qu’un jeu doit pouvoir être restauré. Il contient désormais des originaux partagés entre plusieurs jeux, en plus des réglages et de l’historique. Gardez Hub 1.2.4 ou ultérieur pour restaurer les états migrés ; les anciens Hub refusent leurs nouvelles références. **Paramètres → Espace utilisé** montre la place prise par l’application, les sauvegardes, les runtimes téléchargés, les archives RTX Encore, les jaquettes, les journaux et les autres données du Hub, ainsi que les anciennes sauvegardes encore présentes dans les dossiers des jeux ; une analyse partielle est signalée, et son total est alors un minimum. Désinstaller le programme installé conserve ces données ; les supprimer fait perdre les copies de restauration correspondantes.

Le cache du mod conserve uniquement les ZIP originaux des versions actuellement proposées sur les canaux stable et candidate. Les anciennes versions et les anciens dossiers extraits sont retirés après vérification en ligne de la liste des publications. Un ancien cache extrait peut donc nécessiter un nouveau téléchargement unique. Les sources d’installation sont extraites temporairement.

Sur NTFS, les DLL NVIDIA, Intel et Streamline téléchargées utilisent la compression LZX de Windows. Les DLL déjà en cache sont compressées en arrière-plan après la lecture de la bibliothèque, même si les téléchargements automatiques sont désactivés ; aucune version en cache n’est supprimée. Windows fournit les octets d’origine à la lecture : installation et vérification des signatures fonctionnent comme avant. Le compteur d’espace utilisé tient compte de la compression des runtimes ; dans l’Explorateur, le gain apparaît dans **Taille sur le disque**, tandis que **Taille** reste identique. Les volumes incompatibles (dont les supports portables exFAT), les fichiers verrouillés et ceux qui ne gagnent rien restent sous leur forme ordinaire ; un échec de compression ne bloque pas l’installation.

Le Hub contacte, sans compte et sans rien envoyer de vous :

- GitHub et l’archive officielle XeSS d’Intel, pour les dépendances Intel nécessaires à un mod compatible ;
- GitHub, pour les publications du mod, celles du Hub, les DLL de NVIDIA et les plugins Streamline ;
- `encore-dl.nometa.fr`, pour la DLL de Neural Rendering, une version au choix quand vous la prenez, la liste des sources, et les profils de la communauté quand vous ouvrez sa page ;
- `encore-community.nometa.fr`, seulement quand vous publiez, retirez, aimez, confirmez ou signalez un profil : ce que vous avez relu, signé par la clé de votre machine. Pour couper la communauté, mettez `"Community": "off"` dans `%LOCALAPPDATA%\EncoreHub\settings.json` ;
- Steam et Wikipédia, pour les jaquettes qui manquent : le titre du jeu leur est envoyé. **Paramètres → Jaquettes** coupe cette recherche.

Le Hub prépare les téléchargements NVIDIA sélectionnés par vos choix par défaut dans son propre dossier de données, en réutilisant les copies identiques déjà vérifiées sur l’ordinateur. Les volumes téléchargés et stockés dépendent des composants. L’option de préparation au lancement concerne NVIDIA ; les fichiers Intel nécessaires à un mod compatible restent obtenus lors de l’installation ou de la mise à jour de ce mod.

Il n'y a aucune télémétrie.

## Clavier et lecteur d'écran

Tout se fait au clavier. `Ctrl+F` va à la recherche, `F5` relit les dossiers, `Alt+Gauche` revient en arrière. Chaque état se dit par un mot, pas seulement par une couleur.

## Un problème ?

Si les fiches des jeux ne s’ouvrent pas, utilisez **Paramètres → Diagnostic du Hub → Exporter les journaux du Hub**, ou le bouton d’export sur la fiche en erreur. L’Explorateur affiche le ZIP. Les journaux restent locaux, avec rotation automatique (trois fichiers d’environ 2 Mio), et comprennent la version du Hub, les commandes en échec et les données de jeu illisibles. Ils se trouvent aussi dans `%LOCALAPPDATA%\EncoreHub\logs`, ou `data\logs` à côté du Hub portable. Relisez l’archive avant de la partager : des noms de jeux et chemins d’installation peuvent y figurer. Aucun envoi automatique.

Ouvrez un [ticket](https://github.com/SilyNoMeta/rtx-encore-hub/issues/new/choose) avec la version du Hub, le jeu, le lanceur, la carte, le pilote et les étapes qui reproduisent le problème. Joignez le diagnostic préparé par la page Santé après l'avoir relu.

## Réinstaller proprement

Sur un jeu suivi par le Hub, choisissez **Réinstaller proprement**. Relisez la version du mod proposée et les fichiers, puis appliquez le plan. Il recrée le mod et ses runtimes gérés, y compris les fichiers manquants ou endommagés, en conservant les réglages actuels à l’identique. Les sources exactes des runtimes doivent être disponibles ; des fichiers inconnus dans le dossier privé de runtimes font refuser le nettoyage. Aucune suppression récursive du dossier.

Le lancement automatique du jeu est décoché par défaut. **Santé → Sauvegardes de ce jeu** permet de revenir avant la réinstallation, dans l’historique des huit dernières opérations. Conservez le dossier complet des données du Hub. Cette réparation ne garantit pas la résolution des crashs GTA V Enhanced ; conserver les réglages conserve aussi un éventuel réglage problématique.


## Netteté après reconstruction

**Disponible dans le Hub 1.2.3**, avec RTX Encore 1.2.2 ou un mod compatible plus récent.

Les réglages du jeu proposent **Netteté après reconstruction**. Off est le défaut. Game utilise la valeur envoyée par le jeu ; sans valeur, il ne fait rien. Custom applique à chaud une force de 0 à 100 %, 30 % par défaut. Cette préférence visuelle peut faire partie des profils partagés. Elle concerne DLSS, DLAA, Ray Reconstruction et le remplacement XeSS, après Neural Rendering s'il est actif. Elle se cumule avec la netteté ajoutée ensuite par le jeu ; trop forte, elle crée des halos et accentue le bruit. Certains chemins graphiques restent exclus. Vulkan et le rendu en jeu ne sont pas encore validés. Utilisez un build contenant la fonction ; les anciens builds du mod ignorent ces clés.

## Réglages de RTX Encore 1.3.0

**Disponible dans le Hub 1.3.0**, avec RTX Encore 1.3.0 ou un mod compatible plus récent.

Le **NR fovéal** (expérimental, désactivé par défaut) fait travailler le Neural Rendering à pleine force au centre de l'image et plus légèrement vers les bords : plus de FPS, avec un effet NR plus doux près des bords. Choisissez un préréglage : light garde presque toute l'image à pleine force, balanced est le défaut, strong gagne le plus. Custom utilise quatre valeurs : la largeur et la hauteur du centre à pleine force, la longueur de la transition et le détail NR conservé sur les bords. Ces réglages peuvent faire partie des profils partagés.

**Smooth Motion sur RTX 20** demande le pilote 621.01 et un jeu DirectX 12. Sur une carte RTX 20 détectée, choisissez **V1 (test 1)**, le défaut, ou **V2 (test 2)**, comparez les deux dans la même scène et relancez le jeu après chaque changement. Le choix est masqué sur les autres cartes et n'active pas Smooth Motion.

RTX Encore 1.3.0 a retiré OpenNR et le panneau Cyber Engine Tweaks : le Hub n'affiche plus leurs réglages. Le Neural Rendering NVIDIA reste disponible.
