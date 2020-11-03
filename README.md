# Prometheus Exporters

[![ansible ci](https://github.com/link-u/ansible-roles_prometheus-exporters/workflows/ansible%20ci/badge.svg)](https://github.com/link-u/ansible-roles_prometheus-exporters/actions?query=workflow%3A%22ansible+ci%22)

## 概要
[prometheus-exporters-deck](https://github.com/link-u/dpkg_prometheus-exporter-deck) をインストールして設定する ansible role

## 動作確認バージョン

* Ubuntu: 18.04, 20.04
* ansible: 2.8, 2.9

## 使い方 (ansible)

### Role variables

```yaml
## 基本設定
prometheus_install_flag: True ## インストールフラグ
prometheus_packages:
  - "prometheus-exporter-deck"

prometheus_target_settings:
  demo-service:
    service:
      path: '/test/servers/demo-server'
      args:
        - '--example-flag'
        - 'example-value'
      endpoints:
        - 'http://localhost:9999/metricss'
  local-endpoint:
    exporter:
      endpoints:
        - 'http://localhost:9231/metrics'
  execute-script:
    script:
      path: './test/scripts/42.sh'
      args: []
  cron-job:
    cron:
      path: './test/scripts/now.sh'
      args: []
      # See https://godoc.org/github.com/robfig/cron#hdr-CRON_Expression_Format
      every: '*/10 * * * * *'
  serve-static:
    static:
      paths:
        - './test/static_files'
```

### Example playbook

```yaml
- hosts:
    - servers
  become: True
  roles:
    - { role: prometheus-exporters, tags: ["prometheus-exporters"] }
```

## License

MIT
