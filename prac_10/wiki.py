import wikipedia


def main():
    print("Welcome to the Wikipedia search program!")
    print("Enter a page title or search phrase to get details.")
    print("Leave it blank and press Enter to quit.\n")

    search = input("Enter a page title or search phrase: ").strip()
    while search != "":
        try:
            page = wikipedia.page(search)
            print("\nPage Title:", page.title)
            print("Summary:\n", wikipedia.summary(search, sentences=2))
            print("URL:", page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("\nYour search resulted in multiple options. Here are some:")
            print(", ".join(e.options[:5]))  # Show only the first 5 options
        except wikipedia.exceptions.PageError:
            print("\nSorry, no page was found with that title or search phrase.")
        except Exception as e:
            print("\nAn error occurred:", str(e))

        print("\n---")
        search = input("Enter a page title or search phrase: ").strip()

    print("Goodbye!")


if __name__ == "__main__":
    main()
