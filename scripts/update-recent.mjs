#!/usr/bin/env node
// Regenerate the "Recently shipped" block in README.md from the most recently
// pushed public repos. Safe by construction: it never blanks the section on a
// transient API failure, never lists stale work, and fails loudly if the markers
// are missing. No dependencies (Node 18+ global fetch).

import { readFile, writeFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const USER = "RealRogerWinter";
const PROFILE_REPO = USER; // exclude the profile repo itself
const MAX_ITEMS = 5;
const FRESH_DAYS = 90;
const START = "<!-- RECENT:START -->";
const END = "<!-- RECENT:END -->";

const HERE = dirname(fileURLToPath(import.meta.url));
const README = join(HERE, "..", "README.md");

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const fmtDate = (iso) => {
  const d = new Date(iso);
  return `${MONTHS[d.getUTCMonth()]} ${d.getUTCDate()}, ${d.getUTCFullYear()}`;
};

function die(msg) {
  console.error(`update-recent: ${msg}`);
  process.exit(1);
}

async function fetchRepos() {
  const headers = { "User-Agent": "profile-readme-updater", Accept: "application/vnd.github+json" };
  if (process.env.GITHUB_TOKEN) headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
  const url = `https://api.github.com/users/${USER}/repos?sort=pushed&per_page=100&type=public`;
  const res = await fetch(url, { headers });
  if (!res.ok) die(`GitHub API returned ${res.status} ${res.statusText}`);
  const data = await res.json();
  if (!Array.isArray(data)) die("GitHub API did not return an array");
  // A zero-length response is treated as an error, not "nothing to show":
  // it almost always means a transient/auth problem, and we must not blank the section.
  if (data.length === 0) die("GitHub API returned zero repos (refusing to blank the section)");
  return data;
}

function buildBlock(repos) {
  const cutoff = Date.now() - FRESH_DAYS * 24 * 60 * 60 * 1000;
  const fresh = repos
    .filter((r) => !r.fork && !r.archived && r.name !== PROFILE_REPO)
    .filter((r) => new Date(r.pushed_at).getTime() >= cutoff)
    .slice(0, MAX_ITEMS);

  if (fresh.length === 0) {
    // Legitimate quiet stretch: a neutral line, never a stale date.
    return "Quietly heads-down lately. The projects above are where the work lives.";
  }
  return fresh
    .map((r) => {
      // Sanitize upstream repo descriptions: they may contain em/en dashes, which
      // are banned in this profile's copy. Collapse any dash-as-separator to a comma.
      const desc = (r.description || "").trim().replace(/\s*[—–]\s*/g, ", ");
      const tail = desc ? ` · ${desc}` : "";
      return `- **[${r.name}](${r.html_url})**${tail} _(pushed ${fmtDate(r.pushed_at)})_`;
    })
    .join("\n");
}

async function main() {
  let md = await readFile(README, "utf8");

  // Markers must each appear exactly once, in order.
  const startCount = md.split(START).length - 1;
  const endCount = md.split(END).length - 1;
  if (startCount !== 1 || endCount !== 1) die(`expected exactly one ${START} and one ${END} (found ${startCount}/${endCount})`);
  const startIdx = md.indexOf(START);
  const endIdx = md.indexOf(END);
  if (endIdx < startIdx) die("END marker precedes START marker");

  const repos = await fetchRepos();
  const block = buildBlock(repos);

  const before = md.slice(0, startIdx + START.length);
  const after = md.slice(endIdx);
  const next = `${before}\n${block}\n${after}`;

  if (next === md) {
    console.log("update-recent: no change");
    return;
  }
  await writeFile(README, next);
  console.log("update-recent: README updated");
}

main().catch((e) => die(e.message || String(e)));
