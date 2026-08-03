# Validated 2026-08-03 (build + serve checked) — see ../../SECURITY.md
FROM php:5.6-apache
RUN docker-php-ext-install mysql mysqli pdo_mysql \
    && a2enmod rewrite
RUN { echo 'short_open_tag=On'; echo 'display_errors=On'; } \
    > /usr/local/etc/php/conf.d/tanktrouble.ini
