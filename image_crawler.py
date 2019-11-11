import sys
import tkinter as tk
from icrawler.builtin import GoogleImageCrawler

root = tk.Tk()
root.title('Image Crawler')

# Gets the requested values of the height and widht.
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
position_right = int(root.winfo_screenwidth()/2 - window_width/2)
position_down = int(root.winfo_screenheight()/2 - window_height/2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(position_right, position_down))

var = tk.StringVar()
var.set('')


def crawl_image(keyword, max_num):
    try:
        crawler = GoogleImageCrawler(storage={'root_dir': 'images'})
        crawler.crawl(keyword=keyword, max_num=int(max_num))
        var.set('Crawling is done.')
    except ValueError:
        var.set('Maxinum number of images \n must be integer.')


# label
label_1 = tk.Label(text='Keyword')
label_1.pack(pady=(20, 0))

# entry
keyword_entry = tk.Entry()
keyword_entry.pack()

# label
label_2 = tk.Label(text='Maximum number of images')
label_2.pack(pady=(5, 0))

# entry
max_num_entry = tk.Entry()
max_num_entry.pack()

# button
crawl_button = tk.Button(text='Crawl', width=20,
                         command=lambda: crawl_image(keyword_entry.get(), max_num_entry.get()))
crawl_button.pack(pady=(20, 0))

label_3 = tk.Label(textvariable=var)
label_3.pack(pady=(0, 20))

root.mainloop()
