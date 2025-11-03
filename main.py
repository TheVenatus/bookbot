from stats import word_counter, number_letter, sort
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    try:
        file_contents = get_book_text(str(sys.argv[1]))
        num_words = word_counter(file_contents)
        print(sys.argv)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        counts = number_letter(file_contents)
        sortet_list = sort(counts)
        print("--------- Character Count -------")
        for i in sortet_list:
            print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
if __name__ == "__main__":
    main()