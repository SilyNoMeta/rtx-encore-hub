<div align="center">

<img src="assets/logo.png" alt="RTX Encore Hub logo" width="128" height="128">

![RTX Encore Hub — your games, one place](assets/hero.svg)

# RTX Encore Hub

### Your library. Your installs. Your way back.

The Windows companion for **[RTX Encore](https://github.com/SilyNoMeta/rtx-encore)**.<br>
It finds your games, installs the mod with the NVIDIA files it needs, keeps all of it up to date, and can always put a game back as it was.

[![Latest release](https://img.shields.io/github/v/release/SilyNoMeta/rtx-encore-hub?include_prereleases&style=for-the-badge&label=Latest&color=76b900)](https://github.com/SilyNoMeta/rtx-encore-hub/releases)
[![Downloads](https://img.shields.io/github/downloads/SilyNoMeta/rtx-encore-hub/total?style=for-the-badge&color=2f81f7)](https://github.com/SilyNoMeta/rtx-encore-hub/releases)

[![Windows 10 and 11, x64](https://img.shields.io/badge/platform-Windows_10_%C2%B7_11_x64-8ab4f8?style=flat-square&labelColor=171c22)](#getting-started)
[![English, French and Chinese interface](https://img.shields.io/badge/interface-EN_%C2%B7_FR_%C2%B7_ZH-c4b5fd?style=flat-square&labelColor=171c22)](#getting-started)

[![Download the latest version for Windows x64](assets/download.svg)](https://github.com/SilyNoMeta/rtx-encore-hub/releases)

[Website](https://encore.nometa.fr/) · [User guide](docs/USER-GUIDE.md) · [All releases](https://github.com/SilyNoMeta/rtx-encore-hub/releases) · [Report an issue](https://github.com/SilyNoMeta/rtx-encore-hub/issues/new/choose) · **[Français](README.fr.md)** · **[简体中文](README.zh-CN.md)**

</div>

> [!NOTE]
> **Windows x64.** Open the [releases](https://github.com/SilyNoMeta/rtx-encore-hub/releases) and download `RTX-Encore-Hub-Setup-<version>.exe`, or `RTX-Encore-Hub-Portable-<version>.zip`, which installs nothing. The installer is not code-signed yet, so Windows may show a SmartScreen warning the first time; each release gives the SHA-256 of its installer. The Hub and the RTX Encore mod have separate releases.

## Hub 1.3.1: safer runtime updates

**New in 1.3.1:** safer Streamline and NVIDIA runtime updates for older games, including WRC Generations. Incompatible combinations stay unavailable. [Release notes](docs/notes/1.3.1.md).

Install and update RTX Encore, keep its runtimes matched, and manage your games from one library. The Hub and the mod have separate releases.

- **Settings for RTX Encore 1.3.0.** Turn on the mod's experimental Foveated NR and pick a preset, or choose Smooth Motion V1 or V2 on an RTX 20 card. Both require RTX Encore 1.3.0. **Settings → Storage usage** shows the space the Hub takes.
- **Export Hub logs** — Export recent Hub activity and errors from Settings or a failed game page, even when game pages cannot open. Review the archive before sharing.
- **Shared backups, reliable restoration** — Identical bytes are stored once for originals and history across games. Migration runs automatically, keeps your settings, and cleans verified old copies. Restoring migrated states requires Hub 1.2.4 or newer.
- **Remembered choices** — The game page remembers preset, multiplier and option selections. Back and Apply remain accessible while scrolling; changes still need confirmation.
- **A faster library** — Cached games appear first while verification runs in the background. Favorites, card actions, search, tray mode and remembered executable choices keep games within reach.
- **Intel engines and their runtimes** — Choose experimental XeSS reconstruction or XeFG frame generation where the mod supports them. The Hub installs, verifies, backs up and restores their files; installed files do not establish that an engine is active.
- **NR pass by pass and HDR inputs** — Adjust each of up to four NR passes, or inherit the global style. Common HDR-input and exposure settings follow the chosen reconstruction engine; they do not enable display HDR.
- **Diagnostics and shared profiles** — Review the Health page, prepare a diagnostic and share compatible per-game visual preferences. Shared profiles remain experimental.

**Included from Hub 1.3.0:** settings for RTX Encore 1.3.0 (Foveated NR, Smooth Motion V1 or V2 on RTX 20), storage usage in Settings, and backup maintenance that no longer repeats the same warning for a backup folder the Hub did not create. OpenNR and the Cyber Engine Tweaks panel left with RTX Encore 1.3.0, and so did their settings in the Hub.

**Intel XeSS / XeFG remain very experimental.** Compatibility depends on the mod, game, graphics API and runtimes. Report problems with a reviewed diagnostic archive; neither installed files nor a requested multiplier prove successful rendering.

[Hub 1.3.1](docs/notes/1.3.1.md) · [RTX Encore 1.3.1](https://github.com/SilyNoMeta/rtx-encore/releases/tag/v1.3.1)

![The Hub's game library, with cover art, the state of each install and the update banner](screenshots/library.png)

<p align="center"><sub>Real application capture · English interface · demonstration library of stand-in game folders · 14 October 2026</sub></p>

## Why use the Hub rather than copy files by hand

| By hand | With the Hub |
| :--- | :--- |
| Find the game folder, pick a proxy name that is free, copy the right file. | Your Steam, Epic and GOG games are found by themselves; the Hub picks the name the game really loads and leaves ReShade, OptiScaler or Special K theirs. |
| Hunt for the right DLSS and Streamline files, version by version. | The latest DLSS, Ray Reconstruction and frame generation DLLs the mod admits are taken for you, and the Streamline plugins as a matched set. The game's own interposer is never replaced. |
| Find NVIDIA's Neural Rendering DLL yourself. | `nvngx_dlssnr.dll` 310.9.16, the exact build the mod requires, is downloaded, verified and put beside the mod. |
| Redo it all in every game at each new version. | **Update all** updates the mod, the NVIDIA DLLs and the Streamline plugins in every game. The Hub updates itself too. |
| Keep your own backups, and hope. | Every replaced file is backed up first; **Restore game** puts everything back, driver setting included. |
| Edit a settings file and guess. | A form explains every setting, greys what has no effect on your card, and offers only the presets your game's DLLs take. |
| Something goes wrong and you do not know why. | **Launch and verify** watches the game's first minute and says what happened; a diagnostic is ready for a report. |

## What it does

| Feature | What the Hub does |
| :--- | :--- |
| **One game library** | Finds the games of Steam, Epic and GOG, the folders you add, or a single game by its executable. Each tile says where the game stands: not installed, installed, to update, changed by the game, failing. |
| **A page for every game** | Says what RTX Encore can do there on your card and driver (frame generation, DLSS render scale, Smooth Motion, Neural Rendering) and why, and compares the game's NVIDIA DLLs with what it proposes. |
| **The right NVIDIA files** | Takes the most recent DLSS and Streamline versions the game's RTX Encore admits, from what your machine already has or from a download. A DLL is accepted only with a valid NVIDIA signature. You choose the versions once for every game in Settings, and what you untick in one game stays left alone there. |
| **Install with a way back** | Shows the plan before anything is written, writes it whole or not at all, and undoes an install that was interrupted. Administrator rights are asked only where a folder needs them, for that one operation. |
| **Updates** | Reads the releases of RTX Encore, with their notes, and updates one game or all of them. Looks for its own new version and installs it when you say so; the downloaded update is verified. |
| **Settings** | Edits `rtx-encore.jsonc` through a form, keeps named sets of settings per game, proposes starting settings for your card, and sets the DLSS Super Resolution model, which RTX Encore applies when the game starts. |
| **Health and backups** | Starts the game, watches its first minute, and lists every state the game can be put back to. |

**What the Hub says of a game is deduced from its files, your card and your driver.** It is not a certification that a feature works in that game, and it measures no performance. RTX Encore's own [documentation](https://github.com/SilyNoMeta/rtx-encore) remains the reference for the mod.

## Look before you install

![A game's page: what is possible on this card, and why](screenshots/game-inspection.png)

The page of a game says what is possible before you change anything, and each line gives its reason. An anti-cheat is said so: nothing is written in such a game without your word on the risk.

> [!WARNING]
> Installing a mod in a game an anti-cheat protects can block its startup or put your account at risk, especially online. Accepting the risk in the Hub does not make the mod approved by a publisher or an anti-cheat provider.

![The NVIDIA DLLs of a game and its Streamline plugins, with what the Hub proposes](screenshots/nvidia-files.png)

Each NVIDIA DLL is shown with the version in the game, the best copy this machine has, and what the Hub proposes. The Streamline plugins are replaced as a set; the page says the version of the game's interposer and warns you when it differs.

## Getting started

1. Download `RTX-Encore-Hub-Setup-<version>.exe` from the [releases](https://github.com/SilyNoMeta/rtx-encore-hub/releases) and run it. It installs for your account only, without administrator rights.
2. Open **Library**. Steam, Epic and GOG games are there; add other folders under **Settings**.
3. Open a game's page, read what is possible there, and press **Install**. The plan lists every file before anything is written.
4. Under **Health**, **Launch and verify** starts the game and tells you how its first minute went.
5. When a new RTX Encore is out, **Update all** in the library updates every game.

The interface follows the language of Windows: **English, French or Simplified Chinese**; other languages get English.

Read the **[user guide](docs/USER-GUIDE.md)** for updates, restoration, where the Hub keeps its data and what it reads on the network.

## Community profiles

Since 1.0.0-rc.2, the Hub reads the community's profiles: settings per game shared by other players, ranked by how close their machine is to yours, a few at a time, with filters (same card, Neural Rendering, Smooth Motion…). Importing one shows what would change, section by section, and can be undone; publishing yours shows exactly what is sent before it is. There is no account: a key made on your machine signs what you send. The community is experimental and lightly tested, and it starts empty.

## About this repository

This is the public home of **RTX Encore Hub downloads, documentation and feedback**. The application source is maintained separately and is not included here. NVIDIA binaries and game files are not stored in this repository.

RTX Encore Hub is an independent project, unaffiliated with NVIDIA or game publishers. Game artwork visible in screenshots belongs to its respective owners. See the [project notices](docs/NOTICES.md).
