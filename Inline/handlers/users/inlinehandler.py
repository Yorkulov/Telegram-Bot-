from aiogram import types
from loader import dp
from keyboards.inline.buttons import keys

@dp.inline_handler(text="rasm")
async def photo_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultPhoto(
                id="001",
                photo_url = "https://images.unsplash.com/photo-1607337202714-a88f7abbdee7?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YWxpZW58ZW58MHx8MHx8fDA%3D",
                thumb_url = "https://images.unsplash.com/photo-1607337202714-a88f7abbdee7?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YWxpZW58ZW58MHx8MHx8fDA%3D",
                caption = "<b>Qanaqadir title</b>",
                reply_markup=keys
            )

        ]
    )

@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="rasm001",
                title="1 - rasm",
                input_message_content = types.InputTextMessageContent(
                    message_text="Rasm uchun link: https://google.com"
                ),
                url="https://google.com",
                thumb_url="https://images.unsplash.com/photo-1598759310798-18f8497d9858?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8fA%3D%3D",
                description="Qanaqadir rasmda"                
            ),
            types.InlineQueryResultArticle(
                id="rasm002",
                title="2 - rasm",
                input_message_content = types.InputTextMessageContent(
                    message_text="Rasm uchun link: https://google.com"
                ),
                url="https://google.com",
                thumb_url="https://images.unsplash.com/photo-1566800168617-1dbae8097084?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8M3x8fGVufDB8fHx8fA%3D%3D",
                description="Qanaqadir rasmda"                
            ),
            types.InlineQueryResultArticle(
                id="rasm003",
                title="3 - rasm",
                input_message_content = types.InputTextMessageContent(
                    message_text="Rasm uchun link: https://google.com"
                ),
                url="https://google.com",
                thumb_url="https://images.unsplash.com/photo-1585059895567-a8f81fc3870c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTB8fHxlbnwwfHx8fHw%3D",
                description="Qanaqadir rasmda"                
            ),
            types.InlineQueryResultArticle(
                id="rasm004",
                title="4 - rasm",
                input_message_content = types.InputTextMessageContent(
                    message_text="Rasm uchun link: https://google.com"
                ),
                url="https://google.com",
                thumb_url="https://images.unsplash.com/photo-1581102019793-b6f8748779a1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTZ8fHxlbnwwfHx8fHw%3D",
                description="Qanaqadir rasmda"                
            ),
            types.InlineQueryResultArticle(
                id="rasm005",
                title="5 - rasm",
                input_message_content = types.InputTextMessageContent(
                    message_text="Rasm uchun link: https://google.com"
                ),
                url="https://google.com",
                thumb_url="https://images.unsplash.com/photo-1495231916356-a86217efff12?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTl8fHxlbnwwfHx8fHw%3D",
                description="Qanaqadir rasmda"                
            ),
            types.InlineQueryResultArticle(
                id="rasm006",
                title="6 - rasm",
                input_message_content = types.InputTextMessageContent(
                    message_text="Rasm uchun link: https://google.com"
                ),
                url="https://google.com",
                thumb_url="https://images.unsplash.com/photo-1558552276-3b89167709bd?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fG11c3Rhbmd8ZW58MHx8MHx8fDA%3D",
                description="Qanaqadir rasmda"                
            ),
        ]
    )



# Lug'at shakllantirib for yordamida qilib chiqish mumkin