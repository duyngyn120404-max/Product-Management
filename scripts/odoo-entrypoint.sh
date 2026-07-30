#!/bin/sh
set -eu

base_config="${ODOO_BASE_CONFIG:-/etc/odoo/odoo.conf}"
runtime_config="/tmp/odoo-runtime.conf"

if [ -n "${ODOO_ADMIN_PASSWORD_FILE:-}" ]; then
    ODOO_ADMIN_PASSWORD="$(cat "$ODOO_ADMIN_PASSWORD_FILE")"
fi

: "${ODOO_ADMIN_PASSWORD:?Set ODOO_ADMIN_PASSWORD or ODOO_ADMIN_PASSWORD_FILE}"

umask 077
cp "$base_config" "$runtime_config"
printf '\nadmin_passwd = %s\n' "$ODOO_ADMIN_PASSWORD" >> "$runtime_config"

export ODOO_RC="$runtime_config"
exec /entrypoint.sh odoo server "$@"
