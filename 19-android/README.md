# Android testing

The client is observable and modifiable, so important decisions belong on the
server. Inspect manifests, exported components, intent filters, deep links,
WebViews/bridges, network config, backups, logs, storage, bundled keys, pinning,
and underlying APIs.

Exercise: inventory a training APK with `adb`, JADX, and apktool. Record exported
entry points, accepted URI schemes, storage, contacted hosts, and authorization
assumptions. Try altering a client value and observe whether the server trusts it.

