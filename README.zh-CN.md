<div align="center">

<img src="assets/logo.png" alt="RTX Encore Hub 标志" width="128" height="128">

![RTX Encore Hub — 您的游戏，集中一处](assets/hero.zh-CN.svg)

# RTX Encore Hub

### 您的游戏库。您的安装。您的回退之路。

**[RTX Encore](https://github.com/SilyNoMeta/rtx-encore)** 的 Windows 配套应用。<br>
它会找到您的游戏，连同所需的 NVIDIA 文件一起安装模组，让一切保持最新，并且随时可以把游戏恢复原状。

[![最新版本](https://img.shields.io/github/v/release/SilyNoMeta/rtx-encore-hub?include_prereleases&style=for-the-badge&label=Latest&color=76b900)](https://github.com/SilyNoMeta/rtx-encore-hub/releases)
[![下载量](https://img.shields.io/github/downloads/SilyNoMeta/rtx-encore-hub/total?style=for-the-badge&color=2f81f7)](https://github.com/SilyNoMeta/rtx-encore-hub/releases)

[![Windows 10 和 11，x64](https://img.shields.io/badge/平台-Windows_10_%C2%B7_11_x64-8ab4f8?style=flat-square&labelColor=171c22)](#快速开始)
[![英语、法语和中文界面](https://img.shields.io/badge/界面-EN_%C2%B7_FR_%C2%B7_ZH-c4b5fd?style=flat-square&labelColor=171c22)](#快速开始)

[![下载适用于 Windows x64 的最新版本](assets/download.zh-CN.svg)](https://github.com/SilyNoMeta/rtx-encore-hub/releases)

[网站](https://encore.nometa.fr/zh/) · [用户指南](docs/USER-GUIDE.zh-CN.md) · [所有版本](https://github.com/SilyNoMeta/rtx-encore-hub/releases) · [报告问题](https://github.com/SilyNoMeta/rtx-encore-hub/issues/new/choose) · **[English](README.md)** · **[Français](README.fr.md)**

</div>

> [!NOTE]
> **Windows x64。** 请打开[发布页面](https://github.com/SilyNoMeta/rtx-encore-hub/releases)并下载 `RTX-Encore-Hub-Setup-<version>.exe`，或无需安装的 `RTX-Encore-Hub-Portable-<version>.zip`。安装程序尚未进行代码签名，因此首次运行时 Windows 可能显示 SmartScreen 警告；每个发布版本都会给出安装程序的 SHA-256。Hub 与 RTX Encore 模组分别发布。

## 1.2.0

**XeSS / XeFG：高度实验性。** 这部分集成的开发过程非常艰难，也相当折腾 :) 请预期可能出现错误、崩溃、画面伪影，以及不同游戏和图形 API 之间的行为差异。欢迎报告问题：在 RTX Encore Hub 中打开游戏的 **健康检查** 页面，选择 **生成诊断包**，检查并移除个人信息后，将诊断压缩包附加到 [RTX Encore issue](https://github.com/SilyNoMeta/rtx-encore/issues/new/choose)。请注明选择的引擎、图形 API 和请求的倍率。Hub 不会自动上传该压缩包。

- **游戏库** — 收藏、紧凑的卡片操作和从卡片启动、可恢复游戏库的可选托盘模式，以及可筛选游戏库的标题栏搜索。
- **搭配 RTX Encore 1.2.0** — NVIDIA 621.01 驱动上的 Smooth Motion；Force Smooth Motion 已移除（始终解除 Vulkan 排除）；DLSS 预设和重建引擎可在游戏运行中生效。
- **Intel 引擎及依赖** — 搭配 RTX Encore 1.2，可在模组支持的场景中选择 XeSS 重建或 XeFG 帧生成。Hub 会随模组安装并验证 Intel 文件及许可证，在同一操作中备份和还原它们。文件已安装不能证明引擎已激活。
- **逐轮调整 Neural Rendering** — 四轮处理中的每一轮都可以调整强度、局部色调、局部结构、皮肤结构和角色遮罩，也可以继承全局设置。强度设为零仍会运行该轮处理，不会消除其计算开销。
- **HDR 输入与曝光** — 共用设置 `srHdr` 和 `srAutoExposure` 跟随所选重建引擎，默认跟随游戏，需要重启生效。HDR 输入不会开启显示器 HDR，也不会将 SDR 转换为 HDR。
- **找到正确的游戏** — 全局搜索可直接打开游戏页面。当可执行文件不确定时，游戏页面会提供候选项并记住您的选择，也可以恢复自动选择。
- **更有用的诊断** — 健康页面报告帧生成提供程序，以及精确配置准入、未经认证的启发式准入或拒绝。诊断压缩包包含模组文本日志、设置和游戏目录文件列表。分享前请检查内容；Hub 不会自动上传。

新的 Intel、共用输入、逐轮 NR 和提供程序策略设置需要已识别的模组 1.2.0-beta.1 或更高版本。旧模组保留其支持的控制项。XeFG 路径仍属实验性，取决于模组、图形 API、游戏和运行库。更高倍率有使用条件；请求的倍率不能证明实际显示的帧数。

[版本说明](docs/notes/1.2.0.zh-CN.md) · [1.2.0-beta.1 说明](docs/notes/1.2.0-beta.1.zh-CN.md)

![Hub 的游戏库，包含封面、每个安装的状态和更新横幅](screenshots/library.zh.png)

<p align="center"><sub>真实应用截图 · 简体中文界面 · 由替身游戏文件夹组成的演示游戏库 · 2026 年 10 月 14 日</sub></p>

## 为什么使用 Hub，而不是手动复制文件

| 手动操作 | 使用 Hub |
| :--- | :--- |
| 找到游戏文件夹，选一个未被占用的代理名称，复制正确的文件。 | 自动找到您的 Steam、Epic 和 GOG 游戏；Hub 会选择游戏真正会加载的名称，并把 ReShade、OptiScaler 或 Special K 的名称留给它们。 |
| 逐个版本地寻找合适的 DLSS 和 Streamline 文件。 | 自动采用模组支持的最新 DLSS、Ray Reconstruction 和帧生成 DLL，并整套更换 Streamline 插件。游戏自身的 interposer 从不被替换。 |
| 自己去找 NVIDIA 的 Neural Rendering DLL。 | `nvngx_dlssnr.dll` 310.9.16，也就是模组要求的那个确切构建，会被下载、验证并放在模组旁边。 |
| 每出一个新版本，就在每个游戏里重做一遍。 | **全部更新**会更新所有游戏中的模组、NVIDIA DLL 和 Streamline 插件。Hub 自身也会自动更新。 |
| 自己保存备份，然后听天由命。 | 每个被替换的文件都会先备份；**还原游戏**会把一切恢复原状，包括驱动设置。 |
| 修改设置文件全靠猜。 | 表单会解释每一项设置，把对您的显卡无效的设置变灰，并且只提供游戏 DLL 支持的预设。 |
| 出了问题却不知道原因。 | **启动并验证**会观察游戏的第一分钟并说明发生了什么；还可以准备一份用于报告的诊断。 |

## 它能做什么

| 功能 | Hub 的作用 |
| :--- | :--- |
| **一个游戏库** | 找到 Steam、Epic 和 GOG 的游戏、您添加的文件夹，或通过可执行文件添加单个游戏。每个磁贴都会显示游戏的状态：未安装、已安装、待更新、被游戏修改、失败。 |
| **每个游戏一个页面** | 说明 RTX Encore 在您的显卡和驱动上能做什么（帧生成、DLSS 渲染比例、Smooth Motion、Neural Rendering）以及原因，并把游戏的 NVIDIA DLL 与它的建议进行比较。 |
| **合适的 NVIDIA 文件** | 采用游戏中的 RTX Encore 所支持的最新 DLSS 和 Streamline 版本，来源是本机已有的文件或下载。只有带有效 NVIDIA 签名的 DLL 才会被接受。您可以在设置中为所有游戏统一选择版本，在某个游戏中取消勾选的内容会在该游戏中保持不变。 |
| **可回退的安装** | 写入任何内容之前先显示方案，要么完整写入，要么完全不写，并撤销被中断的安装。只有在文件夹需要时才会请求管理员权限，且仅用于这一次操作。 |
| **更新** | 读取 RTX Encore 的发布版本及其说明，更新单个游戏或全部游戏。查找 Hub 自身的新版本，并在您同意时安装；更新带有签名。 |
| **设置** | 通过表单编辑 `rtx-encore.jsonc`，为每个游戏保存命名的设置组合，为您的显卡建议起始设置，并设置 DLSS Super Resolution 模型，由 RTX Encore 在游戏启动时应用。 |
| **健康与备份** | 启动游戏，观察其第一分钟，并列出游戏可以还原到的每个状态。 |

**Hub 对一个游戏的说明是根据其文件、您的显卡和驱动推断出来的。** 这并不保证某项功能在该游戏中可用，也不测量任何性能。RTX Encore 自己的[文档](https://github.com/SilyNoMeta/rtx-encore)仍是模组的参考依据。

## 安装之前先看清楚

![游戏页面：这张显卡上能做什么，以及原因](screenshots/game-inspection.zh.png)

在您做出任何更改之前，游戏页面会说明这里能做什么，每一行都给出原因。反作弊会被明确指出：未经您确认风险，不会在这样的游戏中写入任何内容。

> [!WARNING]
> 在受反作弊保护的游戏中安装模组，可能导致游戏无法启动或使您的账号面临风险，尤其是在线游戏。在 Hub 中接受风险并不意味着模组获得了发行商或反作弊提供商的认可。

![游戏的 NVIDIA DLL 及其 Streamline 插件，以及 Hub 的建议](screenshots/nvidia-files.zh.png)

每个 NVIDIA DLL 都会显示游戏中的版本、本机已有的最佳副本以及 Hub 的建议。Streamline 插件整套更换；页面会显示游戏 interposer 的版本，并在版本不同时提醒您。

## 快速开始

1. 从[发布页面](https://github.com/SilyNoMeta/rtx-encore-hub/releases)下载 `RTX-Encore-Hub-Setup-<version>.exe` 并运行。它只为您的账户安装，不需要管理员权限。
2. 打开**游戏库**。Steam、Epic 和 GOG 的游戏已经在那里；可在**设置**中添加其他文件夹。
3. 打开某个游戏的页面，查看这里能做什么，然后点击**安装**。写入任何内容之前，方案会列出每一个文件。
4. 在**健康检查**中，**启动并验证**会启动游戏，并告诉您它的第一分钟情况如何。
5. RTX Encore 发布新版本时，游戏库中的**全部更新**会更新所有游戏。

界面跟随 Windows 的语言：**英语、法语或简体中文**；其他语言使用英语。

关于更新、还原、Hub 存放数据的位置以及它在网络上读取的内容，请阅读**[用户指南](docs/USER-GUIDE.zh-CN.md)**。

## 社区配置

自 1.0.0-rc.2 起，Hub 可以读取社区配置：其他玩家分享的各游戏设置，按其机器与您机器的接近程度排序，每次显示一部分，并可筛选（相同显卡、Neural Rendering、Smooth Motion……）。导入前会逐节显示将要更改的内容，并且可以撤销；发布您自己的配置时，发送前会完整显示将要发送的内容。无需账号：由您机器上生成的密钥为您发送的内容签名。社区仍是实验性的、测试较少，并且一开始是空的。

## 关于本仓库

这里是 **RTX Encore Hub 下载、文档和反馈**的公开主页。应用的源代码在别处维护，不包含在此处。本仓库不存放 NVIDIA 的二进制文件和游戏文件。

RTX Encore Hub 是一个独立项目，与 NVIDIA 或游戏发行商无关。截图中可见的游戏美术作品归其各自所有者所有。请参阅[项目声明](docs/NOTICES.zh-CN.md)。
