# LinSysApps

## Shell script segédprogramok Linux rendszerekhez

Fejlesztő: [pphome2](https:/github.com/pphome2)

**Aktuális verzió: 2023.**

**Első megjelenés: 2021.**

## SBackup

Mentési rendszer Linxhoz.

### Működés

Modulos rendszer a mentéshez. A beállításokat a 'bckup-config'
fájlban tárolja. Itt adható meg milyen könytárakat mentsen.

A modulokon keresztül a mentést a web-szerver egy védett könyvtárába
másolja, ahonnan egy másik modul let tudja szedni. Így távoli gép
is menthető.

Modul tud menteni USB eszközre is.

## SFDaemon

Egy daemon, ami egy fájlt figyel, amiben utasításokat kap.

### Működés

A program az 'sfdaemon-config' fájlon keresztül állítható. Külön script indítja
és állítja le a programot. Egy fáljt figyel és ha létezik akkor elindít egy megadott
programot, scriptet. Képes több parancs fogadására, ilyenkor a figyelt fájl
tartalma alapján indít el előre megadott programokat, scripteket.

## SysInfo

Rendszeradatok összegyüjtése, beépülő modulok támogatással.

### Működés

A program a fontosabb információkat szedi össze a rendszerről,
és a log-okból a hibaüzeneteket. Egyszerű txt fájlban tárolja az
információkat.

## RMLCHK

Távoli eszközök (szerverek) portjainak ellenőrzése, hogy működik-e a szolgáltatás.

### Működés

Az 'rmlchk-config' fájlban megadott ip című eszközök megadott protjait ellenőrzi
és log fájlba menti. A log tartalmát e-mail-en keresztül el tudja küldeni egy
megadott címre.

## UPSHTDWN

Szünetmentes jelzésének továbbítása és eszközök leállítása.

### Működés

A helyi szünetmentest kezelő szolgáltatás ( 'nut' ) jelzést ad a host rendszernek a
'/etc/killpower' fájlon keresztül. A program ezt a fájlt 'ssh'-n keresztül átadja a
kliens eszközöknek, melyek leállnak. Mail küldés és modulok támagatása.

## SshTunnel

Két végpont között tunnel kapcsolat létewsítése, közbenső szerveren keresztül.

### Működés

SSH port tunnel-en keresztül két végpont között, publikus szerveren keresztül.
Különböző portok elérhetővé tétele  SSH tunnel segytségével, publikus szerveren
keresztül. Beállításfájlban megadott adatokkal vezérelhető, figyelhető a tunnel
leállása.
