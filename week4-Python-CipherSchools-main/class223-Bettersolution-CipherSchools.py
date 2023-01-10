with open("index.html" ,"r") as webpage:
    with open("output2.txt","a") as wf:
        page = webpage.read()
        link_exist = "True"
        while link_exist:
            pos = line.find('<a href = ')
            if pos == -1:
                link_exists = False
            else:
                first_quote = line.find('\"',pos) 
                second_quote =line.find('\"', first_quote+1)
                url = line[first_quote+1: second_quote]
                wf.write(url+'\n')   
                page = page[second_quote]