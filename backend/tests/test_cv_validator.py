from jobmatcher.services.cv_validator import (
    is_likely_cv,
    validate_cv,
)


def test_valid_cv_is_accepted():
    text = """
    John Doe

    john.doe@example.com
    +1 555 123 4567
    github.com/johndoe

    Skills
    Python
    FastAPI
    Docker
    MySQL

    Work Experience
    Backend Developer
    2022 - 2025

    Education
    Bachelor of Computer Science

    Languages
    English
    French
    """

    assert is_likely_cv(text) is True

    validate_cv(text)


def test_non_cv_document_is_rejected():
    text = """
    Содержание

    Введение

    Целью исследования является разработка архитектуры
    автономной интеллектуальной системы.

    Методология и используемые технологии

    В исследовании рассматриваются Python, PyTorch,
    deep learning, computer vision и нейронные сети.

    Ожидаемые научные результаты

    Планируется разработка и экспериментальная проверка
    методов искусственного интеллекта для автономных систем.

    Заключение

    Представлены основные направления дальнейшего
    исследования и разработки системы.
    """

    assert is_likely_cv(text) is False


def test_empty_document_is_rejected():
    assert is_likely_cv("") is False


def test_short_document_is_rejected():
    assert is_likely_cv(
        "Python FastAPI Docker"
    ) is False