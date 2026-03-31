import pytest
from ndfl.calculator import calculate_tax


# --- Базовые тесты из задания ---

def test_basic_ndfl():
    # 200_000 * 0.13 = 26_000
    assert calculate_tax(200_000) == 26_000


def test_basic_ndfl2():
    # 312_000 + 0.15 * (3_000_000 - 2_400_000) = 312_000 + 90_000 = 402_000
    assert calculate_tax(3_000_000) == 402_000


def test_basic_ndfl3():
    # 702_000 + 0.18 * (7_000_000 - 5_000_000) = 702_000 + 360_000 = 1_062_000
    assert calculate_tax(7_000_000) == 1_062_000


# --- Граничные значения ---

def test_zero_income():
    assert calculate_tax(0) == 0


def test_exact_first_bracket_limit():
    # Ровно на границе первой ступени
    assert calculate_tax(2_400_000) == 312_000


def test_exact_second_bracket_limit():
    # Ровно на границе второй ступени
    assert calculate_tax(5_000_000) == 702_000


def test_exact_third_bracket_limit():
    # Ровно на границе третьей ступени
    assert calculate_tax(20_000_000) == 3_402_000


def test_exact_fourth_bracket_limit():
    # Ровно на границе четвёртой ступени
    assert calculate_tax(50_000_000) == 9_402_000


def test_above_max_bracket():
    assert calculate_tax(60_000_000) == 11_602_000


# --- Корректность прогрессии (повышенная ставка только с превышения) ---

def test_progressive_not_flat():
    # При доходе чуть выше порога налог не должен резко вырасти
    tax_at_border = calculate_tax(2_400_000)
    tax_above_border = calculate_tax(2_400_001)
    assert tax_above_border > tax_at_border
    # Разница должна быть около 0.15 руб., а не тысячи
    assert tax_above_border - tax_at_border < 1


# --- Ошибки ---

def test_negative_income_raises():
    with pytest.raises(ValueError):
        calculate_tax(-1)
