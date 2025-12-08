#!/bin/sh
set -e

hostport="$1"
shift

host=${hostport%:*}
port=${hostport#*:}

echo "Esperando $host:$port..."

until /bin/true >/dev/null 2>&1 && nc -z "$host" "$port" >/dev/null 2>&1; do
  echo "Aguardando o banco de dados iniciar..."
  sleep 1
done

echo "Banco disponível — executando comando: $@"
exec "$@"
