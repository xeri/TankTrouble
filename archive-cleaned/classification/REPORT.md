# Region classification draft (guide 6.1a step 3)

Era window 20170101..20181231. Reference = latest era capture per route.

| route | era captures | ref lines | static lines | dynamic regions |
|---|---|---|---|---|
| root | 44 | 1576 | 1471 (93%) | 37 |
| game | 18 | 1576 | 1473 (93%) | 37 |
| garage | 18 | 2574 | 2474 (96%) | 32 |
| news | 19 | 5973 | 5550 (93%) | 30 |
| forum | 18 | 1720 | 1633 (95%) | 25 |
| lab | 18 | 1538 | 1416 (92%) | 26 |
| shop | 18 | 1451 | 1360 (94%) | 25 |
| embed | 9 | 119 | 21 (18%) | 5 |
| infirmary | 2 | 271 | 271 (100%) | 0 |
| statistics | 0 | — | — | too few era captures |

Every dynamic region needs a milestone-3 annotation naming the
variable/loop that produced it before route PHP is written.
