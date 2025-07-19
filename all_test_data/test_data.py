from conftest import add_new_meme


id_mem = add_new_meme


invalid_data_list = [
    {"info": []},
    {"tags": {}},
    {"text": 1},
    {"url": None},
    {},  # Пустое поле
    {"meme": "items"}  # Лишнее поле которого нет
]

valid_data_list = [
    {"info": dict},
    {"tags": list},
    {"text": str},
    {"url": str}
]

valid_data_json_one_meme_list = [
    {"id": id_mem},
    {"info": {"colors": ["green", "white"]}},
    {"tags": ["face", "smile"]},
    {"text": "I love memes"},
    {"url": "https://miro.medium.com/v2/resize:fit:1200/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg"}
]

valid_data_json_created_meme_list = [
    {
        "id": id_mem,
        "info": {"color": ["purple", "blue", "green", "rose"]},
        "tags": ["child", "pose", "fist"],
        "text": "im 1 of the most popular memes ever",
        "url": "https://slang.net/img/slang/lg/meme_4580.png"
    }
]

negative_data_list = [
{
        "id": id_mem,
        "url": "https://slang.net/img/slang/lg/meme_4580.png",
        "tags": ["child", "pose", "fist"],
        "info": {"color": ["purple", "blue", "green", "rose"]},
    },
    {
        "id": id_mem,
        "text": "im 1 of the most popular memes ever",
        "url": "https://slang.net/img/slang/lg/meme_4580.png",
        "info": {"color": ["purple", "blue", "green", "rose"]},
    },
    {
        "id": id_mem,
        "text": 1234,
        "url": True,
        "tags": dict,
        "info": "is_not_dict"
    }
]
