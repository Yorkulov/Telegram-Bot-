from aiogram import Dispatcher
from filters.admins import AdminFilter
from filters.group_filter import IsGroup
from filters.private_chat import IsPrivate

from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
