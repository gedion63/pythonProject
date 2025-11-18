from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_inf: str) -> str:
    """Функция возвращает строку с замаскированным номером"""
    if "Счет" in card_inf:  # Проверка по типу карта/счет
        return card_inf.replace(
            card_inf[-20:], get_mask_account(card_inf[-20:])
        )  # Возвращает счет с подменой последних 16 значений
    else:
        return card_inf.replace(
            card_inf[-16:], get_mask_card_number(card_inf[-16:])
        )  # Возвращает счет с подменой последних 16 значений
    """Создан модуль widget создана функция mask_account_card"""