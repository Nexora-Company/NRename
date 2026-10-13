"""Tokens oficiales de identidad visual de Nexora.

Fuente unica de verdad: paleta oficial (fondos, superficies, texto y rojo
de marca) y familia tipografica recomendada. Los componentes Qt deben
consumir estos tokens en lugar de duplicar valores hexadecimales.

Referencia: skill `visual-identity` v. paleta oficial.
"""

NX_COLOR_WHITE = "#FFFFFF"
NX_COLOR_NEUTRAL_50 = "#FBFBFD"
NX_COLOR_NEUTRAL_100 = "#F5F5F7"
NX_COLOR_NEUTRAL_200 = "#F0F0F3"
NX_COLOR_NEUTRAL_500 = "#6B6B74"
NX_COLOR_NEUTRAL_700 = "#42424A"
NX_COLOR_NEUTRAL_900 = "#16161A"

NX_COLOR_DARK_950 = "#0D0D0F"
NX_COLOR_DARK_900 = "#131317"
NX_COLOR_DARK_850 = "#191A1E"
NX_COLOR_DARK_800 = "#1F2024"
NX_COLOR_DARK_750 = "#26272C"

NX_COLOR_BRAND_RED = "#A50021"
NX_COLOR_BRAND_RED_DEEP = "#8E001C"
NX_COLOR_BRAND_RED_LIGHT = "#FF8497"
NX_COLOR_BRAND_RED_SOFT = "#FF9DB0"

NX_GLOW_RED_SOFT = "rgba(165, 0, 33, 0.20)"

NX_FONT_FAMILY = "'Inter', -apple-system, sans-serif"

# Roles semanticos para el tema oscuro de la app de escritorio.
# Texto secundario usa un neutro claro para cumplir WCAG 2.2 AA (>= 4.5:1)
# sobre fondos oscuros. NX_COLOR_NEUTRAL_500 se reserva para estados
# deshabilitados y metadatos no esenciales.
NX_TEXT_PRIMARY = NX_COLOR_WHITE
NX_TEXT_SECONDARY = NX_COLOR_NEUTRAL_100
NX_TEXT_MUTED = NX_COLOR_NEUTRAL_200
NX_TEXT_DISABLED = NX_COLOR_NEUTRAL_500

NX_BG_BASE = NX_COLOR_DARK_950
NX_BG_RAISED = NX_COLOR_DARK_900
NX_BG_ELEVATED = NX_COLOR_DARK_850
NX_BG_INTERACTIVE = NX_COLOR_DARK_800
NX_BORDER_SUBTLE = NX_COLOR_DARK_750
