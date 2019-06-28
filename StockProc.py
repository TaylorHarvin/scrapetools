from bs4 import BeautifulSoup



def getSinglePageData(pagePath):
    with open(pagePath, "r") as f:
        return BeautifulSoup(f.read(), 'html.parser')

def procStockTableData(tableBS):
    rows = []

    for stockRow in tableBS.findAll("tr"):
        rows.append(procStockRows(stockRow))

    return "\n".join(rows)

def procStockRows(rowBS):
    cols = []
    colInList = []
    currCol = ""

    for stockCol in rowBS.findAll("td"):
        colInList = stockCol.select("span")
        currCol = ""
        for colItem in colInList:
            currCol += colItem.text
        cols.append(currCol)

    #print(cols)
    return ",".join(cols)

def main():
    count = 0
    pageBS = getSinglePageData("page.html")

    outHTML = ""
    for stockTable in pageBS.findAll("table"):
        outHTML += str(procStockTableData(stockTable))

        '''with open("test/test_"+str(count)+".html","w") as f:
            f.write(str(stockTable))

        count += 1'''

    with open("out.csv", "w") as f:
        f.write(outHTML)

if __name__ == "__main__":
    main()