# Region classification (guide 6.1a step 3, annotated for gate F)

Era window 20170101..20181231. Reference = latest era capture per route.
Maintained by tools/annotate_regions.py; annotations keyed by region_sha survive regeneration.

| route | era captures | ref lines | static lines | dynamic regions | annotated | gate-blocking |
|---|---|---|---|---|---|---|
| root | 44 | 1576 | 1471 (93%) | 37 | 0 | 37 |
| game | 18 | 1576 | 1473 (93%) | 37 | 0 | 37 |
| garage | 18 | 2574 | 2474 (96%) | 32 | 0 | 32 |
| news | 19 | 5973 | 5550 (93%) | 30 | 0 | 30 |
| forum | 18 | 1720 | 1633 (95%) | 25 | 0 | 25 |
| lab | 18 | 1538 | 1416 (92%) | 26 | 0 | 26 |
| shop | 18 | 1451 | 1360 (94%) | 25 | 0 | 25 |
| embed | 9 | 119 | 21 (18%) | 5 | 0 | 5 |
| infirmary | 2 | 271 | 271 (100%) | 0 | 0 | 0 |
| statistics | 0 | — | — | too few era captures | — | — |

A gate-blocking region (empty annotation or needs-split) blocks gate F for its whole route (GATE_F_SPEC).
