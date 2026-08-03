# ruffle-spike — SetVariable / JS-bridge capability probe

Answers guide §7.3 / §9 step 2: can Ruffle run the garage's two Flash⇄JS
channels? Findings and consequences: `../DIVERGENCES.md`.

## Setup (fetched/copied at run time, none of it committed)

```powershell
npm install                       # puppeteer-core (package.json)
npm pack @ruffle-rs/ruffle        # then extract the tgz
tar -xzf ruffle-rs-ruffle-*.tgz
Rename-Item package ruffle
Copy-Item ..\..\srv\includes\signUpTankDesign13StandardColours.swf .
New-Item -ItemType Directory Assets
Copy-Item ..\..\srv\Assets\*.swf Assets\   # editor loads Assets/Tank.swf
```

## Run

```powershell
node run_spike.mjs        # needs any Chromium; TT_BROWSER overrides the path
```

Emits `results.json` (probe results, input values, `bridge_fired`) and
`spike.png`. The click sweep targets the paint-can rows measured from the
rendered stage (cans at stage y≈40-56; groups x≈87-207 and 377-512, matching
the decompile's `leftGroupLow=90 / leftGroupHigh=234 / rightGroupLow=382`).

Re-run against future Ruffle versions by refreshing the `ruffle/` dir.
