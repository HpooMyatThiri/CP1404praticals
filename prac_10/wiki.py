import wikipedia

user_input = input("Page title or search phrase: ")
while user_input != "":
    print(wikipedia.search(user_input))
    try:
        user_page = wikipedia.page(user_input, auto_suggest=False)
        print(user_page.title)
        print(wikipedia.summary(user_input))
        print(user_page.url)
        print(user_page.content)
        print(user_page.images[0])
        print(user_page.links[0])
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    user_input = input("Page title or search phrase: ")


