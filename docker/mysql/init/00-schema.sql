-- @provenance schema: shape M1 (columns observed in archived payloads/pages),
--             names+types M3 (never observable through HTTP -- guide 5.2)
-- @evidence   mazes: loadMaze.php wire format (DEDUCE.md 3.1);
--             forum: modern JSON-RPC field inventory over 467 threads /
--             228,316 replies; news: item shape of captured ?news bodies;
--             users/accessories/achievements: see their seed files
-- @written    2026-08-03 (hand-authored; regenerating seeds does not touch this)
-- @caveat     Engine MyISAM, charset utf8 (utf8mb3), collation
--             utf8_general_ci are period-plausible M3 choices recorded in
--             DECISIONS.md. Corpus scan: zero astral chars, so utf8mb3 is
--             lossless here. Do not present this DDL as recovered.

-- entrypoint client defaults to latin1 in 5.5; every init file sets this
SET NAMES utf8;

-- MYSQL_DATABASE may have pre-created the db with the server default
-- charset; harmless, since every table below carries an explicit charset
CREATE DATABASE IF NOT EXISTS tanktrouble
  CHARACTER SET utf8 COLLATE utf8_general_ci;
USE tanktrouble;

-- one row per (author, slot): loadMaze.php is queried by userName
-- (MazeDataFetcher.as), the response carries s=<slot>, and the corpus is a
-- time series of one live table -- latest capture wins (DECISIONS
-- 2026-08-03). Column SET is M1 (t/n/d/s all observed); author-as-key is
-- M2 (deduced from the userName query); names/types M3.
-- author is VARBINARY: the corpus holds 12 byte-distinct author pairs that
-- collide under any ci PAD-SPACE collation ('Cheesed'/'cheesed',
-- 'b11'/'b11 '); byte-exact keying preserves every observed state instead
-- of merging identities we cannot prove. All corpus authors are pure ASCII.
CREATE TABLE mazes (
  author  VARBINARY(16) NOT NULL,  -- n= field; editor limit 16
  slot    TINYINT UNSIGNED NOT NULL,  -- s= field; observed only 1
  title   VARCHAR(32)  NOT NULL,   -- t= field; editor limit 32, corpus max 32
  data    VARCHAR(512) NOT NULL,   -- d= grid string, corpus max 275
  PRIMARY KEY (author, slot)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- creator/coCreator/moderatedBy are modern numeric user-id STRINGS kept as
-- display metadata; deliberately no FK to users (guide 5.1)
CREATE TABLE forum_threads (
  id            INT UNSIGNED NOT NULL,
  header        VARCHAR(64)  NOT NULL,      -- observed max 50
  message       TEXT         NOT NULL,      -- observed max 5,755
  created       INT UNSIGNED NOT NULL,      -- unix seconds
  creator       VARCHAR(16)  NULL,
  coCreator1    VARCHAR(16)  NULL,
  coCreator2    VARCHAR(16)  NULL,
  latestEdit    INT UNSIGNED NULL,
  latestPost    INT UNSIGNED NOT NULL,
  deleted       TINYINT(1)   NOT NULL,
  moderatedBy   VARCHAR(16)  NULL,
  approved      TINYINT(1)   NOT NULL,
  banned        TINYINT(1)   NULL,          -- observed only as null; type M3
  locked        TINYINT(1)   NOT NULL,
  pinned        TINYINT(1)   NOT NULL,
  hasAnyReplies TINYINT(1)   NOT NULL,
  PRIMARY KEY (id),
  KEY latestPost (latestPost)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE forum_replies (
  id          INT UNSIGNED NOT NULL,
  threadId    INT UNSIGNED NOT NULL,
  message     TEXT         NOT NULL,
  created     INT UNSIGNED NOT NULL,
  creator     VARCHAR(16)  NULL,
  coCreator1  VARCHAR(16)  NULL,
  coCreator2  VARCHAR(16)  NULL,
  latestEdit  INT UNSIGNED NULL,
  deleted     TINYINT(1)   NOT NULL,
  moderatedBy VARCHAR(16)  NULL,
  approved    TINYINT(1)   NOT NULL,
  banned      TINYINT(1)   NULL,
  PRIMARY KEY (id),
  KEY threadId (threadId, created)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- body is the byte-verbatim capture slice (anchor through closing div);
-- whether the original stored these in a DB or a hand-edited file is NOT
-- observable (seed_news.py header) -- this table is the rebuild's container
-- for the blobs, nothing more
CREATE TABLE news (
  posted    DATE         NOT NULL,   -- the item's own permalink anchor
  seq       TINYINT UNSIGNED NOT NULL,  -- anchor dates collide; page order
  css_class VARCHAR(32)  NOT NULL,   -- markup generation, e.g. "news4 standard"
  title     VARCHAR(255) NOT NULL,   -- convenience copy; body is the data
  body      MEDIUMTEXT   NOT NULL,
  PRIMARY KEY (posted, seq)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- M3 throughout: synthetic accounts only (guide 5.1)
CREATE TABLE users (
  id              INT UNSIGNED NOT NULL AUTO_INCREMENT,
  username        VARCHAR(16)  NOT NULL,
  password_hash   VARCHAR(60)  NOT NULL,  -- bcrypt (guide 6.4 divergence: password_hash, never the original GET scheme)
  PRIMARY KEY (id),
  UNIQUE KEY username (username)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- developer debug catalogue, NOT the live shop inventory (seed_static.py)
CREATE TABLE accessories (
  slot         ENUM('turret','barrel','front','back') NOT NULL,
  accessory_id TINYINT UNSIGNED NOT NULL,
  toolbox      TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (slot, accessory_id)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- observed ids only; names/art/thresholds were never client-visible
CREATE TABLE achievements (
  id TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (id)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- Scrapyard counter state (M3 invention -- the ORIGINAL's storage is
-- unobservable; only two response bodies survive, 2015-09-28 and
-- 2016-01-26). Single row id=1. velocity keeps the archived decimal as a
-- STRING so replay emits the exact bytes (no float re-formatting drift).
CREATE TABLE scrapyard_state (
  id       TINYINT UNSIGNED NOT NULL,
  scraps   BIGINT UNSIGNED NOT NULL,
  velocity VARCHAR(32) NULL,
  PRIMARY KEY (id)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
