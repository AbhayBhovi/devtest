FROM datadog/agent:6.6.0-jmx

ENV DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true \
    SD_JMX_ENABLE=true \
    NON_LOCAL_TRAFFIC=true

COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY checks.d /checks.d
COPY conf.d /conf.d
COPY db_drivers /db_drivers
COPY ddconfig /ddconfig
COPY parsers.d /parsers.d

RUN chmod +x /docker-entrypoint.sh \
 && rm -rf /etc/datadog-agent/datadog.yaml \
 && rm -rf /init

EXPOSE 9001 8125/udp 8126/tcp

ENTRYPOINT ["/docker-entrypoint.sh"]
