FROM redis:6.0.10 as app
COPY redis.conf /etc/
CMD ["sh", "-c", "exec redis-server /etc/redis.conf --requirepass \"$REDIS_PASSWORD\""]
