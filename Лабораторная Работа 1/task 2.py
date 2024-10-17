capacity_mb=1.44
capacity_byte=1.44*1024*1024
number_pages=100
number_lines=50
number_letters=25
size_letter=4

number_books=int(capacity_byte//(number_lines*number_pages*number_letters*size_letter))
print("Количество книг, помещающихся на дискету:", number_books)
