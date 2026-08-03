# MTASC 1.14 — Motion-Twin ActionScript 2 compiler

- Source: https://web.archive.org/web/20131126084912id_/http://mtasc.org/zip/mtasc-1.14.zip
  (mtasc.org is dead; CDX shows this capture 2013-11-26, statuscode 200,
  digest YHVE6HV35AUWDFNVQBOTP3B7VTB3ADQM. The `-win`-suffixed zip named in
  old docs was never archived — this combined 1.14 zip carries mtasc.exe,
  std/ and std8/.)
- Fetched: 2026-08-03
- sha256(mtasc-1.14.zip): 99730a81bdc9ad38d2c9e4da0bff2e4cbe98543d93d438bb77327d1323742e4a
- Layout: zip's inner mtasc-1.14/ flattened to this directory
  (mtasc.exe, std/, std8/, CHANGES.txt, Readme.txt, Future.txt).
- Verified: `mtasc.exe` prints its 1.14 usage banner and compiles a
  minimal `-version 8 -header 688:400:25` SWF (CWS magic).
  `std8/flash/external/ExternalInterface.as` present (needed by the
  mazeCreator rebuild's Ruffle channel).
- Role: compiles the rebuilt mazeCreator (M2) — AS2, SWF version 8.
- NOT original site material. Tool provenance only; never enters srv/.
