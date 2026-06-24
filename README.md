<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.png">
  <img alt="Roger Winter, Developer Advocate" src="assets/banner-dark.png" width="100%">
</picture>

# Hi, I'm Roger Winter

Developer advocate and self-taught engineer. I build AI and web software, then write and film the technical content that proves it works. Build it, then prove it: the build is the experiment, the writeup is the result.

The through-line across everything here is verifiable AI. Every project here has a way to make the model prove its work: a CI eval, a learning curve, SymPy re-checking the math, or a server-side gate that confirms only the requested change happened.

I've produced technical content for CircleCI, Microsoft, Meta, Red Hat, Docker, and Snyk, spoken at developer conferences, hosted a recurring AI webinar, and I ship my own AI-backed apps in public.

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![React](https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB) ![Node](https://img.shields.io/badge/Node-339933?logo=node.js&logoColor=white) ![Next.js](https://img.shields.io/badge/Next.js-000000?logo=next.js&logoColor=white) ![LLMs](https://img.shields.io/badge/LLMs-FF6F00) ![WebRTC](https://img.shields.io/badge/WebRTC-333333?logo=webrtc&logoColor=white) ![CircleCI](https://img.shields.io/badge/CircleCI-343434?logo=circleci&logoColor=white)

## What I build

- **AI systems that check their own output** · multi-model orchestration, agents, and evals that catch regressions and gate changes on the results.
- **Web apps, end to end** · TypeScript and Python across the stack, realtime over WebSockets and WebRTC, self-hosted behind Docker and CI.
- **The content that proves it** · tutorials, deep technical writeups, and tutorial video, scripted and presented on camera, with the code tested in CI before it publishes.

## What I'm building

**[sheet-llm](https://sheetllm.com)** · *in development*
An open-source music notation editor you talk to. An LLM orchestrator routes each request by complexity and cost, server-side gates confirm it changed only what you asked, and a four-tier eval suite runs in CI. Next.js, React, TypeScript.

**[OneStreamer](https://onestreamer.live)** · *live*
A browser competitive-streaming platform built around king-of-the-hill: one person holds the broadcast, AI chatbots and real viewers share the room, and anyone can take over. MediaSoup and WebRTC, TURN, mobile NAT traversal.

**[Price Games](https://price.games)** · *live*
A free browser price-guessing game. TypeScript and React on a Node monorepo, test-driven, built with AI coding agents running in parallel via git worktrees. It grew to about 100 daily players, self-hosted on a Linux box at home.

**[Pricey](https://twitch.tv/pricey)** · *live on Twitch*
A 24/7 AI streamer that plays Price Games on a custom neural net (no framework), generated and tested with Claude Code, with simulated moods that change how it plays.

**[multilingual-seo](https://github.com/RealRogerWinter/multilingual-seo)** · *in development*
Research, generate, and optimize content across languages from one workspace. It ranks which locales are worth translating before you spend a word on them.

## Recently shipped
<!-- RECENT:START -->
- **[onestreamer](https://github.com/RealRogerWinter/onestreamer)** · Self-hosted live-streaming platform with viewer takeover, in-stream economy, AI bots, and real-time effects. _(pushed Jun 24, 2026)_
- **[sheet-llm](https://github.com/RealRogerWinter/sheet-llm)** · Publisher-grade sheet music notation editor with native LLM support and chatbot-like conversation interface. _(pushed Jun 23, 2026)_
- **[algebra-1-tutor](https://github.com/RealRogerWinter/algebra-1-tutor)** · Interactive Algebra 1 tutor as a Claude Agent Skill for Claude.ai / the Claude app _(pushed Jun 23, 2026)_
- **[rwinter-dev-portfolio](https://github.com/RealRogerWinter/rwinter-dev-portfolio)** · Roger Winter, personal portfolio (rogerwinter.dev). Static site, Dockerized, deployed via CircleCI behind Cloudflare+Caddy. _(pushed Jun 22, 2026)_
- **[claude-plex-movie-recommender](https://github.com/RealRogerWinter/claude-plex-movie-recommender)** · A Claude Code skill for Plex servers: scans your Plex library and generates bespoke recommendations as a rich HTML page + an interactive proximity map (atlas), with optional Tautulli (per-user) and Overseerr/Jellyseerr (availability + requests). _(pushed Jun 15, 2026)_
<!-- RECENT:END -->

## Stack

TypeScript, Python, React, Node, Next.js, LLMs, and WebRTC, plus a custom neural net (no framework). I design and run AI evals to measure model output, catch regressions, and gate changes on the results. I self-host most things behind Docker, Caddy, and Cloudflare, with CI on every change.

## Find me

- Site and writeups: [rogerwinter.dev](https://rogerwinter.dev)
- LinkedIn: [roger-winter-content-strategy](https://linkedin.com/in/roger-winter-content-strategy)
