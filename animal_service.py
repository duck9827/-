from tkinter import *
from tkinter import font
import tkinter.ttk  #페이지 수를 나누기 위한
import tkinter.messagebox

#동물보호관리시스템 Open API불러오기
import urllib
import http.client
from xml.dom.minidom import parse, parseString
conn = http.client.HTTPConnection("openapi.animal.go.kr")
conn.request("GET","/openapi/service/rest/abandonmentPublicSrvc/shelter?upr_cd=6110000&org_cd=3220000&ServiceKey")
req = conn.getresponse()
#print(req.status,req.reason)
#print(req.read().decode('utf-8'))
DataList = []
#-------------------------------

def SearchFrame1():  # 서치라이브러리 함수? 오픈api로 받아올 함수, 프레임1에서.
# 저거 xml 정보 사이사이에 엔터가 들가있는셈.
# 인덱스 잴 떄 그거 감안해야 함.
#주소를 검색시 해당되는 정보들을 가져옴. xml에서 careAddr 값을 가져와야?
#보호장소를 검색하게...
    global DataList
    DataList.clear()

    if req.status == 200:
        AnimalDoc = req.read().decode('utf-8')
    if AnimalDoc == None:
        print("에러")
    else:
        parseData = parseString(AnimalDoc)
        response = parseData.childNodes  # 이거 xml에 찰드노드
        item = response[0].childNodes

        for i in item:  # 아이템 찰드노드로 갔으면, 담아낼 준비?
            if i.nodeName == "items":
                subitems = i.childNodes
                # xml이면 엔터도 들가서, 인덱스가 3 5 단위로 간거.
                # 아래는 주소 중 구나 동이 검색되었을때?
                if subitems[3].firstChild.nodeValue == InputLabel.get():
                    pass
                elif subitems[3].firstChild.nodeValue == InputLabel.get():
                    pass
                else:
                    continue

                if subitems[7].firstChild is not None:  # 보호소 전화번호 부분이 비어있지 않다면
                    tel = str(subitems[7].firstChild.nodeValue)
                    pass  # ?꾩떆
                    if tel[0] != '0':
                        tel = "02-" + tel
                        pass
                    DataList.append((subitems[19].firstChild.nodeValue, subitems[21].firstChild.nodeValue,
                                     subitems[1].firstChild.nodeValue, subitems[39].firstChild.nodeValue,
                                     subitems[23].firstChild.nodeValue, subitems[41].firstChild.nodeValue,
                                     subitems[5].firstChild.nodeValue, subitems[7].firstChild.nodeValue,
                                     subitems[37].firstChild.nodeValue, subitems[9].firstChild.nodeValue,
                                     subitems[31].firstChild.nodeValue, tel))
                else:  # 전화번호가 없는 경우
                    DataList.append((subitems[19].firstChild.nodeValue, subitems[21].firstChild.nodeValue,
                                     subitems[1].firstChild.nodeValue, subitems[39].firstChild.nodeValue,
                                     subitems[23].firstChild.nodeValue, subitems[41].firstChild.nodeValue,
                                     subitems[5].firstChild.nodeValue, subitems[7].firstChild.nodeValue,
                                     subitems[37].firstChild.nodeValue, subitems[9].firstChild.nodeValue,
                                     subitems[31].firstChild.nodeValue, "-"))
            else:
                print("에러")


        for j in range(len(DataList)):
            RenderText.insert(INSERT, "<")
            RenderText.insert(INSERT, j + 1)
            RenderText.insert(INSERT, "> ")
            RenderText.insert(INSERT, "발견장소: ")  # 첫 번째는 발견장소(인덱스 19)
            RenderText.insert(INSERT, DataList[j][0])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "품종: ")  # 두 번째는 품종(인덱스 21)
            RenderText.insert(INSERT, DataList[j][1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "나이: ")  # 세 번째는 나이(인덱스 1)
            RenderText.insert(INSERT, DataList[j][2])
            RenderText.insert(INSERT, "성별: ")  # 네 번째는 성별(인덱스 39)
            RenderText.insert(INSERT, DataList[j][3])
            RenderText.insert(INSERT, "중성화여부: ")  # 다섯 번째는 중성화여부(인덱스는 23)
            RenderText.insert(INSERT, DataList[j][4])
            RenderText.insert(INSERT, "특징: ")  # 여섯 번째는 특징(인덱스는 41)
            RenderText.insert(INSERT, DataList[j][5])
            RenderText.insert(INSERT, "보호소 이름: ")  # 일곱 번째는 보호소 이름(인덱스는 5)
            RenderText.insert(INSERT, DataList[j][6])
            RenderText.insert(INSERT, "보호소 Tel): ")  # 여덟 번째는 보호소 전화번호(인덱스는 7)
            RenderText.insert(INSERT, DataList[j][7])
            RenderText.insert(INSERT, "상태: ")  # 아홉 번째는 상태(인덱스는 37)
            RenderText.insert(INSERT, DataList[j][8])
            RenderText.insert(INSERT, "담당자: ")  # 열 번째는 담당자 이름(인덱스는 9)
            RenderText.insert(INSERT, DataList[j][9])
            RenderText.insert(INSERT, "담당자 Tel): ")  # 열한 번째는 담당자 전번(인덱스는 31)
            RenderText.insert(INSERT, DataList[j][10])
            RenderText.insert(INSERT, "\n\n")

def SearchButtonAction():
    #global SearchListBox1
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    #iSearchIndex = SearchListBox1.curselection()[0]
    #if iSearchIndex == 0: #강아지
        #SearchFrame1()
    #elif iSearchIndex == 1: #고양이
        #pass
    #elif iSearchIndex == 2:  # 기타
        #pass
    #SearchFrame1()

    RenderText.configure(state='disabled')

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



##프레임 1,2의 입력은 엔트리만으로 변경-----------------
#global SearchListBox1

#ListBoxScrollbar = Scrollbar(window)
#ListBoxScrollbar.pack()
#ListBoxScrollbar.place(x=157, y=78)
#TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
#SearchListBox1 = Listbox(window, font=TempFont, activestyle='none',
                        #width=10, height=1, borderwidth=12, relief='ridge',
                        #yscrollcommand=ListBoxScrollbar.set)
#SearchListBox1.insert(1, "강아지")
#SearchListBox1.insert(2, "고양이")
#SearchListBox1.insert(3, "기타")
#SearchListBox1.pack()
#SearchListBox1.place(x=20, y=78)
#ListBoxScrollbar.config(command=SearchListBox1.yview)
#-----------------------------------------------------


label2=Label(frame1, text="[지역(시/군/구)]", font='helvetica 12')
label2.pack()
label2.place(x=10, y=67)

label3=Label(frame1, text="※주소 작성 예시: 서울특별시 용산구", fg='red', font='helvetica 10')
label3.pack()
label3.place(x=135, y=100)

global InputLabel   #검색창
TempFont = font.Font(frame1, size=10, weight='bold', family='Consolas')
InputLabel = Entry(frame1, font=TempFont, width=30, borderwidth=12, relief='ridge')
InputLabel.pack()
InputLabel.place(x=135, y=60)

#아래는 검색버튼
TempFont = font.Font(frame1, size=12, weight='bold', family='Consolas')
SearchButton = Button(frame1, font=TempFont, text="검색", borderwidth=4, command=SearchButtonAction)
SearchButton.pack()
SearchButton.place(x=375, y=63)

#정보가 뜰 창-1프레임
global RenderText

RenderTextScrollbar = Scrollbar(frame1)  # 스크롤바 만드는 부분은 여기!
RenderTextScrollbar.pack()
RenderTextScrollbar.place(x=375, y=150)

TempFont = font.Font(frame1, size=10, family='Consolas')
RenderText = Text(frame1, width=49, height=33, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
RenderText.pack()
RenderText.place(x=10, y=130)
RenderTextScrollbar.config(command=RenderText.yview)
RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

RenderText.configure(state='disabled')

SearchFrame1()
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
InputLabel1 = Entry(frame2, font=TempFont1, width=30,  borderwidth=12, relief='ridge')
InputLabel1.pack()
InputLabel1.place(x=135, y=60)

#아래는 검색버튼
TempFont = font.Font(frame2, size=12, weight='bold', family='Consolas')
SearchButton = Button(frame2, font=TempFont, text="검색", borderwidth=4, command=SearchButtonAction)
SearchButton.pack()
SearchButton.place(x=375, y=63)

#정보가 뜰 창-2프레임
global RenderText2

RenderTextScrollbar = Scrollbar(frame2)  # 스크롤바 만드는 부분은 여기!
RenderTextScrollbar.pack()
RenderTextScrollbar.place(x=375, y=150)

TempFont = font.Font(frame2, size=10, family='Consolas')
RenderText2 = Text(frame2, width=49, height=33, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
RenderText2.pack()
RenderText2.place(x=10, y=130)
RenderTextScrollbar.config(command=RenderText2.yview)
RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

RenderText2.configure(state='disabled')


#-------------여기까지 2페이지 내용----------------#

frame3=Frame(window)
notebook.add(frame3, text="보호/입양 현황")

##----3페이지 내용: 그래프로 보호수와 입양 수 현황 표시 ----##
#그래프 기능 구현
#시군구 조건을 맞춘 후 조회시 해당 지역의 유기견 보호소현황을 볼 수 있음
#정보를 받아와서 유기견 보호소의 명칭과 전번, 위치(주소) 등을 출력.
#지도 연동: 클릭시 해당 보호소의 구글지도 확인 가능. 이클래스 참고자료 참조

label3=Label(frame3, text="<<보호/입양 현황>>", font='helvetica 14')
label3.pack()
label3.place(x=17, y=15)




#-------------여기까지 3페이지 내용----------------#
frame4=Frame(window)
notebook.add(frame4, text="텔레그램봇 연동")

##----4페이지 내용: 챗봇 연동 ----##

label4=Label(frame4, text="<<텔레그램봇>>", font='helvetica 14')
label4.pack()
label4.place(x=17, y=15)




#-------------여기까지 4페이지 내용----------------#




SearchButtonAction()

window.mainloop()













