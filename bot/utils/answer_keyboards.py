from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def invite_variants():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="invite by @username", callback_data="invite_by_username_callback")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def kata_variants():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="1 kata", callback_data="1_kata_solve")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def data_variants():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="1 day", callback_data="1_day")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()