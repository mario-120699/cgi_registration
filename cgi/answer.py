import cgi


def main():
    form = cgi.FieldStorage()
    nome = form.getfirst("First_name")
    email = form.getfirst("Email")
    class_ = form.getfirst("class")
    time = form.getfirst("Time_preference")
    approval = form.getfirst("approval")
    string = '{};{};{};{};{}\n'.format(nome, email, class_, time, approval)
    with open('enrolled.csv', 'a') as file_write:
        file_write.write(string)
    print "content-type: text/html\n\n"
    print "<h1>Done, thank you!</h1>"
    print "<p>Dear {}, you have been registered successfully</p>".format(nome)
    print " <a href=/cgi/results.py>Tabella risultati</a> "


if __name__ == "__main__":
    main()
