<?php
/*
 * Dev-only ad-slot filler. NOT part of the reconstruction.
 *
 * The era pages carry two AdSense skyscrapers
 * (<ins class="adsbygoogle" style="...width:160px;height:600px">). Offline
 * those slots keep their 160x600 box — the surrounding floats never depended
 * on the ad rendering — but they are blank, which reads as breakage while
 * eyeballing a route.
 *
 * This file lives OUTSIDE srv/, is mounted only by
 * docker/docker-compose.dev.yml, and paints the slots from CSS alone. It
 * cannot be reached by any request, has no ledger row, and changes no byte
 * of srv/. The default stack (`docker compose up -d`) never loads it, so
 * gate F byte-diffs an unmodified page.
 *
 * The fill is deliberately ugly and labelled: nobody should ever mistake it
 * for era artwork, and no screenshot taken with it on can be evidence.
 * Declared in docs/DIVERGENCES-SERVED.md.
 */

if (getenv('TT_DEV_FILLER') !== '1') {
    return;
}

function tt_dev_filler_css()
{
    return "<style id=\"tt-dev-filler\">\n"
        . "/* dev harness — docker/php/dev-filler.php, not part of srv/ */\n"
        . "ins.adsbygoogle{background:repeating-linear-gradient(45deg,"
        . "#ededed 0 10px,#e0e0e0 10px 20px);outline:1px dashed #b9b9b9;"
        . "outline-offset:-1px;position:relative;}\n"
        . "ins.adsbygoogle::after{content:'ad slot \\2014 dev filler, "
        . "not original';position:absolute;top:50%;left:50%;"
        . "transform:translate(-50%,-50%) rotate(-90deg);white-space:nowrap;"
        . "font:11px Arial,sans-serif;letter-spacing:1px;color:#8a8a8a;}\n"
        . "</style>\n";
}

function tt_dev_filler($buffer)
{
    if (stripos($buffer, 'adsbygoogle') === false) {
        return $buffer;
    }
    $pos = stripos($buffer, '</head>');
    if ($pos === false) {
        return $buffer;
    }
    return substr($buffer, 0, $pos) . tt_dev_filler_css()
        . substr($buffer, $pos);
}

ob_start('tt_dev_filler');
