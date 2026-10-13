#!/bin/bash
set -euo pipefail

# Nexora Rename — empaquetado .deb (Linux amd64)
APP_NAME="nexora-rename"
VERSION="1.1.0"
PKG_DIR="deb_build/${APP_NAME}_${VERSION}_amd64"

# 1. Crear estructura de carpetas
mkdir -p "$PKG_DIR/DEBIAN"
mkdir -p "$PKG_DIR/usr/bin"
mkdir -p "$PKG_DIR/usr/share/applications"
mkdir -p "$PKG_DIR/usr/share/nexora-rename"
mkdir -p "$PKG_DIR/usr/share/icons/hicolor/256x256/apps"

# 2. Copiar archivos de PyInstaller
cp -r dist/NexoraRename/* "$PKG_DIR/usr/share/nexora-rename/"
cp resources/IconRename.png "$PKG_DIR/usr/share/icons/hicolor/256x256/apps/nexora-rename.png"

# 3. Crear el script en /usr/bin
cat << 'EOF' > "$PKG_DIR/usr/bin/nexora-rename"
#!/bin/bash
exec /usr/share/nexora-rename/NexoraRename "$@"
EOF
chmod +x "$PKG_DIR/usr/bin/nexora-rename"

# 4. Crear DEBIAN/control
cat << EOF > "$PKG_DIR/DEBIAN/control"
Package: nexora-rename
Version: ${VERSION}-1
Section: utils
Priority: optional
Architecture: amd64
Maintainer: Saarmyx <saarmyx@nexoralabs.com>
Depends: libgl1, libglx-mesa0, libxcb-cursor0, libmediainfo0v5, libimage-exiftool-perl
Description: Utilidad de renombrado masivo y metadatos con diseño Nexora.
EOF

# 5. Crear archivo .desktop
cat << 'EOF' > "$PKG_DIR/usr/share/applications/nexora-rename.desktop"
[Desktop Entry]
Name=Nexora Rename
Comment=Renombrador masivo y metadatos
Exec=nexora-rename
Icon=nexora-rename
Terminal=false
Type=Application
Categories=Utility;FileTools;
EOF

# 6. Construir el .deb
dpkg-deb --build "$PKG_DIR"
echo "Paquete .deb generado en $PKG_DIR.deb"
