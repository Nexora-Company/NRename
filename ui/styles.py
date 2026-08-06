DARK_STYLE = """
/* ==================================================
   NEXORA — DESIGN SYSTEM (Qt QSS Adaptation)
   Base: Monochromatic (#0A0A0A) + Red Accent (#E11D2E)
   ================================================== */

QMainWindow {
    background-color: #0A0A0A;
}

QWidget {
    color: #FFFFFF;
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 13px;
}

/* ==================================================
   BUTTONS (Sharp radius, technical feel)
   ================================================== */
QPushButton {
    background-color: #0A0A0A;
    color: #FFFFFF;
    border: 1px solid #545454;
    border-radius: 2px;
    padding: 8px 16px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

QPushButton:hover {
    background-color: #2B2B2B;
    border-color: #E11D2E;
    color: #FFFFFF;
}

QPushButton:pressed {
    background-color: #E11D2E;
    border-color: #E11D2E;
    color: #FFFFFF;
}

QPushButton:disabled {
    background-color: #0A0A0A;
    color: #545454;
    border-color: #2B2B2B;
}

/* ==================================================
   LISTS & TABLES
   ================================================== */
QListWidget, QTableWidget {
    background-color: #0A0A0A;
    border: 1px solid #2B2B2B;
    border-radius: 2px;
    gridline-color: #2B2B2B;
    outline: none;
    color: #ECECEC;
}

QListWidget::item {
    padding: 8px 12px;
    border-bottom: 1px solid #1A1A1A;
}

QListWidget::item:hover {
    background-color: #1A1A1A;
    color: #FFFFFF;
}

QListWidget::item:selected, QTableWidget::item:selected {
    background-color: #B01522;
    color: #FFFFFF;
}

QHeaderView::section {
    background-color: #0A0A0A;
    color: #8A8A8A;
    padding: 8px 12px;
    border: none;
    border-bottom: 2px solid #E11D2E;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

/* ==================================================
   PROGRESS BAR & STATUS
   ================================================== */
QProgressBar {
    background-color: #1A1A1A;
    border: 1px solid #2B2B2B;
    border-radius: 2px;
    text-align: center;
    color: #FFFFFF;
    font-weight: 600;
}

QProgressBar::chunk {
    background-color: #E11D2E;
}

QLabel {
    color: #8A8A8A;
    font-weight: 500;
}

/* Scrollbars industriales */
QScrollBar:vertical, QScrollBar:horizontal {
    background: #0A0A0A;
    border: none;
    width: 8px;
    height: 8px;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #2B2B2B;
    border-radius: 0px;
}

QScrollBar::handle:hover {
    background: #E11D2E;
}
"""