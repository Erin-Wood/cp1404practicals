import wikipedia


def main():
    print("Welcome to the Wikipedia search program!")
    print("Enter a page title or search phrase to get details.")
    print("Leave it blank and press Enter to quit.\n")

    search = input("Enter page title: ").strip()

    while search != "":
        try:
            page = wikipedia.page(search)
            print(f"\n{page.title}")
            print(f"{wikipedia.summary(search, sentences=2)}")
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(e.options[:5])  # Show the first 5 options for clarity
        except wikipedia.exceptions.PageError:
            print("\nPage id", f'"{search}"', "does not match any pages. Try another id!")
        except Exception as e:
            print("\nAn unexpected error occurred:", str(e))

        print("\n---")
        search = input("Enter page title: ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()
