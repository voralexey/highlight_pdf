import fitz # pip3 install pymupdf

pdfIn = fitz.open("input.pdf") # pdf file to search through

# either open a file with a list of search words *
with open("list_of_words.txt") as file:
    lines = [line.rstrip() for line in file]

for page in pdfIn:
    print(page)
    # * or make a list of words
    #lines = ["Able", "Allow", "Consistency"]
    #text_instances = [page.search_for(text) for text in lines]
    text_instances = [page.search_for(text) for text in lines]

    # coordinates of each word found in PDF-page
    print(text_instances)

    # iterate through each instance for highlighting
    for inst in text_instances:
        annot = page.add_highlight_annot(inst)
        # annot = page.add_rect_annot(inst)

        ## Adding comment to the highlighted text
        info = annot.info
        info["title"] = "word_diffs"
        info["content"] = "diffs"
        annot.set_info(info)
        annot.update()

# Saving the PDF Output
pdfIn.save("output.pdf")