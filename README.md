# Donau-Ries Website Migration Workspace

This workspace contains the local presentation build and SEO migration files for `https://donau-ries-haustechnik.de/`.

Important:
- Existing agency text/images are archived only as internal placeholders/reference.
- Do not publish copied placeholder content or downloaded images without confirmed usage rights.
- The public version should use rewritten copy and licensed/client-owned imagery.

## Folders

- `static-site/` - local static presentation website.
- `data/` - URL inventory, redirect map, SEO audit exports, image inventory.
- `placeholder-archive/` - internal-only crawled source references.
- `scripts/` - helper scripts for crawl/build/check tasks.

## Quick Start

Run the crawler and generator:

```powershell
python .\website-migration\scripts\build_migration_workspace.py
```

Open the local presentation:

```powershell
.\website-migration\static-site\index.html
```

For a local server:

```powershell
python -m http.server 8080 -d .\website-migration\static-site
```

Then open `http://localhost:8080/`.

