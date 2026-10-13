"""Sistema de estilos Qt de Nexora Rename.

Construido exclusivamente con tokens oficiales de `ui.tokens`. No se
duplican valores de color fuera de los tokens.
"""

from ui.tokens import (
    NX_BG_BASE,
    NX_BG_ELEVATED,
    NX_BG_INTERACTIVE,
    NX_BG_RAISED,
    NX_BORDER_SUBTLE,
    NX_COLOR_BRAND_RED,
    NX_COLOR_BRAND_RED_DEEP,
    NX_COLOR_BRAND_RED_LIGHT,
    NX_FONT_FAMILY,
    NX_TEXT_DISABLED,
    NX_TEXT_MUTED,
    NX_TEXT_PRIMARY,
    NX_TEXT_SECONDARY,
)

DARK_STYLE = f"""
QMainWindow {{
    background-color: {NX_BG_BASE};
}}

QWidget {{
    color: {NX_TEXT_PRIMARY};
    font-family: {NX_FONT_FAMILY};
    font-size: 13px;
}}

QPushButton, QToolButton {{
    background-color: {NX_BG_BASE};
    color: {NX_TEXT_PRIMARY};
    border: 1px solid {NX_BORDER_SUBTLE};
    border-radius: 2px;
    padding: 8px 16px;
    font-weight: 600;
}}

QPushButton:hover, QToolButton:hover {{
    background-color: {NX_BG_INTERACTIVE};
    border-color: {NX_COLOR_BRAND_RED};
    color: {NX_TEXT_PRIMARY};
}}

QPushButton:pressed, QToolButton:pressed {{
    background-color: {NX_COLOR_BRAND_RED};
    border-color: {NX_COLOR_BRAND_RED};
    color: {NX_TEXT_PRIMARY};
}}

QPushButton:disabled, QToolButton:disabled {{
    background-color: {NX_BG_BASE};
    color: {NX_TEXT_DISABLED};
    border-color: {NX_BORDER_SUBTLE};
}}

QPushButton:focus, QToolButton:focus {{
    border-color: {NX_COLOR_BRAND_RED_LIGHT};
}}

QMenu {{
    background-color: {NX_BG_BASE};
    border: 1px solid {NX_BORDER_SUBTLE};
    padding: 4px;
}}

QMenu::item {{
    background-color: transparent;
    color: {NX_TEXT_SECONDARY};
    padding: 8px 24px;
    font-weight: 500;
}}

QMenu::item:selected {{
    background-color: {NX_COLOR_BRAND_RED_DEEP};
    color: {NX_TEXT_PRIMARY};
}}

QListWidget, QTableWidget {{
    background-color: {NX_BG_BASE};
    border: 1px solid {NX_BORDER_SUBTLE};
    border-radius: 2px;
    gridline-color: {NX_BORDER_SUBTLE};
    outline: none;
    color: {NX_TEXT_SECONDARY};
}}

QListWidget::item {{
    padding: 8px 12px;
    border-bottom: 1px solid {NX_BG_RAISED};
}}

QListWidget::item:hover {{
    background-color: {NX_BG_RAISED};
    color: {NX_TEXT_PRIMARY};
}}

QListWidget::item:selected, QTableWidget::item:selected {{
    background-color: {NX_COLOR_BRAND_RED_DEEP};
    color: {NX_TEXT_PRIMARY};
}}

QHeaderView::section {{
    background-color: {NX_BG_BASE};
    color: {NX_TEXT_MUTED};
    padding: 8px 12px;
    border: none;
    border-bottom: 2px solid {NX_COLOR_BRAND_RED};
    font-weight: 700;
}}

QProgressBar {{
    background-color: {NX_BG_RAISED};
    border: 1px solid {NX_BORDER_SUBTLE};
    border-radius: 2px;
    text-align: center;
    color: {NX_TEXT_PRIMARY};
    font-weight: 600;
}}

QProgressBar::chunk {{
    background-color: {NX_COLOR_BRAND_RED};
}}

QLabel {{
    color: {NX_TEXT_SECONDARY};
    font-weight: 500;
}}

QScrollBar:vertical, QScrollBar:horizontal {{
    background: {NX_BG_BASE};
    border: none;
    width: 8px;
    height: 8px;
}}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {{
    background: {NX_BORDER_SUBTLE};
    border-radius: 0px;
}}

QScrollBar::handle:hover {{
    background: {NX_COLOR_BRAND_RED};
}}
"""
