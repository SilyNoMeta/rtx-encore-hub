<img src="../assets/logo.png" alt="RTX Encore Hub logo" width="80" height="80">

# Using RTX Encore Hub

[Français](USER-GUIDE.fr.md) · [简体中文](USER-GUIDE.zh-CN.md) · [Back to the project](../README.md)

RTX Encore Hub installs [RTX Encore](https://github.com/SilyNoMeta/rtx-encore) in your games, keeps the mod and the NVIDIA DLLs up to date, checks that a game starts well with it, and can always go back. The interface follows the language of Windows: French, English or Simplified Chinese; other languages use English. This guide uses the English labels of the application.

## Using the 1.2 beta

**XeSS / XeFG: VERY EXPERIMENTAL.** Getting this integration working was a particularly difficult and frustrating part of development :) Expect bugs, crashes, visual artifacts and differences between games and graphics APIs. Please report problems: in RTX Encore Hub, open the game’s **Health** page, choose **Prepare a diagnostic**, review the archive for personal information, then attach it to an [RTX Encore issue](https://github.com/SilyNoMeta/rtx-encore/issues/new/choose). Include your engine choices, graphics API and requested multiplier. The Hub does not upload the archive for you.

This is a pre-release. To receive beta updates in the Hub, select **Candidate** on the **Updates** page; the Stable channel stays on stable releases.

New Intel, common-input, per-pass NR and provider-policy settings require an identified mod 1.2.0-beta.1 or later. Older mods keep their supported controls. XeFG routes are experimental and limited by the mod, graphics API, game and runtime. Higher multipliers are conditional; a requested multiplier is not proof of displayed frames.

### Intel engines, with their dependencies

With RTX Encore 1.2.0-beta.1, choose XeSS reconstruction or XeFG frame generation where the mod supports them. The Hub installs and verifies the Intel files and their license with the mod; they are backed up and restored in the same operation. Installed files do not establish that an engine is active.

### Neural Rendering, pass by pass

For each of the four possible passes, adjust intensity, local tone, local structure, skin structure and the character mask, or inherit the global setting. Setting intensity to zero still runs the pass and does not remove its cost.

With RTX Encore 1.2.0-beta.1, NR can also run after Ray Reconstruction in compatible Direct3D 12 games that provide linear depth. Direct3D 11 and Vulkan still do not support this linear-depth case. Local testing in 007 First Light with path tracing confirmed that NR runs; image quality and cost have not been measured. The intermittent startup crash remains unresolved.

### HDR input and exposure

The common `srHdr` and `srAutoExposure` controls follow the chosen reconstruction engine. Both default to the game and require a restart. HDR input does not enable HDR on the display or convert SDR to HDR.

Leave both controls on `game` unless the game’s input format is known. Incorrect HDR input can degrade the image. Auto exposure may help exposure-related ghosting, but is not a general fix; some DLSS models impose it. XeSS auto exposure has a GPU cost and is not recommended for LDR. XeSS Vulkan with LDR and manual exposure remains unsupported. Ray Reconstruction and frame generation are unchanged.

Provider policy is local to the game: `exact` accepts reviewed NVIDIA providers; `heuristic`, the mod’s default, also allows guarded compatibility with other signed providers. A heuristic admission remains unqualified and is identified in Health. Restart after changing this policy; it is excluded from community profiles.

With XeFG, changing the FPS limit requires a game restart. Variable pacing for higher XeFG multipliers is experimental. An FPS cap does not establish the cadence of source frames.

[Beta notes](notes/1.2.0-beta.1.md)

## Install the Hub

Download `RTX-Encore-Hub-Setup-<version>.exe` from the releases page and run it. It installs for your account only, **without administrator rights**, in `%LOCALAPPDATA%\Programs\RTX Encore Hub`. Nothing else has to be installed first.

The installer is not signed: Windows may show a SmartScreen warning the first time. Each release gives the SHA-256 of its installer; compare it if you want to be sure of the file.

The Hub looks for its own updates when it starts, then once a day. **Updates** shows the new version and its notes; **Update and restart** downloads the installer, verifies its digest, runs it and starts the Hub again. You can choose **Later**, or **Ignore this version**. An update waits for an install going on in a game to end. Your settings and your backups are never touched by an update or an uninstall.

**Portable version.** `RTX-Encore-Hub-Portable-<version>.zip` installs nothing: extract it into a folder you can write to (not under Program Files) and start `rtx-encore-hub.exe`. The file `portable.txt` beside it makes the Hub keep everything in the `data` folder next to it, your backups included: keep that folder. The portable version does not update itself: **Download the portable version**, in **Updates**, opens the release page; close the Hub, then replace `rtx-encore-hub.exe` and `encorehub-elevated.exe` with the new archive's.

## Find your games

**Library** gathers the games of Steam, Epic and GOG installed on the machine. For the others:

- **Settings → Game folders → Add a folder…**: each sub-folder that holds a recognized executable becomes a game;
- **Add a game**: point directly at a game's executable.

The mod goes beside the program that draws the game: behind a launcher (The Witcher 3 on GOG starts `REDprelauncher.exe`), the Hub takes the game the launcher starts; behind RTX Remix, the mod goes beside `NvRemixBridge.exe`, in the game's `.trex` folder.

A tile says the state of the game by a glyph and a word: not installed, installed, to update, changed by the game, failing. The search (`Ctrl+F`) ignores accents and punctuation; a filter limits the list to one graphics API; `F5` reads the folders again. The pane recalls your machine: card, memory, driver, screen.

When the game page is unsure which executable is the game, review the alternatives it offers. Choose the actual game, then return to automatic selection if needed. The global search in the window’s title bar also finds games in your library.

## Read a game's page

Choose a tile.

- **What is possible here** says, for frame generation, DLSS Super Resolution, Smooth Motion and Neural Rendering, whether the feature is possible on your card and driver, and if not, why. It is deduced from the files and the driver: it is not evidence in the game.
- **NVIDIA DLLs** compares, DLL by DLL, the game's version, the best copy already on the machine and what the Hub proposes. A DLL the machine does not have is downloaded: DLSS, Ray Reconstruction and frame generation from NVIDIA's own repository on GitHub, Neural Rendering's DLL from the project's bucket. **A DLL is accepted only with a valid NVIDIA signature**; Neural Rendering's must also be exactly the build the mod expects.
- **Current NVIDIA downloads**: the bundled catalog offers DLSS SR, RR, FG and NR 310.9.16, plus Streamline plugins 2.14.16. A file requiring a newer mod is explained instead of replaced with an older download. A newer DLL already in the game is kept. FG preset C needs compatible 310.9.16; Lite composition has image-quality trade-offs and does not use the normal protection or UI recomposition controls.
- **Streamline plugins** are taken together as a matched set. The game’s own `sl.interposer.dll` is kept. The page shows its version separately from the plugins and explains any difference.
- **Choose once for every game**: in **Settings → Defaults at install**, you say what the Hub takes by default: the version of the Streamline plugins, that of DLSS, Ray Reconstruction and frame generation ("the most recent the mod admits", "do not replace", or a version), and your DLSS presets. Each game's page starts from these choices and lets you change them for that game. A preset chosen this way is written only in a game that does not have its own yet, and only when its DLLs take it; the page says so with the "Write your default presets" box.
- **What you untick in a game stays left alone there**: an NVIDIA DLL, the Streamline plugins or your default presets unticked on a game's page are remembered for that game. The page reminds you, "Update all" does not touch them, and ticking the box again takes them back.
- **DLSS Super Resolution model**: the Hub writes the chosen model in the game's `rtx-encore.jsonc` (`dlssSrPreset`), and RTX Encore applies it when the game starts. The Hub never changes the game's NVIDIA driver profile; when that profile forces a model of its own (set with the NVIDIA app, for example), the page says so, because it may take precedence with a mod older than 1.1.0.

- **Starting settings**: a proposal for your card. The frame generation multiplier is, by default, the one the game decides; ×2, ×3 and ×4 are yours to choose.
- **Proxy name**: the name the game loads the mod under (`version.dll`, `dxgi.dll`, `winmm.dll`, `dinput8.dll`). For each, the page says whether the game will load it and why: what its executable imports, a compatibility fix Windows applies to the game, another tool already there, what happened at the last launch, and what community profiles report. The recommended name follows; you can switch to another in one operation, undone like any other. In a game with an ASI loader, the mod can also be a plugin, `rtx-encore.asi`. A tool already there under a name is never overwritten. A compatibility mode Windows applies to the game can be removed from its page, for your account and, after Windows asks for administrator rights, for every account; the Hub notes what it removed, and **Put back** restores it as it was.

**Anti-cheat.** When the Hub recognizes an anti-cheat (EasyAntiCheat, BattlEye…), the tile and the page name it. Your account may get banned, or the mod may not load: nothing is written in that game before you accepted that risk in the confirmation window. The detection rests on known files and may miss a protection.

## Install or update

The main button of the page opens an assistant in three steps.

1. **Inspection**: what the game holds, what your machine allows.
2. **What will be written**: the exact list, with what is there now and what will be. Nothing is written yet. Each file that is replaced is backed up first, outside the game folder.
3. **Verification at launch**, if you leave the box checked.

An install is all or nothing: if a write fails, everything is put back. If the Hub is stopped in the middle (power cut, crash), it undoes the interrupted install the next time it starts, before anything else, and tells you.

If the game folder refuses writes to your account, Windows asks for administrator rights **for this operation only**. It is not the Hub that receives them, but a small program that applies only the plan you just accepted and checks every file again.

**Update all**, in the library, updates the mod in every game that holds an older copy. With the "Also update the NVIDIA DLLs and the Streamline plugins" box, ticked by default, each game gets at the same time what its page takes by default: the versions chosen in **Settings → Defaults at install**, and your default presets where the game does not have its own. A game one of whose NVIDIA files cannot come still has its mod updated, and the screen names it. Each game has its own transaction, and "Restore game" on its page puts everything back; games with an anti-cheat are left aside.

## Check that a game starts well

**Launch the game**, at the top of a game's page, starts it as its launcher would, and watches nothing.

**Health → Launch and verify** starts the game and watches its first minute: does the process stay up, did the mod load, what does its log say. The result fits in one sentence, "All is well", or the cause in plain words, then in findings: card and architecture recognized, driver recognized or not, modules accepted, Neural Rendering ready or not. When the game took another file under the mod's name or never asked for it, the page says so and proposes the name to switch to; it also warns when the earlier dlssg_for_sm86 mod is still loaded in the game.

If the game stops in its first minute or the mod does not load, the page offers to **restore** the state of before in one click. After two failures in a row on the same install, it is the main button. **Prepare a diagnostic** makes an archive of text files, without your user name or the machine's, to read and then attach yourself to an issue: the Hub sends nothing.

This verification says a game starts and the mod loads in it. It judges neither the image nor the performance.

## Go back

**Backups of this game**, on the Health page, lists every operation of the Hub, dated. You can go back to the state of before one operation, or of before anything the Hub did (**Restore game**).

A file the game, its launcher or another tool changed since is never overwritten: it is left as it is and reported. The settings file `rtx-encore.jsonc` is yours: if it changed since, the Hub asks before putting it back.

A copy of the mod put there by hand is recognized, but the Hub only has an original backup for what it wrote itself.

## When the game updates

If an update or a repair of the game replaced files of the install, the page says so: **The game changed the install**.

- **Reapply** writes the mod again if it is missing, and the NVIDIA DLLs the Hub still has a better copy of. A DLL the game brought newer is kept.
- **Forget** keeps the game's files as they are and stops tracking them.

## Tune the mod

**All the settings of this game** edits `rtx-encore.jsonc` through a form that follows the sections of the file. Each setting carries its explanation, its default value and, where it applies, "restart needed". A setting without effect on your card is greyed, with the reason. The DLSS presets follow the game's DLLs: the form only offers those the installed DLL takes, and says why the others are missing; frame generation preset C, for instance, only exists in DLSS-G 310.9.16. Comments and keys the Hub does not know are kept as they are.

A game that closes at launch with the mod's in-game menu (Star Wars Outlaws) can do without it: turn on `disableInGameMenu` under Compatibility, and change the settings here. When a game closes in its first minute with the mod loaded, **Launch and verify** offers **Launch again without the in-game menu**, which does it for you.

Nothing is written before you saw the changes. The last change is undone with one button. **Profiles of this game** keeps the settings in force under a name, and goes back to them in one click.

## Community profiles

The community is open since 1.0.0-rc.2. It is experimental and lightly tested, and it starts empty: the first profiles will be yours.

- A game's profiles are listed **nearest to your machine first**, with the reason: same card, same resolution, older driver… By default, only profiles made on a card of your family are shown.
- The page first shows a dozen profiles; **Show more profiles** adds to them. **Filters** narrow the list: my profiles, same card, same resolution, confirmed by others, official, with a measurement, Neural Rendering, Smooth Motion, fixed or dynamic FG multiplier. Only those that tell the profiles apart are offered.
- **Import** first shows what would change, section by section. Keyboard shortcuts are taken only if you ask; diagnostics, never. Your settings of before are kept under the name "Before import", and one button puts the file back exactly as it was.
- **Like**, **It works on my machine** and **Report** take one click and can be taken back.
- **Publish my profile**: the machine and the versions are filled in by the Hub; you add the DLSS mode, the ray tracing level, a note. **Everything that leaves is shown before it is sent, as it leaves.** No file path, user name or machine name: a note that holds one is refused.

There is no account. A key is made on your machine and stays there; you choose a pseudonym.

## Update the mod

**Settings → RTX Encore source**: the public releases of the RTX Encore repository, verified by their SHA-256, or a local folder holding a build of the mod. In **Updates**, the **Mod channel** is chosen like the Hub's: **Stable** only offers final versions, **Candidate** also follows pre-releases. Until you choose, a Hub that is itself a pre-release follows the candidate channel, for itself and for the mod. The page says which version of the mod each game holds, and shows the notes of each release.

## Data, network and privacy

The Hub keeps its settings, its downloads, its covers and the backups of each game in `%LOCALAPPDATA%\EncoreHub` (in `data` beside the portable version). That folder is your way back: do not delete it while games hold an install of the Hub.

The Hub contacts, without an account and without sending anything of yours:

- GitHub and Intel’s official XeSS release archive, for the Intel dependencies required by a compatible mod;
- GitHub, for the releases of the mod, those of the Hub, NVIDIA's DLLs and the Streamline plugins;
- `encore-dl.nometa.fr`, for Neural Rendering's DLL, a version you chose to take, the list of sources, and the community's profiles when you open its page;
- `encore-community.nometa.fr`, only when you publish, remove, like, confirm or report a profile: what you read, signed by your machine's key. To turn the community off, put `"Community": "off"` in `%LOCALAPPDATA%\EncoreHub\settings.json`;
- Steam and Wikipedia, for the covers that are missing: the game's title is sent to them. **Settings → Cover images** turns that search off.

The Hub prepares the NVIDIA downloads selected by your defaults in its own data folder, reusing identical verified copies already on the computer. Download and storage sizes depend on the components. The launch-prefetch switch controls NVIDIA files; the Intel files required by a compatible mod are still obtained when installing or updating that mod.

There is no telemetry.

## Keyboard and screen reader

Everything can be done with the keyboard. `Ctrl+F` goes to the search, `F5` reads the folders again, `Alt+Left` goes back. Every state is said by a word, not by a colour alone.

## A problem?

Open an [issue](https://github.com/SilyNoMeta/rtx-encore-hub/issues/new/choose) with the Hub's version, the game, the launcher, the card, the driver and the steps that reproduce the problem. Attach the diagnostic prepared by the Health page once you have read it.
