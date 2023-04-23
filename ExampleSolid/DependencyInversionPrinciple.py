# example one
# wrong way

class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.2


class App:
    def start(self):
        converter = FXConverter()
        converter.convert("EUR", "USD", 100)


# correct way

from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class FXConverterCorrect(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print("Converting currency using FX API")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.15


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print("Converting currency using Alpha API")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.2


class AppCorrect:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert("EUR", "USD", 100)


# example way


# wrong way
class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def print(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)


# correct way

from typing_extensions import Protocol
from dataclasses import dataclass


@dataclass
class HasContentProtocol(Protocol):
    content: str


@dataclass
class Book(HasContentProtocol):
    def __init__(self, content):
        self.content = content


@dataclass
class FormatterProtocol(Protocol):
    def format(self, has_content: HasContentProtocol):
        pass


class A4Formatter(FormatterProtocol):
    def format(self, has_content: HasContentProtocol):
        return has_content.content  # This should obviously


class PrinterCorrect:
    def __init__(self, formatter: FormatterProtocol):
        self.formatter = formatter

    def print(self, has_content: HasContentProtocol):
        formatted_book = self.formatter.format(has_content)
