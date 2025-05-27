"""
AIPyOOP - AI-Powered OOP Learning Assistant

This package provides tools to learn, evaluate, and improve Object-Oriented Programming skills in Python
using interactive AI feedback and pre-built examples.

Modules:
- interactive: Interactive learning interface
- refactor: AI-powered code improvement
- examples: Predefined OOP examples like Car, BankAccount, etc.
- concepts: Core OOP concept explanations
- evaluator: Code analysis and feedback system
"""

__version__ = "1.0.0"

from .interactive import start_learning
from .refactor import refactor_code
from .examples import Car, BankAccount, GameCharacter
