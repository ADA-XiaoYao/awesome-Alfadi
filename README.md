# Awesome Alfadi [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
<div align="center">
	<img width="1168" height="880" src="media/banner.jpg">
	<br>
	<br>
	<br>
	<br>
	<div>
**Awesome Alfadi**: A Structured Atlas for the Technical Cosmos

This repository is a curated, graph-based navigation system for the modern technologist. We map the intricate connections between foundational computer science, modern software development, advanced AI/ML, cybersecurity landscapes, low-level systems architecture, and professional growth pathways.

Unlike conventional resource lists, we emphasize **knowledge connectivity**—showing not just *what* to learn, but *how* concepts interlock across domains. This is designed to be:
- **Systematic**: Following a logical progression from fundamentals to specialization.
- **Living**: Continuously updated and expanded by the community.
- **Actionable**: Each resource is vetted for practical learning value.

Our goal: to transform overwhelming information into a coherent, navigable landscape for developers, engineers, researchers, and lifelong learners.

---

## 目录

- [Awesome 系列精选](#awesome-系列精选)
- [计算机科学与软件工程](#计算机科学与软件工程)
- [编程语言](#编程语言)
- [网络安全与攻防技术 (Cybersecurity)](#网络安全与攻防技术-cybersecurity)
  - [1. 基础入门与信息收集 (Foundation & Reconnaissance)](#1-基础入门与信息收集-foundation--reconnaissance)
  - [2. 漏洞发现与利用 (Vulnerability Discovery & Exploitation)](#2-漏洞发现与利用-vulnerability-discovery--exploitation)
  - [3. Web 攻防 (Web Attack & Defense)](#3-web-攻防-web-attack--defense)
  - [4. 应用与服务攻防 (Application & Service Attack & Defense)](#4-应用与服务攻防-application--service-attack--defense)
  - [5. 系统与云原生攻防 (System & Cloud Native Attack & Defense)](#5-系统与云原生攻防-system--cloud-native-attack--defense)
  - [6. 红队作战与高级威胁 (Red Teaming & Advanced Threats)](#6-红队作战与高级威胁-red-teaming--advanced-threats)
  - [7. 蓝队防御与事件响应 (Blue Teaming & Incident Response)](#7-蓝队防御与事件响应-blue-teaming--incident-response)
  - [8. 安全开发与代码审计 (Secure Development & Code Auditing)](#8-安全开发与代码审计-secure-development--code-auditing)
  - [9. 逆向工程与恶意软件 (Reverse Engineering & Malware)](#9-逆向工程与恶意软件-reverse-engineering--malware)
  - [10. 夺旗赛与技能提升 (CTF & Skill Development)](#10-夺旗赛与技能提升-ctf--skill-development)
- [人工智能与数据科学](#人工智能与数据科学)
- [开发工具与职业成长](#开发工具与职业成长)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

---

## Awesome 系列精选

#### 元列表 & 综合

*   [Awesome](https://github.com/sindresorhus/awesome) - Awesome 列表的元列表，一切的起点。
*   [Awesome Awesomeness](https://github.com/bayandin/awesome-awesomeness) - 一个很棒的 Awesome 列表的列表。
*   [Lists](https://github.com/jnv/lists) - 各种主题的精彩列表集合（不仅限于 Awesome）。
*   [Awesome Standalones](https://github.com/sublimino/awesome-standalones) - 独立的、自成体系的 Awesome 列表。
*   [Awesome-JSON-Datasets](https://github.com/jdorfman/awesome-json-datasets) - 用于测试和原型设计的 JSON 数据集。
*   [Awesome Readme](https://github.com/matiassingers/awesome-readme) - 值得学习的 README 文件范例。
*   [Awesome Cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets) - 各种技术和工具的速查表。
*   [Awesome Falsehood](https://github.com/kdeldycke/awesome-falsehood) - 程序员对于各种概念的错误认知。
*   [Awesome Interviews](https://github.com/DopplerHQ/awesome-interview-questions) - 精选的面试问题列表。
*   [Awesome Analytics](https://github.com/newhouse/awesome-analytics) - 分析工具和服务。
*   [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets) - 高质量的公共数据集。
*   [Awesome Stacks](https://github.com/stackshareio/awesome-stacks) - 各种著名的技术栈。

#### 平台 & 生态

*   [Awesome Mac](https://github.com/jaywcjlove/awesome-mac) - macOS 上的优质软件、工具和资源。
*   [Awesome Windows](https://github.com/Awesome-Windows/Awesome) - Windows 上的优质应用和工具。
*   [Awesome Linux](https://github.com/luong-komorebi/Awesome-Linux-Software) - 适用于 Linux 的优质软件。
*   [Awesome Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - 可自行托管的免费软件网络服务和 Web 应用列表。
*   [Awesome-Android-UI](https://github.com/wasabeef/awesome-android-ui) - 精选的 Android UI/UX 库。
*   [Awesome-iOS](https://github.com/vsouza/awesome-ios) - iOS 库、工具和框架。
*   [Awesome-Docker](https://github.com/veggiemonk/awesome-docker) - Docker 资源和项目。
*   [Awesome-Kubernetes](https://github.com/ramitsurana/awesome-kubernetes) - Kubernetes 资源。
*   [Awesome-Electron](https://github.com/sindresorhus/awesome-electron) - 使用 Electron 构建的应用和工具。
*   [Awesome-VSCode](https://github.com/viatsko/awesome-vscode) - VSCode 插件和资源。
*   [Awesome-Neovim](https://github.com/rockerBOO/awesome-neovim) - Neovim 插件和资源。
*   [Awesome-GitHub-Profile-README](https://github.com/abhisheknaiidu/awesome-github-profile-readme) - GitHub 个人主页 README 范例。
*   [Awesome-Actions](https://github.com/sdras/awesome-actions) - GitHub Actions 资源。
*   [Awesome-Browser-Extensions-for-GitHub](https://github.com/stefanbuck/awesome-browser-extensions-for-github) - 增强 GitHub 体验的浏览器插件。

#### 编程语言

*   [Awesome-Python](https://github.com/vinta/awesome-python) - Python 框架、库、软件和资源。
*   [Awesome-Go](https://github.com/avelino/awesome-go) - Go 框架、库和软件。
*   [Awesome-JavaScript](https://github.com/sorrycc/awesome-javascript) - 浏览器端 JavaScript 库、资源。
*   [Awesome-Rust](https://github.com/rust-unofficial/awesome-rust) - Rust 代码和资源。
*   [Awesome-Java](https://github.com/akullpp/awesome-java) - Java 框架、库和软件。
*   [Awesome-Cpp](https://github.com/fffaraz/awesome-cpp) - C++ 框架、库和资源。
*   [Awesome-PHP](https://github.com/ziadoz/awesome-php) - PHP 库、资源和闪亮的东西。
*   [Awesome-Ruby](https://github.com/markets/awesome-ruby) - Ruby 资源集合。
*   [Awesome-Swift](https://github.com/matteocrippa/awesome-swift) - Swift 资源集合。
*   [Awesome-Kotlin](https://github.com/KotlinBy/awesome-kotlin) - Kotlin 资源集合。
*   [Awesome-TypeScript](https://github.com/dzharii/awesome-typescript) - TypeScript 资源。
*   [Awesome-CSharp](https://github.com/uhub/awesome-csharp) - C# 框架、库和软件。
*   [Awesome-Scala](https://github.com/lauris/awesome-scala) - Scala 库、框架和软件。
*   [Awesome-Elixir](https://github.com/h4cc/awesome-elixir) - Elixir 库、文章、视频等。
*   [Awesome-Haskell](https://github.com/krispo/awesome-haskell) - Haskell 资源。
*   [Awesome-Clojure](https://github.com/razum2um/awesome-clojure) - Clojure 资源。
*   [Awesome-Lua](https://github.com/LewisJEllis/awesome-lua) - Lua 资源。
*   [Awesome-Perl](https://github.com/hachiojipm/awesome-perl) - Perl 资源。
*   [Awesome-OCaml](https://github.com/ocaml-community/awesome-ocaml) - OCaml 资源。
*   [Awesome-R](https://github.com/qinwf/awesome-R) - R 语言资源。
*   [Awesome-D](https://github.com/dlang-community/awesome-d) - D 语言资源。
*   [Awesome-Elm](https://github.com/sporto/awesome-elm) - Elm 语言资源。
*   [Awesome-Erlang](https://github.com/drobakowski/awesome-erlang) - Erlang 资源。
*   [Awesome-Julia](https://github.com/svaksha/Julia.jl) - Julia 语言资源。
*   [Awesome-Crystal](https://github.com/veelenga/awesome-crystal) - Crystal 语言资源。
*   [Awesome-Nim](https://github.com/ringabout/awesome-nim) - Nim 语言资源。
*   [Awesome-Zig](https://github.com/catdevnull/awesome-zig) - Zig 语言资源。
*   [Awesome-FSharp](https://github.com/fsprojects/Awesome-FSharp) - F# 资源。
*   [Awesome-Dart](https://github.com/yissachar/awesome-dart) - Dart 语言资源。
*   [Awesome-V](https://github.com/vlang/awesome-v) - V 语言资源。
*   [Awesome-Assembly](https://github.com/jaspergould/awesome-assembly) - 汇编语言资源。

#### 前端开发

*   [Awesome-React](https://github.com/enaqx/awesome-react) - React 生态系统资源。
*   [Awesome-Vue](https://github.com/vuejs/awesome-vue) - Vue.js 资源。
*   [Awesome-Angular](https://github.com/gdi2290/awesome-angular) - Angular 资源。
*   [Awesome-Svelte](https://github.com/TheComputerM/awesome-svelte) - Svelte 资源。
*   [Awesome-Nodejs](https://github.com/sindresorhus/awesome-nodejs) - Node.js 包和资源。
*   [Awesome-CSS](https://github.com/awesome-css-group/awesome-css) - CSS 框架、预处理器、库和样式指南。
*   [Awesome-Tailwindcss](https://github.com/aniftyco/awesome-tailwindcss) - Tailwind CSS 资源。
*   [Awesome-Nextjs](https://github.com/unicodeveloper/awesome-nextjs) - Next.js 资源。
*   [Awesome-Web-Performance-Budget](https://github.com/pajaydev/awesome-web-performance-budget) - Web 性能预算资源。
*   [Awesome-Storybook](https://github.com/lauthieb/awesome-storybook) - Storybook 资源。
*   [Awesome-WPO](https://github.com/davidsonfellipe/awesome-wpo) - Web 性能优化资源。
*   [Awesome-D3](https://github.com/wbkd/awesome-d3) - D3.js 资源。
*   [Awesome-GraphQL](https://github.com/chentsulin/awesome-graphql) - GraphQL 和 Relay 资源。
*   [Awesome-Web-Animation](https://github.com/sergey-pimenov/awesome-web-animation) - Web 动画资源。

#### 后端开发

*   [Awesome-Django](https://github.com/wsvincent/awesome-django) - Django 资源。
*   [Awesome-Flask](https://github.com/humiaozuzu/awesome-flask) - Flask 资源。
*   [Awesome-Laravel](https://github.com/chiraggude/awesome-laravel) - Laravel 框架资源。
*   [Awesome-Spring](https://github.com/Sigma-Spring/Awesome-Spring) - Spring 生态系统项目。
*   [Awesome-NestJS](https://github.com/juliandavidmr/awesome-nestjs) - NestJS 资源。
*   [Awesome-FastAPI](https://github.com/mjhea0/awesome-fastapi) - FastAPI 资源。
*   [Awesome-Rails](https://github.com/gramantin/awesome-rails) - Ruby on Rails 资源。
*   [Awesome-Serverless](https://github.com/pmuens/awesome-serverless) - Serverless 架构、框架和资源。
*   [Awesome-API](https://github.com/Kikobeats/awesome-api) - API 设计和开发资源。
*   [Awesome-AdonisJS](https://github.com/adonisjs-community/awesome-adonisjs) - AdonisJS 资源。

#### 计算机科学 & 软件工程

*   [Awesome-CS-Courses](https://github.com/prakhar1989/awesome-cs-courses) - 大学里的计算机科学课程。
*   [Awesome-Algorithms](https://github.com/tayllan/awesome-algorithms) - 算法和数据结构学习资源。
*   [Awesome-Design-Patterns](https://github.com/DovAmir/awesome-design-patterns) - 软件设计模式资源。
*   [Awesome-Compilers](https://github.com/aalhour/awesome-compilers) - 编译器、解释器和运行时资源。
*   [Awesome-Distributed-Systems](https://github.com/theanalyst/awesome-distributed-systems) - 分布式系统资源。
*   [Awesome-Concurrency](https://github.com/lukasz-madon/awesome-concurrency) - 并发编程资源。
*   [Awesome-Clean-Code](https://github.com/JuanCrg90/Clean-Code-Notes) - 《代码整洁之道》笔记与实践。
*   [Awesome-Testing](https://github.com/TheJambo/awesome-testing) - 软件测试资源。
*   [Awesome-Devops](https://github.com/bregman-arie/awesome-devops) - DevOps 工具、文化和资源。
*   [Awesome-SRE](https://github.com/dastergon/awesome-sre) - 网站可靠性工程资源。
*   [Awesome-System-Design](https://github.com/maddhruv/awesome-system-design) - 系统设计资源。
*   [Awesome-Computer-Vision](https://github.com/jbhuang0604/awesome-computer-vision) - 计算机视觉资源。
*   [Awesome-NLP](https://github.com/keon/awesome-nlp) - 自然语言处理资源。
*   [Awesome-Mathematics](https://github.com/rossant/awesome-math) - 数学资源。

#### 网络安全

*   [Awesome-Hacking](https://github.com/carpedm20/awesome-hacking) - 黑客与安全资源（再次强调，因为太重要）。
*   [Awesome-Pentest](https://github.com/enaqx/awesome-pentest) - 渗透测试资源。
*   [Awesome-Web-Security](https://github.com/qazbnm456/awesome-web-security) - Web 安全资源。
*   [Awesome-Cybersecurity-Blue-Team](https://github.com/fabacab/awesome-cybersecurity-blueteam) - 蓝队防御资源。
*   [Awesome-Red-Teaming](https://github.com/yeyintminthuhtut/Awesome-Red-Teaming) - 红队资源。
*   [Awesome-Threat-Intelligence](https://github.com/hslatman/awesome-threat-intelligence) - 威胁情报资源。
*   [Awesome-OSINT](https://github.com/jivoi/awesome-osint) - 开源情报资源。
*   [Awesome-Malware-Analysis](https://github.com/rshipp/awesome-malware-analysis) - 恶意软件分析工具和资源。
*   [Awesome-CTF](https://github.com/apsdehal/awesome-ctf) - CTF 框架、库、资源。
*   [Awesome-Honeypots](https://github.com/paralax/awesome-honeypots) - 蜜罐资源。
*   [Awesome-Fuzzing](https://github.com/cpuu/awesome-fuzzing) - Fuzzing 测试资源。
*   [Awesome-Reverse-Engineering](https://github.com/alphaSeclab/awesome-reverse-engineering) - 逆向工程资源。
*   [Awesome-Exploit-Development](https://github.com/FabioBaroni/awesome-exploit-development) - Exploit 开发资源。
*   [Awesome-Incident-Response](https://github.com/meirwah/awesome-incident-response) - 应急响应资源。
*   [Awesome-Forensics](https://github.com/mre/awesome-forensics) - 数字取证资源。
*   [Awesome-Cryptography](https://github.com/sobolevn/awesome-cryptography) - 密码学资源和工具。
*   [Awesome-API-Security](https://github.com/arainho/awesome-api-security) - API 安全资源。
*   [Awesome-Cloud-Security](https://github.com/4ndersonLin/awesome-cloud-security) - 云安全资源。
*   [Awesome-Container-Security](https://github.com/kai5263499/awesome-container-security) - 容器安全资源。
*   [Awesome-AI-Security](https://github.com/Deep-Learning-Security/Awesome-AI-Security) - AI 安全资源。
*   [Awesome-Web3-Security](https://github.com/Anugrahsr/Awesome-Web3-Security) - Web3 安全资源。
*   [Awesome-Vehicle-Security](https://github.com/jaredthecoder/awesome-vehicle-security) - 汽车安全资源。
*   [Awesome-Embedded-and-IoT-Security](https://github.com/fkie-cad/awesome-embedded-and-iot-security) - 嵌入式与物联网安全。

#### 人工智能 & 数据科学

*   [Awesome-Machine-Learning](https://github.com/josephmisiti/awesome-machine-learning) - 机器学习框架、库和软件。
*   [Awesome-Deep-Learning](https://github.com/ChristosChristofidis/awesome-deep-learning) - 深度学习教程、项目和社区。
*   [Awesome-Data-Science](https://github.com/academic/awesome-datascience) - 数据科学资源。
*   [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) - 大语言模型资源。
*   [Awesome-Reinforcement-Learning](https://github.com/aikorea/awesome-rl) - 强化学习资源。
*   [Awesome-MLOps](https://github.com/visenger/awesome-mlops) - MLOps 平台和工具。
*   [Awesome-Prompt-Engineering](https://github.com/prompt-engineering/awesome-prompt-engineering) - 提示工程资源。
*   [Awesome-PyTorch](https://github.com/bharathgs/Awesome-pytorch-list) - PyTorch 资源。
*   [Awesome-TensorFlow](https://github.com/jtoy/awesome-tensorflow) - TensorFlow 资源。
*   [Awesome-Data-Engineering](https://github.com/igorbarinov/awesome-data-engineering) - 数据工程工具和资源。
*   [Awesome-Big-Data](https://github.com/onurakpolat/awesome-bigdata) - 大数据资源。
*   [Awesome-Deep-Vision](https://github.com/kjw0612/awesome-deep-vision) - 深度学习在计算机视觉中的应用。
*   [Awesome-AI-in-Finance](https://github.com/georgezouq/awesome-ai-in-finance) - AI 在金融领域的应用。

#### 硬件 & 底层

*   [Awesome-Embedded-Systems](https://github.com/nhivp/Awesome-Embedded) - 嵌入式系统资源。
*   [Awesome-Electronics](https://github.com/kitspace/awesome-electronics) - 电子工程资源。
*   [Awesome-IoT](https://github.com/HQarroum/awesome-iot) - 物联网资源。
*   [Awesome-Robotics](https://github.com/jslee02/awesome-robotics) - 机器人技术资源。
*   [Awesome-Vulkan](https://github.com/vinjn/awesome-vulkan) - Vulkan API 资源。
*   [Awesome-OpenGL](https://github.com/eug/awesome-opengl) - OpenGL 库、教程等。
*   [Awesome-WebAssembly](https://github.com/mbasso/awesome-wasm) - WebAssembly 资源。
*   [Awesome-RISC-V](https://github.com/drom/awesome-riscv) - RISC-V 设计和实现的资源。
*   [Awesome-Quantum-Computing](https://github.com/desireevl/awesome-quantum-computing) - 量子计算资源。

#### 游戏开发 & 图形

*   [Awesome-Game-Development](https://github.com/ellisonleao/magictools) - 游戏开发资源。
*   [Awesome-Game-Engine-Dev](https://github.com/stevinz/awesome-game-engine-dev) - 游戏引擎开发资源。
*   [Awesome-Graphics](https://github.com/ericjang/awesome-graphics) - 计算机图形学资源。
*   [Awesome-Unity](https://github.com/RyanNielson/awesome-unity) - Unity 游戏引擎资源。
*   [Awesome-Godot](https://github.com/godotengine/awesome-godot) - Godot 游戏引擎资源。
*   [Awesome-Creative-Coding](https://github.com/terkelg/awesome-creative-coding) - 创意编码资源。
*   [Awesome-AR-VR](https://github.com/huningxin/awesome-arvr) - 增强现实与虚拟现实资源。

#### 其他

*   [Awesome-for-Beginners](https://github.com/MunGell/awesome-for-beginners) - 对新手友好的开源项目。
*   [Awesome-Remote-Work](https://github.com/lukasz-madon/awesome-remote-job) - 远程工作资源。
*   [Awesome-Technical-Writing](https://github.com/BolajiAyodeji/awesome-technical-writing) - 技术写作资源。
*   [Awesome-Design](https://github.com/gztchan/awesome-design) - 为开发者准备的设计工具和资源。
*   [Awesome-Stock-Resources](https://github.com/neutraltone/awesome-stock-resources) - 免费的图片、视频、音频等素材资源。
*   [Awesome-Podcasts](https://github.com/rShetty/awesome-podcasts) - 开发者喜欢的播客。
*   [Awesome-Newsletters](https://github.com/zudochkin/awesome-newsletters) - 值得订阅的技术简报。
*   [Awesome-Talks](https://github.com/JanVanRyswyck/awesome-talks) - 精彩的技术演讲。
*   [Awesome-Indie](https://github.com/mezod/awesome-indie) - 独立开发者的资源。
*   [Awesome-Fintech](https://github.com/moov-io/awesome-fintech) - 金融科技资源。
*   [Awesome-Health](https://github.com/prabhic/awesome-health) - 健康科技资源。
*   [Awesome-Open-Source-Documents](https://github.com/42-AI/awesome-open-source-documents) - 开源文档集合。
*   [Awesome-Scientific-Writing](https://github.com/writing-resources/awesome-scientific-writing) - 科学写作资源。
*   [Awesome-Product-Management](https://github.com/dend/awesome-product-management) - 产品管理资源。
*   [Awesome-Sysadmin](https://github.com/awesome-foss/awesome-sysadmin) - 系统管理员资源。
*   [Awesome-CLI-Apps](https://github.com/agarrharr/awesome-cli-apps) - 优秀的命令行应用。
*   [Awesome-Shell](https://github.com/alebcay/awesome-shell) - Shell 工具和资源。
*   [Awesome-Zsh-Plugins](https://github.com/unixorn/awesome-zsh-plugins) - Zsh 插件和主题。
*   [Awesome-Home-Assistant](https://github.com/frenck/awesome-home-assistant) - Home Assistant 资源。
*   [Awesome-3D-Printing](https://github.com/yutannihilation/awesome-3d-printing) - 3D 打印资源。
*   [Awesome-Bioinformatics](https://github.com/danielecook/Awesome-Bioinformatics) - 生物信息学资源。
*   [Awesome-Blockchain-AI](https://github.com/steven2358/awesome-blockchain-ai) - 区块链与 AI 结合的资源。
*   [Awesome-CSV](https://github.com/secretGeek/AwesomeCSV) - CSV 工具和库。
*   [Awesome-Dataviz](https://github.com/javierluraschi/awesome-dataviz) - 数据可视化资源。
*   [Awesome-Deep-Learning-Music](https://github.com/ybayle/awesome-deep-learning-music) - 深度学习在音乐领域的应用。
*   [Awesome-Economics](https://github.com/antontarasenko/awesome-economics) - 经济学资源。
*   [Awesome-Flutter](https://github.com/Solido/awesome-flutter) - Flutter 资源。
*   [Awesome-IPFS](https://github.com/ipfs/awesome-ipfs) - IPFS 资源。
*   [Awesome-Jupyter](https://github.com/markusschanta/awesome-jupyter) - Jupyter 项目、库和资源。
*   [Awesome-Observables](https://github.com/sindresorhus/awesome-observables) - Observables 资源。
*   [Awesome-PICO-8](https://github.com/pico-8/awesome-PICO-8) - PICO-8 资源。
*   [Awesome-Privacy](https://github.com/pluja/awesome-privacy) - 保护隐私的工具和服务。
*   [Awesome-Progressive-Web-Apps](https://github.com/TalAter/awesome-progressive-web-apps) - PWA 资源。
*   [Awesome-React-Native](https://github.com/jondot/awesome-react-native) - React Native 资源。
*   [Awesome-Robotics-Libraries](https://github.com/Kiloreux/awesome-robotics-libraries) - 机器人库。
*   [Awesome-Selenium](https://github.com/christian-bromann/awesome-selenium) - Selenium 资源。
*   [Awesome-Static-Website-Services](https://github.com/agarrharr/awesome-static-website-services) - 静态网站服务。
*   [Awesome-Streaming](https://github.com/manuzhang/awesome-streaming) - 流媒体技术资源。
*   [Awesome-Web-Archiving](https://github.com/iipc/awesome-web-archiving) - Web 归档资源。
*   [Awesome-Web-Design](https://github.com/nicolesaidy/awesome-web-design) - Web 设计资源。
*   [Awesome-Web-Monetization](https://github.com/thomasbnt/awesome-web-monetization) - Web 盈利资源。
*   [Awesome-Xamarin](https://github.com/XamSome/awesome-xamarin) - Xamarin 资源。

---

## 计算机科学与软件工程

#### 2.1 综合学习路径 & 课程

*   [OSSU Computer Science](https://github.com/ossu/computer-science) - 开源社区大学的完整计算机科学自学课程。
*   [Developer Roadmap](https://github.com/kamranahmedse/developer-roadmap) - 成为各类开发者的学习路径图，非常全面。
*   [Coding Interview University](https://github.com/jwasham/coding-interview-university) - 成为软件工程师的完整自学计划，尤其适合面试准备。
*   [CS-Courses](https://github.com/prakhar1989/awesome-cs-courses) - 来自世界名校的计算机科学课程列表。
*   [Free Programming Books](https://github.com/EbookFoundation/free-programming-books) - 海量的免费编程电子书。
*   [Project Based Learning](https://github.com/practical-tutorials/project-based-learning) - 通过构建实际项目来学习编程的教程列表。
*   [Build Your Own X](https://github.com/codecrafters-io/build-your-own-x) - 从零开始构建自己的数据库、操作系统、机器人等的教程集合。
*   [The Art of Computer Science](https://github.com/The-Art-of-Computer-Science/The-Art-of-Computer-Science) - 现代计算机科学自学指南。
*   [CS-Notes](https://github.com/CyC2018/CS-Notes) - 技术面试必备基础知识、Leetcode 题解。
*   [Tech Interview Handbook](https://github.com/yangshun/tech-interview-handbook) - 为忙碌工程师准备的免费技术面试资源。
*   [Teach Yourself CS](https://github.com/ossu/computer-science/blob/master/README.md) - (已包含在 OSSU 中) 自学计算机科学的经典指南。
*   [Every Programmer Should Know](https://github.com/mtdvio/every-programmer-should-know) - 程序员应知应会的知识点列表。
*   [Free for Dev](https://github.com/ripienaar/free-for-dev) - 为开发者提供的免费 SaaS、PaaS、IaaS 等服务。
*   [Professional Programming](https://github.com/charlax/professional-programming) - 成为更专业程序员的资源集合。
*   [What the f*ck Python!](https://github.com/satwikkansal/wtfpython) - 有趣的 Python 代码片段，帮助理解语言细节。
*   [Computer Science](https://github.com/springboard-curriculum/computer-science-fundamentals) - Springboard 的计算机科学基础课程。

#### 2.2 算法与数据结构

*   [The Algorithms - Python](https://github.com/TheAlgorithms/Python) - 所有算法的 Python 实现。
*   [The Algorithms - Java](https://github.com/TheAlgorithms/Java) - 所有算法的 Java 实现。
*   [The Algorithms - C++](https://github.com/TheAlgorithms/C_Plus_Plus) - 所有算法的 C++ 实现。
*   [The Algorithms - JavaScript](https://github.com/TheAlgorithms/JavaScript) - 所有算法的 JavaScript 实现。
*   [The Algorithms - Go](https://github.com/TheAlgorithms/Go) - 所有算法的 Go 实现。
*   [Awesome Algorithms](https://github.com/tayllan/awesome-algorithms) - 算法和数据结构学习资源。
*   [LeetCode](https://github.com/azl397985856/leetcode) - LeetCode 题解（多种语言）。
*   [Algorithm Visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer) - 交互式的算法可视化工具。
*   [Algorithms](https://github.com/keon/algorithms) - 最小化的、人类可读的算法实现。
*   [Hello-Algorithm](https://github.com/krahets/hello-algo) - 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。
*   [Structure and Interpretation of Computer Programs](https://github.com/sarabander/sicp) - 《计算机程序的构造和解释》电子版。
*   [Competitive Programming](https://github.com/lnishan/awesome-competitive-programming) - 算法竞赛资源。
*   [Problem-Solving-with-Algorithms-and-Data-Structures-using-Python](https://github.com/runestone/pythonds) - 使用 Python 解决算法和数据结构问题。
*   [DSA-Bootcamp-Java](https://github.com/kunal-kushwaha/DSA-Bootcamp-Java) - Kunal Kushwaha 的数据结构与算法训练营。
*   [Mastering-Go-Third-Edition](https://github.com/mlowicki/Mastering-Go-Third-Edition) - 《Mastering Go》第三版，包含并发和数据结构。
*   [Sedgewick-Algorithms](https://github.com/reneargento/algorithms-sedgewick-wayne) - Sedgewick 和 Wayne 的《算法》一书的解法。

#### 2.3 系统设计 & 架构

*   [System Design Primer](https://github.com/donnemartin/system-design-primer) - 学习如何设计可扩展的系统，面试必备。
*   [Awesome System Design](https://github.com/maddhruv/awesome-system-design) - 系统设计资源集合。
*   [Grokking the System Design Interview](https://github.com/Jeevan-kumar-Raj/Grokking-the-System-Design-Interview) - 系统设计面试的经典教程。
*   [Systems Design Cheatsheet](https://github.com/karanpratapsingh/system-design) - 系统设计速查表。
*   [Designing Data-Intensive Applications](https://github.com/andres-fr/data-intensive-applications-notes) - 《设计数据密集型应用》的笔记。
*   [Awesome Microservices](https://github.com/mfornos/awesome-microservices) - 微服务架构模式、框架和资源。
*   [Microservices-Patters](https://github.com/microservices-patterns/ftgo-application) - 《微服务模式》一书的示例代码。
*   [Awesome Scalability](https://github.com/binhnguyennus/awesome-scalability) - 可扩展性、可用性和稳定性模式的阅读列表。
*   [The System Design Manual](https://github.com/system-design-ops/system-design) - 系统设计手册。
*   [System-Design-Interview-An-Insiders-Guide](https://github.com/resumejob/system-design-interview) - 《系统设计面试》相关资源。
*   [Cloud Design Patterns](https://github.com/mspnp/cloud-design-patterns) - 微软官方的云设计模式。
*   [Architecture of Open Source Applications](http://aosabook.org/en/index.html) - 开源应用架构剖析。
*   [Web-Architecture-101](https://github.com/matiassingers/web-architecture-101) - Web 架构基础。
*   [Software-Architecture-And-Design-Patterns](https://github.com/MagalixCorp/Software-Architecture-And-Design-Patterns) - 软件架构与设计模式。
*   [How-web-works](https://github.com/vasanthk/how-web-works) - Web 工作原理的简单解释。

#### 2.4 软件工程实践 & DevOps

*   [Awesome DevOps](https://github.com/bregman-arie/awesome-devops) - DevOps 工具、文化和资源。
*   [Awesome SRE](https://github.com/dastergon/awesome-sre) - 网站可靠性工程（SRE）资源。
*   [Awesome Design Patterns](https://github.com/DovAmir/awesome-design-patterns) - 软件设计模式资源。
*   [Refactoring.Guru](https://github.com/Refactoring-Guru/design-patterns-python) - 设计模式的 Python 实现。
*   [Source-Making-Design-Patterns](https://github.com/iluwatar/java-design-patterns) - Java 设计模式实现。
*   [Awesome Testing](https://github.com/TheJambo/awesome-testing) - 软件测试资源、工具和技术。
*   [Awesome Clean Code](https://github.com/JuanCrg90/Clean-Code-Notes) - 《代码整洁之道》笔记与实践。
*   [The Art of Readable Code](https://github.com/YegorBugayenko/the-art-of-readable-code) - 《编写可读代码的艺术》相关资源。
*   [Software Engineering at Google](https://github.com/google/eng-practices) - Google 的工程实践文档。
*   [97-Things-Every-Programmer-Should-Know](https://github.com/97-things/97-things-every-programmer-should-know) - 每个程序员都应该知道的 97 件事。
*   [The Book of Secret Knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) - 系统管理员、渗透测试人员、开发人员等的笔记和清单。
*   [Awesome CI/CD](https://github.com/ciandcd/awesome-ciandcd) - 持续集成和持续部署资源。
*   [Awesome Production Machine Learning](https://github.com/EthicalML/awesome-production-machine-learning) - 生产环境机器学习资源。
*   [Git-Best-Practices](https://github.com/k88hudson/git-flight-rules) - Git 飞行规则，最佳实践指南。
*   [API-Security-Checklist](https://github.com/shieldfy/API-Security-Checklist) - 构建安全 API 的清单。
*   [The-Pragmatic-Programmer](https://github.com/pragmaticprogrammer/pragmatic_programmer_20th_anniversary_edition) - 《程序员的修炼》相关资源。
*   [Awesome Agile](https://github.com/lorabv/awesome-agile) - 敏捷软件开发资源。
*   [Awesome-README](https://github.com/matiassingers/awesome-readme) - 优秀的 README 范例。

#### 2.5 操作系统 & 底层原理

*   [Awesome Operating Systems](https://github.com/jubalh/awesome-os) - 操作系统开发资源。
*   [Linux Kernel](https://github.com/torvalds/linux) - Linux 内核源码。
*   [Awesome Compilers](https://github.com/aalhour/awesome-compilers) - 编译器、解释器和运行时资源。
*   [Crafting Interpreters](https://github.com/munificent/craftinginterpreters) - 《构建解释器》一书的开源版本。
*   [Writing an OS in Rust](https://github.com/phil-opp/blog_os) - 在 Rust 中编写一个操作系统的博客系列。
*   [The little book about OS development](https://github.com/littleosbook/littleosbook) - 关于操作系统开发的小书。
*   [xv6-riscv](https://github.com/mit-pdos/xv6-riscv) - MIT 的教学操作系统 xv6 的 RISC-V 版本。
*   [Awesome Concurrency](https://github.com/lukasz-madon/awesome-concurrency) - 并发编程资源。
*   [Computer-Networking-A-Top-Down-Approach-Solutions](https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-Solutions) - 《计算机网络：自顶向下方法》答案。
*   [Dive into Systems](https://github.com/diveintosystems/diveintosystems.github.io) - 一本免费的计算机系统入门书籍。
*   [Operating Systems: Three Easy Pieces](http://pages.cs.wisc.edu/~remzi/OSTEP/) - 经典的操作系统教材。
*   [Awesome-Virtualization](https://github.com/WJCarpenter/awesome-virtualization) - 虚拟化技术资源。
*   [Awesome-LLVM](https://github.com/HongxuChen/awesome-llvm) - LLVM 相关资源。
*   [Linux-Insides](https://github.com/0xAX/linux-insides) - 深入 Linux 内核。
*   [What Happens When You Type a URL in the Browser](https://github.com/alex/what-happens-when) - 当你在浏览器中输入 URL 后发生了什么。

#### 2.6 数据库

*   [Awesome Database](https://github.com/numetriclabz/awesome-db) - 数据库工具和资源。
*   [Awesome-Postgres](https://github.com/dhamaniasad/awesome-postgres) - PostgreSQL 资源。
*   [Awesome-MySQL](https://github.com/shlomi-noach/awesome-mysql) - MySQL 资源。
*   [Awesome-SQLite](https://github.com/planet-sqlite/awesome-sqlite) - SQLite 资源。
*   [Awesome-Redis](https://github.com/JamzyWang/awesome-redis) - Redis 资源。
*   [Awesome-MongoDB](https://github.com/ramnes/awesome-mongodb) - MongoDB 资源。
*   [Database-Systems-Design-Implementation-and-Management](https://github.com/pingcap/awesome-database-learning) - 数据库学习资源。
*   [Use-The-Index-Luke](https://github.com/unindexed/use-the-index-luke) - SQL 索引指南。
*   [SQL-style-guide](https://github.com/simonholywell/sql-style-guide) - SQL 风格指南。
*   [Advanced-SQL](https://github.com/s-shemmee/advanced-sql) - 高级 SQL 技巧。
*   [DB-Engines](https://db-engines.com/en/ranking) - 数据库流行度排名。

#### 2.7 数学 & 理论基础

*   [Awesome Mathematics](https://github.com/rossant/awesome-math) - 数学资源。
*   [Awesome Cryptography](https://github.com/sobolevn/awesome-cryptography) - 密码学资源。
*   [Awesome-Information-Theory](https://github.com/soroushz/awesome-information-theory) - 信息论资源。
*   [3Blue1Brown](https://github.com/3b1b/manim) - 著名数学可视化视频背后的动画引擎。
*   [Project Euler](https://github.com/nayuki/Project-Euler-solutions) - 欧拉计划问题解法。
*   [Math-as-code](https://github.com/Jam3/math-as-code) - 将数学公式翻译成代码的备忘单。
*   [Homotopy Type Theory](https://github.com/HoTT/book) - 同伦类型理论书籍。
*   [Awesome-Calculus](https://github.com/e-kol/awesome-calculus) - 微积分资源。
*   [Awesome-Linear-Algebra](https://github.com/vochicong/awesome-linear-algebra) - 线性代数资源。
*   [Probability-and-Statistics-Ebook](https://github.com/chervwood/Probability-and-Statistics-Ebook) - 概率与统计电子书。

#### 2.8 其他 & 杂项

*   [Awesome-Falsehood](https://github.com/kdeldycke/awesome-falsehood) - 程序员对于各种概念的错误认知列表。
*   [Awesome-Unicode](https://github.com/jagracey/Awesome-Unicode) - Unicode 资源。
*   [Awesome-Talks](https://github.com/JanVanRyswyck/awesome-talks) - 精彩的技术演讲。
*   [Computer-Science-From-the-Bottom-Up](https://github.com/ianw/bottomupcs) - 从零开始的计算机科学。
*   [How to Design Programs](https://github.com/HtDP/2e) - 《如何设计程序》第二版。
*   [Nand to Tetris](https://www.nand2tetris.org/) - 从与非门到俄罗斯方块，构建一台现代计算机。
*   [Go-SCP](https://github.com/bramvdbogaerde/go-scp) - Go 实现的 SCP 客户端。
*   [Public-APIs](https://github.com/public-apis/public-apis) - 用于开发和测试的免费公共 API 列表。
*   [Learn-anything](https://github.com/learn-anything/learn-anything) - 带有交互式思维导图的学习路径。
*   [The-Art-of-Command-Line](https://github.com/jlevy/the-art-of-command-line) - 命令行使用艺术。
*   [Gitignore](https://github.com/github/gitignore) - 有用的 `.gitignore` 模板集合。
*   [Big-List-of-Naughty-Strings](https://github.com/minimaxir/big-list-of-naughty-strings) - 用于测试的“淘气”字符串列表。
*   [Awesome-Analytics](https://github.com/newhouse/awesome-analytics) - 分析工具和服务。
*   [Awesome-Public-Datasets](https://github.com/awesomedata/awesome-public-datasets) - 高质量的公共数据集。
*   [Awesome-Technical-Writing](https://github.com/BolajiAyodeji/awesome-technical-writing) - 技术写作资源。
*   [Awesome-Scientific-Writing](https://github.com/writing-resources/awesome-scientific-writing) - 科学写作资源。
*   [Awesome-Product-Management](https://github.com/dend/awesome-product-management) - 产品管理资源。
*   [Awesome-Sysadmin](https://github.com/awesome-foss/awesome-sysadmin) - 系统管理员资源。

---

## 编程语言

#### 3.1 综合 & 多语言资源

*   [Awesome Languages](https://github.com/abhishek-pandey/awesome-languages) - 所有编程语言的 Awesome 列表集合。
*   [Learn X in Y minutes](https://github.com/adambard/learnxinyminutes-docs) - 在 Y 分钟内快速学习 X 语言的简明教程。
*   [Programming Language Zoo](https://github.com/andrejbauer/plzoo) - 各种编程语言特性和实现的集合。
*   [Awesome Polyglot](https://github.com/bast/awesome-polyglot) - 多语言编程资源。
*   [Hyperpolyglot](http://hyperpolyglot.org/) - 常见编程语言的语法并排比较。
*   [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code) - 用不同语言实现相同任务的编程示例。
*   [Awesome Compilers](https://github.com/aalhour/awesome-compilers) - 编译器、解释器和运行时资源，与语言设计密切相关。
*   [Crafting Interpreters](https://github.com/munificent/craftinginterpreters) - 开源书籍，教你如何构建解释器。
*   [Build Your Own Lisp](http://www.buildyourownlisp.com/) - 用 C 语言编写自己的 Lisp。
*   [Programming-Language-Benchmarks](https://github.com/drujensen/fib) - 不同语言的斐波那契数列性能基准测试。
*   [The Computer Language Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/) - 各种语言的性能评测。

#### 3.2 C & C++

*   [Awesome Cpp](https://github.com/fffaraz/awesome-cpp) - C++ 框架、库和资源。
*   [Awesome C](https://github.com/inputsh/awesome-c) - C 语言框架、库和资源。
*   [C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines) - C++ 核心指南，由 Bjarne Stroustrup 等人编写。
*   [Modern C++](https://github.com/rigtorp/awesome-modern-cpp) - 现代 C++ (11/14/17/20) 资源。
*   [The C++ Standard Library](https://github.com/sol-prog/The-C-Standard-Library-by-Example) - C++ 标准库示例。
*   [Google Test](https://github.com/google/googletest) - Google 的 C++ 测试框架。
*   [JSON for Modern C++](https://github.com/nlohmann/json) - 现代 C++ 的 JSON 库。
*   [ImGui](https://github.com/ocornut/imgui) - 无依赖的、即时模式的图形用户界面库。
*   [vcpkg](https://github.com/microsoft/vcpkg) - C++ 包管理器。
*   [CMake](https://github.com/Kitware/CMake) - 跨平台的构建、测试和打包工具。
*   [OpenCV](https://github.com/opencv/opencv) - 开源计算机视觉库。
*   [Boost C++ Libraries](https://github.com/boostorg/boost) - 高质量的 C++ 库集合。
*   [fmt](https://github.com/fmtlib/fmt) - 现代 C++ 的格式化库。
*   [spdlog](https://github.com/gabime/spdlog) - 快速的、仅头文件的 C++ 日志库。
*   [gRPC](https://github.com/grpc/grpc) - 高性能、开源的通用 RPC 框架。
*   [Protobuf](https://github.com/protocolbuffers/protobuf) - Google 的数据交换格式。
*   [Effective Modern C++](https://github.com/federico-busato/Modern-CPP-Programming) - 《Effective Modern C++》相关资源。
*   [libuv](https://github.com/libuv/libuv) - 跨平台的异步 I/O 库 (Node.js 的核心)。
*   [PicoHTTPParser](https://github.com/h2o/picohttpparser) - 微小的、快速的 HTTP 解析器。
*   [Crow](https://github.com/CrowCpp/Crow) - 快速、易用的 C++ 微型 Web 框架。

#### 3.3 Python

*   [Awesome Python](https://github.com/vinta/awesome-python) - Python 框架、库、软件和资源。
*   [Awesome Python Applications](https://github.com/mahmoud/awesome-python-applications) - 开源的 Python 应用软件。
*   [Python-Guide](https://github.com/realpython/python-guide) - Python 最佳实践指南。
*   [Full Speed Python](https://github.com/joaoventura/full-speed-python) - 快速学习 Python 的书籍。
*   [Django](https://github.com/django/django) - 高级的 Python Web 框架。
*   [Flask](https://github.com/pallets/flask) - 轻量级的 Python Web 框架。
*   [FastAPI](https://github.com/tiangolo/fastapi) - 现代、快速的 Python Web 框架。
*   [Requests](https://github.com/psf/requests) - 优雅、简洁的 HTTP 库。
*   [Pandas](https://github.com/pandas-dev/pandas) - 强大的数据分析和操作库。
*   [NumPy](https://github.com/numpy/numpy) - Python 科学计算的基础包。
*   [Scikit-learn](https://github.com/scikit-learn/scikit-learn) - Python 机器学习库。
*   [Matplotlib](https://github.com/matplotlib/matplotlib) - Python 绘图库。
*   [Celery](https://github.com/celery/celery) - 分布式任务队列。
*   [Rich](https://github.com/Textualize/rich) - 在终端中创建丰富文本和漂亮格式的库。
*   [Black](https://github.com/psf/black) - 不妥协的 Python 代码格式化工具。
*   [Pytest](https://github.com/pytest-dev/pytest) - 成熟、功能齐全的 Python 测试框架。
*   [Pydantic](https://github.com/pydantic/pydantic) - 使用 Python 类型提示进行数据验证和设置管理。
*   [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) - Python SQL 工具包和对象关系映射器。
*   [Click](https://github.com/pallets/click) - 用于创建漂亮命令行界面的库。
*   [Streamlit](https://github.com/streamlit/streamlit) - 为机器学习和数据科学项目构建 Web 应用的最快方法。
*   [Poetry](https://github.com/python-poetry/poetry) - Python 依赖管理和打包工具。
*   [Manim](https://github.com/3b1b/manim) - 用于精确编程动画的引擎，由 3Blue1Brown 使用。

#### 3.4 JavaScript / TypeScript / Node.js

*   [Awesome JavaScript](https://github.com/sorrycc/awesome-javascript) - 浏览器端 JavaScript 库、资源。
*   [Awesome Node.js](https://github.com/sindresorhus/awesome-nodejs) - Node.js 包和资源。
*   [Awesome TypeScript](https://github.com/dzharii/awesome-typescript) - TypeScript 资源。
*   [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS) - 深入 JavaScript 核心机制的书籍系列。
*   [JavaScript-Algorithms](https://github.com/trekhleb/javascript-algorithms) - 基于 JavaScript 的算法和数据结构。
*   [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript) - Airbnb 的 JavaScript 风格指南。
*   [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices) - Node.js 最佳实践列表。
*   [React](https://github.com/facebook/react) - 用于构建用户界面的 JavaScript 库。
*   [Vue.js](https://github.com/vuejs/vue) - 渐进式 JavaScript 框架。
*   [Angular](https://github.com/angular/angular) - 基于 TypeScript 的 Web 应用框架。
*   [Svelte](https://github.com/sveltejs/svelte) - 将声明性组件转换为高效 JavaScript 代码的编译器。
*   [Express](https://github.com/expressjs/express) - 快速、无主见的、极简的 Node.js Web 框架。
*   [Next.js](https://github.com/vercel/next.js) - React 框架，用于生产环境。
*   [NestJS](https://github.com/nestjs/nest) - 用于构建高效、可扩展的 Node.js 服务器端应用的框架。
*   [D3.js](https://github.com/d3/d3) - 使用动态、交互式的数据可视化来操纵文档。
*   [Three.js](https://github.com/mrdoob/three.js) - JavaScript 3D 图形库。
*   [Lodash](https://github.com/lodash/lodash) - 提供模块化、性能和附加功能的现代 JavaScript 工具库。
*   [Axios](https://github.com/axios/axios) - 基于 Promise 的 HTTP 客户端，适用于浏览器和 Node.js。
*   [Jest](https://github.com/facebook/jest) - 令人愉快的 JavaScript 测试框架。
*   [Webpack](https://github.com/webpack/webpack) - 现代 JavaScript 应用的静态模块打包器。
*   [Vite](https://github.com/vitejs/vite) - 下一代前端开发与构建工具。
*   [ESLint](https://github.com/eslint/eslint) - 可插拔的 JavaScript 和 JSX linting 工具。
*   [Prettier](https://github.com/prettier/prettier) - 有主见的代码格式化工具。
*   [PM2](https://github.com/Unitech/pm2) - Node.js 应用的生产流程管理器。
*   [Puppeteer](https://github.com/puppeteer/puppeteer) - Headless Chrome Node.js API。

#### 3.5 Go

*   [Awesome Go](https://github.com/avelino/awesome-go) - Go 框架、库和软件。
*   [Go by Example](https://gobyexample.com/) - Go 语言示例教程。
*   [Gin](https://github.com/gin-gonic/gin) - Go 编写的 HTTP Web 框架。
*   [Echo](https://github.com/labstack/echo) - 高性能、可扩展、极简的 Go Web 框架。
*   [GORM](https://github.com/go-gorm/gorm) - Go 语言的 ORM 库。
*   [Cobra](https://github.com/spf13/cobra) - 用于创建强大现代 CLI 应用的库。
*   [Viper](https://github.com/spf13/viper) - Go 应用的完整配置解决方案。
*   [Go-Kit](https://github.com/go-kit/kit) - Go 微服务的标准库。
*   [Go-Micro](https://github.com/go-micro/go-micro) - 分布式系统开发框架。
*   [Colly](https://github.com/gocolly/colly) - 优雅、快速的爬虫和抓取框架。
*   [Fyne](https://github.com/fyne-io/fyne) - Go 编写的跨平台 UI 工具包。
*   [Bubble Tea](https://github.com/charmbracelet/bubbletea) - 用于构建交互式终端应用的 Go 框架。
*   [Testify](https://github.com/stretchr/testify) - Go 的断言工具包。
*   [The Go Programming Language](https://github.com/gopl-zh/gopl-zh.github.com) - 《Go 程序设计语言》中文翻译。
*   [Mastering Go](https://github.com/mlowicki/Mastering-Go-Third-Edition) - 《精通 Go》第三版。
*   [100 Go Mistakes](https://github.com/teivah/100-go-mistakes) - 100 个 Go 语言常见错误。

#### 3.6 Rust

*   [Awesome Rust](https://github.com/rust-unofficial/awesome-rust) - Rust 代码和资源。
*   [The Rust Programming Language](https://github.com/rust-lang/book) - 《Rust 程序设计语言》官方书籍。
*   [Rust by Example](https://github.com/rust-lang/rust-by-example) - Rust 示例教程。
*   [Tokio](https://github.com/tokio-rs/tokio) - 用于编写异步应用的运行时。
*   [Serde](https://github.com/serde-rs/serde) - Rust 数据的序列化框架。
*   [Actix-web](https://github.com/actix/actix-web) - 强大、实用且极速的 Rust Web 框架。
*   [Rocket](https://github.com/SergioBenitez/Rocket) - Rust 的 Web 框架，注重安全、速度和易用性。
*   [Diesel](https://github.com/diesel-rs/diesel) - 安全、可扩展的 ORM 和查询构建器。
*   [Rayon](https://github.com/rayon-rs/rayon) - Rust 的数据并行库。
*   [Clap](https://github.com/clap-rs/clap) - Rust 的命令行参数解析器。
*   [Bevy](https://github.com/bevyengine/bevy) - 一个简单的数据驱动的游戏引擎。
*   [Yew](https://github.com/yewstack/yew) - 使用 WebAssembly 构建多线程前端 Web 应用的 Rust 框架。
*   [Tauri](https://github.com/tauri-apps/tauri) - 使用 Web 前端构建更小、更快、更安全的桌面应用。
*   [Alacritty](https://github.com/alacritty/alacritty) - 跨平台的、GPU 加速的终端模拟器。
*   [Bat](https://github.com/sharkdp/bat) - 带有语法高亮和 Git 集成的 `cat` 克隆。
*   [Ripgrep](https://github.com/BurntSushi/ripgrep) - 递归地在目录中搜索正则表达式模式的行导向搜索工具。
*   [Exa](https://github.com/ogham/exa) - `ls` 的现代替代品。

#### 3.7 Java & JVM 生态

*   [Awesome Java](https://github.com/akullpp/awesome-java) - Java 框架、库和软件。
*   [Awesome Kotlin](https://github.com/KotlinBy/awesome-kotlin) - Kotlin 资源。
*   [Awesome Scala](https://github.com/lauris/awesome-scala) - Scala 资源。
*   [Awesome Clojure](https://github.com/razum2um/awesome-clojure) - Clojure 资源。
*   [Spring Framework](https://github.com/spring-projects/spring-framework) - Java 应用开发的核心支持。
*   [Spring Boot](https://github.com/spring-projects/spring-boot) - 简化 Spring 应用的创建。
*   [Guava](https://github.com/google/guava) - Google 的 Java 核心库。
*   [Netty](https://github.com/netty/netty) - 异步事件驱动的网络应用框架。
*   [MyBatis](https://github.com/mybatis/mybatis-3) - 一流的持久化框架。
*   [RxJava](https://github.com/ReactiveX/RxJava) - JVM 的响应式扩展。
*   [OkHttp](https://github.com/square/okhttp) - Android 和 Java 应用的 HTTP 客户端。
*   [JUnit 5](https://github.com/junit-team/junit5) - 下一代 Java 测试框架。
*   [Mockito](https://github.com/mockito/mockito) - Java 的 Mocking 框架。
*   [Lombok](https://github.com/projectlombok/lombok) - 减少 Java 样板代码的库。
*   [Zxing](https://github.com/zxing/zxing) - 多格式的一维/二维条码图像处理库。
*   [On Java 8](https://github.com/LingCoder/OnJava8) - 《On Java 8》中文版。
*   [Effective Java 3rd Edition](https://github.com/s-j-choi/effective-java-3rd-edition) - 《Effective Java》第三版。

#### 3.8 其他语言

*   [Awesome-Swift](https://github.com/matteocrippa/awesome-swift) - Swift 资源。
*   [Awesome-PHP](https://github.com/ziadoz/awesome-php) - PHP 资源。
*   [Awesome-Ruby](https://github.com/markets/awesome-ruby) - Ruby 资源。
*   [Awesome-CSharp](https://github.com/uhub/awesome-csharp) - C# 资源。
*   [Awesome-Elixir](https://github.com/h4cc/awesome-elixir) - Elixir 资源。
*   [Awesome-Haskell](https://github.com/krispo/awesome-haskell) - Haskell 资源。
*   [Awesome-Lua](https://github.com/LewisJEllis/awesome-lua) - Lua 资源。
*   [Awesome-R](https://github.com/qinwf/awesome-R) - R 语言资源。
*   [Awesome-Dart](https://github.com/yissachar/awesome-dart) - Dart 语言资源。
*   [Awesome-Julia](https://github.com/svaksha/Julia.jl) - Julia 语言资源。
*   [Awesome-OCaml](https://github.com/ocaml-community/awesome-ocaml) - OCaml 资源。
*   [Awesome-Crystal](https://github.com/veelenga/awesome-crystal) - Crystal 语言资源。
*   [Awesome-Nim](https://github.com/ringabout/awesome-nim) - Nim 语言资源。
*   [Awesome-Zig](https://github.com/catdevnull/awesome-zig) - Zig 语言资源。
*   [Awesome-WebAssembly](https://github.com/mbasso/awesome-wasm) - WebAssembly 资源。

---

## 网络安全与攻防技术 (Cybersecurity)

### 1. 基础入门与信息收集 (Foundation & Reconnaissance)
*   [SafeLine](https://github.com/chaitin/safeline) - 长亭科技出品的高性能 WAF。
*   [CrowdSec](https://github.com/crowdsecurity/crowdsec) - 社区驱动的协作式入侵防御系统。
*   [Trivy](https://github.com/aquasecurity/trivy) - 全面的容器、Kubernetes 和代码库漏洞扫描器。

#### 1.1 综合性 Awesome 列表 & 资源库

*   [Awesome Hacking](https://github.com/carpedm20/awesome-hacking) - 最全面的黑客资源列表之一，侦察部分非常丰富。
*   [Awesome Pentest](https://github.com/enaqx/awesome-pentest) - 精选的渗透测试资源，信息收集是首要环节。
*   [Awesome OSINT](https://github.com/jivoi/awesome-osint) - 开源情报（OSINT）的权威资源列表，信息收集的核心。
*   [InfoSec Reference](https://github.com/rmusser01/Infosec_Reference) - 包含大量图表、笔记和工具链接的信息安全参考资料。
*   [PT-EveryThing](https://github.com/alphaSeclab/pt-every-thing) - 渗透测试相关的各类资源，非常全面。
*   [Cyber Security Resources](https://github.com/gerryguy311/Cyber-Security-Resources) - 网络安全资源集合，分类清晰。
*   [The Book of Secret Knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) - 系统管理员、渗透测试人员、开发人员等的笔记和清单。
*   [Hacking-Tools](https://github.com/Z4nzu/hackingtool) - 多合一的黑客工具安装器和集合。
*   [Red Teaming Toolkit](https://github.com/infosecn1nja/Red-Teaming-Toolkit) - 红队作战工具包，包含大量侦察工具。
*   [Bug Bounty Reference](https://github.com/ngalongc/bug-bounty-reference) - 漏洞赏金猎人的参考资料，侦察是第一步。
*   [My-Pentest-Workflow](https://github.com/jakejarvis/my-pentest-workflow) - 个人渗透测试工作流。
*   [OSCP-Prep](https://github.com/wwong99/pentest-notes/blob/master/oscp_resources/OSCP-Prep.md) - OSCP 备考资源，包含大量侦察技巧。

#### 1.2 子域名枚举 & 发现

*   [Amass](https://github.com/owasp-amass/amass) - OWASP 出品，最强大的深度子域名枚举与网络映射工具。
*   [Subfinder](https://github.com/projectdiscovery/subfinder) - ProjectDiscovery 出品，快速、模块化的被动子域名枚举工具。
*   [OneForAll](https://github.com/shmilylty/OneForAll) - 一款功能强大的子域收集工具。
*   [Assetfinder](https://github.com/tomnomnom/assetfinder) - 快速发现与给定域相关的子域名和域名。
*   [Findomain](https://github.com/findomain/findomain) - 速度极快的跨平台子域名扫描器。
*   [Sublist3r](https://github.com/aboul3la/Sublist3r) - 使用多个搜索引擎进行被动子域名枚举的 Python 工具。
*   [MassDNS](https://github.com/blechschmidt/massdns) - 高性能的 DNS 解析器，常用于子域名爆破。
*   [Gobuster](https://github.com/OJ/gobuster) - Go 编写的目录/文件、DNS 和 vHost 爆破工具。
*   [Ksubdomain](https://github.com/knownsec/ksubdomain) - 无状态的子域名爆破工具。
*   [ShuffleDNS](https://github.com/projectdiscovery/shuffledns) - 封装了 MassDNS 的子域名爆破和解析工具。
*   [Altdns](https://github.com/infosec-au/altdns) - 基于已有子域名生成变体并进行解析。
*   [CTFR](https://github.com/UnaPibaGeek/ctfr) - 利用证书透明度日志发现子域名。
*   [Sudomy](https://github.com/screetsec/Sudomy) - 子域名枚举、分析和侦察工具。
*   [DNSx](https://github.com/projectdiscovery/dnsx) - 快速、多功能的 DNS 工具包，支持多种查询。
*   [Domain-hunter](https://github.com/bit4woo/domain_hunter) - 强大的域名资产收集和管理工具。
*   [Cero](https://github.com/glebarez/cero) - 从证书透明度日志中抓取子域名。
*   [Crt.sh](https://crt.sh/) - 证书透明度日志搜索引擎网站。
*   [DNS-Recon](https://github.com/darkoperator/dnsrecon) - 强大的 DNS 枚举脚本。
*   [Knock](https://github.com/guelfoweb/knock) - Python 子域名扫描工具。
*   [Lepus](https://github.com/gfek/Lepus) - 子域名枚举和信息收集工具。
*   [BBScan](https://github.com/lijiejie/BBScan) - 快速、简单的信息泄漏扫描器，也包含子域名发现。
*   [dnscan](https://github.com/rbsec/dnscan) - Python 编写的 DNS 扫描器。
*   [subbrute](https://github.com/TheRook/subbrute) - 快速的 DNS 子域名爆破工具。

#### 1.3 网络扫描 & 端口发现

*   [Nmap](https://github.com/nmap/nmap) - 网络发现与安全审计的王者，必备工具。
*   [Masscan](https://github.com/robertdavidgraham/masscan) - 互联网级别端口扫描器，速度极快。
*   [Zmap](https://github.com/zmap/zmap) - 另一个为全网扫描设计的开源网络扫描器。
*   [Naabu](https://github.com/projectdiscovery/naabu) - Go 编写的快速端口扫描器，注重可靠性和简洁性。
*   [RustScan](https://github.com/RustScan/RustScan) - 极速端口扫描器，能自动将结果导入 Nmap。
*   [Sandmap](https://github.com/trimstray/sandmap) - 使用 Nmap 作为引擎的图形化扫描工具。
*   [Unicornscan](http://www.unicornscan.org/) - 异步的 TCP/UDP 扫描器。
*   [TX-Ray](https://github.com/42wim/tx-ray) - 网络诊断工具，功能类似 `mtr`。
*   [Angry IP Scanner](https://github.com/angryip/ipscan) - 快速、友好的网络扫描器。
*   [Advanced-Port-Scanner](https://www.advanced-port-scanner.com/) - 免费的 Windows 端口扫描器。
*   [Netdiscover](https://tools.kali.org/information-gathering/netdiscover) - Kali 自带的 ARP 侦察工具。
*   [Sparta](https://github.com/SECFORCE/sparta) - 图形化的网络基础设施渗透测试工具。
*   [Zgrab2](https://github.com/zmap/zgrab2) - Go 编写的快速、模块化的应用层扫描器。

#### 1.4 Web 爬取 & 目录/路径发现

*   [Dirsearch](https://github.com/maurosoria/dirsearch) - Go 编写的 Web 路径扫描器，速度快，功能强大。
*   [Feroxbuster](https://github.com/epi052/feroxbuster) - Rust 编写的快速、简单、递归的内容发现工具。
*   [FFUF (Fuzz Faster U Fool)](https://github.com/ffuf/ffuf) - Go 编写的快速 Web Fuzzer，常用于目录爆破。
*   [Wfuzz](https://github.com/xmendez/wfuzz) - 灵活的 Web 应用 Fuzzer。
*   [Hakrawler](https://github.com/hakluke/hakrawler) - Go 编写的快速 Web 爬虫，设计用于发现端点和资产。
*   [Gospider](https://github.com/jaeles-project/gospider) - Go 编写的快速 Web 爬虫。
*   [Katana](https://github.com/projectdiscovery/katana) - ProjectDiscovery 出品的下一代 Web 爬虫。
*   [Scrapy](https://github.com/scrapy/scrapy) - 强大的 Python 爬虫框架，可用于信息收集。
*   [Waybackurls](https://github.com/tomnomnom/waybackurls) - 从 Wayback Machine 和 Common Crawl 中提取 URL。
*   [Gau (Get All URLs)](https://github.com/lc/gau) - 从多个来源获取已知 URL。
*   [ParamSpider](https://github.com/devanshbatham/ParamSpider) - 用于挖掘参数的爬虫。
*   [LinkFinder](https://github.com/GerbenJavado/LinkFinder) - 在 JavaScript 文件中发现端点的 Python 脚本。
*   [Arjun](https://github.com/s0md3v/Arjun) - HTTP 参数发现套件。
*   [Meg](https://github.com/tomnomnom/meg) - 用于获取大量 URL 列表的 Fetch 工具。
*   [Dirb](https://tools.kali.org/web-applications/dirb) - Kali 自带的经典 Web 内容扫描器。
*   [GoBuster](https://github.com/OJ/gobuster) - (重复) Go 编写的目录/文件、DNS 和 vHost 爆破工具。
*   [Photon](https://github.com/s0md3v/Photon) - 极速的 OSINT 和 Web 爬虫。
*   [XRay](https://github.com/chaitin/xray) - 一款功能强大的安全评估工具，包含爬虫功能。
*   [URL-Hunter](https://github.com/utkusen/urlhunter) - 实时从 Pastebin 收集 URL。
*   [SecretFinder](https://github.com/m4ll0k/SecretFinder) - 在 JS 文件中发现敏感数据和端点。
*   [Subjs](https://github.com/lc/subjs) - 从网页中提取 JavaScript 文件。
*   [Waymore](https://github.com/xnl-h4ck3r/waymore) - 从更多来源查找 URL。

#### 1.5 开源情报 (OSINT) & 敏感信息泄露

*   [TruffleHog](https://github.com/trufflesecurity/trufflehog) - 在 git 仓库中搜索高熵字符串和秘密，深入历史提交。
*   [Gitleaks](https://github.com/gitleaks/gitleaks) - 在 Git 仓库中检测硬编码的秘密。
*   [Shhgit](https://github.com/eth0izzle/shhgit) - 实时监控 GitHub，查找意外提交的秘密和敏感文件。
*   [Sherlock](https://github.com/sherlock-project/sherlock) - 在各大社交网络上通过用户名查找社交媒体账户。
*   [Maigret](https://github.com/soxoj/maigret) - Sherlock 的一个强大分支，支持更多网站。
*   [Social-analyzer](https://github.com/qeeqbox/social-analyzer) - 通过用户名或邮箱在超过1000个社交媒体/网站上进行分析和查找。
*   [SpiderFoot](https://github.com/smicallef/spiderfoot) - 自动化的 OSINT 工具，集成数十种数据源。
*   [Recon-ng](https://github.com/lanmaster53/recon-ng) - 功能齐全的 Web 侦察框架，受 Metasploit 启发。
*   [Maltego](https://www.maltego.com/) - 强大的图形化链接分析工具，用于 OSINT 和取证。
*   [OSINT-Framework](http://osintframework.com/) - OSINT 框架的 Web 界面，分类清晰。
*   [GitDorker](https://github.com/obheda12/GitDorker) - 使用 dork 在 GitHub 快速、有效地查找敏感信息。
*   [PhoneInfoga](https://github.com/sundowndev/PhoneInfoga) - 先进的电话号码信息收集工具。
*   [Twint](https://github.com/twintproject/twint) - 先进的 Twitter 抓取和 OSINT 工具。
*   [GitGraber](https://github.com/hisxo/gitgraber) - 实时监控 GitHub，查找公司相关的敏感数据泄露。
*   [DumpsterDiver](https://github.com/securing/DumpsterDiver) - 在各类文件中搜索硬编码的秘密。
*   [Git-secrets](https://github.com/awslabs/git-secrets) - 防止将密码或其他敏感信息提交到 git 仓库。
*   [Gitrob](https://github.com/michenriksen/gitrob) - 在 GitHub 的公共组织或成员的仓库中查找潜在的敏感文件。
*   [Holehe](https://github.com/megadose/holehe) - 检查邮箱是否在不同网站上注册。
*   [GHunt](https://github.com/mxrch/GHunt) - Google 账户的 OSINT 工具。
*   [Blackbird](https://github.com/p1ngul1n0/blackbird) - 社交网络上的用户名搜索工具。
*   [Metagoofil](https://github.com/laramies/metagoofil) - 从公共文档中提取元数据。
*   [FOCA](https://github.com/ElevenPaths/FOCA) - 自动化的元数据分析工具。
*   [DataSploit](https://github.com/datasploit/datasploit) - 利用 OSINT 对公司、人员、电话号码等进行侦察。
*   [Instaloader](https://github.com/instaloader/instaloader) - 下载 Instagram 图片（或视频）及其标题和元数据。
*   [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) - 用户名枚举工具。

#### 1.6 可视化 & 数据处理

*   [Aquatone](https://github.com/michenriksen/aquatone) - 对大量主机的网站进行可视化检查的工具。
*   [Gowitness](https://github.com/sensepost/gowitness) - Go 编写的网站截图工具。
*   [Eyewitness](https://github.com/FortyNorthSecurity/EyeWitness) - 设计用于对网站进行截图，评估 Web 服务器的默认凭证。
*   [Httpx](https://github.com/projectdiscovery/httpx) - 快速、多功能的 HTTP 工具包，常用于探测存活主机。
*   [Httprobe](https://github.com/tomnomnom/httprobe) - 探测给定的域名列表是否运行 HTTP 或 HTTPS 服务。
*   [Unfurl](https://github.com/obsidianforensics/unfurl) - 有效地解析和可视化 URL。
*   [Jq](https://github.com/jqlang/jq) - 命令行 JSON 处理工具，信息收集中处理 API 输出的神器。
*   [Anew](https://github.com/tomnomnom/anew) - 将新行附加到文件中（如果它们不存在）。
*   [Grep](https://www.gnu.org/software/grep/) - Linux 基础命令，文本搜索利器。
*   [Curl](https://github.com/curl/curl) - 命令行 URL 传输工具。
*   [Wget](https://www.gnu.org/software/wget/) - 非交互式网络下载工具。
*   [webscreenshot](https://github.com/maaaaz/webscreenshot) - 简单的网站截图工具。
*   [WitnessMe](https://github.com/byt3bl33d3r/WitnessMe) - Web 截图工具。
*   [qsreplace](https://github.com/tomnomnom/qsreplace) - 替换 URL 查询字符串中的参数值。
*   [gf](https://github.com/tomnomnom/gf) - `grep` 的包装器，用于查找潜在的漏洞模式。
*   [Interlace](https://github.com/codingo/Interlace) - 轻松地对不同命令进行多线程和并行化处理。

#### 1.7 综合性侦察框架 & 平台

*   [Sn1per](https://github.com/1N3/Sn1per) - 自动化的渗透测试侦察扫描器。
*   [Osmedeus](https://github.com/j3ssie/osmedeus) - 自动化的进攻性安全工作流。
*   [ReconFTW](https://github.com/six2dez/reconftw) - 旨在通过运行最佳工具集来对目标执行全自动侦察。
*   [IVRE](https://github.com/ivre/ivre) - 开源网络侦察框架，包含被动和主动分析。
*   [Faraday](https://github.com/infobyte/faraday) - 多用户渗透测试协作平台。
*   [Dradis Framework](https://github.com/dradis/dradis-ce) - 用于共享信息和报告的协作框架。
*   [MagicTree](https://www.gremwell.com/magictree) - 数据管理和报告工具，常用于渗透测试。
*   [Discover](https://github.com/leebaird/discover) - 自定义 bash 脚本，用于自动化各种侦察任务。
*   [TIDoS-Framework](https://github.com/0xInfection/TIDoS-Framework) - 全面的 Web 应用渗透测试框架。
*   [ReconDog](https://github.com/s0md3v/ReconDog) - 多合一的侦察工具。

#### 1.8 特定技术栈侦察

*   [Wpscan](https://github.com/wpscanteam/wpscan) - WordPress 安全扫描器。
*   [Joomscan](https://github.com/OWASP/joomscan) - Joomla CMS 扫描器。
*   [Droopescan](https://github.com/droope/droopescan) - Drupal CMS 扫描器。
*   [CMSeeK](https://github.com/Tuhinshubhra/CMSeeK) - CMS 检测和漏洞扫描套件。
*   [S3Scanner](https://github.com/sa7mon/S3Scanner) - 扫描 AWS S3 存储桶的错误配置。
*   [Cloud-enum](https://github.com/initstring/cloud_enum) - 多云 OSINT 枚举工具（AWS, Azure, Google Cloud）。
*   [Git-dumper](https://github.com/arthaud/git-dumper) - 用于 dump 由 .git 目录暴露的源代码的工具。
*   [SVN-dumper](https://github.com/iamstupid/svndumper) - 用于 dump 由 .svn 目录暴露的源代码的工具。
*   [DS_Store-dumper](https://github.com/lijiejie/ds_store_exp) - 解析 .DS_Store 文件并下载源代码。
*   [Cloud-mapper](https://github.com/VirtueSecurity/cloud-mapper) - 分析 AWS 环境，生成网络图。
*   [WeirdAAL](https://github.com/carnal0wnage/weirdAAL) - AWS 攻击和侦察工具。
*   [kube-hunter](https://github.com/aquasecurity/kube-hunter) - 在 Kubernetes 集群中寻找安全弱点。
*   [Nacos-Client](https://github.com/nacos-group/nacos-sdk-python) - Nacos 客户端，可用于未授权访问。
*   [Finger](https://github.com/trailofbits/finger) - Go 编写的 Web 服务器指纹识别工具。

#### 1.9 学习资源 & 靶场

*   [Bug Bounty Hunting Methodology](https://github.com/jhaddix/tbhm) - Jason Haddix 的漏洞赏金猎人方法论。
*   [PayloadsAllTheThings/Reconnaissance](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources#reconnaissance) - Recon 方法论和资源。
*   [NahamSec/Resources](https://github.com/nahamsec/Resources-for-Beginner-Bug-Bounty-Hunters) - 新手漏洞赏金猎人资源。
*   [Pentester Land](https://pentester.land/list-of-bug-bounty-writeups.html) - 大量的漏洞赏金 Writeup。
*   [HackerOne/hacktivity](https://hackerone.com/hacktivity) - 公开的漏洞报告。
*   [Bugcrowd/bug-bounty-list](https://github.com/bugcrowd/bug-bounty-list) - Bugcrowd 的漏洞赏金项目列表。
*   [OSINT Dojo](https://www.osintdojo.com/) - OSINT 学习和挑战。
*   [The Hacker's Handbook](https://thehackerish.com/the-ultimate-guide-to-hacking-and-penetration-testing/) - 黑客手册。
*   [Recon-Cheatsheet](https://github.com/daffainfo/Recon-Cheatsheet) - 侦察速查表。
*   [Bug-Bounty-Toolz](https://github.com/m4ll0k/Bug-Bounty-Toolz) - 漏洞赏金工具集合。

---

### 2. 漏洞发现与利用 (Vulnerability Discovery & Exploitation)

#### 2.1 综合性 Awesome 列表 & 资源库

*   [Awesome Pentest](https://github.com/enaqx/awesome-pentest) - 精选的渗透测试资源，漏洞利用是核心。
*   [Awesome Exploit Development](https://github.com/FabioBaroni/awesome-exploit-development) - Exploit 开发的权威资源列表。
*   [Awesome Fuzzing](https://github.com/cpuu/awesome-fuzzing) - Fuzzing（模糊测试）资源、书籍、工具的集合。
*   [Awesome Vulnerability Research](https://github.com/re-pronin/awesome-vulnerability-research) - 漏洞研究资源。
*   [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - 各种漏洞的 Payload 和绕过技巧集合。
*   [Exploit-DB](https://www.exploit-db.com/) - 最著名的公开漏洞利用代码数据库。
*   [Packet Storm](https://packetstormsecurity.com/files/tags/exploit/) - 提供漏洞、利用代码和安全资讯。
*   [Vulners](https://vulners.com/) - 巨大的、可搜索的安全内容数据库（漏洞、补丁、文章等）。
*   [0day.today](https://0day.today/) - 另一个漏洞利用代码市场和数据库。
*   [VX-Underground](https://vx-underground.org/papers.html) - 大量的恶意软件源码和安全论文。
*   [PoC-in-GitHub](https://github.com/nomi-sec/PoC-in-GitHub) - 自动追踪 GitHub 上的 PoC/Exploit 项目。
*   [Awesome Proof-of-Concept-Archive](https://github.com/j-j-m/awesome-poc-exploits) - PoC 和 Exploit 的归档。
*   [Vulnerability-Lab](https://www.vulnerability-lab.com/) - 漏洞研究和披露平台。

#### 2.2 漏洞扫描 & 自动化评估

*   [Nuclei](https://github.com/projectdiscovery/nuclei) - 基于模板的快速漏洞扫描器，社区模板库非常强大。
*   [Nuclei Templates](https://github.com/projectdiscovery/nuclei-templates) - Nuclei 的官方社区模板库。
*   [Nikto](https://github.com/sullo/nikto) - 经典的 Web 服务器漏洞扫描器。
*   [OpenVAS / GVM](https://github.com/greenbone/gvm) - 开源的、功能全面的漏洞评估系统。
*   [Wapiti](https://github.com/wapiti-scanner/wapiti) - Web 应用漏洞黑盒扫描器。
*   [Arachni](https://github.com/Arachni/arachni) - 功能丰富的模块化 Web 应用安全扫描框架。
*   [Nessus](https://www.tenable.com/products/nessus) - 业界最知名的商业漏洞扫描器之一。
*   [Acunetix](https://www.acunetix.com/) - 商业 Web 应用安全扫描器。
*   [Netsparker / Invicti](https://www.invicti.com/) - 另一款顶级的商业 DAST 工具。
*   [XRay](https://github.com/chaitin/xray) - 长亭科技出品，功能强大的安全评估工具。
*   [Goby](https://github.com/gobysec/Goby) - 新一代网络安全测试工具，集成了大量漏洞利用。
*   [Vulmap](https://github.com/zhzyker/vulmap) - 一款 web 漏洞扫描和验证工具。
*   [AppScan](https://www.hcltechsw.com/appscan) - HCL 的应用安全测试工具套件。
*   [Qualys](https://www.qualys.com/apps/vulnerability-management-detection-response/) - 基于云的漏洞管理平台。
*   [Rapid7 InsightVM](https://www.rapid7.com/products/insightvm/) - 漏洞风险管理工具。
*   [Metasploit Framework](https://github.com/rapid7/metasploit-framework) - (重复) 不仅是利用框架，也包含大量扫描和辅助模块。
*   [Sn1per](https://github.com/1N3/Sn1per) - (重复) 自动化的渗透测试侦察扫描器，包含漏洞扫描。
*   [Tsunami Security Scanner](https://github.com/google/tsunami-security-scanner) - Google 出品的通用网络安全扫描器。
*   [Skipfish](https://code.google.com/archive/p/skipfish/) - Google 早期的 Web 应用安全侦察工具。
*   [Jaeles](https://github.com/jaeles-project/jaeles) - 强大的 Web 应用扫描框架，与 Nuclei 类似。
*   [Sitadel](https://github.com/shenril/Sitadel) - 基于文本模板的 Web 应用扫描器。

#### 2.3 Fuzzing (模糊测试)

*   [AFL++ (American Fuzzy Lop)](https://github.com/AFLplusplus/AFLplusplus) - 最著名的覆盖率引导的 Fuzzer 之一，有大量分支和改进。
*   [libFuzzer](https://llvm.org/docs/LibFuzzer.html) - LLVM 内置的覆盖率引导的 Fuzzing 引擎，常用于 C/C++ 项目。
*   [Honggfuzz](https://github.com/google/honggfuzz) - Google 出品的、注重安全、多线程的 Fuzzer。
*   [Boofuzz](https://github.com/jtpereyda/boofuzz) - 网络协议 Fuzzing 框架，是 Sulley 的继任者。
*   [FFUF (Fuzz Faster U Fool)](https://github.com/ffuf/ffuf) - (重复) Go 编写的快速 Web Fuzzer，用于发现路径、参数等。
*   [Wfuzz](https://github.com/xmendez/wfuzz) - (重复) 灵活的 Web 应用 Fuzzer。
*   [Radamsa](https://github.com/aoh/radamsa) - 通用的、健壮的 Fuzzer。
*   [AFL.js](https://github.com/AFLplusplus/afl.js) - 用于 JavaScript 引擎的 AFL。
*   [Syzkaller](https://github.com/google/syzkaller) - 针对操作系统内核的、无监督的、覆盖率引导的 Fuzzer。
*   [Peach Fuzzer](https://www.peach.tech/) - 强大的商业 Fuzzing 平台。
*   [Kitty](https://github.com/cisco-sas/kitty) - Fuzzing 框架，易于编写自定义 Fuzzer。
*   [Domato](https://github.com/google/domato) - Google 出品的 DOM Fuzzer。
*   [WinAFL](https://github.com/googleprojectzero/winafl) - AFL 的一个分支，用于对 Windows 二进制文件进行 Fuzzing。
*   [Python-AFL](https://github.com/jdbirdwell/python-afl) - AFL 的 Python 绑定。
*   [Go-fuzz](https://github.com/dvyukov/go-fuzz) - Go 语言的覆盖率引导的 Fuzzing。
*   [Atheris](https://github.com/google/atheris) - Python 的覆盖率引导的 Fuzzing 引擎。
*   [Jazzer](https://github.com/CodeIntelligenceTesting/jazzer) - JVM 平台的覆盖率引导的 Fuzzing。
*   [OSS-Fuzz](https://github.com/google/oss-fuzz) - Google 为开源软件提供的大规模持续 Fuzzing 服务。

#### 2.4 Exploit 开发 & 后渗透

*   [Metasploit Framework](https://github.com/rapid7/metasploit-framework) - 全球最流行的渗透测试和漏洞利用框架。
*   [Pwntools](https://github.com/Gallopsled/pwntools) - CTF 框架和 Exploit 开发库，pwn 手必备。
*   [ROPgadget](https://github.com/JonathanSalwan/ROPgadget) - 在二进制文件中查找 ROP/JOP gadgets 的工具。
*   [Ropper](https://github.com/sashs/ropper) - 显示各种文件格式中 gadgets 信息的工具。
*   [One-gadget](https://github.com/david942j/one_gadget) - 在 glibc 中查找 `execve('/bin/sh', NULL, NULL)` gadgets 的工具。
*   [Seccomp-tools](https://github.com/david942j/seccomp-tools) - 分析 seccomp 过滤器的工具。
*   [Shellsploit](https://github.com/b3mb4m/shellsploit-framework) - Shellcode 生成器。
*   [Mona.py](https://github.com/corelan/mona) - Immunity Debugger 和 WinDbg 的插件，用于辅助 Exploit 开发。
*   [GEF](https://github.com/hugsy/gef) - GDB 增强功能，为漏洞利用开发和逆向工程设计。
*   [PEDA](https://github.com/longld/peda) - GDB 的 Python Exploit 开发辅助。
*   [Pwndbg](https://github.com/pwndbg/pwndbg) - GDB 的一个插件，使调试对逆向工程师和 Exploit 开发者更友好。
*   [Qiling Framework](https://github.com/qilingframework/qiling) - 先进的二进制仿真框架，可用于漏洞分析。
*   [Triton](https://github.com/JonathanSalwan/Triton) - 动态二进制分析（DBA）框架。
*   [Barf-project](https://github.com/programa-stic/barf-project) - 多平台二进制分析和逆向工程框架。
*   [Checksec.sh](https://github.com/slimm609/checksec.sh) - 检查二进制文件开启了哪些安全保护。
*   [Libformatstr](https://github.com/anarcheuz/libformatstr) - 简化格式化字符串漏洞利用。
*   [Dirty-Cow](https://github.com/gbonacini/CVE-2016-5195) - Linux 内核“脏牛”漏洞的 PoC。
*   [EternalBlue](https://github.com/ShadowBrokers/EternalBlue-DoublePulsar-Metasploit) - "永恒之蓝"漏洞的 Metasploit 模块。
*   [MS17-010](https://github.com/worawit/MS17-010) - MS17-010 漏洞的扫描和利用工具。
*   [Auto-Exploit](https://github.com/joker25000/Exploit-Tool) - 自动化漏洞利用工具。

#### 2.5 特定漏洞利用工具

*   [sqlmap](https://github.com/sqlmapproject/sqlmap) - 自动化的 SQL 注入和数据库接管工具。
*   [Commix](https://github.com/commixproject/commix) - 自动化的命令注入和利用工具。
*   [XXEinjector](https://github.com/enjoiz/XXEinjector) - 自动化的 XXE 漏洞利用工具。
*   [ysoserial](https://github.com/frohoff/ysoserial) - 生成 Java 反序列化 Payload 的工具。
*   [ysoserial.net](https://github.com/pwntester/ysoserial.net) - .NET 平台的反序列化 Payload 生成工具。
*   [PHPGGC](https://github.com/ambionics/phpggc) - PHP 反序列化 Payload 生成器。
*   [Gopherus](https://github.com/tarunkant/Gopherus) - 生成 Gopher Payload，用于 SSRF 等。
*   [SSRFmap](https://github.com/swisskyrepo/SSRFmap) - 自动化的 SSRF 漏洞利用工具。
*   [XSSHunter](https://github.com/mandatoryprogrammer/xsshunter-express) - (重复) XSS 漏洞利用框架。
*   [BeEF (The Browser Exploitation Framework)](https://github.com/beefproject/beef) - 浏览器攻击框架。
*   [CRLFsuite](https://github.com/Nefcore/CRLFsuite) - 快速的 CRLF 注入扫描器。
*   [Log4j-scan](https://github.com/fullhunt/log4j-scan) - Log4Shell 漏洞的扫描器。
*   [Spring4Shell-scan](https://github.com/fullhunt/spring4shell-scan) - Spring4Shell 漏洞的扫描器。
*   [Heartbleed](https://github.com/FiloSottile/Heartbleed) - "心脏滴血"漏洞的 PoC。
*   [Shellshock](https://github.com/mubix/shellshocker-pocs) - "破壳"漏洞的 PoC 集合。
*   [NoSQLMap](https://github.com/codingo/NoSQLMap) - 自动化的 NoSQL 注入和数据库接管工具。
*   [Tplmap](https://github.com/epinna/tplmap) - 自动化的服务器端模板注入检测和利用工具。
*   [Race The Web](https://github.com/TheHackerDev/race-the-web) - 测试 Web 应用的竞争条件漏洞。
*   [Request-Smuggler](https://github.com/gwen001/request-smuggler) - HTTP 请求走私漏洞检测工具。
*   [Pad-buster](https://github.com/GDSSecurity/PadBuster) - 自动化的 Padding Oracle 攻击工具。
*   [Hash-Buster](https://github.com/s0md3v/Hash-Buster) - 破解哈希的脚本。
*   [John the Ripper](https://github.com/openwall/john) - 著名的密码破解工具。
*   [Hashcat](https://github.com/hashcat/hashcat) - 世界上最快的密码破解工具。
*   [Hydra](https://github.com/vanhauser-thc/thc-hydra) - 并行的网络登录破解工具。
*   [Ncrack](https://github.com/nmap/ncrack) - 高速的网络认证破解工具。

#### 2.6 漏洞数据库 & 报告

*   [CVE-Search](https://github.com/cve-search/cve-search) - 用于导入 CVE 和 CPE 数据以进行本地搜索的工具。
*   [NVD-Database](https://nvd.nist.gov/vuln/search) - 美国国家漏洞数据库。
*   [MITRE CVE](https://cve.mitre.org/) - CVE 计划的官方网站。
*   [China National Vulnerability Database (CNVD)](https://www.cnvd.org.cn/) - 中国国家信息安全漏洞共享平台。
*   [GitHub Advisory Database](https://github.com/advisories) - GitHub 的安全公告数据库。
*   [Project Zero Blog](https://googleprojectzero.blogspot.com/) - Google Project Zero 团队的技术博客，包含大量 0-day 分析。
*   [The Hacker News](https://thehackernews.com/) - 著名的网络安全新闻网站。
*   [Threatpost](https://threatpost.com/) - 另一个网络安全新闻来源。
*   [ZDI-Advisories](https://www.zerodayinitiative.com/advisories/published/) - Zero Day Initiative 的漏洞公告。
*   [Awesome-CVE-PoC](https://github.com/qazbnm456/awesome-cve-poc) - 精选的 CVE PoC 列表。
*   [CVE-Trends](https://github.com/trickest/cve) - 追踪 Twitter 上热门 CVE 的工具。
*   [Vulnerability-Writeups](https://github.com/dev-sec/vulnerability-lab) - 漏洞 Writeup 集合。

#### 2.7 漏洞管理 & 协作

*   [DefectDojo](https://github.com/DefectDojo/django-DefectDojo) - 开源的漏洞管理和应用安全编排平台。
*   [Faraday](https://github.com/infobyte/faraday) - (重复) 多用户渗透测试协作平台。
*   [Dradis Framework](https://github.com/dradis/dradis-ce) - (重复) 用于共享信息和报告的协作框架。
*   [ArcherySec](https://github.com/archerysec/archerysec) - 开源的漏洞评估和管理工具。
*   [VECTR](https://github.com/SecurityRiskAdvisors/VECTR) - 用于追踪红队和蓝队活动的工具。
*   [Lair](https://github.com/lair-framework/lair) - 用于存储渗透测试数据的协作框架。
*   [Serpico](https://github.com/SerpicoProject/Serpico) - 简化的渗透测试报告生成工具。
*   [PwnDoc](https://github.com/pwndoc/pwndoc) - 渗透测试报告协作生成器。

---

### 3. Web 攻防 (Web Attack & Defense)

#### 3.1 综合性 Awesome 列表 & 资源库

*   [Awesome Web Security](https://github.com/qazbnm456/awesome-web-security) - 最全面的 Web 安全资源列表，涵盖各种主题。
*   [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - Web 攻击 Payload 和绕过技巧的终极集合。
*   [OWASP Top 10 Project](https://github.com/OWASP/Top10) - OWASP Top 10 官方项目和文档。
*   [OWASP Cheat Sheet Series](https://github.com/OWASP/CheatSheetSeries) - OWASP 出品的安全开发速查表，也是学习 Web 漏洞的绝佳资源。
*   [Web Hacking 101](https://github.com/Hacker0x01/web-hacking-101) - HackerOne 出品的免费电子书。
*   [Awesome Web Hacking](https://github.com/infoslack/awesome-web-hacking) - 另一个关于 Web 安全和漏洞赏金的资源列表。
*   [Hacking-Articles](https://github.com/aaronguostudio/hacking-articles) - 大量黑客与安全文章的集合，Web 安全占很大比重。
*   [Pentest-Bookmark](https://github.com/jaiswalakshaye/pentest-bookmarks) - 渗透测试书签，包含大量 Web 安全工具和博客。
*   [Awesome-Bug-Bounty](https://github.com/djadmin/awesome-bug-bounty) - 漏洞赏金资源列表。
*   [Web-Security-Learning](https://github.com/CHYbeta/Web-Security-Learning) - Web 安全学习笔记。
*   [PortSwigger Web Security Academy](https://portswigger.net/web-security) - Burp Suite 官方出品的免费在线 Web 安全培训。
*   [Awesome-WAF](https://github.com/0xInfection/Awesome-WAF) - Web 应用防火墙（WAF）资源列表。
*   [Awesome API Security](https://github.com/arainho/awesome-api-security) - API 安全资源。
*   [Awesome GraphQL](https://github.com/chentsulin/awesome-graphql) - (重复) 包含 GraphQL 安全部分。

#### 3.2 代理、扫描器 & 综合测试平台

*   [Burp Suite](https://portswigger.net/burp) - Web 安全测试的行业标准，集代理、扫描、爆破等功能于一体。
*   [OWASP ZAP (Zed Attack Proxy)](https://github.com/zaproxy/zaproxy) - 开源的、功能强大的 Web 应用安全扫描器和代理工具。
*   [mitmproxy](https://github.com/mitmproxy/mitmproxy) - 交互式的、支持 SSL/TLS 的 HTTPS 代理。
*   [Caido](https://caido.io/) - 一个新兴的、轻量级的、快速的 Web 安全审计工具包。
*   [Nikto](https://github.com/sullo/nikto) - (重复) 经典的 Web 服务器漏洞扫描器。
*   [Wapiti](https://github.com/wapiti-scanner/wapiti) - (重复) Web 应用漏洞黑盒扫描器。
*   [Arachni](https://github.com/Arachni/arachni) - (重复) 功能丰富的模块化 Web 应用安全扫描框架。
*   [GoLismero](https://github.com/golismero/golismero) - 开源的 Web 应用安全框架。
*   [Vega](https://subgraph.com/vega/) - 开源的 Web 安全扫描器和测试平台。
*   [Fiddler](https://www.telerik.com/fiddler) - 免费的 Web 调试代理，适用于 Windows。
*   [Charles Proxy](https://www.charlesproxy.com/) - 商业 HTTP 代理/监视器，支持 Windows, Mac, Linux。
*   [Proxify](https://github.com/projectdiscovery/proxify) - Go 编写的多功能、可定制的 HTTPS 代理。
*   [Mitm-tools](https://github.com/mitm-tools) - mitmproxy 相关工具集合。
*   [Bettercap](https://github.com/bettercap/bettercap) - 中间人攻击的瑞士军刀。

#### 3.3 注入类漏洞 (SQLi, NoSQLi, Command Injection, etc.)

*   [sqlmap](https://github.com/sqlmapproject/sqlmap) - 自动化的 SQL 注入和数据库接管工具。
*   [NoSQLMap](https://github.com/codingo/NoSQLMap) - 自动化的 NoSQL 注入和数据库接管工具。
*   [Commix](https://github.com/commixproject/commix) - 自动化的命令注入和利用工具。
*   [Tplmap](https://github.com/epinna/tplmap) - 自动化的服务器端模板注入检测和利用工具。
*   [SQLi-Payloads](https://github.com/payloadbox/sql-injection-payload-list) - SQL 注入 Payload 列表。
*   [GraphQLmap](https://github.com/swisskyrepo/GraphQLmap) - 用于映射 GraphQL 端点并进行渗透测试的脚本。
*   [Inject-Payloads](https://github.com/1N3/IntruderPayloads) - 用于 Web Fuzzing 的 Payload 集合。
*   [Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA) - 经典的、包含各种漏洞的 PHP/MySQL Web 应用。
*   [SQLi-Labs](https://github.com/Audi-1/sqli-labs) - SQL 注入练习靶场。
*   [Ghauri](https://github.com/r0oth3x49/ghauri) - 先进的 SQL 注入检测和利用工具。
*   [DSSS (Damn Small SQLi Scanner)](https://github.com/stamparm/DSSS) - 小巧的 SQL 注入扫描器。

#### 3.4 跨站脚本 (XSS)

*   [BeEF (The Browser Exploitation Framework)](https://github.com/beefproject/beef) - 浏览器攻击框架，常与 XSS 结合使用。
*   [XSSHunter](https://github.com/mandatoryprogrammer/xsshunter-express) - 识别和管理盲 XSS 漏洞的框架。
*   [XSStrike](https://github.com/s0md3v/XSStrike) - 先进的 XSS 扫描器。
*   [Dalfox](https://github.com/hahwul/dalfox) - Go 编写的 XSS 参数分析和扫描工具。
*   [XSS-Payloads](https://github.com/payloadbox/xss-payload-list) - XSS Payload 集合。
*   [Awesome-XSS](https://github.com/s0md3v/AwesomeXSS) - XSS 资源列表。
*   [DOMPurify](https://github.com/cure53/DOMPurify) - 用于 HTML, MathML 和 SVG 的仅 DOM 的、超快速的、极其健壮的 XSS 清理工具。
*   [js-xss](https://github.com/leizongmin/js-xss) - 用于防止 XSS 的 JavaScript 库。
*   [bXSS](https://github.com/LewisArdern/bXSS) - 盲 XSS 框架。
*   [xssor2](https://github.com/evilcos/xssor2) - XSS 数据接收和利用平台。
*   [EzXSS](https://github.com/ssl/ezXSS) - 简单易用的 XSS 盲打平台。

#### 3.5 CSRF, SSRF, RFI/LFI, XXE

*   [SSRFmap](https://github.com/swisskyrepo/SSRFmap) - 自动化的 SSRF 漏洞利用工具。
*   [Gopherus](https://github.com/tarunkant/Gopherus) - 生成 Gopher Payload，用于 SSRF 等。
*   [XXEinjector](https://github.com/enjoiz/XXEinjector) - 自动化的 XXE 漏洞利用工具。
*   [LFISuite](https://github.com/D35m0nd142/LFISuite) - 全自动的 LFI 扫描和利用工具。
*   [dotdotpwn](https://github.com/wireghoul/dotdotpwn) - 目录遍历 Fuzzer。
*   [SSRF-Bible-Cheatsheet](https://github.com/Phuong39/SSRF-bible-cheatsheet) - SSRF 备忘单。
*   [XXE-Payloads](https://github.com/payloadbox/xxe-injection-payload-list) - XXE 注入 Payload 列表。
*   [LFI-Payloads](https://github.com/payloadbox/file-inclusion-payload-list) - LFI/RFI Payload 列表。
*   [Interactsh](https://github.com/projectdiscovery/interactsh) - OAST (Out-of-Band Application Security Testing) 服务器，用于检测 SSRF、盲注等。
*   [Request-Baskets](https://github.com/darklynx/request-baskets) - 用于收集 HTTP 请求的 Web 服务，可用于测试 SSRF。
*   [SSRF-Detector](https://github.com/cujanovic/SSRF-Detector) - SSRF 漏洞检测工具。

#### 3.6 反序列化 & 对象注入

*   [ysoserial](https://github.com/frohoff/ysoserial) - 生成 Java 反序列化 Payload 的工具。
*   [ysoserial.net](https://github.com/pwntester/ysoserial.net) - .NET 平台的反序列化 Payload 生成工具。
*   [PHPGGC](https://github.com/ambionics/phpggc) - PHP 反序列化 Payload 生成器。
*   [Marshalsec](https://github.com/mbechler/marshalsec) - Java 反序列化利用库。
*   [GadgetProbe](https://github.com/BishopFox/gadgetprobe) - 探测 Java 反序列化中可用的 gadget 链。
*   [Java-Deserialization-Cheat-Sheet](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet) - Java 反序列化备忘单。
*   [Fastjson-Exploit](https://github.com/c0ny1/fastjson-exploits) - Fastjson 漏洞利用工具。
*   [Jackson-databind-deser-PoC](https://github.com/FasterXML/jackson-docs) - Jackson 官方文档，包含安全部分。

#### 3.7 HTTP 请求走私 & 竞争条件

*   [Request-Smuggler](https://github.com/gwen001/request-smuggler) - HTTP 请求走私漏洞检测工具。
*   [HTTP-Request-Smuggling](https://github.com/PortSwigger/http-request-smuggling) - PortSwigger 的请求走私研究和工具。
*   [Smuggler](https://github.com/defparam/smuggler) - 一个用于测试 HTTP 请求走私的 Python 脚本。
*   [Race The Web](https://github.com/TheHackerDev/race-the-web) - 测试 Web 应用的竞争条件漏洞。
*   [Turbo Intruder](https://portswigger.net/bapp/9abaa233-c348-47a8-835e-43641d35a467) - Burp Suite 插件，用于发送大量高速 HTTP 请求，适合测试竞争条件。
*   [Race-Condition-Exploits](https://github.com/lucyoa/race-condition-exploit-scripts) - 竞争条件漏洞利用脚本。

#### 3.8 JavaScript 安全 & 客户端攻击

*   [Awesome JavaScript Reversing](https://github.com/jsoverson/awesome-js-reversing) - JS 逆向资源。
*   [de4js](https://github.com/lelinhtinh/de4js) - JavaScript 反混淆工具。
*   [AST Explorer](https://astexplorer.net/) - 分析 JavaScript AST 的在线工具。
*   [Retire.js](https://github.com/RetireJS/retire.js) - 检测使用了已知漏洞的 JS 库。
*   [JS-Scan](https://github.com/zricethezav/js-scan) - 扫描 JS 文件以获取有趣信息的工具。
*   [LinkFinder](https://github.com/GerbenJavado/LinkFinder) - (重复) 在 JavaScript 文件中发现端点。
*   [SecretFinder](https://github.com/m4ll0k/SecretFinder) - (重复) 在 JS 文件中发现敏感数据和端点。
*   [PostMessage-tracker](https://github.com/fransr/postmessage-tracker) - 用于追踪 `postMessage` 通信的 Chrome 插件。
*   [JSCrunch](http://www.iteral.com/jscrunch/) - JavaScript 混淆器。
*   [Obfuscator.io](https://obfuscator.io/) - 免费的 JavaScript 混淆工具。
*   [JS-Vuln-DB](https://github.com/tunz/js-vuln-db) - JavaScript 漏洞数据库。

#### 3.9 Web3 & 智能合约安全

*   [Awesome Web3 Security](https://github.com/Anugrahsr/Awesome-Web3-Security) - Web3 安全资源。
*   [Smart Contract Best Practices](https://github.com/ConsenSys/smart-contract-best-practices) - 智能合约安全最佳实践。
*   [Echidna](https://github.com/crytic/echidna) - 以太坊智能合约 Fuzzer。
*   [Slither](https://github.com/crytic/slither) - Solidity 静态分析框架。
*   [Manticore](https://github.com/trailofbits/manticore) - 动态二进制分析和符号执行工具，支持智能合约。
*   [Mythril](https://github.com/ConsenSys/mythril-classic) - 以太坊智能合约安全分析工具。
*   [Damn Vulnerable DeFi](https://www.damnvulnerabledefi.xyz/) - DeFi 智能合约的攻防演练靶场。
*   [Ethernaut](https://github.com/OpenZeppelin/ethernaut) - 基于 Web3/Solidity 的黑客游戏。
*   [Solidity-doc](https://github.com/ethereum/solidity) - Solidity 官方文档。
*   [OpenZeppelin Contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) - 用于安全智能合约开发的库。
*   [Foundry](https://github.com/foundry-rs/foundry) - Rust 编写的、极速的、可移植的、模块化的以太坊应用开发工具包。
*   [Hardhat](https://github.com/NomicFoundation/hardhat) - 以太坊开发环境。
*   [Ganache](https://github.com/trufflesuite/ganache) - 个人以太坊区块链，用于开发和测试。

#### 3.10 其他 Web 漏洞 & 工具

*   [WAF-Bypass-Techniques-and-Tools](https://github.com/Zoooook/WAF-Bypass-Techniques-and-Tools) - WAF 绕过技术和工具。
*   [WAFW00F](https://github.com/EnableSecurity/wafw00f) - 识别和指纹识别 Web 应用防火墙。
*   [WhatWeb](https://github.com/urbanadventurer/WhatWeb) - 下一代 Web 指纹识别器。
*   [Wappalyzer](https://github.com/wappalyzer/wappalyzer) - 识别网站上使用的技术。
*   [CORStest](https://github.com/RUB-NDS/CORStest) - 全面的 CORS 错误配置扫描器。
*   [JWT-tool](https://github.com/ticarpi/jwt_tool) - 用于验证、伪造和破解 JWT 的工具包。
*   [C-jwt-cracker](https://github.com/brendan-rius/c-jwt-cracker) - C 语言编写的 JWT 破解工具。
*   [OAuth-2.0-Security-Best-Current-Practice](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - OAuth 2.0 安全最佳实践。
*   [Web-Cache-Vulnerability-Scanner](https://github.com/Hackmanit/Web-Cache-Vulnerability-Scanner) - Web 缓存中毒漏洞扫描器。
*   [Wordlists (SecLists)](https://github.com/danielmiessler/SecLists) - 安全测试者的字典集合，包含大量用于 Web 攻击的列表。
*   [FuzzDB](https://github.com/fuzzdb-project/fuzzdb) - 攻击性安全测试的 Payload 字典。
*   [Intruder-Payloads](https://github.com/1N3/IntruderPayloads) - (重复) Web Fuzzing Payload 集合。
*   [HTTPie](https://github.com/httpie/httpie) - 现代化的、用户友好的命令行 HTTP 客户端。
*   [cURL](https://github.com/curl/curl) - (重复) 强大的命令行 URL 传输工具。

---

### 4. 应用与服务攻防 (Application & Service Attack & Defense)

#### 4.1 综合性 Awesome 列表 & 资源库

*   [Awesome API Security](https://github.com/arainho/awesome-api-security) - API 安全的权威资源列表，涵盖工具、文章和最佳实践。
*   [Awesome-Hacking](https://github.com/carpedm20/awesome-hacking) - (重复) 包含大量针对各种服务的攻击工具和资源。
*   [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - (重复) 包含针对各种应用、协议和服务的攻击 Payload。
*   [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) - OWASP 官方的 API 安全十大风险项目。
*   [Awesome-gRPC](https://github.com/grpc-ecosystem/awesome-grpc) - gRPC 生态系统资源，包含安全相关工具。
*   [Awesome-GraphQL](https://github.com/chentsulin/awesome-graphql) - (重复) 包含大量用于测试和保护 GraphQL 的工具。
*   [Checklist-Web-Aplication-Security](https://github.com/shieldfy/API-Security-Checklist) - API 安全清单，用于保护 API 的设计和实现。
*   [Hacking-APIs](https://github.com/Hacking-APIs/hacking-apis) - 《Hacking APIs》一书的官方仓库。
*   [Server-Side-Request-Forgery-SSRF-Bible](https://github.com/Phuong39/SSRF-bible-cheatsheet) - (重复) SSRF 备忘单，常用于攻击内部服务。
*   [Awesome-Web-Services](https://github.com/bregman-arie/awesome-web-services) - Web 服务相关资源，了解其工作原理是攻击的基础。

#### 4.2 API 攻防 (REST, GraphQL, gRPC)

*   [Postman](https://www.postman.com/) - API 开发、测试和文档化的协作平台，也是 API 安全测试的起点。
*   [Insomnia](https://github.com/Kong/insomnia) - 开源的、跨平台的 API 设计和测试工具。
*   [Kiterunner](https://github.com/assetnote/kiterunner) - API 暴力破解和内容发现工具，用于扫描 API 端点。
*   [GraphQLmap](https://github.com/swisskyrepo/GraphQLmap) - (重复) 用于映射 GraphQL 端点并进行渗透测试的脚本。
*   [InQL](https://github.com/doyensec/inql) - Burp Suite 插件，用于高级 GraphQL 测试。
*   [gRPC-UI](https://github.com/fullstorydev/grpcui) - gRPC 的交互式 Web UI，类似 Postman。
*   [gRPCurl](https://github.com/fullstorydev/grpcurl) - 类似 cURL 的 gRPC 命令行工具。
*   [Clairvoyance](https://github.com/nikitastupin/clairvoyance) - 无需单词表即可获取 GraphQL API 模式的工具。
*   [Astra](https://github.com/flipkart-incubator/Astra) - REST API 的自动化安全测试套件。
*   [Cherrybomb](https://github.com/blst-security/cherrybomb) - 用于发现 OpenAPI 规范中不一致性的 CLI 工具。
*   [Talisman](https://github.com/thoughtworks/talisman) - 在 Git 钩子中检测潜在秘密或敏感信息的工具，防止 API 密钥泄露。
*   [Mitm-relay](https://github.com/jrmdev/mitm_relay) - 旨在拦截、修改和重放非 HTTP 流量的中间人工具。
*   [Widdershins](https://github.com/Mermade/widdershins) - 将 OpenAPI/Swagger 等格式转换为 Markdown 文档。
*   [Swagger-Editor](https://github.com/swagger-api/swagger-editor) - OpenAPI/Swagger 规范的编辑器。
*   [OpenAPI-Generator](https://github.com/OpenAPITools/openapi-generator) - 根据 OpenAPI 规范生成客户端、服务器存根等。
*   [SOAP-UI](https://www.soapui.org/) - 开源的 Web 服务测试工具，支持 SOAP 和 REST。
*   [Karate](https://github.com/karatelabs/karate) - 开源的 API 测试自动化工具。
*   [Rest-assured](https://github.com/rest-assured/rest-assured) - 用于在 Java 中轻松测试 REST 服务的库。
*   [Frisby.js](https://github.com/frisby/frisby) - 基于 Jest 构建的 REST API 测试框架。

#### 4.3 Java 应用攻防 (反序列化, JNDI, etc.)

*   [ysoserial](https://github.com/frohoff/ysoserial) - (重复) 生成 Java 反序列化 Payload 的工具。
*   [Marshalsec](https://github.com/mbechler/marshalsec) - (重复) Java 反序列化利用库，支持多种格式和 payload。
*   [GadgetProbe](https://github.com/BishopFox/gadgetprobe) - (重复) 探测 Java 反序列化中可用的 gadget 链。
*   [Java-Deserialization-Cheat-Sheet](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet) - (重复) Java 反序列化备忘单。
*   [Fastjson-Exploit](https://github.com/c0ny1/fastjson-exploits) - (重复) Fastjson 漏洞利用工具。
*   [Log4j-scan](https://github.com/fullhunt/log4j-scan) - (重复) Log4Shell (CVE-2021-44228) 漏洞的扫描器。
*   [JNDI-Injection-Exploit](https://github.com/welk1n/JNDI-Injection-Exploit) - JNDI 注入利用工具。
*   [JNDI-Exploit-Kit](https://github.com/pimps/JNDI-Exploit-Kit) - JNDI 注入利用工具包。
*   [Shiro-Attack](https://github.com/j1anFen/shiro_attack) - Shiro 反序列化漏洞利用工具。
*   [Weblogic-Exploit](https://github.com/21superman/weblogic_exploit) - Weblogic 漏洞利用工具集合。
*   [Struts2-Scan](https://github.com/m-c-y/struts-scan) - Struts2 漏洞扫描和利用工具。
*   [Jackson-databind-deser-PoC](https://github.com/FasterXML/jackson-docs) - (重复) Jackson 官方文档，包含安全部分。
*   [Java-Decompiler](http://java-decompiler.github.io/) - Java 反编译工具 GUI。
*   [Recaf](https://github.com/Col-E/Recaf) - 现代化的 Java 字节码编辑器。
*   [Arthas](https://github.com/alibaba/arthas) - Alibaba 开源的 Java 诊断工具，也可用于安全分析。
*   [RASP (Runtime application self-protection)](https://github.com/baidu/openrasp) - 百度开源的运行时应用自我保护方案。
*   [Java-Bug-Bounty-Recon](https://github.com/s-p-k/Java-Bug-Bounty-Recon) - Java 应用的漏洞赏金侦察。
*   [Burp-ysoserial](https://github.com/summitt/burp-ysoserial) - 在 Burp Suite 中集成 ysoserial 的插件。
*   [Java-Exploit-Framework](https://github.com/4ra1n/y4-lang) - 一个 Java 安全研究与利用框架。

#### 4.4 .NET 应用攻防

*   [ysoserial.net](https://github.com/pwntester/ysoserial.net) - (重复) .NET 平台的反序列化 Payload 生成工具。
*   [dnSpy](https://github.com/dnSpy/dnSpy) - .NET 调试器和程序集编辑器。
*   [ILSpy](https://github.com/icsharpcode/ILSpy) - 开源的 .NET 程序集浏览器和反编译器。
*   [dotPeek](https://www.jetbrains.com/decompiler/) - JetBrains 出品的免费 .NET 反编译器。
*   [SharpExploit](https://github.com/knownsec/SharpExploit) - .NET 漏洞利用工具集。
*   [Exchange-Vulns](https://github.com/Yt1g3r/CVE-2021-26855_SSRF) - Exchange Server (ProxyLogon) 漏洞利用 PoC。
*   [ViewGen](https://github.com/0xacx/viewgen) - .NET ViewState 生成和解码工具。
*   [Sharepoint-Hacking](https://github.com/V1n1v131r4/SharePoint-Stuff) - Sharepoint 相关的攻击资源。

#### 4.5 PHP 应用攻防

*   [PHPGGC](https://github.com/ambionics/phpggc) - (重复) PHP 反序列化 Payload 生成器。
*   [PHP-Exploit-Scripts](https://github.com/cujanovic/PHP-Exploit-Scripts) - PHP 漏洞利用脚本集合。
*   [Weevely](https://github.com/epinna/weevely3) - 隐蔽的 PHP webshell 和后门。
*   [AntSword (中国蚁剑)](https://github.com/AntSwordProject/antSword) - 开源的、跨平台的网站管理工具（Webshell 管理）。
*   [Behinder (冰蝎)](https://github.com/rebeyond/Behinder) - 动态二进制加密网站管理客户端（Webshell 管理）。
*   [Godzilla (哥斯拉)](https://github.com/BeichenDream/Godzilla) - 另一款功能强大的 Webshell 管理工具。
*   [PHP-Vulnerability-Hunter](https://github.com/OneSourceCat/php-vulnerability-hunter) - PHP 漏洞静态分析工具。
*   [PHP-FPM-RCE](https://github.com/vulhub/vulhub/tree/master/php/fpm-rce) - PHP-FPM 远程命令执行漏洞环境。
*   [LFI-PHP-Wrapper](https://github.com/gellin/Team-Pentesting-LFI-Cheatsheet) - LFI 中利用 PHP wrapper 的备忘单。

#### 4.6 数据库攻防

*   [sqlmap](https://github.com/sqlmapproject/sqlmap) - (重复) 自动化的 SQL 注入和数据库接管工具。
*   [PowerUpSQL](https://github.com/NetSPI/PowerUpSQL) - (重复) 用于攻击 SQL Server 的 PowerShell 工具包。
*   [SQL-Server-Cheatsheet](https://github.com/trimstray/the-book-of-secret-knowledge/blob/master/docs/sql-injection-and-more.md) - SQL Server 攻击备忘单。
*   [Redis-Rogue-Server](https://github.com/Dliv3/redis-rogue-server) - (重复) Redis 未授权访问利用工具。
*   [MongoDB-Exploits](https://github.com/pedroetb/mongo-hacker) - MongoDB 的命令行增强工具，也可用于安全测试。
*   [Oracle-Pentest-Cheatsheet](https://github.com/Mohamed-512/Oracle-Pentest-Cheatsheet) - Oracle 数据库渗透测试备忘单。
*   [MSDAT (Microsoft SQL Database Attacking Tool)](https://github.com/quentinhardy/msdat) - 微软 SQL 数据库攻击工具。
*   [Elasticsearch-Exploit](https://github.com/vulhub/vulhub/tree/master/elasticsearch) - Elasticsearch 漏洞利用。
*   [DB-PT-Cheatsheet](https://github.com/mishmashclone/mishmash-pentest-tools/blob/master/cheatsheets/sqli-cheatsheet.txt) - 数据库渗透测试备忘单。

#### 4.7 中间件 & 消息队列攻防

*   [JBoss-Scan](https://github.com/joaomatosf/jexboss) - JBoss 应用服务器的漏洞扫描和利用工具。
*   [Tomcat-Exploits](https://github.com/A-poc/RedTeam-Tools/tree/master/web/Tomcat) - Tomcat 相关的漏洞利用工具。
*   [Nginx-Exploits](https://github.com/yandex/gixy) - Nginx 配置分析工具。
*   [Apache-Struts-Exploits](https://github.com/rapid7/metasploit-framework/tree/master/modules/exploits/multi/http) - Metasploit 中的 Struts 漏洞利用模块。
*   [Jenkins-Vulns](https://github.com/gquere/pwn_jenkins) - Jenkins 漏洞利用。
*   [RabbitMQ-Vulns](https://www.rabbitmq.com/security.html) - RabbitMQ 官方安全页面。
*   [ActiveMQ-RCE](https://github.com/apache/activemq/tree/main/activemq-website/src/components/classic/documentation/security-advisories) - ActiveMQ 安全公告。
*   [Awesome-Web-Server-Security](https://github.com/joesecurity/awesome-web-server-security) - Web 服务器安全资源。

#### 4.8 其他服务 & 协议攻防

*   [Memcached-injection-payloads](https://github.com/payloadbox/memcached-injection-payload-list) - Memcached 注入 Payload。
*   [FTP-Attack](https://github.com/vanhauser-thc/thc-hydra) - (重复) Hydra 可用于爆破 FTP。
*   [SMTP-Exploits](https://github.com/ticarpi/sparta/blob/master/modules/smtp.py) - SMTP 相关的利用脚本。
*   [SNMP-Attack](https://github.com/SECFORCE/sparta/blob/master/modules/snmp.py) - SNMP 相关的利用脚本。
*   [RDP-Exploits (BlueKeep)](https://github.com/robertdavidgraham/rdpscan) - BlueKeep (CVE-2019-0708) 扫描器。
*   [VNC-Hacking](https://github.com/htr-tech/zphisher) - (包含) Zphisher 中有 VNC 相关的钓鱼模板。
*   [LDAP-Injection-Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html) - OWASP 的 LDAP 注入备忘单。
*   [SIP-Hacking](https://github.com/EnableSecurity/sipvicious) - SIPVicious 套件，用于审计基于 SIP 的 VoIP 系统。
*   [VoIP-Hacking](https://github.com/jesusprubio/awesome-voip#security) - VoIP 安全资源。
*   [NTP-Amplification-Attack](https://github.com/vpnguy/ntp-amplification-attack) - NTP 放大攻击脚本。
*   [DNS-Amplification-Attack](https://github.com/crshd/dns-reflection-attack) - DNS 反射攻击脚本。
*   [DHCP-Attack](https://github.com/golismero/golismero/blob/master/plugins/recon/dhcp.py) - DHCP 侦察和攻击。

---

### 5. 系统与云原生攻防 (System & Cloud Native Attack & Defense)

#### 5.1 综合性 Awesome 列表 & 资源库

*   [Awesome Cloud Security](https://github.com/4ndersonLin/awesome-cloud-security) - 云安全领域的综合资源列表。
*   [Awesome Kubernetes Security](https://github.com/magnologan/awesome-k8s-security) - Kubernetes 安全资源列表。
*   [Awesome Container Security](https://github.com/kai5263499/awesome-container-security) - 容器安全资源列表。
*   [Awesome Cloud Native Security](https://github.com/Metarget/awesome-cloud-native-security) - 云原生安全资源列表。
*   [Awesome-Hacking](https://github.com/carpedm20/awesome-hacking) - (重复) 包含大量系统层面的攻击工具和资源。
*   [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - (重复) 包含大量针对 Linux 和 Windows 的提权、后门等 Payload。
*   [Linux-Kernel-Exploitation](https://github.com/xairy/linux-kernel-exploitation) - Linux 内核漏洞利用的学习资源。
*   [Windows-Kernel-Exploits](https://github.com/SecWiki/windows-kernel-exploits) - Windows 内核漏洞利用代码集合。
*   [Awesome-Serverless-Security](https://github.com/puresec/awesome-serverless-security) - Serverless 安全资源。
*   [Cloud-Sec-List](https://github.com/cloud-security-list/cloud-security-list) - 云安全工具、博客、事件等列表。
*   [Container-Security-Book](https://github.com/lizrice/container-security) - Liz Rice 的《容器安全》一书。
*   [Hacking-Kubernetes](https://github.com/Hacking-Kubernetes/Hacking-Kubernetes) - 《Hacking Kubernetes》一书的官方仓库。
*   [Cloud-Native-Security-Whitepaper](https://github.com/cncf/tag-security/tree/main/security-whitepaper) - CNCF 安全技术咨询小组的云原生安全白皮书。

#### 5.2 Windows 系统攻防

*   [Mimikatz](https://github.com/gentilkiwi/mimikatz) - 从 Windows 内存中提取明文密码、哈希、PIN 码和 Kerberos 票据的神器。
*   [PowerSploit](https://github.com/PowerShellMafia/PowerSploit) - PowerShell 的后渗透框架。
*   [Empire](https://github.com/BC-SECURITY/Empire) - PowerShell 和 Python 的后渗透利用代理。
*   [Sysinternals Suite](https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite) - 微软官方的 Windows 系统高级排错、管理和诊断工具集。
*   [BloodHound](https://github.com/BloodHoundAD/BloodHound) - 可视化 Active Directory 信任关系的工具，用于寻找攻击路径。
*   [Responder](https://github.com/lgandx/Responder) - LLMNR, NBT-NS 和 MDNS 投毒工具，用于获取 Net-NTLM 哈希。
*   [Impacket](https://github.com/fortra/impacket) - 用于处理网络协议的 Python 类库集合，包含大量 Windows 网络协议攻击脚本。
*   [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) - 用于评估大型 Active Directory 网络的后渗透工具。
*   [Rubeus](https://github.com/GhostPack/Rubeus) - Kerberos 交互和滥用的工具集。
*   [SharpHound](https://github.com/BloodHoundAD/SharpHound) - BloodHound 的官方 C# 数据收集器。
*   [PowerUpSQL](https://github.com/NetSPI/PowerUpSQL) - 用于攻击 SQL Server 的 PowerShell 工具包。
*   [LaZagne](https://github.com/AlessandroZ/LaZagne) - 开源的密码恢复工具，可抓取多种软件的密码。
*   [Juicy Potato](https://github.com/ohpe/juicy-potato) - Windows 权限提升工具 (Rotten Potato 的变种)。
*   [PrintSpoofer](https://github.com/itm4n/PrintSpoofer) - 滥用打印机服务进行权限提升。
*   [Windows-Exploit-Suggester](https://github.com/AonCyberLabs/Windows-Exploit-Suggester) - 根据系统补丁级别建议可用漏洞利用的工具。
*   [Sherlock](https://github.com/rasta-mouse/Sherlock) - PowerShell 脚本，用于快速查找本地提权漏洞。
*   [Watson](https://github.com/rasta-mouse/Watson) - .NET 工具，用于枚举 Windows 内核漏洞。
*   [Seatbelt](https://github.com/GhostPack/Seatbelt) - C# 工具，用于执行主机侦察和安全态势检查。
*   [DeathStar](https://github.com/byt3bl33d3r/DeathStar) - 通过 Empire 利用 GPO 在 AD 林中横向移动的脚本。
*   [AD-Attack-Defense](https://github.com/infosecn1nja/AD-Attack-Defense) - Active Directory 攻防资源。
*   [LOLBAS (Living Off The Land Binaries and Scripts)](https://github.com/LOLBAS-Project/LOLBAS) - 利用 Windows 系统自带的二进制文件和脚本进行攻击。
*   [ProcDump](https://docs.microsoft.com/en-us/sysinternals/downloads/procdump) - 微软官方的进程内存转储工具，可与 Mimikatz 配合。
*   [Sticky-Keys-Slayer](https://github.com/linuz/Sticky-Keys-Slayer) - 自动化利用粘滞键进行后门植入。
*   [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation) - PowerShell 命令混淆框架。
*   [Process-Hacker](https://github.com/processhacker/processhacker) - 强大的多功能工具，用于监视系统资源、调试软件和检测恶意软件。

#### 5.3 Linux 系统攻防

*   [LinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linpeas) - Linux 提权检查脚本 (Privilege Escalation Awesome Scripts SUITE)。
*   [Linux-Exploit-Suggester](https://github.com/mzet-/linux-exploit-suggester) - 基于操作系统版本号建议可用漏洞利用的工具。
*   [GTFOBins](https://gtfobins.github.io/) - 利用 Unix/Linux 系统自带二进制文件进行提权或绕过。
*   [PwnKit Exploit (CVE-2021-4034)](https://github.com/berdav/CVE-2021-4034) - Polkit 的 PwnKit 本地提权漏洞利用。
*   [Dirty-Pipe (CVE-2022-0847)](https://github.com/DataDog/dirty-pipe-scanner) - "脏管道"漏洞的检测和利用。
*   [Chkrootkit](http://www.chkrootkit.org/) - 本地检查 rootkit 的工具。
*   [RKHunter (Rootkit Hunter)](https://rkhunter.sourceforge.net/) - 扫描 rootkit、后门和本地漏洞。
*   [Lynis](https://github.com/CISOfy/lynis) - Linux, macOS 和 Unix-like 系统的安全审计和加固工具。
*   [Linux-Privilege-Escalation-Resources](https://github.com/lucyoa/kernel-exploits) - Linux 内核漏洞利用资源。
*   [Sudo-Killers](https://github.com/TH3xACE/SUDO_KILLER) - 利用 Sudo 配置错误进行提权的工具。
*   [Linux-Post-Exploitation-Command-List](https://github.com/mubix/post-exploitation/wiki/Linux-Post-Exploitation-Command-List) - Linux 后渗透命令列表。
*   [Linux-Hardening-Guid](https://github.com/trimstray/linux-hardening-guide) - Linux 安全加固指南。
*   [SELinux-Game](http://selinuxgame.io/) - 通过游戏学习 SELinux。
*   [AppArmor](https://apparmor.net/) - Linux 内核的安全模块，用于限制程序的能力。
*   [Auditd](https://github.com/linux-audit/audit-userspace) - Linux 审计系统。
*   [OSSEC](https://github.com/ossec/ossec-hids) - 开源的主机入侵检测系统 (HIDS)。
*   [Wazuh](https://github.com/wazuh/wazuh) - (重复) 基于 OSSEC 的开源安全平台。
*   [Falco](https://github.com/falcosecurity/falco) - (重复) 云原生运行时安全工具，常用于 Linux 主机和容器。

#### 5.4 容器攻防 (Docker, containerd)

*   [Deepce](https://github.com/zane-f/Deepce) - Docker/K8s 攻防利用工具。
*   [Docker-bench-security](https://github.com/docker/docker-bench-security) - 检查 Docker 是否遵循安全最佳实践的脚本。
*   [Trivy](https://github.com/aquasecurity/trivy) - (重复) 简单而全面的容器镜像、文件系统和 Git 仓库漏洞扫描器。
*   [Clair](https://github.com/quay/clair) - 开源的容器镜像漏洞静态分析工具。
*   [Grype](https://github.com/anchore/grype) - Anchore 出品的容器镜像和文件系统漏洞扫描器。
*   [Dagda](https://github.com/eliasgranderubio/dagda) - 扫描 Docker 镜像中的已知漏洞、木马、病毒等。
*   [Dive](https://github.com/wagoodman/dive) - 用于探索 Docker/OCI 镜像、层内容和发现减小镜像大小方法的工具。
*   [Hadolint](https://github.com/hadolint/hadolint) - Dockerfile 的 linter 和静态分析工具。
*   [Slim](https://github.com/slimtoolkit/slim) - 自动瘦身 Docker 镜像的工具，减少攻击面。
*   [Docker-escape-ctf](https://github.com/reni2/docker-escape-cve-2019-5736) - runC 容器逃逸漏洞 (CVE-2019-5736) 的 PoC。
*   [Control-groups-in-containers](https://github.com/lizrice/cgroups-hands-on) - 动手学习 cgroups。
*   [Namespaces-in-Go](https://github.com/lizrice/namespaces-in-go) - 动手学习 namespaces。
*   [Sysdig](https://github.com/draios/sysdig) - (重复) 系统级的探索、监控和排错工具，支持容器。
*   [Kata-Containers](https://github.com/kata-containers/kata-containers) - 使用轻量级虚拟机提供更强隔离性的安全容器运行时。
*   [gVisor](https://github.com/google/gvisor) - Google 出品的应用内核（沙箱），为容器提供安全隔离。
*   [Container-security-checklist](https://github.com/krol3/container-security-checklist) - 容器安全清单。
*   [Docker-Secure-Deployment-Guidelines](https://github.com/CISOfy/lynis/blob/master/controls/DOCK.md) - Docker 安全部署指南。

#### 5.5 Kubernetes 攻防

*   [Kube-hunter](https://github.com/aquasecurity/kube-hunter) - 在 Kubernetes 集群中寻找安全弱点。
*   [Kube-bench](https://github.com/aquasecurity/kube-bench) - 检查 Kubernetes 是否部署安全的工具，基于 CIS Kubernetes Benchmark。
*   [Kube-score](https://github.com/zegl/kube-score) - Kubernetes 对象定义的静态代码分析工具。
*   [Kube-scan](https://github.com/octarinesec/kube-scan) - 扫描 Kubernetes 集群的风险，给出评分。
*   [Kubelet-attack](https://github.com/cncf/wg-security/blob/main/best-practices/kubernetes-pod-security.md) - Kubelet 相关的攻击面分析。
*   [Kubescape](https://github.com/kubescape/kubescape) - 第一个用于测试 Kubernetes 是否基于 NSA 和 CISA 的 K8s 加固指南部署的工具。
*   [Peirates](https://github.com/inguardians/peirates) - Kubernetes 渗透测试工具。
*   [CDK (Container-Device-Interface)](https://github.com/cdk-team/CDK) - CDK 是一款为容器环境定制的渗透测试工具。
*   [Helm-secrets](https://github.com/jkroepke/helm-secrets) - 用于管理 Helm chart 中秘密的插件。
*   [Kyverno](https://github.com/kyverno/kyverno) - 为 Kubernetes 设计的策略引擎。
*   [OPA/Gatekeeper](https://github.com/open-policy-agent/gatekeeper) - 使用 Open Policy Agent 的 Kubernetes 策略控制器。
*   [Kube-apiserver-attack](https://github.com/cncf/tag-security/blob/main/security-whitepaper/v2/Section-4-Kubernetes-Security.md#41-api-server) - Kube-apiserver 攻击面分析。
*   [ETCD-Security](https://etcd.io/docs/v3.5/op-guide/security/) - etcd 官方安全指南。
*   [Kubernetes-Goat](https://github.com/madhuakula/kubernetes-goat) - 有意设计为易受攻击的 Kubernetes 集群，用于学习。
*   [Kube-Linter](https://github.com/stackrox/kube-linter) - 静态分析 Kubernetes YAML 文件和 Helm chart 的工具。
*   [Terrascan](https://github.com/tenable/terrascan) - (重复) 检测 IaC 中的安全问题，支持 Kubernetes。
*   [Checkov](https://github.com/bridgecrewio/checkov) - (重复) IaC 的静态代码分析工具，支持 Kubernetes。
*   [Datree](https://github.com/datreeio/datree) - 防止将错误的 Kubernetes 配置推送到生产环境。
*   [K9s](https://github.com/derailed/k9s) - Kubernetes CLI，用于管理集群，也可用于安全审查。
*   [Lens](https://github.com/lensapp/lens) - Kubernetes IDE，提供强大的可视化和管理能力。

#### 5.6 云平台攻防 (AWS, Azure, GCP)

*   [Pacu](https://github.com/RhinoSecurityLabs/pacu) - AWS 漏洞利用框架。
*   [Cloud-sploit](https://github.com/aquasecurity/cloudsploit) - AWS, Azure, GCP 和 Oracle Cloud 的安全与合规性检查工具。
*   [Prowler](https://github.com/prowler-cloud/prowler) - AWS 安全最佳实践评估、审计、加固和应急响应工具。
*   [ScoutSuite](https://github.com/nccgroup/ScoutSuite) - 多云安全审计工具。
*   [Cloud-enum](https://github.com/initstring/cloud_enum) - (重复) 多云 OSINT 枚举工具。
*   [WeirdAAL](https://github.com/carnal0wnage/weirdAAL) - (重复) AWS 攻击和侦察工具。
*   [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) - Rhino Security Labs 的“易受攻击的 by design” AWS 部署工具。
*   [TerraGoat](https://github.com/bridgecrewio/terragoat) - Bridgecrew 的“易受攻击的 by design” Terraform 项目。
*   [Lambda-Guard](https://github.com/Skyscanner/LambdaGuard) - AWS Lambda 安全扫描器。
*   [GCP-Bucket-Brute](https://github.com/RhinoSecurityLabs/GCPBucketBrute) - 暴力破解 Google Cloud Storage 存储桶名称的脚本。
*   [S3Scanner](https://github.com/sa7mon/S3Scanner) - (重复) 扫描 AWS S3 存储桶的错误配置。
*   [Cloud-mapper](https://github.com/VirtueSecurity/cloud-mapper) - (重复) 分析 AWS 环境，生成网络图。
*   [Steampipe](https://github.com/turbot/steampipe) - 使用 SQL 查询你的云基础设施。
*   [Cartography](https://github.com/lyft/cartography) - 将基础设施资产及其关系在直观的图表中进行可视化。
*   [ElectricEye](https://github.com/cisagov/ElectricEye) - 持续的 AWS 安全审计。
*   [Azure-Hunter](https://github.com/darkbitio/azure-hunter) - Azure 平台的威胁狩猎工具。
*   [MicroBurst](https://github.com/NetSPI/MicroBurst) - Azure 服务的 PowerShell 工具集。
*   [Azucar](https://github.com/nccgroup/azucar) - Azure 平台的安全审计工具。

#### 5.7 IaC & GitOps 安全

*   [Checkov](https://github.com/bridgecrewio/checkov) - IaC 的静态代码分析工具 (Terraform, CloudFormation, Kubernetes, etc.)。
*   [Terrascan](https://github.com/tenable/terrascan) - 检测 IaC 中的安全问题。
*   [Tfsec](https://github.com/aquasecurity/tfsec) - Terraform 代码的静态分析安全扫描器。
*   [Kics](https://github.com/Checkmarx/kics) - 查找 IaC 中的安全漏洞、合规性问题和基础设施错误配置。
*   [Regula](https://github.com/fugue/regula) - 评估 Terraform 和 CloudFormation 基础设施即代码的合规性。
*   [Atlantis](https://github.com/runatlantis/atlantis) - Terraform 的 Pull Request 自动化。
*   [Argo CD](https://github.com/argoproj/argo-cd) - Kubernetes 的声明式 GitOps 持续交付工具。
*   [Flux](https://github.com/fluxcd/flux2) - 为 Kubernetes 提供 GitOps 的工具集。
*   [Awesome-IaC-Security](https://github.com/jens-classen/awesome-iac-security) - IaC 安全资源列表。

---

### 6. 红队作战与高级威胁 (Red Teaming & Advanced Threats)

#### 6.1 综合性 Awesome 列表 & 资源库

*   [Awesome Red Teaming](https://github.com/yeyintminthuhtut/Awesome-Red-Teaming) - 最全面的红队资源列表，涵盖所有阶段。
*   [Awesome C2 (Command and Control)](https://github.com/uhub/awesome-c2) - C2 框架、项目和资源的权威列表。
*   [Awesome Evasion](https://github.com/s3cr3t-t0p/awesome-evasion) - 专注于免杀和绕过技术的资源列表。
*   [Awesome-Cobalt-Strike](https://github.com/zer0yu/Awesome-CobaltStrike) - Cobalt Strike 相关资源、插件和工具。
*   [Red Teaming Toolkit](https://github.com/infosecn1nja/Red-Teaming-Toolkit) - (重复) 红队作战工具包。
*   [MITRE ATT&CK®](https://github.com/mitre/attack-navigator) - MITRE ATT&CK 框架的导航器，红蓝对抗的通用语言。
*   [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - (重复) 包含大量横向移动、权限维持和免杀的 Payload。
*   [APT-Notes](https://github.com/kbandla/APTnotes) - 多年来公开的 APT（高级持续性威胁）报告和文档集合。
*   [Red-Team-Infrastructure-Wiki](https://github.com/bluscreenofjeff/Red-Team-Infrastructure-Wiki) - 红队基础设施搭建的 Wiki。
*   [Red-Team-Tips](https://github.com/rvrsh3ll/Red-Team-Tips) - 红队技巧集合。
*   [The-Red-Team-Tool-Kit](https://github.com/S3cur3Th1sSh1t/The-Red-Team-Tool-Kit) - 红队工具包脚本。
*   [Awesome-APT-Reports](https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections) - APT 报告集合。
*   [Tradecraft](https://github.com/S3cur3Th1sSh1t/A-Red-Teamer-s-guide-to-GPO-and-OPSEC) - 红队 GPO 操作指南。
*   [RedTeam-Techniques](https://github.com/mantvydasb/RedTeam-Tactics-and-Techniques) - 红队战术与技术。
*   [Adversary Emulation Library](https://github.com/center-for-threat-informed-defense/adversary_emulation_library) - 对手模拟计划库。

#### 6.2 命令与控制 (C2) 框架

*   [Cobalt Strike](https://www.cobaltstrike.com/) - 红队作战和对手模拟的商业标杆 C2 框架。
*   [Metasploit Framework](https://github.com/rapid7/metasploit-framework) - (重复) 经典的开源渗透测试框架，包含 C2 功能。
*   [Empire](https://github.com/BC-SECURITY/Empire) - (重复) PowerShell 和 Python 的后渗透利用代理。
*   [Sliver](https://github.com/BishopFox/sliver) - Go 编写的、跨平台的、开源的 C2 框架，被认为是 Cobalt Strike 的有力替代品。
*   [Covenant](https://github.com/cobbr/Covenant) - .NET 编写的、Web 界面的 C2 框架。
*   [Havoc](https://github.com/HavocFramework/Havoc) - 现代化、可扩展的后渗透 C2 框架。
*   [Brute Ratel C4](https://bruteratel.com/) - 商业 C2 框架，以其强大的免杀能力著称。
*   [Mythic](https://github.com/its-a-feature/Mythic) - Go 编写的、跨平台的、基于 Web 的 C2 框架，支持多种 Agent。
*   [PoshC2](https://github.com/nettitude/PoshC2) - 完全由 PowerShell 编写的 C2 框架。
*   [Merlin](https://github.com/Ne0nd0g/merlin) - Go 编写的、跨平台的、利用 HTTP/2 进行 C2 通信的后渗透工具。
*   [Starkiller](https://github.com/BC-SECURITY/Starkiller) - Empire 的图形化前端界面。
*   [SILENTTRINITY](https://github.com/byt3bl33d3r/SILENTTRINITY) - 使用 IronPython 和 .NET DLR 的异步 C2。
*   [Koadic](https://github.com/zerosum0x0/koadic) - Windows JScript / VBScript C2。
*   [Quasar](https://github.com/quasar/QuasarRAT) - C# 编写的开源远程管理工具 (RAT)。
*   [AsyncRAT](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp) - C# 编写的开源远程访问木马。
*   [DeimosC2](https://github.com/DeimosC2/DeimosC2) - Go 编写的 C2。
*   [GoPhish](https://github.com/gophish/gophish) - (重复) 开源钓鱼框架，常用于初始访问。
*   [Evilginx2](https://github.com/kgretzky/evilginx2) - (重复) 中间人攻击框架，用于网络钓鱼凭证和会话劫持。

#### 6.3 权限维持 & 持久化

*   [Awesome-Persistence](https://github.com/Karneades/awesome-persistence) - 权限维持技术资源列表。
*   [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) - (重复) 映射到 MITRE ATT&CK 的小型、可移植的检测测试库，包含大量持久化技术。
*   [SharpPersist](https://github.com/fireeye/SharpPersist) - .NET 程序集，用于实现 Windows 权限维持。
*   [Persistence-Sniper](https://github.com/last-byte/Persistence-Sniper) - Powershell 脚本，用于在 Windows 上寻找持久化后门。
*   [Python-for-Red-Teaming](https://github.com/nassiben/Red-Team-Python-Tooling) - 用于红队的 Python 工具，包含持久化脚本。
*   [Schtasks-persistence](https://attack.mitre.org/techniques/T1053/005/) - 利用计划任务进行持久化。
*   [WMI-Persistence](https://github.com/fireeye/SharPersist/blob/master/SharPersist/SharPersist.cs) - 利用 WMI 事件订阅进行持久化。
*   [Registry-RunKeys-Persistence](https://attack.mitre.org/techniques/T1547/001/) - 利用注册表运行键进行持久化。
*   [DLL-Hijacking](https://github.com/KINGSABRI/DLL-Hijacking-Hunter) - DLL 劫持猎手。
*   [COM-Hijacking](https://github.com/tyranid/oleviewdotnet) - .NET 编写的 OLE/COM 对象查看和反编译工具。
*   [Powershell-Persistence-Cookbook](https://github.com/darkoperator/Posh-Sec-Mod/blob/master/Post-Exploitation/Persistence.ps1) - PowerShell 持久化脚本。
*   [Weevely](https://github.com/epinna/weevely3) - (重复) 隐蔽的 PHP webshell。
*   [AntSword](https://github.com/AntSwordProject/antSword) - (重复) Webshell 管理工具。

#### 6.4 横向移动

*   [Impacket](https://github.com/fortra/impacket) - (重复) 包含 `psexec.py`, `smbexec.py`, `wmiexec.py` 等大量横向移动脚本。
*   [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) - (重复) 自动化利用凭证在网络中进行横向移动。
*   [BloodHound](https://github.com/BloodHoundAD/BloodHound) - (重复) 寻找 Active Directory 中的横向移动路径。
*   [Invoke-TheHash](https://github.com/Kevin-Robertson/Invoke-TheHash) - PowerShell 哈希传递攻击工具。
*   [Mimikatz](https://github.com/gentilkiwi/mimikatz) - (重复) 包含 `sekurlsa::pth` (Pass-the-Hash) 和 `sekurlsa::tickets` (Pass-the-Ticket) 功能。
*   [Rubeus](https://github.com/GhostPack/Rubeus) - (重复) Kerberos 滥用工具，用于 Kerberoasting, AS-REP Roasting 等。
*   [KrbRelayUp](https://github.com/Dec0ne/KrbRelayUp) - 通用的 Kerberos 中继提权工具。
*   [SharpExec](https://github.com/anthemtotheego/SharpExec) - .NET 编写的横向移动工具集。
*   [Go-psexec](https://github.com/vincd/go-psexec) - Go 语言实现的 PsExec。
*   [SSH-Lateral-Movement](https://github.com/mubix/post-exploitation/wiki/SSH-Pivoting) - SSH 代理和隧道技术。
*   [Plink](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) - PuTTY 的命令行接口，可用于隧道和代理。
*   [Chisel](https://github.com/jpillora/chisel) - Go 编写的快速 TCP/UDP 隧道，可通过 HTTP 传输。
*   [Ligolo-ng](https://github.com/nicocha30/ligolo-ng) - 先进、简单、快速的隧道/代理工具，使用 TUN/TAP 接口。
*   [Pivotnacci](https://github.com/blackarrowsec/pivotnacci) - 通过 socks4 代理进行网络扫描。
*   [Ssh-mitm](https://github.com/jtesta/ssh-mitm) - SSH 中间人服务器。
*   [Evil-WinRM](https://github.com/Hackplayers/evil-winrm) - WinRM 的终极 shell。
*   [PsExec](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec) - 微软官方的 PsExec。

#### 6.5 免杀 & 绕过 (AV/EDR Evasion)

*   [ScareCrow](https://github.com/optiv/ScareCrow) - EDR 绕过 Payload 生成框架。
*   [Shellcode-Loader](https://github.com/TheWover/donut) - 将 .NET 程序集转换为 Shellcode。
*   [Gargoyle](https://github.com/JLospinoso/gargoyle) - 使用 PEB 混淆和加密来绕过内存扫描的工具。
*   [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation) - (重复) PowerShell 命令混淆框架。
*   [AMSI.fail](https://amsi.fail/) - 在线生成绕过 AMSI (Antimalware Scan Interface) 的 PowerShell 脚本。
*   [Amsi-Bypass-Powershell](https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell) - 绕过 AMSI 的方法集合。
*   [UAC-bypass](https://github.com/hfiref0x/UACME) - 绕过 Windows UAC 的方法集合。
*   [SysWhispers2](https://github.com/jthuraisamy/SysWhispers2) - 在不使用 Windows API 的情况下直接生成系统调用的工具。
*   [Hell's Gate](https://github.com/am0nsec/HellsGate) - 使用 Hell's Gate 技术绕过 EDR 的 PoC。
*   [SharpBlock](https://github.com/gaasedelen/SharpBlock) - 阻止 EDR 对 .NET 程序集进行 hook 的工具。
*   [Invisibility-Cloak](https://github.com/peewpw/Invoke-PSImage) - 将 PowerShell 脚本编码到 PNG 图片像素中并执行。
*   [Unhooking-Patching-EDR-Bypass](https://github.com/TheD1rkMtr/Unhooking-Patching-EDR-Bypass) - EDR 绕过技术。
*   [Reflective-DLL-Injection](https://github.com/stephenfewer/ReflectiveDLLInjection) - 反射式 DLL 注入技术。
*   [Process-Injection](https://github.com/s3cur3th1ssh1t/Process-Injection) - 进程注入技术集合。
*   [Process-Hollowing](https://github.com/m0n0ph1/Process-Hollowing) - 进程镂空技术 PoC。
*   [Phantom-Evasion](https://github.com/oddcod3/Phantom-Evasion) - Python 编写的杀毒软件规避工具。
*   [Veil-Framework](https://github.com/Veil-Framework/Veil) - 生成绕过常见杀毒软件的 Metasploit Payload。
*   [The-Backdoor-Factory](https://github.com/secretsquirrel/the-backdoor-factory) - 在可执行文件中植入后门。
*   [Al-Khaser](https://github.com/LordNoteworthy/al-khaser) - 用于反调试和反虚拟机检测的 PoC。
*   [Vba-obfuscator](https://github.com/decalage2/VBA-obfuscator) - VBA 宏混淆工具。
*   [Evil-Office](https://github.com/the-xentropy/xencrypt) - Office 文档加密和混淆工具。
*   [DKMC (Don't Kill My Cat)](https://github.com/Mr-Un1k0d3r/DKMC) - Shellcode 混淆和生成工具。
*   [Nim-Shellcode-Loader](https://github.com/a-rey/Nim-Shellcode-Loader) - 使用 Nim 语言编写的 Shellcode 加载器。
*   [Freeze](https://github.com/optiv/Freeze) - 使用多种技术来规避 EDR 和 AV 的 Payload 工具包。

#### 6.6 武器化 & Payload 开发

*   [Metasploit's msfvenom](https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-msfvenom.html) - Metasploit 的 Payload 生成器。
*   [Shellcode-Generators](https://github.com/b3mb4m/shellsploit-framework) - (重复) Shellsploit 框架。
*   [Donut](https://github.com/TheWover/donut) - (重复) 将 .NET 程序集转换为 Shellcode。
*   [Macro-Pack](https://github.com/sevagas/macro_pack) - 用于自动生成混淆的 MS Office 宏、VBS 脚本等的工具。
*   [Unicorn](https://github.com/trustedsec/unicorn) - 用于 PowerShell 降级攻击并直接将 Shellcode 注入内存的工具。
*   [HTA-Attack](https://github.com/trustedsec/unicorn/blob/master/unicorn.py) - Unicorn 可生成 HTA 攻击向量。
*   [Social-Engineer-Toolkit (SET)](https://github.com/trustedsec/social-engineer-toolkit) - 专为社会工程学设计的开源渗透测试框架。
*   [Certutil-Payloads](https://lolbas-project.github.io/lolbas/Binaries/Certutil/) - 利用 certutil.exe 下载和执行 Payload。
*   [PowerShell-Armory](https://github.com/cfalta/PowerShellArmory) - PowerShell 武器化脚本。
*   [Malicious-Macro-Generator](https://github.com/Mr-Un1k0d3r/MaliciousMacroGenerator) - 恶意宏生成器。
*   [GadgetToJScript](https://github.com/med0x2e/GadgetToJScript) - 生成 .NET 反序列化 Payload 并用于 JScript/VBScript。
*   [CACTUSTORCH](https://github.com/mdsecactivebreach/CACTUSTORCH) - 用于执行 Shellcode 的 VBScript 和 JScript。
*   [SharpShooter](https://github.com/mdsecactivebreach/SharpShooter) - Payload 创建框架，用于检索和执行任意 C# 源代码。
*   [DotNetToJScript](https://github.com/tyranid/DotNetToJScript) - 将 .NET 程序集转换为 JScript/VBScript/VBA 的工具。

#### 6.7 APT 报告 & 对手模拟

*   [APT-Simulator](https://github.com/NextronSystems/APTSimulator) - 模拟 APT 攻击行为的 Windows 批处理脚本。
*   [Red-Team-Automation (RTA)](https://github.com/endgameinc/RTA) - 提供一个模拟恶意行为的脚本框架。
*   [Caldera](https://github.com/mitre/caldera) - MITRE 的自动化对手模拟系统。
*   [FlightSim](https://github.com/alphasoc/flightsim) - 用于生成和执行对手模拟场景的工具。
*   [Invoke-Adversary](https://github.com/CyberMonitor/Invoke-Adversary) - PowerShell 脚本，用于模拟对手技术。
*   [APT-Hunter](https://github.com/ahmed-mesbah/APT-Hunter) - 威胁狩猎工具，用于检测 APT 活动。
*   [APT-Group-Paper](https://github.com/Oshlack/APT-groups-and-operations) - APT 组织和行动的资料。
*   [MITRE-ATTACK-scripts](https://github.com/mitre-attack/attack-scripts) - MITRE ATT&CK 相关的脚本。
*   [FireEye-Threat-Research](https://www.mandiant.com/resources/insights/threat-research) - FireEye/Mandiant 的威胁研究报告。
*   [Kaspersky-APT-Reports](https://securelist.com/category/apt-reports/) - 卡巴斯基的 APT 报告。
*   [CrowdStrike-Adversary-Reports](https://www.crowdstrike.com/resources/reports/) - CrowdStrike 的对手报告。
*   [Talos-Threat-Research](https://blog.talosintelligence.com/) - Cisco Talos 的威胁研究博客。

---

### 7. 蓝队防御与事件响应 (Blue Teaming & Incident Response)

#### 7.1 综合性 Awesome 列表 & 资源库

*   [Awesome Cybersecurity Blue Team](https://github.com/fabacab/awesome-cybersecurity-blueteam) - 最全面的蓝队资源列表，覆盖所有方面。
*   [Awesome Incident Response](https://github.com/meirwah/awesome-incident-response) - 专注于事件响应的工具和资源列表。
*   [Awesome Threat Intelligence](https://github.com/hslatman/awesome-threat-intelligence) - 威胁情报资源，蓝队的关键输入。
*   [Awesome Threat Detection](https://github.com/0x4D31/awesome-threat-detection) - 威胁检测技术和资源。
*   [Awesome Forensics](https://github.com/mre/awesome-forensics) - 数字取证工具和资源。
*   [Awesome-Honeypots](https://github.com/paralax/awesome-honeypots) - 蜜罐资源，用于欺骗和捕获攻击者。
*   [Blue-Team-Tools](https://github.com/Purp1eW0lf/Blue-Team-Tools) - 蓝队工具集合。
*   [Blue Team Field Manual (BTFM)](https://github.com/sans-blue-team/BTFM) - SANS 蓝队现场手册。
*   [The-Hunters-Handbook](https://github.com/The-Art-of-Hacking/h4cker/blob/master/The_Hunters_Handbook.md) - 威胁猎人手册。
*   [Incident-Response-Plan-template](https://github.com/SANS-Templates/incident-response-plan-template) - SANS 事件响应计划模板。
*   [Awesome-Security-Hardening](https://github.com/decalage2/awesome-security-hardening) - 安全加固资源。
*   [Awesome-YARA](https://github.com/InQuest/awesome-yara) - YARA 规则、工具和资源。
*   [Awesome-PCAP](https://github.com/hadynz/awesome-pcaptools) - PCAP 分析工具。
*   [Security-Playbooks](https://github.com/counteractive/incident-response-plan-template/tree/master/playbooks) - 事件响应剧本。
*   [Awesome-SOAR](https://github.com/correlatedsecurity/awesome-soar) - SOAR (安全编排、自动化与响应) 平台资源。

#### 7.2 SIEM, SOAR & 日志管理

*   [Wazuh](https://github.com/wazuh/wazuh) - 开源的、统一的 XDR 和 SIEM 平台。
*   [OSSEC](https://github.com/ossec/ossec-hids) - 开源的主机入侵检测系统 (HIDS)。
*   [Elastic Stack (ELK)](https://github.com/elastic/elasticsearch) - Elasticsearch, Logstash, Kibana 组合，强大的日志分析和 SIEM 解决方案。
*   [Graylog](https://github.com/Graylog2/graylog2-server) - 开源的日志管理平台。
*   [Splunk](https://www.splunk.com/) - 商业日志管理和数据分析的领导者。
*   [TheHive](https://github.com/TheHive-Project/TheHive) - 可扩展的、开源的、免费的安全事件响应平台。
*   [Shuffle](https://github.com/frikky/Shuffle) - 开源的 SOAR 平台。
*   [Fluentd](https://github.com/fluent/fluentd) - 开源的数据收集器，用于统一日志记录层。
*   [Log-MD](https://github.com/PUNCH-Cyber/log-md) - Windows 日志分析工具。
*   [Sigma](https://github.com/SigmaHQ/sigma) - 通用的、开放的 SIEM 告警规则格式。
*   [ElastAlert](https://github.com/Yelp/elastalert) - 对 Elasticsearch 中的数据进行异常、峰值或其他模式检测并发出告警。
*   [StreamAlert](https://github.com/airbnb/streamalert) - Airbnb 出品的实时数据分析和告警框架。
*   [OpenCTI](https://github.com/OpenCTI-Platform/opencti) - 开源的威胁情报平台。
*   [MISP (Malware Information Sharing Platform)](https://github.com/MISP/MISP) - 开源的威胁情报共享平台。
*   [Loki](https://github.com/grafana/loki) - Grafana 出品的、类似 Prometheus 但用于日志的系统。
*   [Vector](https://github.com/vectordotdev/vector) - 高性能的可观测性数据管道。
*   [GoAccess](https://github.com/allinurl/goaccess) - 实时的 Web 日志分析器和交互式查看器。
*   [Log-Dissector](https://github.com/A-k-s-h-a-y/Log-Dissector) - 日志分析和事件关联工具。

#### 7.3 主机入侵检测 & 监控 (HIDS / EDR)

*   [Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) - 微软官方的 Windows 系统高级监控工具。
*   [Sysmon-modular](https://github.com/olafhartong/sysmon-modular) - 模块化的 Sysmon 配置文件。
*   [Velociraptor](https://github.com/Velocidex/velociraptor) - 先进的数字取证和事件响应工具。
*   [Osquery](https://github.com/osquery/osquery) - 将操作系统视为高性能关系数据库，使用 SQL 进行查询。
*   [GRR Rapid Response](https://github.com/google/grr) - Google 出品的远程实时取证框架。
*   [Auditd](https://github.com/linux-audit/audit-userspace) - (重复) Linux 审计系统。
*   [Loki (Simple IOC Scanner)](https://github.com/Neo23x0/Loki) - 简单的 IOC (Indicators of Compromise) 扫描器。
*   [ClamAV](https://github.com/Cisco-Talos/clamav) - 开源的反病毒引擎。
*   [Linux-Process-Monitor](https://github.com/netblue30/firejail) - Firejail，使用 Linux 命名空间和 seccomp-bpf 的 SUID 程序沙箱。
*   [ProcMon-for-Linux](https://github.com/microsoft/ProcMon-for-Linux) - 微软官方的 ProcMon 的 Linux 版本。
*   [Autoruns](https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns) - 微软官方的 Windows 启动项检查工具。
*   [OSSEC-Rules](https://github.com/ossec/ossec-rules) - OSSEC 官方规则。
*   [Sysdig](https://github.com/draios/sysdig) - (重复) 系统级的探索、监控和排错工具。
*   [Zeek (formerly Bro)](https://github.com/zeek/zeek) - (重复) 强大的网络分析框架，也可用于主机事件分析。
*   [LimaCharlie](https://github.com/refractionPOINT/limacharlie) - 提供 EDR 功能的安全中间件。

#### 7.4 网络入侵检测 & 监控 (NIDS / NSM)

*   [Snort](https://github.com/snort3/snort3) - 著名的开源网络入侵防御系统 (NIPS) 和网络入侵检测系统 (NIDS)。
*   [Suricata](https://github.com/OISF/suricata-rules) - 高性能的网络 IDS, IPS 和网络安全监控引擎。
*   [Zeek (formerly Bro)](https://github.com/zeek/zeek) - 强大的网络分析框架，远不止于 NIDS。
*   [Wireshark](https://www.wireshark.org/) - 最流行的网络协议分析器。
*   [Tshark](https://www.wireshark.org/docs/man-pages/tshark.html) - Wireshark 的命令行版本。
*   [Tcpdump](https://github.com/the-tcpdump-group/tcpdump) - 强大的命令行网络抓包工具。
*   [Moloch / Arkime](https://github.com/arkime/arkime) - 开源的、大规模的全包捕获、索引和数据库系统。
*   [Stenographer](https://github.com/google/stenographer) - Google 出品的全包捕获工具。
*   [Ntopng](https://github.com/ntop/ntopng) - 网络流量探针和分析器。
*   [Security-Onion](https://github.com/Security-Onion-Solutions/securityonion) - 用于威胁狩猎、网络安全监控和日志管理的免费开源 Linux 发行版。
*   [Malcolm](https://github.com/idaholab/Malcolm) - 强大的、易于部署的网络流量分析工具套件。
*   [Nfsen](https://github.com/phaag/nfsen) - NetFlow 分析工具。
*   [Awesome-PCAP-Analysis](https://github.com/haka-security/haka) - Haka，开源的安全监控语言。
*   [Network-Miner](http://www.netresec.com/?page=NetworkMiner) - 开源的网络取证分析工具 (NFAT)。
*   [Sguil](https://github.com/bammv/sguil) - 用于网络安全分析的 GUI。
*   [PF_RING](https://github.com/ntop/PF_RING) - 高速抓包库。
*   [DPDK](https://github.com/DPDK/dpdk) - 数据平面开发套件，用于快速包处理。

#### 7.5 数字取证 & 内存分析

*   [The Volatility Framework](https://github.com/volatilityfoundation/volatility) - 领先的开源内存取证框架 (Volatility 2)。
*   [Volatility3](https://github.com/volatilityfoundation/volatility3) - Volatility 的下一代版本。
*   [Autopsy](https://github.com/sleuthkit/autopsy) - The Sleuth Kit 的图形化界面，数字取证平台。
*   [The Sleuth Kit](https://github.com/sleuthkit/sleuthkit) - 用于分析磁盘镜像和恢复文件的命令行工具库。
*   [Plaso / log2timeline](https://github.com/log2timeline/plaso) - 从各种来源提取时间戳并将其合并到一条时间线中。
*   [LiME (Linux Memory Extractor)](https://github.com/504ensicsLabs/LiME) - 可加载的内核模块，用于从 Linux 和 Android 设备获取内存镜像。
*   [Redline](https://www.fireeye.com/services/freeware/redline.html) - FireEye/Mandiant 的免费主机调查工具。
*   [Bulk_extractor](https://github.com/simsong/bulk_extractor) - 快速的、并行的、可扩展的特征扫描器。
*   [Forensic-Tools](https://github.com/sandflysecurity/sandfly-files) - Sandfly Security 的取证工具。
*   [Timesketch](https://github.com/google/timesketch) - 用于协作取证时间线分析的开源工具。
*   [Kansa](https://github.com/davehull/Kansa) - PowerShell 编写的模块化事件响应框架。
*   [AVML (Acquire Volatile Memory for Linux)](https://github.com/microsoft/avml) - 微软出品的 Linux 内存获取工具。
*   [DumpIt](https://www.comae.com/dumpit/) - Windows 内存获取工具。
*   [Magnet RAM Capture](https://www.magnetforensics.com/resources/magnet-ram-capture/) - 免费的 Windows 内存获取工具。
*   [FTK Imager](https://www.exterro.com/ftk-imager) - 免费的数据预览和镜像工具。
*   [Eric Zimmerman's Tools](https://ericzimmerman.github.io/) - 一系列优秀的 Windows 取证工具。
*   [DFIR-Cheat-Sheets](https://github.com/sans-dfir/dfir-cheatsheets) - SANS DFIR 备忘单。
*   [Awesome-Forensics-Resources](https://github.com/PaulSec/awesome-forensics) - 另一个数字取证资源列表。
*   [DFIR-Training](https://dfir.training/) - DFIR 培训资源网站。

#### 7.6 威胁狩猎 & 对手模拟

*   [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) - 映射到 MITRE ATT&CK 的小型、可移植的检测测试库。
*   [Caldera](https://github.com/mitre/caldera) - (重复) MITRE 的自动化对手模拟系统。
*   [APT-Simulator](https://github.com/NextronSystems/APTSimulator) - (重复) 模拟 APT 攻击行为的 Windows 批处理脚本。
*   [Threat-Hunter-Playbook](https://github.com/OTRF/ThreatHunter-Playbook) - 将 ATT&CK 技术映射到各种数据源和分析方法的剧本。
*   [HELK (Hunting ELK Stack)](https://github.com/Cyb3rWard0g/HELK) - 具有高级分析能力的威胁狩猎 ELK 栈。
*   [DeepBlueCLI](https://github.com/sans-blue-team/DeepBlueCLI) - 使用 PowerShell 进行 Windows 事件日志威胁狩猎。
*   [Chainsaw](https://github.com/WithSecureLabs/chainsaw) - 快速搜索和提取 Windows 事件日志中的记录。
*   [Hayabusa](https://github.com/Yamato-Security/hayabusa) - Go 编写的 Windows 事件日志快速取证时间线生成器。
*   [VECTR](https://github.com/SecurityRiskAdvisors/VECTR) - (重复) 用于追踪红队和蓝队活动的工具。
*   [Detection-Rules](https://github.com/elastic/detection-rules) - Elastic Security 的检测规则。
*   [Splunk-Security-Content](https://github.com/splunk/security_content) - Splunk 安全内容的分析故事、搜索、仪表板等。
*   [Yara-Rules](https://github.com/Yara-Rules/rules) - 开源的 YARA 规则集合。
*   [Florian-Roth-Sigma-Rules](https://github.com/Neo23x0/sigma) - Florian Roth 的 Sigma 规则。
*   [ThreatHunting](https://github.com/ThreatHuntingProject/ThreatHunting) - 威胁狩猎项目。
*   [Invoke-ThreatIntel](https://github.com/darkoperator/Posh-ThreatIntel) - PowerShell 的威胁情报模块。

#### 7.7 安全加固 & 合规性

*   [Lynis](https://github.com/CISOfy/lynis) - (重复) Linux, macOS 和 Unix-like 系统的安全审计和加固工具。
*   [OpenSCAP](https://github.com/OpenSCAP/openscap) - 实现 SCAP (Security Content Automation Protocol) 标准的开源工具集。
*   [CIS-Benchmarks](https://www.cisecurity.org/cis-benchmarks/) - 业界公认的安全配置基线。
*   [InSpec](https://github.com/inspec/inspec) - 开源的测试、审计和合规性框架。
*   [Dev-Sec-Hardening-Framework](https://github.com/dev-sec/ansible-os-hardening) - 使用 Ansible 进行操作系统加固。
*   [Windows-Hardening](https://github.com/teusink/Windows-10-hardening) - Windows 10 加固脚本。
*   [Linux-Hardening-Guid](https://github.com/trimstray/linux-hardening-guide) - (重复) Linux 安全加固指南。
*   [Docker-bench-security](https://github.com/docker/docker-bench-security) - (重复) 检查 Docker 是否遵循安全最佳实践的脚本。
*   [Kube-bench](https://github.com/aquasecurity/kube-bench) - (重复) 检查 Kubernetes 是否部署安全的工具。
*   [Prowler](https://github.com/prowler-cloud/prowler) - (重复) AWS 安全最佳实践评估、审计、加固工具。
*   [ScoutSuite](https://github.com/nccgroup/ScoutSuite) - (重复) 多云安全审计工具。
*   [Awesome-Security-Policy](https://github.com/trylinux/awesome-security-policy) - 安全策略模板和资源。

---

### 8. 安全开发与代码审计 (Secure Development & Code Auditing)

#### 8.1 综合性 Awesome 列表 & 资源库

*   [Awesome AppSec](https://github.com/paragonie/awesome-appsec) - 应用安全（AppSec）的综合资源列表。
*   [OWASP Cheat Sheet Series](https://github.com/OWASP/CheatSheetSeries) - (重复) OWASP 出品的安全开发速查表，安全编码的黄金标准。
*   [OWASP Secure Coding Practices-Quick Reference Guide](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) - OWASP 安全编码实践快速参考指南。
*   [Awesome DevSecOps](https://github.com/TaptuIT/awesome-devsecops) - DevSecOps 相关的工具、服务和资源。
*   [Awesome-Static-Analysis](https://github.com/mre/awesome-static-analysis) - 静态分析工具、linter 和代码质量检查器的集合。
*   [Awesome-Code-Review](https://github.com/joho/awesome-code-review) - 代码审查工具和资源。
*   [Secure-Coding-Guidlines](https://github.com/CERT-SEI/code-guidelines) - CERT 的安全编码标准。
*   [Web-Security-Learning](https://github.com/CHYbeta/Web-Security-Learning) - (重复) Web 安全学习笔记，包含代码审计部分。
*   [Code-Audit-Learning](https://github.com/cn-src/Code-Audit-Learning) - 代码审计学习资料。
*   [Application-Security-Checklist](https://github.com/mainstay/appsec-checklist) - 应用安全清单。
*   [Awesome-Software-Composition-Analysis](https://github.com/sonatype-nexus-community/awesome-software-composition-analysis) - 软件成分分析（SCA）工具和资源。
*   [OWASP-SAMM](https://github.com/OWASP/samm) - 软件保障成熟度模型（SAMM）。
*   [OWASP-ASVS](https://github.com/OWASP/ASVS) - 应用安全验证标准（ASVS）。
*   [Security-Champion-Playbook](https://github.com/c0rdis/security-champion-playbook) - 安全冠军手册。

#### 8.2 静态应用安全测试 (SAST) - 多语言

*   [Semgrep](https://github.com/semgrep/semgrep) - 快速、开源的静态分析工具，易于编写自定义规则。
*   [CodeQL](https://github.com/github/codeql) - GitHub 出品的代码分析引擎，用于自动化安全检查。
*   [SonarQube](https://github.com/SonarSource/sonarqube) - 开源的、用于持续检查代码质量和安全的平台。
*   [Bandit](https://github.com/PyCQA/bandit) - 专为查找 Python 代码中常见安全问题而设计的工具。
*   [Brakeman](https://github.com/presidentbeef/brakeman) - Ruby on Rails 应用的静态分析安全漏洞扫描器。
*   [Gitleaks](https://github.com/gitleaks/gitleaks) - (重复) 在 Git 仓库中检测硬编码的秘密。
*   [TruffleHog](https://github.com/trufflesecurity/trufflehog) - (重复) 在 git 仓库中搜索高熵字符串和秘密。
*   [Horusec](https://github.com/ZupIT/horusec) - 开源的 SAST, SCA 和 IaC 扫描工具。
*   [Graudit](https://github.com/wireghoul/graudit) - 简单的脚本和签名，允许对代码库进行 grep 以查找潜在的安全漏洞。
*   [SCA-Sanner](https://github.com/DDuarte/sca-scanner) - 静态代码分析器。
*   [Insider](https://github.com/insidersec/insider) - 专注于覆盖 OWASP Top 10 的开源 SAST 工具。
*   [PMD](https://github.com/pmd/pmd) - 可扩展的多语言静态代码分析器。
*   [FindBugs](https://github.com/findbugsproject/findbugs) - (已不活跃，但有继任者) Java 静态分析工具。
*   [SpotBugs](https://github.com/spotbugs/spotbugs) - FindBugs 的精神继任者，用于 Java 静态分析。
*   [Checkmarx](https://checkmarx.com/) - 商业 SAST 解决方案的领导者。
*   [Veracode](https://www.veracode.com/products/static-analysis-sast) - 商业应用安全平台，提供 SAST。
*   [Fortify](https://www.microfocus.com/en-us/cyberres/application-security/static-code-analyzer) - Micro Focus 的 Fortify SCA。
*   [Snyk Code](https://snyk.io/product/snyk-code/) - Snyk 的开发者优先的 SAST 工具。
*   [Dependency-Check](https://github.com/jeremylong/DependencyCheck) - (重复) OWASP 的 SCA 工具，也可视为广义 SAST 的一部分。
*   [Mega-Linter](https://github.com/oxsecurity/megalinter) - 可嵌入 CI/CD 流程的开源 Linter 聚合器。

#### 8.3 静态应用安全测试 (SAST) - 特定语言

*   **Java**
    *   [SpotBugs](https://github.com/spotbugs/spotbugs) - (重复) FindBugs 的继任者。
    *   [Kunlun-Mirror](https://github.com/LoRexxar/Kunlun-Mirror) - 国产的白盒代码审计工具，支持 PHP, JavaScript, Java。
    *   [Fortify-Java-Rules](https://github.com/fortify-inc/fortify-rules) - Fortify 的 Java 规则。
    *   [Error-prone](https://github.com/google/error-prone) - Google 出品的 Java 静态分析工具，能捕获编译时错误。
*   **Python**
    *   [Bandit](https://github.com/PyCQA/bandit) - (重复) 查找 Python 代码中的常见安全问题。
    *   [Pyt](https://github.com/python-security/pyt) - 基于污点分析的 Python 静态分析器。
    *   [Flake8](https://github.com/PyCQA/flake8) - Python 代码 linter，可集成安全插件。
    *   [Safety](https://github.com/pyupio/safety) - (重复) 检查 Python 依赖中的已知安全漏洞。
*   **JavaScript / TypeScript**
    *   [ESLint](https://github.com/eslint/eslint) - (重复) 可插拔的 JS linting 工具，可配置安全规则。
    *   [Nodejsscan](https://github.com/ajinabraham/nodejsscan) - Node.js 应用的静态安全代码扫描器。
    *   [Retire.js](https://github.com/RetireJS/retire.js) - (重复) 检测使用了已知漏洞的 JS 库。
    *   [ScanJS](https://github.com/scanjs/scanjs) - 专注于 Node.js 安全的静态分析器。
*   **PHP**
    *   [PHPStan](https://github.com/phpstan/phpstan) - PHP 静态分析工具。
    *   [Psalm](https://github.com/vimeo/psalm) - Vimeo 出品的 PHP 静态分析工具。
    *   [Phan](https://github.com/phan/phan) - PHP 的静态分析器。
    *   [RIPS](https://www.ripstech.com/) - (已被 Sonar 收购) 商业 PHP 静态分析工具。
    *   [Seay-Source-Code-Auditing-System](https://github.com/f1tz/seay) - 国产的 PHP 代码审计系统。
*   **Ruby**
    *   [Brakeman](https://github.com/presidentbeef/brakeman) - (重复) Rails 应用的静态分析安全扫描器。
    *   [RuboCop](https://github.com/rubocop/rubocop) - Ruby 静态代码分析器和格式化工具。
*   **Go**
    *   [Gosec](https://github.com/securego/gosec) - Go 语言安全检查器。
    *   [Staticcheck](https://github.com/dominikh/go-tools) - Go 语言的高级静态分析工具集。
*   **C / C++**
    *   [Flawfinder](https://dwheeler.com/flawfinder/) - 扫描 C/C++ 源代码，报告潜在的安全漏洞。
    *   [Cppcheck](https://github.com/danmar/cppcheck) - C/C++ 代码的静态分析工具。
*   **Solidity (Smart Contracts)**
    *   [Slither](https://github.com/crytic/slither) - (重复) Solidity 静态分析框架。
    *   [Mythril](https://github.com/ConsenSys/mythril-classic) - (重复) 以太坊智能合约安全分析工具。

#### 8.4 软件成分分析 (SCA) & 依赖安全

*   [OWASP Dependency-Check](https://github.com/jeremylong/DependencyCheck) - 扫描项目依赖项并检查是否存在已知、公开披露的漏洞。
*   [Snyk Open Source](https://snyk.io/product/software-composition-analysis/) - 查找并修复开源依赖项中的漏洞。
*   [Dependabot](https://github.com/dependabot) - (已集成到 GitHub) 自动创建 PR 来保持你的依赖项更新。
*   [Trivy](https://github.com/aquasecurity/trivy) - (重复) 不仅扫描容器，也扫描文件系统和 Git 仓库的依赖。
*   [Syft](https://github.com/anchore/syft) - 从容器镜像和文件系统中生成软件物料清单 (SBOM)。
*   [Grype](https://github.com/anchore/grype) - (重复) 扫描 Syft 生成的 SBOM 以查找漏洞。
*   [CycloneDX](https://github.com/CycloneDX) - 轻量级的软件物料清单 (SBOM) 标准。
*   [SPDX (Software Package Data Exchange)](https://github.com/spdx) - 另一个 SBOM 标准。
*   [Safety](https://github.com/pyupio/safety) - 检查 Python 依赖中的已知安全漏洞。
*   [Bundler-audit](https://github.com/rubysec/bundler-audit) - 为 Ruby 的 Bundler 提供补丁级别的版本验证。
*   [NPM-audit](https://docs.npmjs.com/cli/v8/commands/npm-audit) - npm CLI 内置的依赖审计工具。
*   [Yarn-audit](https://classic.yarnpkg.com/en/docs/cli/audit/) - Yarn 内置的依赖审计工具。
*   [OSSIndex](https://ossindex.sonatype.org/) - Sonatype 提供的免费漏洞数据库。
*   [Renovate](https://github.com/renovatebot/renovate) - 自动化的依赖更新工具，类似 Dependabot。
*   [JFrog Xray](https://jfrog.com/xray/) - 商业 SCA 工具。
*   [Black Duck](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis.html) - Synopsys 的商业 SCA 解决方案。

#### 8.5 动态应用安全测试 (DAST)

*   [OWASP ZAP (Zed Attack Proxy)](https://github.com/zaproxy/zaproxy) - (重复) 开源的 DAST 工具。
*   [Arachni](https://github.com/Arachni/arachni) - (重复) 功能丰富的模块化 Web 应用安全扫描框架。
*   [Nikto](https://github.com/sullo/nikto) - (重复) Web 服务器漏洞扫描器。
*   [Wapiti](https://github.com/wapiti-scanner/wapiti) - (重复) Web 应用漏洞黑盒扫描器。
*   [Burp Suite Scanner](https://portswigger.net/burp/vulnerability-scanner) - (重复) Burp Suite 的主动扫描功能。
*   [Acunetix](https://www.acunetix.com/) - (重复) 商业 DAST 工具。
*   [Invicti (Netsparker)](https://www.invicti.com/) - (重复) 商业 DAST 工具。
*   [Gauntlt](https://github.com/gauntlt/gauntlt) - 将各种安全工具转换为测试框架，用于 BDD（行为驱动开发）。
*   [BDD-Security](https://github.com/continuumsecurity/bdd-security) - 使用 BDD 方式进行安全测试的框架。

#### 8.6 交互式应用安全测试 (IAST) & 运行时保护 (RASP)

*   [Contrast Security](https://www.contrastsecurity.com/) - IAST 和 RASP 领域的商业领导者。
*   [Seeker (Synopsys)](https://www.synopsys.com/software-integrity/security-testing/interactive-application-security-testing.html) - Synopsys 的 IAST 解决方案。
*   [OpenRASP](https://github.com/baidu/openrasp) - (重复) 百度开源的运行时应用自我保护（RASP）方案。
*   [Sqreen](https://www.sqreen.com/) - (已被 Datadog 收购) RASP 和应用安全监控。
*   [IAST-Resources](https://github.com/IAST/awesome-iast) - IAST 相关资源。

#### 8.7 代码审计方法论 & 学习

*   [Code-Auditing-Notes](https://github.com/hongriSec/Code-Auditing-Notes) - 代码审计学习笔记。
*   [PHP-Audit-Labs](https://github.com/Monyer/php-audit-labs) - PHP 代码审计入门学习靶场。
*   [RIPS-Code-Auditing-Challenges](https://www.ripstech.com/java-security-challenge-2018/) - RIPS 的代码审计挑战赛。
*   [Awesome-Vulnerable-Apps](https://github.com/vulnerables/awesome-vulnerable-apps) - 精选的各种“易受攻击”的应用，用于学习和练习。
*   [Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA) - (重复) 经典的漏洞练习靶场。
*   [WebGoat](https://github.com/WebGoat/WebGoat) - OWASP 出品的、有意设计为不安全的 J2EE Web 应用。
*   [Juice Shop](https://github.com/juice-shop/juice-shop) - OWASP 出品的、可能是最现代和最复杂的 Web 漏洞练习应用。
*   [Code-Review-Best-Practices](https://google.github.io/eng-practices/review/reviewer/) - Google 的代码审查最佳实践。
*   [How-to-read-code](https://github.com/bolshchikov/js-good-parts) - 如何阅读代码。
*   [Source-Code-Analysis-Tools](https://owasp.org/www-community/Source_Code_Analysis_Tools) - OWASP 的源代码分析工具列表。

---

### 9. 逆向工程与恶意软件 (Reverse Engineering & Malware)

#### 9.1 综合性 Awesome 列表 & 资源库

*   [Awesome Reverse Engineering](https://github.com/alphaSeclab/awesome-reverse-engineering) - 最全面的逆向工程资源列表，涵盖工具、课程、书籍等。
*   [Awesome Malware Analysis](https://github.com/rshipp/awesome-malware-analysis) - 恶意软件分析工具和资源的权威列表。
*   [Awesome-Hacking](https://github.com/carpedm20/awesome-hacking) - (重复) 包含大量逆向和恶意软件分析工具。
*   [Reverse-Engineering-Tutorials](https://github.com/mytechnotalent/Reverse-Engineering-Tutorials) - 逆向工程教程。
*   [Malware-Analysis-Training](https://github.com/OpenRCE/Malware-Analysis-Training) - 恶意软件分析培训材料。
*   [The-Art-of-Reversing](https://github.com/The-Art-of-Hacking/h4cker/blob/master/The_Art_of_Reversing.md) - 逆向工程艺术。
*   [Reverse-Engineering-for-Beginners](https://github.com/rev-eng-for-beginners/reverse-engineering-for-beginners) - 为初学者准备的免费书籍。
*   [Malware-Source-Code](https://github.com/vxunderground/MalwareSourceCode) - VX-Underground 收集的大量恶意软件源代码。
*   [Awesome-Android-Security](https://github.com/ashishb/android-security-awesome) - Android 安全资源，包含大量逆向工具。
*   [Awesome-iOS-Security](https://github.com/Siguza/ios-resources) - iOS 安全资源。
*   [Awesome-Firmware-Security](https://github.com/PreOS-Security/awesome-firmware-security) - 固件安全和逆向资源。
*   [RE-for-beginners](https://begin.re/) - 逆向工程入门网站。
*   [Legend-of-Roppers](https://github.com/a1exdandy/Ropper-YSoSirius) - 逆向工程挑战。

#### 9.2 反汇编器 & 反编译器

*   [IDA Pro](https://hex-rays.com/ida-pro/) - 交互式反汇编器的行业标杆，功能极其强大。
*   [Ghidra](https://github.com/NationalSecurityAgency/ghidra) - NSA 出品的开源软件逆向工程框架，包含反编译器。
*   [Binary Ninja](https://binary.ninja/) - 现代化的、可编程的二进制分析平台。
*   [Radare2](https://github.com/radareorg/radare2) - 开源的、功能强大的逆向工程框架和命令行工具集。
*   [Cutter](https://github.com/rizinorg/cutter) - Radare2 的图形化界面。
*   [Rizin](https://github.com/rizinorg/rizin) - Radare2 的一个分支，专注于可用性和社区。
*   [JEB Decompiler](https://www.pnfsoftware.com/) - 专业的 Android 和 Java 反编译器。
*   [Hopper Disassembler](https://www.hopperapp.com/) - 适用于 macOS 和 Linux 的反汇编器/反编译器。
*   [dnSpy](https://github.com/dnSpy/dnSpy) - (重复) .NET 调试器和程序集编辑器，包含反编译器。
*   [ILSpy](https://github.com/icsharpcode/ILSpy) - (重复) 开源的 .NET 程序集浏览器和反编译器。
*   [Jadx](https://github.com/skylot/jadx) - Android Dex 和 Apk 文件的反编译器。
*   [Bytecode-Viewer](https://github.com/Konloch/bytecode-viewer) - Java 8 字节码查看器、反编译器、编辑器等。
*   [Recaf](https://github.com/Col-E/Recaf) - (重复) 现代化的 Java 字节码编辑器。
*   [Objdump](https://sourceware.org/binutils/docs/binutils/objdump.html) - GNU Binutils 中的一部分，用于显示二进制文件信息。
*   [Capstone Engine](https://github.com/capstone-engine/capstone) - 轻量级的多平台、多架构反汇编框架。
*   [DiStorm](https://github.com/gdabah/distorm) - 用于 x86/AMD64 的快速反汇编库。
*   [RetDec](https://github.com/avast/retdec) - Avast 出品的、可重定向的机器码反编译器。

#### 9.3 调试器

*   [x64dbg](https://github.com/x64dbg/x64dbg) - 适用于 Windows 的开源 x64/x32 调试器，被认为是 OllyDbg 的现代替代品。
*   [WinDbg](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools) - 微软官方的 Windows 调试器。
*   [GDB (GNU Debugger)](https://www.gnu.org/software/gdb/) - GNU 项目的标准化调试器。
*   [GEF](https://github.com/hugsy/gef) - (重复) GDB 增强功能，为漏洞利用开发和逆向工程设计。
*   [Pwndbg](https://github.com/pwndbg/pwndbg) - (重复) GDB 的一个插件，使调试对逆向工程师和 Exploit 开发者更友好。
*   [PEDA](https://github.com/longld/peda) - (重复) GDB 的 Python Exploit 开发辅助。
*   [Immunity Debugger](https://www.immunityinc.com/products/debugger/) - 专为漏洞利用开发和恶意软件分析设计的调试器。
*   [OllyDbg](http://www.ollydbg.de/) - 经典的 32 位 Windows 汇编级分析调试器。
*   [Frida](https://github.com/frida/frida) - 动态代码插桩工具包，可用于注入脚本到黑盒进程。
*   [Frida-Tools](https://github.com/frida/frida-tools) - Frida 的命令行工具。
*   [Objection](https://github.com/sensepost/objection) - 运行时移动端安全评估框架，基于 Frida。
*   [LLDB](https://github.com/llvm/llvm-project/tree/main/lldb) - LLVM 项目中的下一代高性能调试器。
*   [ScyllaHide](https://github.com/x64dbg/ScyllaHide) - x64dbg 的反-反调试插件。
*   [IDASkins](https://github.com/zyantific/IDASkins) - IDA Pro 的皮肤插件。
*   [IDAPython](https://github.com/idapython/src) - IDA Pro 的 Python 插件。

#### 9.4 动态分析 & 沙箱

*   [Cuckoo Sandbox](https://github.com/cuckoosandbox/cuckoo) - 领先的开源自动化恶意软件分析系统。
*   [CAPE Sandbox](https://github.com/kevoreilly/CAPEv2) - Cuckoo 的一个分支，专注于配置提取和恶意软件功能检测。
*   [Any.run](https://any.run/) - 交互式的在线恶意软件分析沙箱。
*   [Hybrid-Analysis](https://www.hybrid-analysis.com/) - CrowdStrike 的免费恶意软件分析服务。
*   [Joe Sandbox](https://www.joesandbox.com/) - 商业深度恶意软件分析平台。
*   [INetSim](https://github.com/inetsim/inetsim) - 模拟常见互联网服务的套件，用于在实验室环境中分析恶意软件的网络行为。
*   [Fakenet-NG](https://github.com/fireeye/flare-fakenet-ng) - FireEye 的下一代动态网络分析工具。
*   [ProcMon (Process Monitor)](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) - 微软官方的 Windows 高级监控工具，显示实时文件系统、注册表和进程/线程活动。
*   [ProcDot](https://www.procdot.com/) - ProcMon 日志的可视化和分析工具。
*   [Regshot](https://github.com/bro-devel/regshot-1.9.0) - 开源的注册表比较工具，用于分析恶意软件对注册表的修改。
*   [Apktool](https://github.com/iBotPeaches/apktool) - 用于逆向 Android 应用的工具。
*   [MobSF (Mobile Security Framework)](https://github.com/MobSF/Mobile-Security-Framework) - 自动化的、一体化的移动应用（Android/iOS/Windows）渗透测试、恶意软件分析和安全评估框架。
*   [Qiling Framework](https://github.com/qilingframework/qiling) - (重复) 先进的二进制仿真框架，可用于动态分析。
*   [Unicorn Engine](https://github.com/unicorn-engine/unicorn) - 轻量级的多平台、多架构 CPU 模拟器框架。
*   [Tiny-Tracer](https://github.com/hasherezade/tiny_tracer) - 用于动态追踪二进制文件执行的工具。
*   [Noriben](https://github.com/Rurik/Noriben) - 可移植的、基于 ProcMon 的恶意软件分析沙箱。
*   [DRAKVUF](https://github.com/tklengyel/drakvuf) - 基于虚拟化、无代理的恶意软件动态分析系统。

#### 9.5 静态分析 & 文件格式

*   [YARA](https://github.com/VirusTotal/yara) - 用于识别和分类恶意软件样本的“模式匹配瑞士军刀”。
*   [Yara-Rules](https://github.com/Yara-Rules/rules) - (重复) 开源的 YARA 规则集合。
*   [PE-bear](https://github.com/hasherezade/pe-bear) - 可移植的 PE 文件查看器。
*   [PEview](http://wjradburn.com/software/) - 查看 PE 文件头信息的经典工具。
*   [Detect It Easy (DIE)](https://github.com/horsicq/Detect-It-Easy) - 用于确定文件类型的程序。
*   [Exeinfo PE](http://www.exeinfo.pe.hu/) - PE 文件加壳、加密、编译器信息检测工具。
*   [Manalyze](https://github.com/JusticeRage/Manalyze) - 强大的 PE 文件静态分析器。
*   [Strings](https://docs.microsoft.com/en-us/sysinternals/downloads/strings) - 微软官方的字符串提取工具。
*   [FLOSS (FireEye Labs Obfuscated String Solver)](https://github.com/fireeye/flare-floss) - 自动从恶意软件二进制文件中提取混淆字符串。
*   [Resource Hacker](http://www.angusj.com/resourcehacker/) - Windows 应用程序的资源编辑器。
*   [010 Editor](https://www.sweetscape.com/010editor/) - 专业的十六进制编辑器和文件解析器。
*   [HxD](https://mh-nexus.de/en/hxd/) - 免费的、快速的十六进制编辑器。
*   [Ghidra-Scripts](https://github.com/ghidraninja/ghidra_scripts) - Ghidra 脚本集合。
*   [IDA-Scripts](https://github.com/onethawt/idapython-cheatsheet) - IDA Pro Python 脚本备忘单。
*   [BinText](https://www.aldeid.com/wiki/BinText) - 文本字符串提取工具。
*   [PDF-Parser](https://github.com/smalot/pdfparser) - 解析 PDF 文件以提取关键元素的 PHP 库。
*   [PDFStreamDumper](https://github.com/dzzie/pdfstreamdumper) - 用于分析恶意 PDF 文件的工具。
*   [Oletools](https://github.com/decalage2/oletools) - 用于分析 MS OLE2 文件（如 Word, Excel）的 Python 工具集。
*   [Viper](https://github.com/viper-framework/viper) - 二进制分析和管理框架。

#### 9.6 反混淆 & 脱壳

*   [De4dot](https://github.com/de4dot/de4dot) - .NET 反混淆器和脱壳器。
*   [UnpacMe](https://www.unpac.me/) - 自动化的在线脱壳服务。
*   [UPX](https://github.com/upx/upx) - 著名的可执行文件压缩器，也常被恶意软件使用。
*   [NoMoreXOR](https://github.com/hiddenillusion/NoMoreXOR) - 猜测 256 字节 XOR 密钥的工具。
*   [Packer-Detector](https://github.com/accupara/packer-detector) - 加壳检测工具。
*   [XORSearch](https://blog.didierstevens.com/programs/xorsearch/) - 在文件中搜索异或、移位等编码的字符串。
*   [FLARE-VM](https://github.com/fireeye/flare-vm) - FireEye 出品的、用于恶意软件分析的 Windows 虚拟机配置脚本。
*   [REMnux](https://remnux.org/) - 用于逆向工程和恶意软件分析的 Linux 发行版。
*   [Deobfuscator](https://github.com/ben-holland/deobfuscator) - JavaScript 反混淆器。
*   [JS-Beautifier](https://github.com/beautify-web/js-beautify) - JavaScript 代码格式化工具。
*   [Py-unpacker](https://github.com/extremecoders-re/pyinstxtractor) - PyInstaller 生成的 Windows 可执行文件的提取器。
*   [Uncompyle6](https://github.com/rocky/python-uncompyle6) - Python 跨版本反编译器。

#### 9.7 恶意软件样本 & 报告

*   [MalwareBazaar](https://bazaar.abuse.ch/) - abuse.ch 的恶意软件样本交换平台。
*   [VirusTotal](https://www.virustotal.com/) - 分析文件和 URL 以检测恶意内容的服务。
*   [TheZoo](https://github.com/ytisf/theZoo) - 包含大量恶意软件样本的仓库。
*   [InQuest-Labs](https://labs.inquest.net/) - InQuest 的恶意文件数据库。
*   [Malshare](https://malshare.com/) - 免费的恶意软件样本库。
*   [VirusShare](https://virusshare.com/) - 提供大量恶意软件样本的系统。
*   [Any.run-Public-Tasks](https://app.any.run/submissions/) - Any.run 上的公开分析任务。
*   [FireEye-Threat-Research](https://www.mandiant.com/resources/insights/threat-research) - (重复) FireEye/Mandiant 的威胁研究报告。
*   [Kaspersky-Securelist](https://securelist.com/) - (重复) 卡巴斯基的威胁研究博客。
*   [Talos-Blog](https://blog.talosintelligence.com/) - (重复) Cisco Talos 的威胁研究博客。
*   [Unit42-Paloalto](https://unit42.paloaltonetworks.com/) - Palo Alto Networks 的威胁情报团队博客。
*   [Threat-Hunting-Reports](https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries) - 微软 365 Defender 的威胁狩猎查询。

---

### 10. 夺旗赛与技能提升 (CTF & Skill Development)

#### 10.1 综合性 Awesome 列表 & 资源库

*   [Awesome CTF](https://github.com/apsdehal/awesome-ctf) - 最全面的 CTF 资源列表，涵盖平台、工具、Writeup 等。
*   [Awesome-Hacking](https://github.com/carpedm20/awesome-hacking) - (重复) 包含大量适用于 CTF 的工具和资源。
*   [CTF-Tools](https://github.com/ZJAZAn/CTF-Tools) - CTF 工具集合，分类清晰。
*   [CTF-All-In-One](https://github.com/firmianay/CTF-All-In-One) - CTF 知识库，包含各种类型的题目和解法。
*   [CTF-Wiki](https://github.com/ctf-wiki/ctf-wiki) - 一个自由、开放的 CTF 知识库，系统性地介绍了 CTF 各个方向的知识。
*   [CTF-Resources](https://github.com/ctfs/resources) - CTF 资源集合，包含入门指南和工具。
*   [Awesome-Vulnerable-Apps](https://github.com/vulnerables/awesome-vulnerable-apps) - (重复) 精选的各种“易受攻击”的应用，是绝佳的练习靶场。
*   [Capture-The-Flag-Tools](https://github.com/r00t-3xp10it/capture-the-flag-framework) - CTF 框架。
*   [CTF-Cheatsheet](https://github.com/w181496/CTF-Cheatsheet) - CTF 速查表。
*   [Hacker-Roadmap](https://github.com/sundowndev/hacker-roadmap) - 成为黑客的学习路线图。
*   [Red-Team-Challenges](https://github.com/cyprosecurity/Red-Team-Challenges) - 红队挑战题目。
*   [Blue-Team-Challenges](https://github.com/cyprosecurity/Blue-Team-Challenges) - 蓝队挑战题目。
*   [CTF-From-Scratch](https://github.com/google/google-ctf/tree/master/docs/beginners-guide) - Google CTF 的新手指南。

#### 10.2 CTF 平台 & 靶场

*   **综合平台**
    *   [Hack The Box](https://www.hackthebox.com/) - 最著名的在线渗透测试靶场平台之一。
    *   [TryHackMe](https://tryhackme.com/) - 对新手非常友好的、游戏化的在线网络安全学习平台。
    *   [VulnHub](https://www.vulnhub.com/) - 提供大量可下载的、含有漏洞的虚拟机镜像。
    *   [CTFtime](https://ctftime.org/) - 全球 CTF 赛事日历和队伍排名。
    *   [PicoCTF](https://picoctf.org/) - CMU 主办的、面向初学者的免费 CTF 平台。
    *   [Root-me](https://www.root-me.org/) - 提供超过 400 个网络安全挑战。
    *   [Hacker101](https://www.hackerone.com/hackers/hacker101) - HackerOne 出品的免费 Web 安全课程和 CTF。
    *   [WeChall](https://www.wechall.net/) - 挑战站点聚合平台。
    *   [OverTheWire](https://overthewire.org/wargames/) - 通过 Wargames 学习安全概念。
    *   [PentesterLab](https://pentesterlab.com/) - 提供从入门到高级的 Web 渗透测试练习。
    *   [Immersive Labs](https://immersivelabs.com/) - 企业级的网络安全技能提升平台。
    *   [RingZer0 Team Online CTF](https://ringzer0ctf.com/) - 提供超过 200 个挑战。
    *   [CTFd](https://github.com/CTFd/CTFd) - 流行的、开源的 CTF 竞赛平台搭建框架。
    *   [Mellivora](https://github.com/Nakiami/mellivora) - 另一个开源的 CTF 引擎。
    *   [FBCTF](https://github.com/facebook/fbctf) - Facebook 开源的 CTF 平台。
*   **Web 安全**
    *   [Juice Shop](https://github.com/juice-shop/juice-shop) - (重复) OWASP 出品的现代 Web 漏洞练习应用。
    *   [Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA) - (重复) 经典的 PHP/MySQL 漏洞练习靶场。
    *   [WebGoat](https://github.com/WebGoat/WebGoat) - (重复) OWASP 出品的 J2EE 漏洞练习应用。
    *   [bWAPP](http://www.itsecgames.com/) - 有意设计为不安全的 Web 应用，包含超过 100 个漏洞。
    *   [PortSwigger Web Security Academy](https://portswigger.net/web-security) - (重复) Burp Suite 官方的免费在线 Web 安全实验室。
    *   [XSS-Game](https://xss-game.appspot.com/) - Google 出品的 XSS 挑战游戏。
*   **Pwn / 二进制**
    *   [Pwnable.kr](http://pwnable.kr/) - 提供各种 pwn 挑战。
    *   [Pwnable.tw](https://pwnable.tw/) - 台湾的 pwn 挑战平台。
    *   [ROP Emporium](https://ropemporium.com/) - 学习 ROP（返回导向编程）技术的挑战。
    *   [How2Heap](https://github.com/shellphish/how2heap) - 用于学习堆漏洞利用的教程和示例。
    *   [Microcorruption](https://microcorruption.com/) - 嵌入式安全 CTF，逆向一个锁。
*   **逆向 & 恶意软件**
    *   [Crackmes.one](https://crackmes.one/) - 共享 Crackme（破解程序）的平台。
    *   [Reversing.kr](http://reversing.kr/) - 逆向工程挑战。
    *   [Flare-On Challenge](https://www.mandiant.com/flare-on) - FireEye/Mandiant 举办的年度逆向工程挑战赛。
*   **云安全**
    *   [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) - (重复) AWS 漏洞练习靶场。
    *   [Kubernetes-Goat](https://github.com/madhuakula/kubernetes-goat) - (重复) Kubernetes 漏洞练习靶场。
    *   [Sadcloud](https://github.com/nccgroup/sadcloud) - NCC Group 的易受攻击的云部署工具。
*   **其他**
    *   [Damn Vulnerable DeFi](https://www.damnvulnerabledefi.xyz/) - (重复) DeFi 智能合约攻防演练靶场。
    *   [Ethernaut](https://github.com/OpenZeppelin/ethernaut) - (重复) Web3/Solidity 黑客游戏。

#### 10.3 CTF 工具

*   **Pwn**
    *   [Pwntools](https://github.com/Gallopsled/pwntools) - (重复) CTF 框架和 Exploit 开发库，pwn 手必备。
    *   [GEF](https://github.com/hugsy/gef) - (重复) GDB 增强插件。
    *   [Pwndbg](https://github.com/pwndbg/pwndbg) - (重复) GDB 增强插件。
    *   [PEDA](https://github.com/longld/peda) - (重复) GDB 增强插件。
    *   [One-gadget](https://github.com/david942j/one_gadget) - (重复) 在 glibc 中查找 `execve` gadgets。
    *   [ROPgadget](https://github.com/JonathanSalwan/ROPgadget) - (重复) 查找 ROP/JOP gadgets。
    *   [Libc-database](https://github.com/niklasb/libc-database) - 收集不同版本的 libc，用于计算偏移。
*   **Web**
    *   [Burp Suite](https://portswigger.net/burp) - (重复) Web 渗透测试瑞士军刀。
    *   [sqlmap](https://github.com/sqlmapproject/sqlmap) - (重复) SQL 注入神器。
    *   [Commix](https://github.com/commixproject/commix) - (重复) 命令注入神器。
    *   [Wfuzz](https://github.com/xmendez/wfuzz) - (重复) Web Fuzzer。
    *   [XSSHunter](https://github.com/mandatoryprogrammer/xsshunter-express) - (重复) 盲 XSS 框架。
*   **逆向 (RE)**
    *   [Ghidra](https://github.com/NationalSecurityAgency/ghidra) - (重复) NSA 出品的逆向工程框架。
    *   [IDA Pro](https://hex-rays.com/ida-pro/) - (重复) 逆向工程标杆。
    *   [Radare2](https://github.com/radareorg/radare2) - (重复) 开源逆向工程框架。
    *   [x64dbg](https://github.com/x64dbg/x64dbg) - (重复) Windows 调试器。
    *   [Frida](https://github.com/frida/frida) - (重复) 动态代码插桩工具。
    *   [Angr](https://github.com/angr/angr) - 强大的二进制分析平台，擅长符号执行。
*   **密码学 (Crypto)**
    *   [CyberChef](https://github.com/gchq/CyberChef) - GCHQ 出品的“网络瑞士军刀”，用于各种编码、加密、压缩和数据分析。
    *   [FeatherDuster](https://github.com/nccgroup/featherduster) - 自动化的密码分析工具。
    *   [Rsactftool](https://github.com/Ganapati/RsaCtfTool) - 针对弱 RSA 密钥的攻击工具。
    *   [Hash-Identifier](https://github.com/blackploit/hash-identifier) - 哈希类型识别工具。
    *   [John the Ripper](https://github.com/openwall/john) - (重复) 密码破解工具。
    *   [Hashcat](https://github.com/hashcat/hashcat) - (重复) 高速密码破解工具。
*   **隐写 (Stego) & 取证 (Forensics)**
    *   [Stegsolve](http://www.caesum.com/handbook/stego.htm) - 经典的图片隐写分析工具。
    *   [Zsteg](https://github.com/zed-0xff/zsteg) - PNG 和 BMP 文件的隐写检测工具。
    *   [Foremost](http://foremost.sourceforge.net/) - 文件恢复工具。
    *   [Binwalk](https://github.com/ReFirmLabs/binwalk) - 固件分析和提取工具，也常用于文件分析。
    *   [ExifTool](https://github.com/exiftool/exiftool) - 读取、写入和编辑多种文件元信息的工具。
    *   [Volatility](https://github.com/volatilityfoundation/volatility) - (重复) 内存取证框架。
    *   [Autopsy](https://github.com/sleuthkit/autopsy) - (重复) 数字取证平台。
*   **综合 & 其他**
    *   [CTF-Katana](https://github.com/JohnHammond/ctf-katana) - 一站式 CTF 工具安装脚本。
    *   [GDB-Dashboard](https://github.com/cyrus-and/gdb-dashboard) - GDB 的模块化可视化界面。
    *   [Z3](https://github.com/Z3Prover/z3) - 微软研究院的 SMT 求解器，常用于 pwn 和逆向。
    *   [Claripy](https://github.com/angr/claripy) - Angr 使用的约束求解器。
    *   [Pwntools-template](https://github.com/Gallopsled/pwntools-template) - Pwntools 的模板。

#### 10.4 Writeup & 学习资源

*   [CTFtime.org/writeups](https://ctftime.org/writeups) - CTFtime 上的 Writeup 聚合。
*   [Hack The Box Writeups](https://github.com/topics/hackthebox-writeup) - GitHub 上关于 Hack The Box 的 Writeup。
*   [VulnHub Writeups](https://github.com/topics/vulnhub-writeup) - GitHub 上关于 VulnHub 的 Writeup。
*   [LiveOverflow](https://www.youtube.com/c/LiveOverflow) - 著名的安全教育 YouTube 频道，包含大量 CTF 和底层知识。
*   [John Hammond](https://www.youtube.com/c/JohnHammond0) - 另一个优秀的 CTF 和网络安全 YouTube 频道。
*   [Gynvael's Hacking Livestream](https://www.youtube.com/c/GynvaelEN) - Dragon Sector 队长的直播录像。
*   [Pwn.college](https://pwn.college/) - 亚利桑那州立大学的程序安全课程。
*   [Modern Binary Exploitation](https://github.com/RPISEC/MBE) - RPISEC 的现代二进制漏洞利用课程。
*   [Nightmare](https://guyinatuxedo.github.io/) - 二进制漏洞利用入门课程。
*   [CryptoHack](https://cryptohack.org/) - 通过一系列有趣的挑战来学习现代密码学。
*   [Trail of Bits Blog](https://blog.trailofbits.com/) - Trail of Bits 的博客，包含大量高质量的技术文章。
*   [Project Zero Blog](https://googleprojectzero.blogspot.com/) - (重复) Google Project Zero 的博客。
*   [CTF-Archives](https://github.com/ctfs) - 历年 CTF 赛题归档。
*   [DEF CON CTF Archives](https://www.defcon.org/html/links/dc-ctf.html) - DEF CON CTF 官方归档。
*   [PlaidCTF Archives](https://github.com/plaidctf) - PlaidCTF 赛题归档。

---

## 人工智能与数据科学

#### 11.1 综合性 Awesome 列表 & 资源库

*   [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning) - 最全面的机器学习框架、库和软件列表。
*   [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning) - 深度学习教程、项目和社区的集合。
*   [Awesome Data Science](https://github.com/academic/awesome-datascience) - 数据科学领域的资源，包括课程、博客、数据集等。
*   [Awesome LLM](https://github.com/Hannibal046/Awesome-LLM) - 大语言模型（LLM）的权威资源列表。
*   [Awesome-AI-Agents](https://github.com/e2b-dev/awesome-ai-agents) - AI 智能体资源列表。
*   [Awesome Generative AI](https://github.com/steven-tey/awesome-generative-ai) - 生成式 AI 应用和工具的精选列表。
*   [Awesome MLOps](https://github.com/visenger/awesome-mlops) - MLOps 平台、工具和资源的集合。
*   [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering) - 数据工程工具和资源。
*   [Awesome AI Security](https://github.com/Deep-Learning-Security/Awesome-AI-Security) - AI 安全资源，涵盖攻击与防御。
*   [Awesome Production Machine Learning](https://github.com/EthicalML/awesome-production-machine-learning) - 生产环境机器学习资源。
*   [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets) - (重复) 高质量的公共数据集，AI/DS 的燃料。
*   [AI-Expert-Roadmap](https://github.com/AMAI-GmbH/AI-Expert-Roadmap) - 成为 AI 专家的学习路线图。
*   [Data-Science-Cheatsheet](https://github.com/abhat222/Data-Science--Cheat-Sheet) - 数据科学备忘单。
*   [Deep-Learning-Drizzle](https://github.com/kmario23/deep-learning-drizzle) - 深度学习资源集合。
*   [Hugging Face](https://huggingface.co/) - AI 社区，提供海量的模型、数据集和工具。

#### 11.2 机器学习 & 深度学习框架

*   [TensorFlow](https://github.com/tensorflow/tensorflow) - Google 开发的端到端开源机器学习平台。
*   [PyTorch](https://github.com/pytorch/pytorch) - Facebook 开发的开源机器学习框架，以其灵活性和动态图著称。
*   [Keras](https://github.com/keras-team/keras) - 高度模块化、用户友好的神经网络库，可运行在 TensorFlow, PyTorch 等之上。
*   [Scikit-learn](https://github.com/scikit-learn/scikit-learn) - (重复) Python 中最流行的传统机器学习库。
*   [JAX](https://github.com/google/jax) - Google 开发的、用于高性能机器学习研究的 NumPy 增强版。
*   [MXNet](https://github.com/apache/mxnet) - Apache 的深度学习框架。
*   [Caffe](https://github.com/BVLC/caffe) - 伯克利人工智能研究室开发的深度学习框架。
*   [Theano](https://github.com/Theano/Theano) - (已停止开发，但有历史意义) Python 深度学习库。
*   [ONNX (Open Neural Network Exchange)](https://github.com/onnx/onnx) - 用于表示深度学习模型的开放格式。
*   [Deeplearning4j](https://github.com/eclipse/deeplearning4j) - JVM 平台的开源、分布式深度学习库。
*   [Fastai](https://github.com/fastai/fastai) - 基于 PyTorch 的高级深度学习库，简化了训练过程。
*   [Chainer](https://github.com/chainer/chainer) - (已转向 PyTorch) 灵活的神经网络框架。
*   [PaddlePaddle](https://github.com/PaddlePaddle/Paddle) - 百度开发的开源深度学习平台。
*   [TFLearn](https://github.com/tflearn/tflearn) - 基于 TensorFlow 的模块化深度学习库。
*   [Sonnet](https://github.com/deepmind/sonnet) - DeepMind 基于 TensorFlow 构建的神经网络库。

#### 11.3 大语言模型 (LLM) & AIGC
*   [n8n](https://github.com/n8n-io/n8n) - 支持 AI 节点的开源工作流自动化平台。
*   [Langflow](https://github.com/langflow-ai/langflow) - 用于设计和部署 LLM 应用的可视化构建器。
*   [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) - 目前最强的开源大语言模型之一。
*   [Dify](https://github.com/langgenius/dify) - 生产级 LLM 应用开发平台。
*   [Ollama](https://github.com/ollama/ollama) - 在本地轻松运行大语言模型的工具。
*   [RAGFlow](https://github.com/infiniflow/ragflow) - 基于深度文档理解的下一代 RAG 引擎。
*   [vLLM](https://github.com/vllm-project/vllm) - 高吞吐量、内存高效的 LLM 推理和服务库。
*   [OpenHands](https://github.com/All-Hands-AI/OpenHands) - 开源的 AI 软件工程师智能体。

*   [LangChain](https://github.com/langchain-ai/langchain) - 用于开发由语言模型驱动的应用的框架。
*   [LlamaIndex](https://github.com/run-llama/llama_index) - 连接 LLM 和外部数据的接口。
*   [Transformers](https://github.com/huggingface/transformers) - Hugging Face 出品，提供数千个预训练模型，用于 NLP, NLU 和 NLG。
*   [Stable Diffusion](https://github.com/CompVis/stable-diffusion) - 开源的文本到图像生成模型。
*   [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) - Stable Diffusion 的浏览器界面。
*   [Whisper](https://github.com/openai/whisper) - OpenAI 开源的通用语音识别模型。
*   [LLaMA](https://github.com/facebookresearch/llama) - Meta AI 的基础大语言模型。
*   [Alpaca](https://github.com/tatsu-lab/stanford_alpaca) - 在 LLaMA 基础上进行指令微调的模型。
*   [Vicuna](https://github.com/lm-sys/FastChat) - 基于 LLaMA 的、性能接近 ChatGPT 的开源聊天模型。
*   [Oobabooga's Text Generation WebUI](https://github.com/oobabooga/text-generation-webui) - 用于运行大语言模型的 Gradio Web UI。
*   [PrivateGPT](https://github.com/imartinez/privateGPT) - 在本地、无网络连接的情况下与文档进行交互。
*   [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) - 旨在实现完全自主运行 GPT-4 的实验性开源尝试。
*   [AgentGPT](https://github.com/reworkd/AgentGPT) - 在浏览器中组装、配置和部署自主 AI 智能体。
*   [Awesome-Prompt-Engineering](https://github.com/prompt-engineering/awesome-prompt-engineering) - (重复) 提示工程资源。
*   [LLM-From-Scratch](https://github.com/rasbt/LLMs-from-scratch) - 从零开始构建 LLM 的教程。
*   [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA) - 微软提出的、用于高效微调大模型的技术。
*   [vLLM](https://github.com/vllm-project/vllm) - 用于 LLM 推理和服务的高吞吐量库。
*   [Sentence-Transformers](https://github.com/UKPLab/sentence-transformers) - 用于生成句子/文本嵌入的库。
*   [PEFT (Parameter-Efficient Fine-Tuning)](https://github.com/huggingface/peft) - Hugging Face 的参数高效微调库。
*   [bitsandbytes](https.github.com/TimDettmers/bitsandbytes) - 8 位量化库，用于在消费级硬件上运行大模型。
*   [GPT-Engineer](https://github.com/gpt-engineer-org/gpt-engineer) - 根据提示生成整个代码库。
*   [InvokeAI](https://github.com/invoke-ai/InvokeAI) - 领先的 Stable Diffusion GUI 和 API。
*   [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 强大和模块化的 Stable Diffusion GUI，基于节点图。
*   [Fooocus](https://github.com/lllyasviel/Fooocus) - 极简但功能强大的 Stable Diffusion 软件。

#### 11.4 计算机视觉 (CV)

*   [OpenCV](https://github.com/opencv/opencv) - (重复) 开源计算机视觉库的王者。
*   [YOLO (You Only Look Once)](https://github.com/ultralytics/yolov5) - 实时目标检测算法（v5 版本）。
*   [Detectron2](https://github.com/facebookresearch/detectron2) - Facebook AI Research 的下一代目标检测和分割平台。
*   [MMDetection](https://github.com/open-mmlab/mmdetection) - OpenMMLab 的目标检测工具箱和基准。
*   [Awesome Computer Vision](https://github.com/jbhuang0604/awesome-computer-vision) - (重复) 计算机视觉资源列表。
*   [Pillow](https://github.com/python-pillow/Pillow) - 友好的 Python 图像处理库（PIL 的分支）。
*   [Tesseract](https://github.com/tesseract-ocr/tesseract) - Google 支持的开源 OCR 引擎。
*   [Albumentations](https://github.com/albumentations-team/albumentations) - 快速的图像增强库。
*   [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) - 实时多人关键点检测库。
*   [DeepFaceLab](https://github.com/iperov/DeepFaceLab) - 领先的 Deepfake 软件。
*   [Face-recognition](https://github.com/ageitgey/face_recognition) - 世界上最简单的 Python 人脸识别库。
*   [MediaPipe](https://github.com/google/mediapipe) - Google 的跨平台、可定制的机器学习解决方案，用于实时流媒体。

#### 11.5 自然语言处理 (NLP)

*   [NLTK (Natural Language Toolkit)](https://github.com/nltk/nltk) - 领先的 Python 平台，用于处理人类语言数据。
*   [SpaCy](https://github.com/explosion/spaCy) - 用于生产环境的工业级 NLP 库。
*   [Gensim](https://github.com/RaRe-Technologies/gensim) - 用于主题建模、文档索引和相似性检索的 Python 库。
*   [Awesome NLP](https://github.com/keon/awesome-nlp) - (重复) NLP 资源列表。
*   [Stanza](https://github.com/stanfordnlp/stanza) - 斯坦福大学的 Python NLP 库。
*   [Flair](https://github.com/flairNLP/flair) - 非常简单的 NLP 框架。
*   [TextBlob](https://github.com/sloria/TextBlob) - 简化的文本处理 Python 库。
*   [CoreNLP](https://stanfordnlp.github.io/CoreNLP/) - 斯坦福大学的 Java NLP 工具套件。

#### 11.6 数据处理 & 可视化

*   [Pandas](https://github.com/pandas-dev/pandas) - (重复) 强大的 Python 数据分析和操作库。
*   [NumPy](https://github.com/numpy/numpy) - (重复) Python 科学计算的基础包。
*   [Matplotlib](https://github.com/matplotlib/matplotlib) - (重复) Python 绘图库。
*   [Seaborn](https://github.com/mwaskom/seaborn) - 基于 Matplotlib 的统计数据可视化库。
*   [Plotly](https://github.com/plotly/plotly.py) - 交互式图表库。
*   [Bokeh](https://github.com/bokeh/bokeh) - 用于现代 Web 浏览器的交互式可视化库。
*   [Dask](https://github.com/dask/dask) - 用于并行计算的灵活库，可扩展 Pandas, Scikit-learn 等。
*   [Vaex](https://github.com/vaexio/vaex) - 用于核外（out-of-core）DataFrame 的高性能 Python 库。
*   [Jupyter Notebook](https://github.com/jupyter/notebook) - 基于 Web 的交互式计算环境。
*   [JupyterLab](https://github.com/jupyterlab/jupyterlab) - 下一代 Jupyter Notebook。
*   [Streamlit](https://github.com/streamlit/streamlit) - (重复) 为机器学习和数据科学项目构建 Web 应用的最快方法。
*   [Gradio](https://github.com/gradio-app/gradio) - 为机器学习模型创建可定制的 UI 组件。
*   [Apache Spark](https://github.com/apache/spark) - 统一的、用于大规模数据处理的分析引擎。
*   [Apache Arrow](https://github.com/apache/arrow) - 跨语言的、用于内存中数据的开发平台。
*   [Polars](https://github.com/pola-rs/polars) - Rust 编写的、极速的 DataFrame 库。

#### 11.7 MLOps & 数据工程

*   [MLflow](https://github.com/mlflow/mlflow) - 开源平台，用于管理端到端的机器学习生命周期。
*   [Kubeflow](https://github.com/kubeflow/kubeflow) - 在 Kubernetes 上进行机器学习的工具包。
*   [DVC (Data Version Control)](https://github.com/iterative/dvc) - 开源的版本控制系统，用于机器学习项目。
*   [Airflow](https://github.com/apache/airflow) - 以编程方式创作、调度和监控工作流的平台。
*   [Prefect](https://github.com/PrefectHQ/prefect) - 现代化的数据工作流自动化平台。
*   [BentoML](https://github.com/bentoml/BentoML) - 用于机器学习模型服务和部署的框架。
*   [Feast](https://github.com/feast-dev/feast) - 开源的特征存储。
*   [Ray](https://github.com/ray-project/ray) - 用于扩展 AI 和 Python 应用的统一计算框架。
*   [Optuna](https://github.com/optuna/optuna) - 自动化的超参数优化框架。
*   [Weights & Biases (Wandb)](https://wandb.ai/site) - 用于跟踪实验、可视化数据和协作的 MLOps 平台。
*   [ClearML](https://github.com/allegroai/clearml) - 自动化的 MLOps 平台。
*   [DBT (Data Build Tool)](https://github.com/dbt-labs/dbt-core) - 数据转换工具，使数据分析师能够像软件工程师一样工作。
*   [Great Expectations](https://github.com/great-expectations/great_expectations) - 用于数据测试、文档化和分析的工具。
*   [Trino (formerly PrestoSQL)](https://github.com/trinodb/trino) - 分布式 SQL 查询引擎，用于大数据分析。
*   [Delta Lake](https://github.com/delta-io/delta) - 为数据湖带来 ACID 事务的存储层。

#### 11.8 AI 安全 & 可解释性

*   [Adversarial Robustness Toolbox (ART)](https://github.com/Trusted-AI/adversarial-robustness-toolbox) - 用于机器学习安全的 Python 库。
*   [CleverHans](https://github.com/cleverhans-lab/cleverhans) - 用于对机器学习系统进行基准测试的对抗样本库。
*   [SHAP (SHapley Additive exPlanations)](https://github.com/slundberg/shap) - 一种博弈论方法，用于解释任何机器学习模型的输出。
*   [LIME (Local Interpretable Model-agnostic Explanations)](https://github.com/marcotcr/lime) - 解释任何分类器或回归器预测的 Python 包。
*   [Captum](https://github.com/pytorch/captum) - PyTorch 的模型可解释性库。
*   [Counterfit](https://github.com/Azure/counterfit) - 自动化 AI 系统安全风险评估的命令行工具。
*   [TextAttack](https://github.com/QData/TextAttack) - 用于 NLP 对抗性攻击、数据增强和模型训练的 Python 框架。
*   [DeepFool](https://github.com/LTS4/deepfool) - 计算深度网络鲁棒性的简单而准确的方法。
*   [AI-Exploits](https://github.com/protectai/ai-exploits) - 针对 AI 系统的漏洞利用集合。
*   [Garak](https://github.com/leondz/garak) - LLM 漏洞扫描器。

---

## 开发工具与职业成长

#### 12.1 综合性 Awesome 列表 & 资源库

*   [Awesome Dev Env](https://github.com/jondot/awesome-dev-env) - 开发环境的综合资源列表。
*   [Awesome Developer Tools](https://github.com/goabstract/awesome-developer-tools) - 各种开发者工具的集合。
*   [Awesome Productivity](https://github.com/jyguyomarch/awesome-productivity) - 提升生产力的工具和资源。
*   [Developer Roadmap](https://github.com/kamranahmedse/developer-roadmap) - (重复) 成为各类开发者的学习路径图。
*   [Free for Dev](https://github.com/ripienaar/free-for-dev) - (重复) 为开发者提供的免费 SaaS、PaaS、IaaS 等服务。
*   [Awesome-README](https://github.com/matiassingers/awesome-readme) - (重复) 优秀的 README 范例。
*   [Awesome Technical Writing](https://github.com/BolajiAyodeji/awesome-technical-writing) - 技术写作资源。
*   [Awesome Cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets) - (重复) 各种技术和工具的速查表。
*   [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) - 命令行使用艺术。
*   [Awesome-Interview-Questions](https://github.com/DopplerHQ/awesome-interview-questions) - (重复) 精选的面试问题列表。
*   [Tech Interview Handbook](https://github.com/yangshun/tech-interview-handbook) - (重复) 为忙碌工程师准备的免费技术面试资源。
*   [Coding Interview University](https://github.com/jwasham/coding-interview-university) - (重复) 成为软件工程师的完整自学计划。
*   [Professional Programming](https://github.com/charlax/professional-programming) - (重复) 成为更专业程序员的资源集合。
*   [Awesome-for-Beginners](https://github.com/MunGell/awesome-for-beginners) - 对新手友好的开源项目。
*   [Awesome-Talks](https://github.com/JanVanRyswyck/awesome-talks) - (重复) 精彩的技术演讲。
*   [Awesome-Podcasts](https://github.com/rShetty/awesome-podcasts) - (重复) 开发者喜欢的播客。
*   [Awesome-Newsletters](https://github.com/zudochkin/awesome-newsletters) - (重复) 值得订阅的技术简报。
*   [Developer-Health](https://github.com/zen-pro/awesome-developer-health) - 开发者健康资源。

#### 12.2 代码编辑器 & IDE
*   [Claude Code](https://github.com/anthropics/claude-code) - Anthropic 官方出品的 AI 编程命令行工具。
*   [Zed](https://github.com/zed-industries/zed) - 由 Atom 创始人打造的高性能代码编辑器。

*   [Visual Studio Code (VS Code)](https://github.com/microsoft/vscode) - 微软出品的、最流行的开源代码编辑器。
*   [Awesome-VSCode](https://github.com/viatsko/awesome-vscode) - (重复) VSCode 插件和资源。
*   [Neovim](https://github.com/neovim/neovim) - Vim 的一个分支，专注于可扩展性和可用性。
*   [Awesome-Neovim](https://github.com/rockerBOO/awesome-neovim) - (重复) Neovim 插件和资源。
*   [Vim](https://github.com/vim/vim) - 高度可配置的文本编辑器。
*   [The Ultimate Vim Configuration](https://github.com/amix/vimrc) - 终极 Vim 配置。
*   [SpaceVim](https://github.com/SpaceVim/SpaceVim) - 社区驱动的、模块化的 Vim/Neovim 配置。
*   [Emacs](https://www.gnu.org/software/emacs/) - 可扩展的、可定制的、自文档化的实时显示编辑器。
*   [Doom Emacs](https://github.com/doomemacs/doomemacs) - 为“Vim 精英”设计的 Emacs 配置框架。
*   [Spacemacs](https://github.com/syl20bnr/spacemacs) - 社区驱动的 Emacs 发行版。
*   [JetBrains IDEs](https://www.jetbrains.com/products/) - (商业) IntelliJ IDEA, PyCharm, GoLand, WebStorm 等。
*   [Sublime Text](https://www.sublimetext.com/) - (商业) 成熟的、精致的文本编辑器。
*   [Atom](https://github.com/atom/atom) - (已归档) GitHub 出品的可定制文本编辑器。
*   [Zed](https://github.com/zed-industries/zed) - (macOS) Atom 和 Tree-sitter 创始人打造的高性能、多人协作代码编辑器。
*   [Lapce](https://github.com/lapce/lapce) - Rust 编写的、快如闪电的、强大的代码编辑器。
*   [Helix](https://github.com/helix-editor/helix) - Rust 编写的、受 Kakoune/Neovim 启发的、后现代文本编辑器。
*   [OniVim 2](https://github.com/onivim/oni2) - (已归档) 结合 Vim 和 VS Code 优点的编辑器。

#### 12.3 终端 & Shell

*   [Alacritty](https://github.com/alacritty/alacritty) - (重复) 跨平台的、GPU 加速的终端模拟器。
*   [WezTerm](https://github.com/wez/wezterm) - Rust 编写的、GPU 加速的、跨平台的终端模拟器和多路复用器。
*   [Kitty](https://github.com/kovidgoyal/kitty) - 快速的、功能丰富的、GPU 加速的终端模拟器。
*   [Hyper](https://github.com/vercel/hyper) - 基于 Web 技术的终端。
*   [iTerm2](https://iterm2.com/) - (macOS) macOS 的终端替代品。
*   [Windows Terminal](https://github.com/microsoft/terminal) - 微软为 Windows 打造的现代终端应用。
*   [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh) - 社区驱动的、用于管理 Zsh 配置的框架。
*   [Awesome-Zsh-Plugins](https://github.com/unixorn/awesome-zsh-plugins) - (重复) Zsh 插件和主题。
*   [Starship](https://github.com/starship/starship) - 极简的、极速的、可无限定制的跨 Shell 提示符。
*   [Fish Shell](https://github.com/fish-shell/fish-shell) - 智能且用户友好的命令行 Shell。
*   [Oh My Fish](https://github.com/oh-my-fish/oh-my-fish) - Fish Shell 的框架。
*   [Fig](https://fig.io/) - (已被 AWS 收购) 为终端添加 IDE 风格的自动补全。
*   [Warp](https://www.warp.dev/) - (macOS) Rust 编写的、现代化的终端。
*   [Tmux](https://github.com/tmux/tmux) - 终端多路复用器。
*   [Zellij](https://github.com/zellij-org/zellij) - Rust 编写的、面向开发者的终端工作区。
*   [Fzf](https://github.com/junegunn/fzf) - 通用的命令行模糊查找器。
*   [Bat](https://github.com/sharkdp/bat) - (重复) 带有语法高亮和 Git 集成的 `cat` 克隆。
*   [Ripgrep](https://github.com/BurntSushi/ripgrep) - (重复) 极速的行导向搜索工具。
*   [Exa](https://github.com/ogham/exa) - (重复) `ls` 的现代替代品。
*   [Fd](https://github.com/sharkdp/fd) - `find` 的简单、快速、用户友好的替代品。
*   [Sd](https://github.com/chmln/sd) - 直观的查找和替换命令行工具。
*   [Zoxide](https://github.com/ajeetdsouza/zoxide) - 更智能的 `cd` 命令。
*   [Tldr](https://github.com/tldr-pages/tldr) - 社区维护的、简化的 man pages。
*   [Cheat.sh](https://github.com/chubin/cheat.sh) - 统一的、社区驱动的备忘单。
*   [Awesome-Shell](https://github.com/alebcay/awesome-shell) - (重复) Shell 工具和资源。
*   [Awesome-CLI-Apps](https://github.com/agarrharr/awesome-cli-apps) - (重复) 优秀的命令行应用。

#### 12.4 Git & 版本控制

*   [Git](https://github.com/git/git) - 分布式版本控制系统。
*   [Pro Git](https://github.com/progit/progit2) - 《Pro Git》第二版电子书。
*   [Git-flight-rules](https://github.com/k88hudson/git-flight-rules) - (重复) Git 飞行规则，处理各种紧急情况的指南。
*   [Gitignore](https://github.com/github/gitignore) - (重复) 有用的 `.gitignore` 模板集合。
*   [Lazygit](https://github.com/jesseduffield/lazygit) - 简单的 Git 终端 UI。
*   [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) - 规范化的 Git 提交信息标准。
*   [Commitizen](https://github.com/commitizen/cz-cli) - 帮助生成符合 Conventional Commits 标准的提交信息。
*   [Husky](https://github.com/typicode/husky) - 现代化的原生 Git 钩子。
*   [GitKraken](https://www.gitkraken.com/) - (商业) 跨平台的 Git GUI 客户端。
*   [SourceTree](https://www.sourcetreeapp.com/) - (免费) 适用于 Windows 和 Mac 的 Git GUI。
*   [GitHub Desktop](https://github.com/desktop/desktop) - GitHub 官方的桌面客户端。
*   [Gitea](https://github.com/go-gitea/gitea) - Go 编写的、自托管的 Git 服务。
*   [Gogs](https://github.com/gogs/gogs) - 另一个 Go 编写的、自托管的 Git 服务。
*   [GitLab](https://gitlab.com/gitlab-org/gitlab) - 开源的、完整的 DevOps 平台。
*   [BFG Repo-Cleaner](https://github.com/rtyley/bfg-repo-cleaner) - 用于从 Git 仓库中删除大文件或敏感数据的工具。
*   [Git-LFS (Large File Storage)](https://github.com/git-lfs/git-lfs) - Git 的大文件存储扩展。
*   [Delta](https://github.com/dandavison/delta) - Git 和 diff 输出的查看器。

#### 12.5 文档 & 知识管理

*   [Docusaurus](https://github.com/facebook/docusaurus) - Facebook 出品的、易于维护的开源文档网站。
*   [MkDocs](https://github.com/mkdocs/mkdocs) - 快速、简单、美观的静态网站生成器，专为项目文档设计。
*   [Material for MkDocs](https://github.com/squidfunk/mkdocs-material) - MkDocs 的一个非常流行的主题。
*   [VitePress](https://github.com/vuejs/vitepress) - Vue.js 团队出品的、基于 Vite 的静态网站生成器。
*   [Docsify](https://github.com/docsifyjs/docsify) - 神奇的文档网站生成器，无需构建过程。
*   [Read the Docs](https://github.com/readthedocs/readthedocs.org) - 自动化构建、版本化和托管文档的平台。
*   [Obsidian](https://obsidian.md/) - (免费增值) 基于本地 Markdown 文件的强大的知识库。
*   [Logseq](https://github.com/logseq/logseq) - 注重隐私的、开源的知识管理和协作平台。
*   [Joplin](https://github.com/laurent22/joplin) - 开源的笔记和待办事项应用，支持端到端加密。
*   [Notion](https://www.notion.so/) - (商业) 将笔记、任务、Wiki 和数据库集成在一起的一体化工作空间。
*   [Typora](https://typora.io/) - (商业) 极简的、所见即所得的 Markdown 编辑器。
*   [Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) - Markdown 语法备忘单。
*   [Awesome-Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - (重复) 可自行托管的服务列表，包含大量文档和 Wiki 系统。
*   [Diataxis Framework](https://diataxis.fr/) - 技术文档写作的系统性框架。
*   [Write the Docs](https://www.writethedocs.org/) - 关注文档、文档编写者和用户的全球社区。

#### 12.6 职业成长 & 软技能

*   [The Pragmatic Programmer](https://github.com/pragmaticprogrammer/pragmatic_programmer_20th_anniversary_edition) - (重复) 《程序员的修炼》相关资源。
*   [Clean Code](https://github.com/JuanCrg90/Clean-Code-Notes) - (重复) 《代码整洁之道》笔记与实践。
*   [Design Patterns](https://github.com/iluwatar/java-design-patterns) - (重复) Java 设计模式实现。
*   [Refactoring Guru](https://refactoring.guru/) - 设计模式、重构、SOLID 原则等的可视化学习网站。
*   [97-Things-Every-Programmer-Should-Know](https://github.com/97-things/97-things-every-programmer-should-know) - (重复) 每个程序员都应该知道的 97 件事。
*   [Software Engineering at Google](https://github.com/google/eng-practices) - (重复) Google 的工程实践文档。
*   [System Design Primer](https://github.com/donnemartin/system-design-primer) - (重复) 学习如何设计可扩展的系统。
*   [Staff Engineer](https://staffeng.com/) - Staff+ 级别工程师的故事和经验。
*   [The Manager's Path](https://www.amazon.com/Managers-Path-Leaders-Navigating-Growth/dp/1491973897) - 《技术领导之路》书籍。
*   [Pragmatic Engineer](https://blog.pragmaticengineer.com/) - Gergely Orosz 的博客，深入探讨软件工程和技术职业。
*   [Levels.fyi](https://www.levels.fyi/) - 科技公司的职级、薪酬和职业路径对比。
*   [Blind](https://www.teamblind.com/) - 匿名的职业社区。
*   [LeetCode](https://leetcode.com/) - (重复) 算法和数据结构练习平台。
*   [HackerRank](https://www.hackerrank.com/) - 另一个编程技能练习和竞赛平台。
*   [Codewars](https://www.codewars.com/) - 通过挑战来提升编码技能。
*   [Project Euler](https://projecteuler.net/) - 一系列具有挑战性的数学/计算机编程问题。
*   [Awesome-Remote-Work](https://github.com/lukasz-madon/awesome-remote-job) - (重复) 远程工作资源。
*   [Public-Speaking](https://github.com/vmbrasseur/Public_Speaking) - 公开演讲资源。
*   [How to be a Programmer](https://github.com/braydie/HowToBeAProgrammer) - 如何成为一名程序员。
*   [You-are-not-a-visual-learner](https://www.youtube.com/watch?v=rhgwIhB58PA) - 关于学习方法论的讨论。
*   [Learning How to Learn](https://www.coursera.org/learn/learning-how-to-learn) - Coursera 上的热门课程。

#### 12.7 其他实用工具

*   [HTTPie](https://github.com/httpie/httpie) - (重复) 现代化的、用户友好的命令行 HTTP 客户端。
*   [Postman](https://www.postman.com/) - (重复) API 开发、测试和文档化的协作平台。
*   [Insomnia](https://github.com/Kong/insomnia) - (重复) 开源的、跨平台的 API 设计和测试工具。
*   [Docker](https://github.com/docker/cli) - (重复) 应用容器化平台。
*   [Kubernetes](https://github.com/kubernetes/kubernetes) - (重复) 容器编排系统。
*   [Ansible](https://github.com/ansible/ansible) - 简单的 IT 自动化引擎。
*   [Terraform](https://github.com/hashicorp/terraform) - (重复) 基础设施即代码（IaC）工具。
*   [NVM (Node Version Manager)](https://github.com/nvm-sh/nvm) - Node.js 版本管理器。
*   [Pyenv](https://github.com/pyenv/pyenv) - Python 版本管理器。
*   [asdf](https://github.com/asdf-vm/asdf) - 可扩展的版本管理器，支持多种语言。
*   [jq](https://github.com/jqlang/jq) - (重复) 命令行 JSON 处理工具。
*   [yq](https://github.com/mikefarah/yq) - 类似 jq 但用于 YAML, JSON, XML, properties 和 TOML 的工具。
*   [ngrok](https://ngrok.com/) - 将本地服务器暴露到公网的工具。
*   [LocalStack](https://github.com/localstack/localstack) - 在本地模拟 AWS 云服务的框架。
*   [DBngin](https://dbngin.com/) - 一体化的数据库版本管理工具。
*   [DB-Gate](https://github.com/dbeaver/dbeaver) - DBeaver，免费的通用数据库工具。
*   [Responsively App](https://github.com/responsively-app/responsively-app) - 用于 Web 开发的、修改版的浏览器，可同时预览多个屏幕尺寸。
*   [Carbon](https://github.com/carbon-app/carbon) - 创建和分享源代码的精美图片。
*   [ScreenToGif](https://github.com/NickeManarin/ScreenToGif) - 屏幕、摄像头和白板录制工具，可导出为 GIF、视频等。
*   [Kap](https://github.com/wulkano/kap) - (macOS) 开源的屏幕录制工具。
*   [LiceCap](https://www.cockos.com/licecap/) - 简单的动画屏幕捕捉工具。
*   [GIMP](https://www.gimp.org/) - 开源的图像编辑器。
*   [Inkscape](https://inkscape.org/) - 开源的矢量图形编辑器。
*   [Excalidraw](https://github.com/excalidraw/excalidraw) - 虚拟协作白板工具。

---

## 贡献指南

欢迎任何形式的贡献。随着仓库规模扩大，请确保您添加的资源具有代表性且放置在最合适的分类下。

1.  Fork 本仓库
2.  创建分支 `feature/add-awesome-resource`
3.  添加资源并保持格式统一
4.  提交 Commit
5.  Push 并创建 Pull Request

---

## 许可证

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，作者已放弃所有版权及相关权利。
