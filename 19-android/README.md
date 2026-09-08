# Android testing

The client is observable and modifiable, so important decisions belong on the
server. Inspect manifests, exported components, intent filters, deep links,
WebViews/bridges, network config, backups, logs, storage, bundled keys, pinning,
and underlying APIs.

Exercise: inventory a training APK with `adb`, JADX, and apktool. Record exported
entry points, accepted URI schemes, storage, contacted hosts, and authorization
assumptions. Try altering a client value and observe whether the server trusts it.

## Why an attacker cares

An APK exposes routes, schemas, feature flags, deep-link grammar, storage, and UI
assumptions. Exported components may let another app invoke privileged flows; a
WebView bridge may turn web content into native capability; client-only premium
checks may reveal a server authorization failure when requests are replayed.

Make separate static and dynamic inventories. Statically map manifest components,
intent filters, WebViews, JavaScript interfaces, network configuration, backup
flags, hardcoded material, and hosts. Dynamically launch exported activities,
send deep links, inspect controlled logs/storage, and proxy APIs. The finding is
the crossed native or server boundary, not that decompilation is possible.
