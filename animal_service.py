from tkinter import *
from tkinter import font
import tkinter.ttk  #페이지 수를 나누기 위한
import tkinter.messagebox

#페이지 수를 나누기로 합니다.
#1페이지: 시/군/구로 하여금 유기동물 정보 조회/품종이나 날짜별로 선택 가능하게?
#2페이지: 시/군/구 별로 보호소 현황 조회 (어디에 무슨 보호소가 있고...)-지도는 여기연결?
#3페이지: 그래프로 보호수 / 입양수 표시+챗봇은 여기?

window=Tk()
window.title("유기동물 보호소 및 정보 조회")
DataList = []

notebook=tkinter.ttk.Notebook(window, width=800, height=600)
notebook.pack()

frame1=Frame(window)
notebook.add(frame1, text="유기동물 정보 조회")

##----1페이지 내용: 시군구 조건을 갖춘 후 유기동물 정보를 조회할 수 있게----##
#검색기능 & 이미지 출력 기능 구현
#시군구 조건을 맞춘 후 조회시 해당 지역의 유기견 보호소에서의 유기견 현황을 볼 수 있음
#품종이나 날짜 필터 가능하게? 어떻게?

label1=Label(frame1, text="<<유기동물 정보 조회>>", font='helvetica 14')
label1.pack()
label1.place(x=17, y=15) #페이지 항목 제목!

#시/군/구를 선택할 스크롤박스 /1페이지 전용이라 함수선언은 하지 않았습니다.
#강아지(또는 개)/고양이/기타로 나누어 선택 가능.
#주소는 엔트리 입력으로?

global SearchListBox1

ListBoxScrollbar = Scrollbar(window)
ListBoxScrollbar.pack()
ListBoxScrollbar.place(x=157, y=78)
TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
SearchListBox1 = Listbox(window, font=TempFont, activestyle='none',
                        width=10, height=1, borderwidth=12, relief='ridge',
                        yscrollcommand=ListBoxScrollbar.set)
SearchListBox1.insert(1, "강아지")
SearchListBox1.insert(2, "고양이")
SearchListBox1.insert(3, "기타")
SearchListBox1.pack()
SearchListBox1.place(x=20, y=78)
ListBoxScrollbar.config(command=SearchListBox1.yview)

label2=Label(frame1, text="[지역(시/군/구)]", font='helvetica 12')
label2.pack()
label2.place(x=185, y=67)

label3=Label(frame1, text="※주소 작성 예시: 서울특별시 용산구", fg='red', font='helvetica 10')
label3.pack()
label3.place(x=300, y=100)

global InputLabel
TempFont = font.Font(frame1, size=10, weight='bold', family='Consolas')
InputLabel = Entry(frame1, font=TempFont, width=26,  borderwidth=12, relief='ridge')
InputLabel.pack()
InputLabel.place(x=300, y=60)

#-------------여기까지 1페이지 내용----------------#
frame2=Frame(window)
notebook.add(frame2, text="유기동물 보호소 조회")

##----2페이지 내용: 시군구 조건을 갖춘 후 유기동물 보호소 현황을 조회할 수 있게----##
#검색기능 & 지도 연동 기능 구현
#시군구 조건을 맞춘 후 조회시 해당 지역의 유기견 보호소현황을 볼 수 있음
#정보를 받아와서 유기견 보호소의 명칭과 전번, 위치(주소) 등을 출력.
#지도 연동: 클릭시 해당 보호소의 구글지도 확인 가능. 이클래스 참고자료 참조

label2=Label(frame2, text="<<유기동물 보호소 조회>>", font='helvetica 14')
label2.pack()
label2.place(x=17, y=15)

label2=Label(frame2, text="[지역(시/군/구)]", font='helvetica 12')
label2.pack()
label2.place(x=10, y=67)

label3=Label(frame2, text="※주소 작성 예시: 서울특별시 용산구", fg='red', font='helvetica 10')
label3.pack()
label3.place(x=135, y=100)

global InputLabel1
TempFont1 = font.Font(frame2, size=10, weight='bold', family='Consolas')
InputLabel1 = Entry(frame2, font=TempFont1, width=26,  borderwidth=12, relief='ridge')
InputLabel1.pack()
InputLabel1.place(x=135, y=60)


#-------------여기까지 2페이지 내용----------------#

frame3=Frame(window)
notebook.add(frame3, text="보호/입양 현황")

##----3페이지 내용: 그래프로 보호수와 입양 수 현황 표시 / 챗봇 연동 ----##
#그래프 기능 & 챗봇 연동 구현
#시군구 조건을 맞춘 후 조회시 해당 지역의 유기견 보호소현황을 볼 수 있음
#정보를 받아와서 유기견 보호소의 명칭과 전번, 위치(주소) 등을 출력.
#지도 연동: 클릭시 해당 보호소의 구글지도 확인 가능. 이클래스 참고자료 참조

label3=Label(frame3, text="<<보호/입양 현황>>", font='helvetica 14')
label3.pack()
label3.place(x=17, y=15)




#-------------여기까지 3페이지 내용----------------#



window.mainloop()