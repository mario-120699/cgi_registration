def main():
    table = str()
    with open("enrolled.csv") as file_:
        line = file_.read().split("\n")
        for l in line:
            attr = l.split(";")
            if len(attr) == 5:
                table += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(attr[0], attr[1], attr[2], attr[3], attr[4])
    print "content-type: text/html\n\n"
    with open('results.html') as page:
        text = page.read()
        print text.format(table)


if __name__ == "__main__":
    main()