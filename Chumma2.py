import wikipedia
import warnings

q = input("Enter your search: ")
result = wikipedia.search(q)

warnings.catch_warnings()
warnings.simplefilter("ignore")

try:
    page = wikipedia.page(result[0], auto_suggest=False)
    title = page.title
    content = page.content
    print(title)
    print("-------------------------------------------------------")
    print(content)
except wikipedia.exceptions.DisambiguationError as e:
    print("Sorry, the word " + q + " has many pages. Did you mean any one of these:")
    print(*e.options, sep = "\n")
except wikipedia.exceptions.PageError as e:
    print("Sorry, the page doesn't exist")
except:
    print("Please enter a valid word!")

