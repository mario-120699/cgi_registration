# import cgi


def main():
    # form = cgi.FieldStorage()
    print "content-type: text/html\n\n"
    with open('page.html') as page:
        text = page.read()
        print text


if __name__ == "__main__":
    main()
