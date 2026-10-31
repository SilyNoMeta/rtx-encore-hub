<img src="../assets/logo.png" alt="RTX Encore Hub logo" width="80" height="80">

# Using RTX Encore Hub

[Français](USER-GUIDE.fr.md) · [简体中文](USER-GUIDE.zh-CN.md) · [Back to the project](../README.md)

RTX Encore Hub installs [RTX Encore](https://github.com/SilyNoMeta/rtx-encore) in your games, keeps the mod and the NVIDIA DLLs up to date, checks that a game starts well with it, and can always go back. The interface follows the language of Windows: French, English or Simplified Chinese; other languages use English. This guide uses the English labels of the application.

## XeSS and XeFG Tensor Cores (1.5.0)

With **RTX Encore 1.5.0 or later**, choose the XeSS reconstruction engine to use **XeSS Tensor Cores**, or the XeFG engine to use **XeFG Tensor Cores**. The switches are independent, experimental and off by default. Initial qualification is **RTX 4090, NVIDIA 621.01, DirectX 12 and the Intel runtimes supplied by Hub**. Other configurations are not implied to be supported.

Both switches apply live: XeSS at its next execution, XeFG as command recordings renew. Qualified fixed XeFG factors X2–X6 can also change live within initialized capacity. Close the game when installing the new mod; changing the FG engine still needs a restart. Refused preparation retains the standard Intel path; a Tensor execution fault needs a restart. Community profiles preserve both choices, but importing them does not qualify a different GPU or driver.

Earlier TW3 XeSS measurements found about 30.7% less XeSS GPU time and 2.8–3.2% more rendered-source FPS in one scene; later final-pass changes have deterministic replay validation rather than a new in-game comparison. No general XeFG FPS or latency gain is established. [Full conditions and measurements](https://github.com/SilyNoMeta/rtx-encore/blob/main/docs/INTEL-ENGINES.md).


## Using 1.2.2

**XeSS / XeFG: VERY EXPERIMENTAL.** Getting this integration working was a particularly difficult and frustrating part of development :) Expect bugs, crashes, visual artifacts and differences between games and graphics APIs. Please report problems: in RTX Encore Hub, open the game’s **Health** page, choose **Prepare a diagnostic**, review the archive for personal information, then attach it to an [RTX Encore issue](https://github.com/SilyNoMeta/rtx-encore/issues/new/choose). Include your engine choices, graphics API and requested multiplier. The Hub does not upload the archive for you.

Stable 1.2.2 is available on the Stable update channel. Candidate also includes pre-releases.

Intel, common-input and per-pass NR settings require mod 1.2.0-beta.1 or later. Mod 1.2.2 no longer uses the NVIDIA provider-policy setting, so the Hub hides it; older mods retain their supported controls. XeFG remains experimental and depends on the mod, graphics API, game and runtime. A requested multiplier does not prove displayed frames.

### Intel engines, with their dependencies

With RTX Encore 1.2, choose XeSS reconstruction or XeFG frame generation where the mod supports them. The Hub installs and verifies the Intel files and their license with the mod; they are backed up and restored in the same operation. Installed files do not establish that an engine is active.

### Neural Rendering, pass by pass

For each of the four possible passes, adjust intensity, local tone, local structure, skin structure and the character mask, or inherit the global setting. Setting intensity to zero still runs the pass and does not remove its cost.

Since RTX Encore 1.2.0-beta.1, NR can also run after Ray Reconstruction in compatible Direct3D 12 games that provide linear depth. Direct3D 11 and Vulkan still do not support this linear-depth case. Local testing in 007 First Light with path tracing confirmed that NR runs; image quality and cost have not been measured. The intermittent startup crash remains unresolved.

### HDR input and exposure

The common `srHdr` and `srAutoExposure` controls follow the chosen reconstruction engine. Both default to the game and require a restart. HDR input does not enable HDR on the display or convert SDR to HDR.

Leave both controls on `game` unless the game’s input format is known. Incorrect HDR input can degrade the image. Auto exposure may help exposure-related ghosting, but is not a general fix; some DLSS models impose it. XeSS auto exposure has a GPU cost and is not recommended for LDR. XeSS Vulkan with LDR and manual exposure remains unsupported. Ray Reconstruction and frame generation are unchanged.

Provider-policy controls apply only to older mods that use them and stay local to the game. RTX Encore 1.2.2 ignores an old `providerPatchPolicy` entry. NVIDIA runtime compatibility no longer needs a fixed version list; Intel runtime checks remain unchanged. These policy controls do not travel in community profiles.

With XeFG, changing the FPS limit requires a game restart. Variable pacing for higher XeFG multipliers is experimental. An FPS cap does not establish the cadence of source frames.

[Release notes](notes/1.2.2.md) · [1.2.0-beta.1 notes](notes/1.2.0-beta.1.md)

## Install the Hub

Download `RTX-Encore-Hub-Setup-<version>.exe` from the releases page and run it. It installs for your account only, **without administrator rights**, in `%LOCALAPPDATA%\Programs\RTX Encore Hub`. Nothing else has to be installed first.

The installer is not signed: Windows may show a SmartScreen warning the first time. Each release gives the SHA-256 of its installer; compare it if you want to be sure of the file.

The Hub looks for its own updates when it starts, then once a day. **Updates** shows the new version and its notes; **Update and restart** downloads the installer, verifies its digest, runs it and starts the Hub again. You can choose **Later**, or **Ignore this version**. An update waits for an install going on in a game to end. Updating or uninstalling the installed program preserves your settings and restoration data.

**Portable version.** `RTX-Encore-Hub-Portable-<version>.zip` installs nothing: extract it into a folder you can write to (not under Program Files) and start `rtx-encore-hub.exe`. The file `portable.txt` beside it makes the Hub keep its state in the `data` folder next to it: keep that folder. Original game files and history backups are shared in that data folder; keep it when moving or updating the portable Hub. The portable version does not update itself: **Download the portable version**, in **Updates**, opens the release page; close the Hub, then replace `rtx-encore-hub.exe` and `encorehub-elevated.exe` with the new archive's.

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
2. **What will be written**: the exact list, with what is there now and what will be. Nothing is written yet. Each original file is saved first in the Hub data folder.
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

A file the game, its launcher or another tool changed since is never overwritten: it is left as it is and reported. Restoring the game to before any Hub intervention keeps a modified `rtx-encore.jsonc`; restoring before a specific operation asks before replacing modified settings.

Uninstalling removes the tracked mod and runtime files and restores any originals. Empty private `rtx-encore-runtimes/intel` and `rtx-encore-runtimes` folders are removed. Session logs in `rtx-encore-logs` and modified settings are kept; their presence does not mean the mod is still installed. You can delete these logs and settings yourself if you no longer need them. Runtime folders containing other files are kept.

A copy of the mod put there by hand is recognized, but the Hub only has an original backup for what it wrote itself.

## When the game updates

If an update or a repair of the game replaced files of the install, the page says so: **The game changed the install**.

- **Reapply** writes the mod again if it is missing, and the NVIDIA DLLs the Hub still has a better copy of. A DLL the game brought newer is kept.
- **Forget** keeps the game's files as they are and stops tracking them.

## Tune the mod

The game page remembers your last preset, multiplier and option selections on this device. They remain proposals until you apply them; unavailable choices are checked again against the game's current components. Back and Apply stay accessible while you scroll through the game page or all settings.

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

Original files and operation history use shared verified ZIP backups in the Hub data folder. Only identical bytes with the same full SHA-256 share a copy; different files with the same version number remain separate. A copy is collected only when no game, retained operation or recovery needs it. The eight-operation history limit is unchanged; the runtime download store is separate.

On the first Hub startup after upgrading from 1.0.x, 1.1.x or 1.2.x, backup optimization runs automatically, including saved games no longer in the library. Originals and history remain restorable, with settings unchanged. Verified copies in the old Hub folders and games’ `rtx-encore-backups` folders are removed only after conversion is committed. Unknown or altered files are kept. You can stop between games; an interruption, unavailable game or locked file is retried at the next start. For pending permission failures, use **Retry with administrator rights** in the library; Windows asks before a bounded helper runs.

Keep the complete `%LOCALAPPDATA%\EncoreHub` folder, or `data` beside the portable Hub, while any game needs restoration. It now holds original files shared by multiple games, as well as settings and history. Keep Hub 1.2.4 or newer to restore migrated states; older Hubs refuse their new references. **Settings → Storage usage** shows the space taken by the application, backups, downloaded runtimes, RTX Encore archives, covers, logs and other Hub data, plus older backups still in game folders; a partial scan says so, and its total is then a minimum. Uninstalling the installed program preserves these data, but deleting them loses the corresponding restoration copies.

The mod cache keeps only the original ZIPs of the versions currently offered on the stable and candidate channels. Older versions and the former extracted cache folders are removed after the release list is checked online. An old extracted cache may therefore need to be downloaded once again. Installation sources are extracted temporarily.

On NTFS, downloaded NVIDIA, Intel and Streamline runtime DLLs use Windows LZX compression. Existing cached DLLs are compressed in the background after the library is read, even with automatic runtime downloads disabled; no cached versions are removed. Windows reads their original bytes transparently, so installation and signature checks work as before. Storage usage counts compressed runtime bytes; Explorer's **Size on disk** shows the saving, while **Size** stays the same. Unsupported volumes (including exFAT portable drives), locked files and files that do not benefit keep their ordinary form; a compression failure does not prevent installation.

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

If game pages cannot open, use **Settings → Hub diagnostics → Export Hub logs** or the export button on the failed game page. The ZIP is shown in Explorer. Logs are local, rotate automatically (three files of about 2 MiB each), and include the Hub version, command failures and unreadable game data. You can also find them in `%LOCALAPPDATA%\EncoreHub\logs`, or `data\logs` beside the portable Hub. Review the archive before sharing it: game names and installation paths may be present. Nothing is uploaded automatically.

Open an [issue](https://github.com/SilyNoMeta/rtx-encore-hub/issues/new/choose) with the Hub's version, the game, the launcher, the card, the driver and the steps that reproduce the problem. Attach the diagnostic prepared by the Health page once you have read it.

## Reinstall cleanly

On a game managed by the Hub, choose **Reinstall cleanly**. Review the proposed mod version and files, then apply the plan. It recreates the mod and its managed runtimes, including missing or damaged files, and preserves the current settings exactly. Exact runtime sources must be available; unknown files in the private runtime folder refuse cleanup. No recursive folder deletion is used.

The game is not launched automatically by default. **Health → Backups of this game** lets you go back before the reinstall, within the history of the last eight operations. Keep the complete Hub data folder. This repair does not guarantee a fix for GTA V Enhanced crashes; preserving settings also preserves any setting that may cause a problem.


## Sharpening after reconstruction

**Available in Hub 1.2.3**, with RTX Encore 1.2.2 or a newer compatible mod.

The game settings include **Sharpening after reconstruction**. Off is the default. Game uses the game's supplied sharpness value; it has no effect if the game sends none. Custom applies a strength from 0 to 100%, default 30%, while playing. This visual preference can be included in shared profiles. It applies to DLSS, DLAA, Ray Reconstruction and replacement XeSS, after Neural Rendering when enabled. It adds to any sharpening the game performs later; high strengths can create halos and amplify noise. Some graphics paths remain unsupported. Vulkan and real-game appearance have not yet been validated. Use a build that includes this feature; older mod builds ignore these keys.

## Settings for RTX Encore 1.3.0

**Available in Hub 1.3.0**, with RTX Encore 1.3.0 or a newer compatible mod.

**Foveated NR** (experimental, off by default) runs Neural Rendering at full strength in the middle of the image and lighter towards the edges: more FPS, with a softer NR effect near the edges. Choose a preset: light keeps most of the image at full strength, balanced is the default, strong saves the most. Custom uses four values: the width and height of the full-strength centre, the length of the transition, and the NR detail kept at the edges. These settings can be shared in profiles.

**Smooth Motion on RTX 20** needs driver 621.01 and a DirectX 12 game. On a detected RTX 20 card, RTX Encore 1.3.0 to 1.5.0 let you choose **V1 (test 1)**, the default, or **V2 (test 2)**: compare both in the same scene and restart the game after each change. From RTX Encore 1.5.1, RTX 20 always uses V2 and the Hub no longer shows the choice. The choice is hidden on other cards and does not turn Smooth Motion on.

RTX Encore 1.3.0 removed OpenNR and the Cyber Engine Tweaks panel, so the Hub no longer shows their settings. NVIDIA Neural Rendering stays available.


**Native Smooth Motion on RTX 40/50** requires RTX Encore 1.4.5 or newer and a supported driver. Use the Smooth Motion settings, choose the game’s actual graphics API and restart. API detection is a static recommendation, not proof of the active renderer. The mod’s 2x FPS counter is an estimate; it does not count interpolated frames.
