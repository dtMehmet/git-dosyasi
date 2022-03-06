"""
     IKI SAYI ORTALAMA ORNEGI
sayi1 = input('sayi giriniz : ') 
sayi2 = input('sayi giriniz : ')   
ortalama = (int(sayi1) + int(sayi2))/2
print('ortalama :{0} ' .format(ortalama))                         


    GIRILEN ve final VIZE NOTU ORTALAMASI
vize = input('vize notunuz  :') 
final = input('final notunuz :')
ortalama= (float(vize)*0.3) + (float(final)*0.7)
print('ortalma  :{0} '.format(ortalama)) 

 GIRILEN 3 SINAV NOTU ORTALAMASI   
y1= float(input('yazili notu :'))   
y2= float(input('yazili notu :'))
y3= float(input('yazili notu :'))
ortalama= (y1 + y2 + y3)/3
print('ortalama :{0} '.format(ortalama))
  
  
       YAZILI ORTALAMASI GIRILEN OGRENCI GECTI KALDI CIKTISI

ort=input('ortalama giriniz :')
if(int(ort)>=50):
   print('gectiniz')
else:
    print('kaldiniz')    
    
    
   GIRILEN SAYININ TEK MI CIFT MI OLMASI
 
sayi=int(input('sayi giriniz :'))
if(sayi)%2==0:
    print('sayi cifttir')
else :
   print('sayi tektir')
        
   GIRILEN SAYI POZITIF MI NEGATIF MI POZITIF MI

sayi=input('sayi giriniz :')
if(int(sayi))>0:
    print('sayi pozitifitr')
elif(int(sayi))<0:
   print('sayi negatiftir')    
else:
#   print('sayi sifirdir')    



#   VUCUT KITLE ENDEKSI HESAPLAMA PROGRAMI

#boy=float(input('boy giriniz(m) :'))
#kilo=float(input('kilo giriniz (kg) :'))
#endeks=kilo/(boy*boy)

#if endeks <= 18:
#    print('VKI zayif {}' .format(endeks))
#elif endeks > 18 and endeks <=25 :
#    print ('VKI normal  :{}'.format(endeks))
#elif endeks > 25 and endeks <= 30 :
#    print('VKI obez :{}' .format(endeks))   
#elif endeks > 30 :
#    print('VKI ciddi obez :'.format(endeks) )  

#  BIRDEN 99 A KADAR YAZDIRMA
#print(*range(1,100))
#  veya alt alta yazdirma
#for i in  range(1,100):
#    print(i) 
#   SAYILARI GERI YAZDIRMA 
#print(*range(1,100)[::-1])  
 
#    BIRDEN 99 A KADAR CIFT SAYILARIN CIKTISI

#print(*range(0,100)[::2])

#for i in range(1,100):
 #   if i%2==0:
  #      print(i)
 
 
#       BIRDEN 100 E KADAR 3,E VE 5,E BOLUNEN SAYILAR 
#for i in range(1,101):
      
#      if i%3==0 and i%5==0 :
#       print(i)


#   SORU 16 1 den kullanicinin girdigi sayiya kadar listeleyen ornek 

#sayi= input('sayi gir  :' )  
#for i in range(1,int(sayi)+1) :    

#    print(i)



##soru 17 kenarlari girilen dikdortgenin cevresini  bulan Program
 
#kisa=float(input('kisa kenar  :'))        
#uzun=float(input('uzun kenar :'))
#alan=float(kisa)*float(uzun)
##cevre=2*(float(kisa)+float(uzun))
#print("alan :{0}".format(alan))
#print('cevre  :{0}'.format(cevre))

#soru 17 girilen ismin harflerini alt alta yazdirma ornegi

#isim= input('isminizi girin')
#sayac=0
#hile sayac < len(isim):
#    print(isim[sayac])
#    sayac += 1
#else :
#    print('adinin harflerini listeledim')    

#  soru 19  kullanicinin girdigi iki sayi arasindaki sayilarin toplami

#toplam=0;
#sayi1=int(input('sayi giriniz1 :'))
#sayi2=int(input('sayi giriniz2 :'))

#for i in range((sayi1)+1 , (sayi2) ):
#   toplam +=i
#print('{0} ile{1} arasindaki sayi toplami: {2}'.format(sayi1,sayi2,toplam))

         

#  soru 20) kullaniciya sinema yada tiyatro tercihi sorulsun. sinema izlemek isteyenler 15 tl  tiyatro icin 10 tl 
#odesin. ogrencilere %50 indirim yapildigi dusunulerek  ogrenci ise  indirim yapilir. degilse normal fiyati odesin

#ogrenci= input("orencimisiniz? :evet/hayir")
#tercih1= input(('sinema icin (1),(tiyatro icin(2) tuslayiniz  :'))
#ucret=0
 #indirimsiz ucret hesaplama
##if tercih1 == '1':
#    ucret= 15 #sinema
#elif tercih1 == '2':
#    ucret= 10 #tiyatro
    
##ogrenci indirimi
#if ogrenci=='evet' :
 #   ucret= ucret/2  #%50
#print('odemeniz gereken ucret  :{}'.format (ucret))


# girilen sayi asal sayi mi degil mi oldugunu bildiren ornek

  #sayac=0
#sayi=input('sayi  : ')
#for i in range (2,int(sayi)):
 #   if(int(sayi)%i==0):
#        sayac+=1
#        break
#if (sayac!=0): 
#    print('sayi asal sayi degildir')   
#else:
 #   print('asal sayi')
 
 #### soru 22) 1 den kullanicinin girdigi sayiya kadar olan  tek ve cift sayilarin toplamini ayri ayri bulan  ve sonucu ekranda gosteren  ornek
 
##sayi = input('sayi girin :')
##tek_toplam=0
##cift_toplam=0
##for i in range (1, int(sayi)):
##    if (i%2==0):
##        cift_toplam+=i
 ##   else :
##        tek_toplam+=i
##print('tek sayilarin toplami : {0}'.format(tek_toplam))
##print('cift sayilarin toplami : {0}'.format(cift_toplam))

#soru 23) maasi ve zam orani girilen iscinin zamli maasini hesaplama ornegi

##yeni_maas=0
##maas=input('maasi girimiz :')
##zam=input('zam orani(%) :')
##yeni_maas=int(maas)+(int(maas)*int(zam)/100)
##print('zamli maas :', yeni_maas)
      
 #  soru 24) liste icindeki sayilarin 5 in katlari ni listeleme


  #sayilar=[18, 22, 15, 85, 65, 30, 10, 20, 32, 34, 28, 101, 5, 4, 32 ]
#sayac=0      
#for sayi in sayilar:
#   if sayi%5 == 0:
 #       print (str(sayi)+(' : 5 in katidir'))
#        sayac=sayac+1
#else:
 #   print('dongu bitti')
#print('5 in kati olansayi adedi :'+str(sayac))


   #aklimizda tuttugumuz sayiyi bulma programi

from tkinter.messagebox import QUESTION

#answer = 44
#question= 'what number am i thinking of'

#while True :
 #   guess=int(input(question ))
 
#    if guess < answer :
#             print('little higher')     
#    elif guess > answer :
#             print ('little lower')  
#    else :     # guess == answer    
             
#        print(' are you MINDREADER')
#        break
#for i in {'n1' : 'one', 'n2' : 'two'} : 
#    print(i)

# soru 1500 ile 2700 arasindaki 5 ve 7 ye bolunen sayilarin listesi
#numbers=range(1500,2700)

#for i in range(1500,2700) :

 #if i %7==0 and i %5==0 :
 #   print(i)
 
 
# soru kullanicidan 1-9 arasi bir sayi tahmin etmesi istenir tahmin dogru olana kadar islem devam eder
tutulan_sayi=('akildaki sayi')
number=int(input('bir sayi tahmin et, 1 to 9 :'))
if number==('tututlan_sayi') :
    
    print('tekrar dene')
else :
    print('iyi tahmin')   
"""            