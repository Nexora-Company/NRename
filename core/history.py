import json
from pathlib import Path


HISTORY_FILE = Path("history.json")


def initialize_history():
    """
    Crea el archivo history.json si no existe.
    """

    if not HISTORY_FILE.exists():

        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                [],
                f,
                indent=4,
                ensure_ascii=False
            )


def load_history():
    """
    Carga el historial completo.
    """

    initialize_history()

    try:

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception as e:

        print(
            "[HISTORY LOAD ERROR]"
        )

        print(e)

        return []


def save_history(history):
    """
    Guarda el historial completo.
    """

    try:

        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                history,
                f,
                indent=4,
                ensure_ascii=False
            )

    except Exception as e:

        print(
            "[HISTORY SAVE ERROR]"
        )

        print(e)


def add_history_entry(
        original_path,
        new_path):
    """
    Añade una entrada al historial.
    """

    history = load_history()

    history.append({

        "original":
            str(original_path),

        "new":
            str(new_path)

    })

    save_history(history)


def clear_history():
    """
    Elimina todo el historial.
    """

    save_history([])


def undo_last_operation():
    """
    Revierte todos los cambios guardados.

    Devuelve estadísticas.
    """

    history = load_history()

    stats = {

        "restored": 0,
        "errors": 0

    }

    if not history:
        return stats

    # Revertir en orden inverso

    for item in reversed(history):

        try:

            original = Path(
                item["original"]
            )

            new = Path(
                item["new"]
            )

            if not new.exists():
                continue

            new.rename(original)

            stats["restored"] += 1

        except Exception as e:

            print(
                "[UNDO ERROR]"
            )

            print(e)

            stats["errors"] += 1

    clear_history()

    return stats


def has_history():
    """
    Comprueba si existe historial.
    """

    history = load_history()

    return len(history) > 0