char_to_index = {' ': 0,'ئ':320, 'أ':330, 'ّ': 300,'ة': 310, 'ا': 10, 'ب': 20, 'ت': 30, 'ث': 40, 'ج': 50, 'ح': 60, 'خ': 70, 'د': 80, 'ذ': 90, 'ر': 100, 'ز': 110, 'س': 120, 'ش': 130, 'ص': 140, 'ض': 150, 'ط': 160, 'ظ': 170, 'ع': 180, 'غ': 190, 'ف': 200, 'ق': 210, 'ك': 220, 'ل': 230, 'م': 240, 'ن': 250, 'ه': 260, 'و': 270, 'ي': 280, 'ى': 290}

index_to_char={y:x for x,y in char_to_index.items()}
words=[]
roots=[]
def change_to_char(input_list):
    output_char=[]
    for i in input_list:
        output_char.append(index_to_char[i])
    return output_char

def join_char(input_char):
    word=""
    for c in input_char:
        word +=''.join(c)
    return word

def change_to_int(input_word):
    output_int=[]
    for char in input_word:
        output_int.append(char_to_index[char])
    return output_int

def write_list_to_file(file_path, items):
    
    with open(file_path, 'w') as file:
        for item in items:
            c=change_to_char(item)
            j=join_char(c)
            file.write(j +'\n')


file_names=["افتعال","افتعل","تفاعيل","تفعل","حرف","فاعل","فعال",
"فعل","فعول","فعيل","فل","مفتعل"]
k=0
al=0
faa=0
words=[]
roots=[]
start_numbers=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,330]
middle_numbers=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,320,330]
end_numbers=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,320,330,300,310]
for fname in file_names:

    
    total=0
    
    with open ("root_stem_patterns/{}.txt".format(fname),"r", encoding="utf-8") as file:
        file_read=file.readlines()
        k+=1
        print(k)
        for i in start_numbers:
            for f in middle_numbers:
                for y in end_numbers:
                    if i !=f and f!=y:
                        if fname=="فاعل" and i!=10 and i!=330 and f!=10 and f!=330:
                            root=[]
                            word=[]
                            
                            
                            root.append(i)
                               
                            root.append(f)
                               
                            root.append(y)
                               
                            for line in file_read:
                                word=[]
                            
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)

                        elif fname=="افتعال" and i!=10 and i!=330 and f!=10 and f!=330 and y!=10 and y!=330:
                            root=[]
                            word=[]
                            
                            
                            root.append(i)
                               
                            root.append(f)
                               
                            root.append(y)

                            for line in file_read:
                                word=[]
                               
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)

                        elif fname=="افتعل" and i!=10 and i!=330:
                            root=[]
                            word=[]
                            
                            
                            root.append(i)
                               
                            root.append(f)
                               
                            root.append(y)

                            for line in file_read:
                                word=[]
                                
                                
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)

                        elif fname=="تفاعيل" and i!=10 and i!=330 and f!=10 and f!=330 and y!=280 and y!=290:
                            root=[]
                            word=[]
                            
                            
                            root.append(i)
                               
                            root.append(f)
                               
                            root.append(y)

                            for line in file_read:
                                word=[]
                                
                                
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)

                        
                                
                        elif fname=="فعال" and f!=10 and f!=330 and y!=10 and y!=330:
                            root=[]
                            word=[]
                            
                            
                            root.append(i)
                               
                            root.append(f)
                               
                            root.append(y)

                            for line in file_read:
                                word=[]
                                
                                
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)

                        elif fname=="فعل" and i!=y:
                            root=[]
                            word=[]
                            
                            
                            root.append(i)
                               
                            root.append(f)
                               
                            root.append(y)

                            for line in file_read:
                                word=[]
                                
                                
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)


                        elif fname=="فعول" and f!=270 and y!=270:
                            root=[]
                            word=[]
                            
                            
                            root.append(i)
                               
                            root.append(f)
                               
                            root.append(y)

                            for line in file_read:
                                word=[]
                                
                                
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)

                        elif fname=="فعيل" and f!=280 and f!=290 and y!=280 and y!=290:
                            root=[]
                            word=[]
                            
                            
                            root.append(i)
                               
                            root.append(f)
                               
                            root.append(y)

                            for line in file_read:
                                word=[]
                                
                                
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)
                        elif fname=="فل" and i!=y:
                            root=[]
                            word=[]
                            
                            
                            root.append(i)
                               
                            root.append(y)

                            for line in file_read:
                                word=[]
                                
                                
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)
                        elif fname=="حرف":
                            root=[]
                            word=[]
                            
                            root.append(0)

                            for line in file_read:
                                word=[]
                                
                                
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)
                        else:
                            root=[]
                            word=[]
                            
                            
                            root.append(i)
                               
                            root.append(f)
                               
                            root.append(y)

                            for line in file_read:
                                word=[]
                                
                                
                                for char in line.strip():
                                    if char=='ف':
                                        word.append(i)
                                    elif char=='ع':
                                        word.append(f)
                                    elif char=="#":
                                        word.append(y)
                                    else:
                                        word.append(char_to_index[char])
                                words.append(word)
                                        
                                roots.append(root)
                              
                
    print("lenghth of words {} ".format(len(words)))
    print("length of roots {} ".format(len(roots)))

file_path="words_root_based_revised.txt"
write_list_to_file(file_path,words)

file_path="roots_root_based_revised.txt"
write_list_to_file(file_path,roots)

words=[]
roots=[]
